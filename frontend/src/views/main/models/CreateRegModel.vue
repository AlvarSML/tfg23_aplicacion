<template>
  <v-container fluid>

      <form @submit.prevent="onSubmit" @reset.prevent="onReset">
        <v-card class="ma-3 pa-3">
          <v-card-title primary-title>
            <div class="headline primary--text">Subir modelo</div>
            <v-btn-toggle
              v-model="reg_seg"
              rounded="2"
              color="deep-purple-accent-3"
              group
            >
              <v-btn value="reg">
                Regresion
              </v-btn>

              <v-btn value="seg">
                Segmentacion
              </v-btn>

            </v-btn-toggle>
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
                v-if="reg_seg == 'reg'"
                suffix="mm"
              ></v-text-field>
              <v-text-field
                v-model="iou"
                label="IOU"
                v-if="reg_seg == 'seg'"
                suffix="%"
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

import { defineComponent } from "vue";
import { appName } from "@/env";
import { CreateRegModel } from "@/types/RegModel";
import { CreateSegModel } from "@/types/SegModel";

export default defineComponent ({
  name: "Create-RegModel",
  data() {
    return {
      appName: appName,
      name: "",
      short_desc: "",
      model_description: "",
      rmse: 0,
      iou: 0,
      reg_seg: "reg"

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
      this.iou = 0;
      this.$store.commit("setUploadRegModel",null)
    },
    cancel() {
      this.$router.back();
    },
    onFileChange(event:any) {
      this.$store.commit("setUploadRegModel",event.target.files[0])
    },
    async onSubmit() {

      if (this.reg_seg == "reg"){
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
      } else {
        const seg_model : CreateSegModel = {
          name: this.name,
          short_desc: this.short_desc,
          model_description: this.model_description,
          iou: this.iou,
          model_file: this.$store.getters.getUploadRegModel
        };
        console.log(seg_model)
        await this.$store.dispatch("uploadSegModel", seg_model)
      }
    }
  }
})

</script>
