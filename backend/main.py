from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
import io
from rembg import remove
from PIL import Image
from transformers import pipeline
from diffusers import DiffusionPipeline
import torch
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------
# TEXT GENERATION (GPT-2)
# ------------------------------
device = "cuda" if torch.cuda.is_available() else "cpu"
text_gen = pipeline("text-generation", model="gpt2", device=0 if device == "cuda" else -1)

# ------------------------------
# IMAGE GENERATION (SDXL Turbo)
# ------------------------------
torch_dtype = torch.float32 if device == "cpu" else torch.float16
sd_pipe = DiffusionPipeline.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch_dtype).to(device)

# ------------------------------
# FASTAPI ENDPOINTS
# ------------------------------

@app.get("/generate-text")
def generate_text(word: str):
    if not word:
        raise HTTPException(status_code=400, detail="Word parameter is required.")
    prompt = f"Write a short story about {word}:"
    result = text_gen(prompt, max_length=100)
    return {"text": result[0]['generated_text']}

@app.get("/generate-image")
def generate_image(prompt: str):
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt parameter is required.")
    image = sd_pipe(prompt).images[0]
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return StreamingResponse(img_byte_arr, media_type="image/png")

@app.post("/remove-background")
async def remove_background(file: UploadFile = File(...)):
    input_image = await file.read()
    output_image = remove(input_image)
    return StreamingResponse(io.BytesIO(output_image), media_type="image/png")
