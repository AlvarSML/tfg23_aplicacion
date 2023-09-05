<template>
  <div>
    <v-toolbar>
      <v-toolbar-title> Gestion de modelos </v-toolbar-title>
      <v-divider class="mx-4" inset vertical></v-divider>

      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/models/create">Nuevo Modelo</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="models" item-value="name" item-key="id">
      <template v-slot:[`item.actions`]="{ item }">
        <v-btn class="mx-2" fab dark small color="indigo-lighten-2" @click="selectModel(item)">
          Activar
        </v-btn>
      </template>


    </v-data-table>

  </div>
</template>

<script lang="ts">

import { ref } from "vue";
import { appName } from "@/env";
import { defineComponent } from "vue";
import { RegModel } from "@/types/RegModel";


export default defineComponent({
  name: "Models-list",
  data() {
    return {
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
        },
        {
          title: "Ubicacion",
          sortable: true,
          key: "file_path",
          align: "left"
        },
        { title: 'Actions', key: 'actions', sortable: false }

      ],
      msg: ""
    }
  },
  computed: {
    models() {
      return this.$store.getters.getModels
    }
  },
  methods: {
    selectModel(item:any){
      console.log(item.raw.id)
    }
  },
  mounted() {
    this.$store.dispatch("getModels")
  }
})
</script>