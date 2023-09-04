<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Dashboard</div>
      </v-card-title>
      <v-card-text>
        <div class="headline font-weight-light ma-5">Welcome {{ getGreetedUser }}</div>
      </v-card-text>
      <v-card-actions>
        <v-btn to="/main/profile/view">View Profile</v-btn>
        <v-btn to="/main/profile/edit">Edit Profile</v-btn>
        <v-btn to="/main/profile/password">Change Password</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">

import { appName } from "@/env";
import { defineComponent } from "vue";

export default defineComponent ({
  name: "Dashboard-app",
  computed: {
    getGreetedUser() {
      const userProfile = this.$store.getters.userProfile;
      //const userProfile = readUserProfile(this.$store);
      if (userProfile) {
        if (userProfile.full_name) {
          return userProfile.full_name;
        } else {
          return userProfile.email;
        }
      }
      return "";
    }
  },
  methods: {
    greetedUser() {
      const userProfile = this.$store.getters.userProfile;
      //const userProfile = readUserProfile(this.$store);
      if (userProfile) {
        if (userProfile.full_name) {
          return userProfile.full_name;
        } else {
          return userProfile.email;
        }
      }
      return "";
    }
  }
})

</script>
