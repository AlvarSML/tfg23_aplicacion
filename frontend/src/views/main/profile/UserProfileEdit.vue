<template>
  <v-container fluid>
    <form @submit.prevent="onSubmit" @reset.prevent="onReset">
      <v-card class="ma-3 pa-3">
        <v-card-title primary-title>
          <div class="headline primary--text">Editar perfil</div>
        </v-card-title>
        <v-card-text>
          <v-text-field v-model="fullName" label="Nombre Completo" required></v-text-field>
          <v-text-field v-model="email" label="E-mail" type="email" :error-messages="errors" required></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="cancel">Cancelar</v-btn>
          <v-btn type="reset">Reset</v-btn>
          <v-btn type="submit"> Guardar </v-btn>
        </v-card-actions>
      </v-card>
    </form>
  </v-container>
</template>

<script lang="ts">

import { IUserProfileUpdate } from "@/interfaces";

import { defineComponent } from "vue";

export default defineComponent({
  name: "Profile-Edit",
  components: {},
  data() {
    return {
      valid: true,
      fullName: "",
      email: "",
      errors: ""
    }
  },
  computed: {
    userProfile() {
      return this.$store.getters.userProfile;
    }
  },
  methods: {
    onReset() {
      const userProfile = this.$store.getters.userProfile;
      if (userProfile) {
        this.fullName = userProfile.full_name;
        this.email = userProfile.email;
      }
    },
    cancel() {
      this.$router.back();
    },
    async onSubmit() {
      const success = true;
      if (!success) {
        return;
      }

      const updatedProfile: IUserProfileUpdate = {};
      if (this.fullName) {
        updatedProfile.full_name = this.fullName;
      }
      if (this.email) {
        updatedProfile.email = this.email;
      }
      await this.$store.dispatch("actionUpdateUserProfile", updatedProfile)
      this.$router.push("/main/profile");
    }
  },
  created() {
    this.onReset()
  }
})

</script>
