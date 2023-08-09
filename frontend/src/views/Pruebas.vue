<template>
  <v-main>
    <v-container fluid fill-height>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="6" l="5" xl="4">
          <v-card class="elevation-12">
            <p>Pruebas</p>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { appName } from "@/env";
import { readLoginError } from "@/store/main/getters";
import { dispatchLogIn } from "@/store/main/actions";

@Component
export default class Pruebas extends Vue {
  public email = "";
  public password = "";
  public appName = appName;

  public get loginError() {
    return readLoginError(this.$store);
  }

  public submit() {
    dispatchLogIn(this.$store, { username: this.email, password: this.password });
  }
}
</script>

<style></style>
