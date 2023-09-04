<script setup lang="ts">
import { ref } from "vue";
import RegModel from "../types/RegModel";

console.log("ModelList");

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
    name: "Modelo2",
    short_desc: "Loren ipsum",
    model_description: "string|null",
    rmse: 0.56
  }
]);

const headers = [
  {
    text: "Nombre",
    sortable: true,
    value: "name",
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
    value: "-",
    align: "right"
  }
];
</script>

<template>
  <div>
    <h1>Modelos</h1>
  </div>
</template>
