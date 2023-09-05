<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title> Gestion de modelos </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="TODO">Nuevo Modelo</v-btn>
    </v-toolbar>


    <v-data-table 
      :headers="headers" 
      :items="models"
      item-value="name"
      item-key="id"
      >
    </v-data-table>

  </div>
</template>

<script lang="ts">

import { ref } from "vue";
import { appName } from "@/env";
import { defineComponent } from "vue";
import RegModel from "@/types/RegModel";


export default defineComponent ({
  name: "Models-list",
  data() {
    return {
      /*
      models: [
        {
          id: 1,
          name: "Modelo1",
          short_desc: "Loren ipsum",
          model_description: "string|null",
          rmse: 0.56
        },
        {
          id: 2,
          name: "Modelo1",
          short_desc: "Loren ipsum",
          model_description: "string|null",
          rmse: 0.56
        }
      ],*/
      headers: [
        {
          title: "Nombre",
          sortable: true,
          key: "name",
          align: "left"
        },
        {
          title: "Caracteristicas",
          sortable: true,
          key: "short_desc",
          align: "left"
        }
      ],
    }
  },
  computed: {
    models() {
      return this.$store.getters.getModels
    }
  },
  mounted() {
    this.$store.dispatch("getModels")
  }
})
</script>