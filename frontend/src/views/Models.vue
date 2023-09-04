<script setup lang="ts">

import { ref } from "vue";
import { appName } from "@/env";
import { defineComponent } from "vue";
import RegModel from "../types/RegModel";

const jobs = ref<RegModel[]>([]);

const models = ref<RegModel[]>([
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
]);

const headers = [
  {
    text: "Nombre",
    sortable: true,
    value: "full_name",
    align: "left"
  },
  {
    text: "Caracteristicas",
    sortable: true,
    value: "short_desc",
    align: "left"
  },
  {
    text: "Activo",
    sortable: true,
    value: "is_active",
    align: "left"
  }
];

</script>

<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title> Gestion de modelos </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="TODO">Nuevo Modelo</v-btn>
    </v-toolbar>
  </div>
</template>


