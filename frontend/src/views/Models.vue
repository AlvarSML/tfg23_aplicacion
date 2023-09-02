<template>
    <div>
        <v-toolbar light>
            <v-toolbar-title> Gestion de modelos </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn color="primary" to="TODO">Nuevo Modelo</v-btn>
        </v-toolbar>
        
   </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { ref } from "vue";

import RegModel from "../types/RegModel"

@Component
export default class Models extends Vue {
  public jobs= ref<RegModel[]>([])
  public models = ref<RegModel[]>([
    { 
      id:1,
      name:"Modelo1",
      short_desc:"Loren ipsum",
      model_description:"string|null",
      rmse:.56
    },
    { 
      id:2,
      name:"Modelo1",
      short_desc:"Loren ipsum",
      model_description:"string|null",
      rmse:.56
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
    },
  ];
}
</script>