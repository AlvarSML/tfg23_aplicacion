<template>
  <v-main>
    <v-container fluid fill-height>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="6" l="5" xl="4">
          <v-card class="elevation-12">
            <v-form @keyup.enter="submit">
              <v-card-text>Pruebas</v-card-text>
              <v-file-input
                label="File input"
                variant="filled"
                prepend-icon="mdi-camera"
                accept="image/png, image/jpeg "
                @change="onFileChange"
              ></v-file-input>
              <v-img :src="imageUrl" />
            </v-form>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn @click.prevent="submit">Medir</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { appName } from "@/env";
//import { readLoginError } from "@/store/main/getters";
//import { dispatchLogIn } from "@/store/main/actions";

@Component
export default class Pruebas extends Vue {
  public imagen = "";
  public appName = appName;
  public imageUrl: string | ArrayBuffer | null = null;
  public submit() {
    //dispatchLogIn(this.$store, { username: this.email, password: this.password });
    // Funcion de api
  }

  public onFileChange(file) {
    if (file) {
      this.imageUrl = URL.createObjectURL(file);
    } else {
      this.imageUrl = null;
    }
  }
}
</script>

<style></style>
