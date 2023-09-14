<template>
  <v-container fluid>

    <form @submit.prevent="onSubmit" @reset.prevent="onReset">
      <v-card class="ma-3 pa-3">
        <v-card-title primary-title>
          <div class="headline primary--text">Edit User</div>
        </v-card-title>
        <v-card-text>
          <div class="my-3">
            <div class="subheading secondary--text text--lighten-2">Username</div>
            <div v-if="user" class="title primary--text text--darken-2">
              {{ user.email }}
            </div>
            <div v-else class="title primary--text text--darken-2">-----</div>
          </div>

          <v-text-field v-model="fullName" label="Full Name" required :error-messages="errors"></v-text-field>


          <v-text-field v-model="email" label="E-mail" type="email" :error-messages="errors" required></v-text-field>

          <div class="subheading secondary--text text--lighten-2">
            User is superuser
            <span v-if="isSuperuser">(currently is a superuser)</span><span v-else>(currently is not a superuser)</span>
          </div>
          <v-checkbox v-model="isSuperuser" label="Is Superuser"></v-checkbox>
          <div class="subheading secondary--text text--lighten-2">
            User is active <span v-if="isActive">(currently active)</span><span v-else>(currently not active)</span>
          </div>
          <v-checkbox v-model="isActive" label="Is Active"></v-checkbox>
          <v-row align="center">
            <v-col class="flex-shrink-1">
              <v-checkbox v-model="setPassword" class="mr-2"></v-checkbox>
            </v-col>
            <v-col>

              <v-text-field v-model="password1" :disabled="!setPassword" type="password" label="Set Password"
                :error-messages="errors">
              </v-text-field>

              <v-text-field v-model="password2" type="password" :disabled="!setPassword" label="Confirm Password"
                :error-messages="errors">
              </v-text-field>

            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="cancel">Cancel</v-btn>
          <v-btn type="reset">Reset</v-btn>
          <v-btn type="submit"> Save </v-btn>
        </v-card-actions>
      </v-card>
    </form>

  </v-container>
</template>

<script lang="ts">

import { IUserProfileUpdate } from "@/interfaces";
import { defineComponent } from "vue";
import { appName } from "@/env";

export default defineComponent({
  name: "Create-User",
  data() {
    return {
      appName: appName,
      valid: false,
      fullName: "",
      email: "",
      isActive: true,
      isSuperuser: false,
      setPassword: false,
      password1: "",
      password2: "",
      errors:""
    }
  },
  computed: {
    user() {
      console.log("user:",this.$store.getters.adminOneUser(this.$route.params.id)); 
      return this.$store.getters.adminOneUser(this.$route.params.id)
    }
  },
  async mounted() {
    await this.$store.dispatch("actionGetUsers")
    this.onReset();
  },
  methods: {
    onReset() {
      this.setPassword = false;
      this.password1 = "";
      this.password2 = "";
      if (this.user) {
        this.fullName = this.user.full_name;
        this.email = this.user.email;
        this.isActive = this.user.is_active;
        this.isSuperuser = this.user.is_superuser;
      }      
    },
    cancel() {
      this.$router.back();
    },
    async onSubmit() {
      const updatedProfile: IUserProfileUpdate = {};
      if (this.fullName) {
        updatedProfile.full_name = this.fullName;
      }
      if (this.email) {
        updatedProfile.email = this.email;
      }
      updatedProfile.is_active = this.isActive;
      updatedProfile.is_superuser = this.isSuperuser;
      if (this.setPassword) {
        updatedProfile.password = this.password1;
      }
      if (this.user) {
        await this.$store.dispatch("actionUpdateUser", {
          id: this.user.id,
          user: updatedProfile
        });
      }
      this.$router.push("/main/admin/users");
    }
  }
});

</script>