<template>
  <v-main>
    <v-container fluid fill-height>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="4">
          <validation-observer ref="observer" v-slot="{ invalid }">
            <form @submit.prevent="onSubmit">
              <v-card class="elevation-12">
                <v-toolbar dark color="primary">
                  <v-toolbar-title>{{ appName }} - Password Recovery</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                  <p class="subheading">
                    A password recovery email will be sent to the registered account
                  </p>
                  <validation-provider
                    v-slot="{ errors }"
                    rules="required"
                    name="Email"
                    mode="lazy"
                  >
                    <v-text-field
                      v-model="username"
                      label="Username"
                      type="text"
                      prepend-icon="mdi-account"
                      :error-messages="errors"
                      required
                      @keyup.enter="submit"
                    ></v-text-field>
                  </validation-provider>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn @click="cancel">Cancel</v-btn>
                  <v-btn type="submit" :disabled="invalid"> Recover Password </v-btn>
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
/*
import { Component, Vue } from "vue-property-decorator";
import { appName } from "@/env";
import { dispatchPasswordRecovery } from "@/store/main/actions";
import { required } from "vee-validate/dist/rules";
import { ValidationProvider, ValidationObserver, extend } from "vee-validate";

// register validation rules
extend("required", { ...required, message: "{_field_} can not be empty" });

@Component({
  components: {
    ValidationObserver,
    ValidationProvider
  }
})
export default class Login extends Vue {
  $refs!: {
    observer: InstanceType<typeof ValidationObserver>;
  };

  public valid = true;
  public username = "";
  public appName = appName;

  public cancel() {
    this.$router.back();
  }

  public async onSubmit() {
    const success = await this.$refs.observer.validate();
    if (!success) {
      return;
    }

    dispatchPasswordRecovery(this.$store, { username: this.username });
  }
}
*/
</script>
<script lang="ts">
import { defineComponent, ref } from "vue";
import { appName } from "@/env";
import { commitAddNotification } from "@/store/main/mutations";
import { dispatchResetPassword } from "@/store/main/actions";
import { required, confirmed } from "vee-validate/dist/rules";
import { ValidationProvider, ValidationObserver } from "vee-validate";

// register validation rules
const extend = (rule) => ({
  ...rule,
  message: "{_field_} can not be empty"
});
extend("required", extend(required));
extend("confirmed", extend(confirmed));

export default defineComponent({
  name: "Password-Recovery",
  methods() {
    checkToken() {
      const token = this.$route.query.token as string;
      if (!token) {
        commitAddNotification(this.$store, {
          content: "No token provided in the URL, start a new password recovery",
          color: "error"
        });
        this.$router.push("/recover-password");
      } else {
        return token;
      }
    },
    onSubmit = async () => {
      const success = await observer.value.validate();
      if (!success) {
        return;
      }
    }
  },
  setup() {
  

    const onSubmit = async () => {
      const success = await observer.value.validate();
      if (!success) {
        return;
      }

      const token = await checkToken();
      if (token) {
        await dispatchResetPassword(this.$store, { token, password: password1.value });
        this.$router.push("/");
      }
    };

    const cancel() {
      this.$router.back();
    }

    return {
      appName,
      observer,
      password1,
      password2,
      checkToken,
      onSubmit
    };
  }
});
</script>

<style></style>
