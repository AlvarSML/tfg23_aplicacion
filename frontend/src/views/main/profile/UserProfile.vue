<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Perfil de usuario</div>
      </v-card-title>
      <v-card-text>
        <div class="my-4">
          <div class="subheading secondary--text text--lighten-3">Nombre completo</div>
          <div
            v-if="userProfile && userProfile.full_name"
            class="title primary--text text--darken-2"
          >
            {{ userProfile.full_name }}
          </div>
          <div v-else class="title primary--text text--darken-2">-----</div>
        </div>
        <div class="my-3">
          <div class="subheading secondary--text text--lighten-3">Email</div>
          <div
            v-if="userProfile && userProfile.email"
            class="title primary--text text--darken-2"
          >
            {{ userProfile.email }}
          </div>
          <div v-else class="title primary--text text--darken-2">-----</div>
        </div>
      </v-card-text>
      <v-card-actions>
        <v-btn to="/main/profile/edit">Editar</v-btn>
        <v-btn to="/main/profile/password">Cambio de contraseña</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">

import { appName } from "@/env";
import { defineComponent } from "vue";

export default defineComponent ({
  name: "User-Profile",
  computed: {
    userProfile() {
      return this.$store.getters.userProfile;
    }
  },
  methods: {
    
    goToEdit() {
      this.$router.push("/main/profile/edit");
    },
    goToPassword() {
      this.$router.push("/main/profile/password");
    }
  }

})

</script>
