<template>
  <div class="app">
    <ImageEditor />
  </div>
</template>

<script setup>
import ImageEditor from './components/ImageEditor.vue'
</script>

<style>
.app {
  display: flex;
  justify-content: center;
  align-items: center;
  height: auto;
  width: auto;
  flex-direction: column;
}
</style>
