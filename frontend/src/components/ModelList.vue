<template>
  <v-data-table :headers="headers" :items="models">
    <!-- eslint-disable-next-line vue/valid-v-slot -->
    <template #item.is_active="{ item }">
      <v-icon v-if="item.is_active">mdi-check</v-icon>
    </template>
    <!-- eslint-disable-next-line vue/valid-v-slot -->
    <template #item.actions="{ item }">
      <v-btn
        slot="activator"
        icon
        :to="{ name: 'main-admin-users-edit', params: { id: item.id } }"
      >
        <v-icon>mdi-pencil</v-icon>
      </v-btn>
    </template>
  </v-data-table>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

import { ref } from "vue";

import RegModel from "../types/RegModel";

@Component
export default class AdminUsers extends Vue {
  public models = ref<RegModel[]>([
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

  public headers = [
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
}
</script>
