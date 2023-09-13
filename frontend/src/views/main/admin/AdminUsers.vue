<script setup lang="ts">
import { computed, onMounted } from "vue";
import { useStore } from "vuex";
import { IUserProfile } from "@/interfaces"

const store = useStore();

onMounted(() => {
  store.dispatch("actionGetUsers")
})

const users = computed(() => {
  console.log(store.getters.adminUsers);
  return store.getters.adminUsers;
});

const headers = [
  {
    title: "Name",
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
    title: "Full Name",
    sortable: true,
    key: "full_name",
    align: "left"
  },
  {
    title: "Is Active",
    sortable: true,
    key: "is_active",
    align: "left"
  },
  {
    title: "Is Superuser",
    sortable: true,
    key: "is_superuser",
    align: "left"
  },
  {
    title: "Actions",
    key: "actions",
    sortable: false
  }
];
</script>

<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title> Manage Users </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/users/create">Create User</v-btn>
    </v-toolbar>

    <v-data-table :headers="headers" :items="users">
      <template #[`item.actions`]="{ item }">
        <v-icon v-if="item.is_active">mdi-check</v-icon>
        <v-icon v-if="item.is_superuser">mdi-check</v-icon>
        <v-btn
          icon
          :to="{ name: 'main-admin-users-edit', params: { id: item.id } }"
        >
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
      </template>
    </v-data-table>
  </div>
</template>
