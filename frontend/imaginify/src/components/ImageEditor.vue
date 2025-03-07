<template>
  <div class="flex w-full items-center justify-center bg-gray-100">
    <div class="w-full max-w-lg bg-white shadow-lg rounded-2xl p-6 space-y-4" style="margin: 10px;">
      <h2 class="text-2xl mb-10 font-bold text-center text-gray-800" style="margin-bottom: 20px;">Imaginify - AI Image Generator & Editor</h2>

      <label for="inputWord" class="mt-4 block mb-2 text-LG font-medium text-gray-900">Write a word to generate the story about</label>
      <input v-model="inputWord" placeholder="Enter a word (e.g., castle)" class="mt-4 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />

      <button @click="generateText" class="w-full text-white bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 shadow-lg shadow-cyan-500/50 dark:shadow-lg dark:shadow-cyan-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
        Generate Story
      </button>

      <div v-if="description" class="text-center font-bold text-gray-700 font-medium">
        "{{ description }}"
      </div>

      <button v-if="description" @click="generateImage" class="w-full text-white bg-gradient-to-r from-green-400 via-green-500 to-green-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-green-300 dark:focus:ring-green-800 shadow-lg shadow-green-500/50 dark:shadow-lg dark:shadow-green-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
        Generate Image
      </button>

      <div v-if="imageUrl" class="flex justify-center">
        <img :src="imageUrl" alt="Generated Image" class="mt-4 w-80 rounded-lg border shadow-md" />
      </div>

      <button v-if="imageUrl" @click="removeBackground" class="w-full text-white bg-gradient-to-r from-purple-500 via-purple-600 to-purple-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-purple-300 dark:focus:ring-purple-800 shadow-lg shadow-purple-500/50 dark:shadow-lg dark:shadow-purple-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
        Remove Background
      </button>

      <div v-if="resultImage" class="flex justify-center">
        <img :src="resultImage" alt="Background Removed" class="mt-4 w-80 max-w-xs rounded-lg border shadow-md" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const inputWord = ref('')
const description = ref('')
const imageUrl = ref('')
const resultImage = ref('')
let imageBlob = null

async function generateText() {
    if (!inputWord.value) {
        alert('Please enter a word to generate a story.')
        return
    }

    try {
        const res = await fetch(`http://localhost:8000/generate-text?word=${encodeURIComponent(inputWord.value)}`)
        const data = await res.json()
        description.value = data.text
    } catch (error) {
        console.error('Error generating text:', error)
    }
}

async function generateImage() {
    try {
        const res = await fetch(`http://localhost:8000/generate-image?prompt=${encodeURIComponent(description.value)}`)
        imageBlob = await res.blob()
        imageUrl.value = URL.createObjectURL(imageBlob)
    } catch (error) {
        console.error('Error generating image:', error)
    }
}

async function removeBackground() {
    try {
        const formData = new FormData()
        formData.append('file', new File([imageBlob], 'generated.png', { type: 'image/png' }))

        const res = await fetch('http://localhost:8000/remove-background', {
            method: 'POST',
            body: formData
        })
        const bgRemovedBlob = await res.blob()
        resultImage.value = URL.createObjectURL(bgRemovedBlob)
    } catch (error) {
        console.error('Error removing background:', error)
    }
}
</script>

<style scoped>
button {
  transition: background-color 0.2s;
  margin-top: 1rem;
  margin-bottom: 1rem;
}
button:hover {
  cursor: pointer;
}
</style>
