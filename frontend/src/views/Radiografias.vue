<template>
  <v-main>
    <v-container fluid>

          <v-form @keyup.enter="onSubmit">
            <v-card-text>Radiografia Endodoncia</v-card-text>
            <v-file-input clearable label="Radiografia" variant="filled" prepend-icon="mdi-camera"
              accept="image/png, image/jpeg" @change="onFileChange">
            </v-file-input>

            <div class="d-flex flex-column justify-start align-center">
              <v-slider v-model="width" class="align-self-stretch" min="300" max="2000" step="1"></v-slider>
              <v-img v-if="mostrarPrev" :width="width" :src="imagenSubir" />
              <v-img v-if="mostrarProcesada" :width="width" :src="imagenProcesada" />
              <v-progress-circular v-if="mostrarCarga" indeterminate  :size="76" :width="6"></v-progress-circular>
            </div>

          </v-form>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click.prevent="onSubmit">Medir</v-btn>
            <v-btn @click="dum">Dummy</v-btn>
          </v-card-actions>

    </v-container>
  </v-main>
</template>

<script lang="ts">

import { appName } from "@/env";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Radiografias-app",
  data() {
    return {
      appName: appName,
      width: 500,
      medido: false,
      clickMedido: false,
    }
  },
  computed: {
    imagenSubir(): string {
      if (this.$store.getters.imagePreview)
        return URL.createObjectURL(this.$store.getters.imagePreview);
      else {
        return ""
      }
    },
    imagenProcesada(): string {
      console.log("cambio")
      if (this.$store.getters.imageProcessed) {
        console.log("procesada", URL.createObjectURL(this.$store.getters.imageProcessed));
        return URL.createObjectURL(this.$store.getters.imageProcessed);
      } else {
        return ""
      }
    },
    mostrarPrev(): boolean {
      // Se muestra si no hay una imagen procesada y no se ha hecho click en medir
      // para la imagen actual
      if (this.imagenProcesada && this.clickMedido){
        return false
      } else {
        return true
      }
    },
    mostrarProcesada(): boolean {
      // Se muestra si se ha hecho click medir y hay una imagen procesada
      if (this.imagenProcesada && this.clickMedido){
        return true
      } else {
        return false
      }
    },
    mostrarCarga(): boolean {
      return !this.imagenProcesada && this.clickMedido
    }
  },
  methods: {
    async onSubmit() {
      // Se ejecuta al mandar el formualrio
      if (this.$store.getters.imagePreview) {
        //await dispatchInference(this.$store, { image: this.imagen })
        await this.$store.dispatch("actionInference", { image: this.$store.getters.imagePreview })
      }
      this.clickMedido = true;
    },
    onFileChange(event: any) {
      this.$store.commit("setImagePreview", event.target.files[0])
      this.$store.commit("setImageProcessed",null)
      this.clickMedido = false;
    },
    dum() {
      console.log(URL.createObjectURL(this.$store.getters.imageProcessed))
    }
  }
})

</script>

<style></style>
