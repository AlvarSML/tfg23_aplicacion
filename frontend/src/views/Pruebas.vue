<template>
  <v-main>
    <v-container fluid>
      <v-row dense>
        <v-col cols="card.flex">
          <v-form @keyup.enter="submit">
            <v-card-text>Pruebas</v-card-text>
            <v-file-input
              label="File input"
              variant="filled"
              prepend-icon="mdi-camera"
              accept="image/png, image/jpeg "
              @change="onFileChange"
            >
            </v-file-input>
            <v-container fluid>
              <v-col cols="card.flex">
                <v-card width="auto">
                  <v-img height="400px" width="400px" :src="imageUrl" contain />
                </v-card>
                <v-card width="auto">
                  <v-img height="400px" width="400px" :src="imgInference" contain />
                </v-card>
              </v-col>
            </v-container>
          </v-form>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click.prevent="submit">Medir</v-btn>
          </v-card-actions>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { appName } from "@/env";
import { dispatchInference } from "@/store/inference/actions";

@Component
export default class Pruebas extends Vue {
  public imagen: File | null = null;
  public appName = appName;
  public imageUrl: string | null = null;
  public imgInference: string | null = null;

  mounted() {
    //console.log(this.$store.state.inference);
  }

  public async submit() {
    // Se ejecuta al mandar el formualrio
    if (this.imagen) {
      await dispatchInference(this.$store, { image: this.imagen }).then(() => {
        this.imgInference = this.$store.state.inference.imageUrl;
        console.log(this.$store.state.imageUrl);
      });
      console.log("aa", this.$store.state.inference.imageUrl);
    }
  }

  public onFileChange(file: File) {
    console.log(file);
    if (file) {
      this.imagen = file;
      this.imageUrl = URL.createObjectURL(file);
    } else {
      this.imageUrl = null;
      this.imagen = null;
    }
  }
}
</script>

<style></style>
