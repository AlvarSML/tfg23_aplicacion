<template>
  <v-main>
    <v-container fluid>
      <v-row dense>
        <v-col cols="card.flex">
          <v-form @keyup.enter="onSubmit">
            <v-card-text>Radiografia Endodoncia</v-card-text>
            <v-file-input
              clearable
              label="Radiografia"
              variant="filled"
              prepend-icon="mdi-camera"
              accept="image/png, image/jpeg"
              @change="onFileChange"
            >
            </v-file-input>

            <v-container fluid>
              <v-col cols="card.flex">

                <v-card width="auto">
                  <v-img height="400px" width="400px" :src="imagenSubir" contain />
                </v-card>

                <v-card width="auto">
                  <v-img height="400px" width="400px" :src="imgInference" contain />
                </v-card>

              </v-col>
            </v-container>

          </v-form>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click.prevent="onSubmit">Medir</v-btn>
          </v-card-actions>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script lang="ts">

import { appName } from "@/env";
import { defineComponent } from "vue";

export default defineComponent ({
  name: "Radiografias-app",
  data() {
    this.imagen;
    this.imageUrl;
    this.imgInference;
    return {
      imagen: {},
      imagetest: null,
      imageUrl: "",
      imgInference: "{}",
      appName: appName,
      
    }
  },
  computed: {
    imagenSubir(): string {
      if(this.$store.getters.imagePreview)
        return URL.createObjectURL(this.$store.getters.imagePreview);
      else {
        return ""
      }
    }
  },
  methods: {
    async onSubmit() {
      // Se ejecuta al mandar el formualrio
      if (this.imagen) {
        //await dispatchInference(this.$store, { image: this.imagen })
        await this.$store.dispatch("actionInference",{ image: this.$store.getters.imagePreview}).then(() => {
          this.imgInference = this.$store.getters.imageUrl;
          console.log("imageurl",this.$store.getters.imageUrl);
        });
        console.log("imageurl", this.$store.getters.imageUrl);
      }
    },
    onFileChange(event:any) {
      this.$store.commit("setImagePreview",event.target.files[0])
      console.log(this.imagenSubir)
    }
  }
})

</script>

<style></style>
