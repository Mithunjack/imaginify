# Imaginify - AI Image Generator & Editor
<table><tr>
    <td><img src="https://github.com/user-attachments/assets/ed2fd0aa-857f-4860-b137-872e521ce979" width="200" /></td>
    <td><img src="https://github.com/user-attachments/assets/8e499dc7-36a3-4ce4-8205-91eddbd78c26" width="200" /></td>
    <td><img src="https://github.com/user-attachments/assets/e73d805c-7fc0-4d8a-9c5e-3687de87475c" width="200" /></td>
    <td><img src="https://github.com/user-attachments/assets/49d3b645-4530-4604-b39e-e9136609ffe0" width="200" /></td>
</tr>
<tr>
     <td><img src="https://github.com/user-attachments/assets/96d5efd2-ea98-4625-9136-1371a85283dd" width="200" /></td>
</tr></table>




## 📌 Project Overview

**Imaginify** is a full-stack AI-powered application that allows users to:

- 🔮 **Generate creative text prompts using AI**
- 🎨 **Generate images from text prompts using Stable Diffusion**
- ✂️ **Edit images by removing backgrounds**
- 🪄 Future Scope: Inpainting (object removal/replacement), outpainting (extending images)

---

## 💻 Workflow

1. Click **Generate Text** - Backend generates creative text.
2. Click **Generate Image** - Backend uses Stable Diffusion to generate image from the text.
3. Click **Remove Background** - Backend uses `rembg` to remove background from generated image.

---

## ⚙️ Tech Stack

### Frontend

- Framework: **Vue 3 + Vite**
- Language: **JavaScript**
- Styling: **Tailwind CSS**

### Backend

- Framework: **FastAPI** (Python)
- Environment: **Conda (imaginify)**
- Key Libraries:
  - `rembg` for background removal
  - `diffusers` for image generation
  - `transformers` for text generation
  - `PIL` for image handling

---

## 📂 Folder Structure

```text
.
├── backend                 # FastAPI Backend
│   ├── main.py
│   ├── requirements.txt    # To be created if needed
├── frontend                 # Vue 3 Frontend
│   ├── src
│   │   ├── App.vue
│   │   ├── components
│   │   │   ├── ImageEditor.vue
│   ├── main.js
├── README.md
```

---

## 🚀 How to Run (Development)

### 1️⃣ Backend Setup

- Activate Conda environment:
  ```bash
  conda activate imaginify
  ```
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Start FastAPI backend:
  ```bash
  uvicorn main:app --reload
  ```
- Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

### 2️⃣ Frontend Setup

- Navigate to `frontend/` folder:
  ```bash
  cd frontend
  ```
- Install dependencies:
  ```bash
  npm install
  ```
- Start Vue frontend:
  ```bash
  npm run dev
  ```
- Visit: [http://localhost:5173](http://localhost:5173)

---

## 🔗 Key API Endpoints

| Method | Endpoint             | Description                                      |
| ------ | -------------------- | ------------------------------------------------ |
| GET    | `/generate-text`     | Generates creative text prompt                   |
| GET    | `/generate-image`    | Generates image from generated text prompt       |
| POST   | `/remove-background` | Removes background from uploaded/generated image |

---

## 📦 Requirements (Python)

```text
fastapi
uvicorn
pillow
rembg
transformers
diffusers
torch
accelerate
onnxruntime
```

---

## 🚀 Deployment (Optional)

### Backend

- Add `Procfile` with:
  ```
  web: uvicorn main:app --host 0.0.0.0 --port $PORT
  ```
- Deploy to Railway (root = backend folder).

### Frontend

- Build frontend:
  ```bash
  npm run build
  ```
- Deploy `dist/` to Railway Static Service or Vercel.

## 💡 Future Features (Planned)

✅ Object Removal (Inpainting)  
✅ Object Replacement (Prompt-based Editing)  
✅ Outpainting (Extending Images Beyond Borders)  
✅ Project Saving (Save edit history per user)
