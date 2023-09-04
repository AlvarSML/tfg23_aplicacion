<script setup lang="ts">
const props =  defineProps({
  color: String,
  multiple: Boolean,
})

const color = "";
const multiple = false;

function files(e:any): FileList {
  return e.target.files;
}



</script>


<template>
  <div>
    <v-btn :color="color" ><slot>Choose File</slot></v-btn>
    <input
      ref="fileInput"
      :multiple="multiple"
      class="visually-hidden"
      type="file"
      @change="files"
    />
  </div>
</template>


<style scoped>
.visually-hidden {
  position: absolute !important;
  height: 1px;
  width: 1px;
  overflow: hidden;
  clip: rect(1px, 1px, 1px, 1px);
}
</style>
