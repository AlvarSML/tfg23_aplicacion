<template>
  <v-container fluid>

      <form @submit.prevent="onSubmit" @reset.prevent="onReset">
        <v-card class="ma-3 pa-3">
          <v-card-title primary-title>
            <div class="headline primary--text">Subir modelo de regresion</div>
          </v-card-title>
          <v-card-text>
              <v-text-field
                v-model="name"
                label="Nombre"
                required
              ></v-text-field>
              <v-text-field
                v-model="short_desc"
                label="Descripcion breve"
                required
              ></v-text-field>
              <v-text-field
                v-model="model_description"
                label="Detalles"
                required
              ></v-text-field>
              <v-text-field
                v-model="rmse"
                label="RMSE"
                required
              ></v-text-field>
          </v-card-text>
          <v-file-input
            clearable
            label="Modelo ONNX"
            variant="filled"
            prepend-icon="mdi-database"
            accept=".onnx"
            @change="onFileChange"
          ></v-file-input>
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

import { IUserProfileCreate } from "@/interfaces";
import { defineComponent } from "vue";
import { appName } from "@/env";
import { RegModel, CreateRegModel } from "@/types/RegModel";

export default defineComponent ({
  name: "Create-RegModel",
  data() {
    return {
      appName: appName,
      name: "",
      short_desc: "",
      model_description: "",
      rmse: 0

    }
  },
  async mounted() {
    await this.$store.dispatch("actionGetUsers")
    //dispatchGetUsers(this.$store);
    this.onReset();
  },
  methods: {
    onReset() {
      this.name = "";
      this.short_desc = "";
      this.model_description = "";
      this.rmse = 0;
      this.$store.commit("setUploadRegModel",null)
    },
    cancel() {
      this.$router.back();
    },
    onFileChange(event:any) {
      this.$store.commit("setUploadRegModel",event.target.files[0])
    },
    async onSubmit() {
      const reg_model : CreateRegModel = {
        name: this.name,
        short_desc: this.short_desc,
        model_description: this.model_description,
        rmse: this.rmse,
        model_file: this.$store.getters.getUploadRegModel
      };
      console.log(reg_model)
      await this.$store.dispatch("uploadRegModel", reg_model)
      //this.$router.push("/main/admin/models/all");
    }
  }
})

</script>
