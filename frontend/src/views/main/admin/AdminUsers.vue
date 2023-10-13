<script setup lang="ts">
import { computed, onMounted } from "vue";
import { useStore } from "vuex";
import { IUserProfile } from "@/interfaces"
import router from "@/router";

const store = useStore();

onMounted(() => {
  store.dispatch("actionGetUsers")
})

const users = computed(() => {
  return store.getters.adminUsers;
});

const headers = [
  {
    title: "Nombre",
    sortable: true,
    key: "full_name",
    align: "left"
  },
  {
    title: "Email",
    sortable: true,
    key: "email",
    align: "left"
  },
  {
    title: "Está activo",
    sortable: true,
    key: "is_active",
    align: "left"
  },
  {
    title: "Es administrador",
    sortable: true,
    key: "is_superuser",
    align: "left"
  },
  {
    title: "Editar",
    key: "actions",
    sortable: false,
    align: "right"
  }
];

function navigate(item:any ){
  console.log("item",item)
  router.push({ name: 'main-admin-users-edit', params: { id: item.raw.id } })
}
</script>

<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title> Gestion de usuarios </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/users/create">Crear usuario</v-btn>
    </v-toolbar>

    <v-data-table :headers="headers" :items="users">
      <template v-slot:[`item.is_active`]="{ item }">
        <v-icon v-if="item.raw.is_active">mdi-check</v-icon>
      </template>

      <template v-slot:[`item.is_superuser`]="{ item }">
        <v-icon v-if="item.raw.is_superuser">mdi-check</v-icon>
      </template>

      <template v-slot:[`item.actions`]="{ item }">   
        
        <v-btn
          icon="mdi-pencil"
          @click='navigate(item)'
        >
        </v-btn>
      </template>
    </v-data-table>
  </div>
</template>
