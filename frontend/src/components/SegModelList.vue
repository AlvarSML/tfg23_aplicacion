
<template>
  <div>
    <v-toolbar>
      <v-toolbar-title> Modelos de Segmetnación </v-toolbar-title>
      <v-divider class="mx-4" inset vertical></v-divider>

      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/models/create">Nuevo Modelo</v-btn>
    </v-toolbar>
    <v-data-table 
      v-model:expanded="expanded" 
      :headers="headers" 
      :items="models" 
      item-value="id"
      :single-expand="false"      
      show-expand
      class="elevation-1">
      <template v-slot:[`item.actions`]="{ item }">
        <v-btn v-if="displayIf(item)" class="mx-2" fab dark small color="indigo-lighten-2" @click="selectModel(item)">
          Activar
        </v-btn>
        <v-btn
          v-if="!displayIf(item)"
          disabled
          class="mx-2" 
          fab 
          dark 
          small 
          color="pink" 
          @click="selectModel(item)">
          Activo
        </v-btn>
      </template>
      
      <template v-slot:[`item.delete_button`]="{ item }">
        <v-btn
          v-if="displayIf(item)"
          class="mx-2" 
          fab 
          dark 
          small 
          color="red-lighten-1" 
          density="comfortable"
          @click="deleteModel(item)"
          icon="mdi-delete-forever">          
        </v-btn>
      </template>

      <template v-slot:expanded-row="{ columns, item}">
        <tr>
        <td :colspan="columns.length">
          {{ item.raw.model_description || "Este modelo no tiene descripción" }}
        </td>
        </tr>
      </template>

    </v-data-table>
  </div>
</template>

<script lang="ts">

import { defineComponent } from "vue";


export default defineComponent({
  name: "Models-reg-list",
  data() {
    return {
      expanded: [],
      headers: [
        {
          title: "Nombre",
          sortable: true,
          key: "name",
          align: "left"
        },
        {
          title: "Caracteristicas",
          sortable: false,
          key: "short_desc",
          align: "left"
        },
        {
          title: "IOU (%)",
          sortable: true,
          key: "iou",
          align: "left"
        },        
        {
          title: "Ubicacion",
          sortable: true,
          key: "file_path",
          align: "left"
        },
        { title: 'Activar', key: 'actions', sortable: false },
        { title: 'Eliminar', key: 'delete_button', sortable: false },
        { text: '', key: 'data-table-expand' }

      ],
      msg: ""
    }
  },
  computed: {
    models() {
      return this.$store.getters.getSegModels
    }
  },
  methods: {
    selectModel(item:any){
      this.$store.dispatch("updateStateSeg",item.raw.id)
    },
    deleteModel(item:any){
      this.$store.dispatch("deleteModel",item.raw.id)
      this.$store.dispatch("getSegModels")
    },
    displayIf(item:any){      
      return item.raw.id != this.$store.getters.getSegActive
    }
  },
  mounted() {
    this.$store.dispatch("getSegModels")
  }
})
</script>