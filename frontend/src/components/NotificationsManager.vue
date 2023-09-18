<template>
    <v-snackbar v-model="show" auto-height :color="currentNotificationColor" class="d-flex mb-6">
      <v-btn @click="close" icon="mdi-close" density="comfortable" color="white" class="ma-2 pa-2" v-if="!showProgress"></v-btn>
      <v-progress-circular v-show="showProgress" class="ma-2" indeterminate></v-progress-circular>
      {{ currentNotificationContent }}
      
    </v-snackbar>
</template>

<script lang="ts">

import { AppNotification } from "@/store/main/state";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Notification-Manager",
  data() {
    return {
      show: false,
      text: "",
      showProgress: false,
      curr: null as AppNotification | null
    }
  },
  computed: {
    currentNotification: {
      get: function () {
        return this.curr;
      },
      set: function (val) {
        this.curr = val
      }
    },
    firstNotification(): AppNotification {
      return this.$store.getters.firstNotification;
    },
    currentNotificationContent(): string {
      if (this.currentNotification != null) {
        return this.currentNotification.content
      } else {
        return ""
      }
    },
    currentNotificationColor(): string {
      return (this.currentNotification && this.currentNotification.color) || "info";
    }
  },
  methods: {
    async hide() {
      this.show = false;
      await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500));
    },
    async close() {
      await this.hide();
      await this.removeCurrentNotification();
    },
    async removeCurrentNotification() {
      if (this.currentNotification) {
        this.$store.commit("removeNotification", this.currentNotification);
      }
    },
    async setNotification(notification: AppNotification | false) {
      if (this.show) {
        await this.hide();
      }
      if (notification) {
        this.currentNotification = notification;
        this.showProgress = notification.showProgress || false;
        this.show = true;
      } else {
        this.currentNotification = null;
      }
    }
  },
  watch: {
    async firstNotification(newNotification: AppNotification | false) {
      console.log("NOTIFICACION")
      if (newNotification !== this.currentNotification) {
        await this.setNotification(newNotification);
        if (newNotification) {
          this.$store.dispatch("removeNotification", {
            notification: newNotification,
            timeout: 6500
          })
        }
      }
    }
  }
})

</script>