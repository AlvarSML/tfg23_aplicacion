<template>
  <v-main>
    <v-container fluid class="fill-height">
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="4">
          <validation-observer ref="observer" v-slot="{ invalid }">
            <form @submit.prevent="onSubmit" @reset.prevent="onReset">
              <v-card class="elevation-12">
                <v-toolbar dark color="primary">
                  <v-toolbar-title>{{ appName }} - Reset de contraseña</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                  <p class="subheading">Introduzaca su nueva contraseña</p>
                  <validation-provider
                    v-slot="{ errors }"
                    :debounce="100"
                    name="Password"
                    vid="password1"
                    rules="required"
                  >
                    <v-text-field
                      v-model="password1"
                      type="password"
                      label="Password"
                      :error-messages="errors"
                    >
                    </v-text-field>
                  </validation-provider>
                  <validation-provider
                    v-slot="{ errors }"
                    debounce="100"
                    name="Password confirmation"
                    vid="password2"
                    rules="required|confirmed:password1"
                  >
                    <v-text-field
                      v-model="password2"
                      type="password"
                      label="Confirm Password"
                      :error-messages="errors"
                    >
                    </v-text-field>
                  </validation-provider>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn @click="cancel">Cancelar</v-btn>
                  <v-btn type="reset">Limpiar</v-btn>
                  <v-btn type="submit" :disabled="invalid">Guardar</v-btn>
                </v-card-actions>
              </v-card>
            </form>
          </validation-observer>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { appName } from "@/env";


export default defineComponent({
  name: "Reset-Passwd",
  data() {
    return {
      appName: appName,
      valid: true,
      password1: "",
      password2: "",
    }
  },
  mounted() {
    this.checkToken();
  },
  methods: {
    onReset() {
      this.password1 = "";
      this.password2 = "";
    },
    cancel() {
      this.$router.push("/");
    },
    checkToken() {
      //const token = this.$router.currentRoute.query.token as string;
      console.warn("TODO")
      const token = "asd"
      if (!token) {
        this.$store.commit("addNotification", {
          content: "No token provided in the URL, start a new password recovery",
          color: "error"
        });
        this.$router.push("/recover-password");
      } else {
        return token;
      }
    },
    async onSubmit() {
      //const success = await this.$refs.observer.validate();
      const success = true;
      if (!success) {
        return;
      }

      const token = this.checkToken();
      if (token) {
        await this.$store.dispatch("resetPassword", { token, password: this.password1 })
        //await dispatchResetPassword(this.$store, { token, password: this.password1 });
        this.$router.push("/");
      }
    }
  }
})
</script>
