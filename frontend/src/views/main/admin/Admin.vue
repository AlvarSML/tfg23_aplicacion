<template>
  <router-view></router-view>
</template>

<script lang="ts">

import { store } from "@/store";
import { defineComponent } from "vue";
import { appName } from "@/env";

export default defineComponent ({
  name: "Admin-app",
  data() {
    return {
      appName: appName
    }
  },
  beforeRouteEnter (to, from, next) {
    if (store.getters.hasAdminAccess) {
      next("/main");
    } else {
      next();
    }
  },
  beforeRouteUpdate (to, from, next) {
    if (!this.$store.getters.hasAdminAccess) {
      next("/main");
    } else {
      next();
    }
  },
})

</script>
