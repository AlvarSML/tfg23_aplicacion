<template>
  <div>
    <v-snackbar v-model="show" auto-height :color="currentNotificationColor">
      <v-progress-circular
        v-show="showProgress"
        class="ma-2"
        indeterminate
      ></v-progress-circular
      >{{ currentNotificationContent }}
      <template action="{ attrs }">
        <v-btn v-bind="$attrs"  @click.native="close">Close</v-btn>
      </template>
    </v-snackbar>
  </div>
</template>
<script lang="ts">

import { AppNotification } from "@/store/main/state";
import { appName } from "@/env";
import { defineComponent } from "vue";

export default defineComponent ({
  name: "Notification-Manager",
  data() {
    return{
      show: false,
      text: "",
      showProgress: false
    }
  },
  computed: {
    currentNotification():AppNotification {
      return this.$store.getters.currentNotification;
    },
    firstNotification():AppNotification {
      return this.$store.getters.firstNotification;
    },
    currentNotificationContent():string {
      return (this.currentNotification.content) || "";
    },
    currentNotificationColor():string {
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
        //this.currentNotification = false;
      }
    }
  },
  watch: {
    async onNotificationChange(newNotification: AppNotification | false) {
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

