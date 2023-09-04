<template>
  <v-container fluid>
    <validation-observer ref="observer" v-slot="{ invalid }">
      <form @submit.prevent="onSubmit" @reset.prevent="onReset">
        <v-card class="ma-3 pa-3">
          <v-card-title primary-title>
            <div class="headline primary--text">Create User</div>
          </v-card-title>
          <v-card-text>
            <validation-provider v-slot="{ errors }" name="Full Name" rules="required">
              <v-text-field
                v-model="fullName"
                label="Full Name"
                required
                :error-messages="errors"
              ></v-text-field>
            </validation-provider>
            <validation-provider
              v-slot="{ errors }"
              rules="required|email"
              name="E-mail"
            >
              <v-text-field
                v-model="email"
                label="E-mail"
                type="email"
                :error-messages="errors"
                required
              ></v-text-field>
            </validation-provider>
            <div class="subheading secondary--text text--lighten-2">
              User is superuser
              <span v-if="isSuperuser">(currently is a superuser)</span
              ><span v-else>(currently is not a superuser)</span>
            </div>
            <v-checkbox v-model="isSuperuser" label="Is Superuser"></v-checkbox>
            <div class="subheading secondary--text text--lighten-2">
              User is active <span v-if="isActive">(currently active)</span
              ><span v-else>(currently not active)</span>
            </div>
            <v-checkbox v-model="isActive" label="Is Active"></v-checkbox>
            <v-row align="center">
              <v-col>
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
                    label="Set Password"
                    :error-messages="errors"
                  ></v-text-field>
                </validation-provider>
                <validation-provider
                  v-slot="{ errors }"
                  :debounce="100"
                  name="Password confirmation"
                  vid="password2"
                  rules="required|confirmed:password1"
                >
                  <v-text-field
                    v-model="password2"
                    type="password"
                    label="Confirm Password"
                    :error-messages="errors"
                  ></v-text-field>
                </validation-provider>
              </v-col>
            </v-row>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click="cancel">Cancel</v-btn>
            <v-btn type="reset">Reset</v-btn>
            <v-btn :disabled="invalid" type="submit"> Save </v-btn>
          </v-card-actions>
        </v-card>
      </form>
    </validation-observer>
  </v-container>
</template>

<script lang="ts">

import { IUserProfileCreate } from "@/interfaces";
import { defineComponent } from "vue";
import { appName } from "@/env";

export default defineComponent ({
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
      password2: ""
    }
  },
  async mounted() {
    await this.$store.dispatch("actionGetUsers")
    //dispatchGetUsers(this.$store);
    this.onReset();
  },
  methods: {
    onReset() {
      this.password1 = "";
      this.password2 = "";
      this.fullName = "";
      this.email = "";
      this.isActive = true;
      this.isSuperuser = false;
    },
    cancel() {
      this.$router.back();
    },
    async onSubmit() {
      const success = true;
      if (!success) {
        return;
      }

      const updatedProfile: IUserProfileCreate = {
        email: this.email
      };
      if (this.fullName) {
        updatedProfile.full_name = this.fullName;
      }
      if (this.email) {
        updatedProfile.email = this.email;
      }
      updatedProfile.is_active = this.isActive;
      updatedProfile.is_superuser = this.isSuperuser;
      updatedProfile.password = this.password1;
      await this.$store.dispatch("actionCreateUser")
      //await dispatchCreateUser(this.$store, updatedProfile);
      this.$router.push("/main/admin/users");
    }
  }
})

</script>
