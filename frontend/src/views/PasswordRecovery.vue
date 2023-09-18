<template>
  <v-main>
    <v-container fluid fill-height>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="4">

            <form @submit.prevent="onSubmit">
              <v-card class="elevation-12">
                <v-toolbar dark color="primary">
                  <v-toolbar-title>{{ appName }} - Recuperacion de contraseña</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                  <p class="subheading">
                    Se enviara un email de recuperacion de contraseña a su correo
                  </p>

                    <v-text-field
                      v-model="username"
                      label="Username"
                      type="text"
                      prepend-icon="mdi-account"
                      :error-messages="errors"
                      required
                      @keyup.enter="onSubmit"
                    ></v-text-field>

                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn @click="cancel">Cancelar</v-btn>
                  <v-btn type="submit" > Recuperar </v-btn>
                </v-card-actions>
              </v-card>
            </form>

        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script lang="ts">

import { appName } from "@/env";
import { defineComponent } from "vue";
//import { required } from "vee-validate/dist/rules";

export default defineComponent ({
  name: "Passwd-Recovery",
  components: {
  },
  data() {
    return {
      valid: true,
      username: "",
      appName: appName,
      errors: ""
    }
  },
  methods: {
    cancel() {
      this.$router.back();
    },
    async onSubmit() {
      // const success = await this.$refs.observer.validate();
      const success = true;
      if (!success) {
        return;
      }
      this.$store.dispatch("asswordRecovery",{ username: this.username })
      //dispatchPasswordRecovery(this.$store, { username: this.username });
    }
  },
  mounted() {
    this.errors = "";
  }
})
</script>

<style></style>
