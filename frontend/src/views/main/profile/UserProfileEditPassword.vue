<template>
  <v-container fluid>
      <form @submit.prevent="onSubmit" @reset.prevent="onReset">
        <v-card class="ma-3 pa-3">
          <v-card-title primary-title>
            <div class="headline primary--text">Set Password</div>
          </v-card-title>
          <v-card-text>
            <div class="my-3">
              <div class="subheading secondary--text text--lighten-2">User</div>
              <div
                v-if="userProfile.full_name"
                class="title primary--text text--darken-2"
              >
                {{ userProfile.full_name }}
              </div>
              <div v-else class="title primary--text text--darken-2">
                {{ userProfile.email }}
              </div>
            </div>
              <v-text-field
                v-model="password1"
                type="password"
                label="Password"
                :error-messages="errors"
              >
              </v-text-field>
              <v-text-field
                v-model="password2"
                type="password"
                label="Confirm Password"
                :error-messages="errors"
              >
              </v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click="cancel">Cancel</v-btn>
            <v-btn type="reset">Reset</v-btn>
            <v-btn type="submit" :disabled="invalid">Save</v-btn>
          </v-card-actions>
        </v-card>
      </form>
  </v-container>
</template>

<script lang="ts">

import { IUserProfileUpdate } from "@/interfaces";

import { appName } from "@/env";
import { defineComponent } from "vue";

export default defineComponent ({
  name: "Profile-Edit-Passwd",
  components: {},
  data() {
    return {
      valid: true,
      invalid: false,
      password2: "",
      password1: "",
      appName: appName,
      errors: ""
    }
  },
  computed: {
    userProfile() {
      return this.$store.getters.userProfile || {};
    }
  },
  methods: {
    onReset() {
      this.password1 = "";
      this.password2 = "";
    },
    cancel() {
      this.$router.back();
    },
    async onSubmit() {
      const success = true;
      //const success = await this.$refs.observer.validate();
      if (!success) {
        return;
      }

      const updatedProfile: IUserProfileUpdate = {};
      updatedProfile.password = this.password1;
      this.$store.dispatch("actionUpdateUserProfile",updatedProfile)
      //await dispatchUpdateUserProfile(this.$store, updatedProfile);
      this.$router.push("/main/profile");
    }
  }
})
</script>
