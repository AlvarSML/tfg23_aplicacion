<template>
  <div>
    <v-navigation-drawer
      v-model="showDrawer"
      persistent
      :mini-variant="miniDrawer"
      fixed
      app
    >        
      <v-list nav density="compact">
        <v-list-subheader>Menu</v-list-subheader>

        <v-list-item
          v-for="(item, i) in mainMenu"
          :key="i"
          :value="item"
          :to="item.route"
          color="primary"
        >
          <template v-slot:prepend>
            <v-icon :icon="item.icon"></v-icon>
          </template>

          <v-list-item-title v-text="item.text"></v-list-item-title>
        </v-list-item>
      </v-list>

      <v-list nav density="compact">
        <v-list-subheader>Herramientas</v-list-subheader>

        <v-list-item
          v-for="(item, i) in tools"
          :key="i"
          :value="item"
          :to="item.route"
          color="primary"
        >
          <template v-slot:prepend>
            <v-icon :icon="item.icon"></v-icon>
          </template>

          <v-list-item-title v-text="item.text"></v-list-item-title>
        </v-list-item>
      </v-list>

      <v-list v-if="isAdmin" nav density="compact">
        <v-list-subheader>Administrador</v-list-subheader>

        <v-list-item
          v-for="(item, i) in adminTools"
          :key="i"
          :value="item"
          :to="item.route"
          color="primary"
        >
          <template v-slot:prepend>
            <v-icon :icon="item.icon"></v-icon>
          </template>

          <v-list-item-title v-text="item.text"></v-list-item-title>
        </v-list-item>
      </v-list>

      <template v-slot:append>
        <div class="pa-2">
          <v-btn block @click="logout">
            <v-icon start icon="mdi-logout"></v-icon>
            Logout
          </v-btn>
        </div>
        <div class="pa-2">
          <v-btn block @click="switchMiniDrawer">
            <v-icon start>{{
              miniDrawer ? "mdi-chevron-right" : "mdi-chevron-left"
            }}</v-icon>
            Collapse            
          </v-btn>
          
        </div>
      </template>
            
    </v-navigation-drawer>
    
    <v-app-bar dark color="primary" app>
      <template v-slot:prepend>
          <v-app-bar-nav-icon @click.stop="switchShowDrawer"></v-app-bar-nav-icon>
       </template>
      <!--<v-app-bar-nav-icon variant="text" ></v-app-bar-nav-icon>-->
      <v-toolbar-title>{{ appName }}</v-toolbar-title>
      <v-spacer></v-spacer>

      <v-menu bottom left offset-y>
        <template v-slot:activator="{ props }">
          <v-btn icon v-bind="props">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-btn block @click="logout">
          <v-icon start icon="mdi-logout"></v-icon>
          Logout
        </v-btn>
        <v-btn block to="/main/profile">
          <v-icon start icon="mdi-account"></v-icon>
          Peril
        </v-btn>

      </v-menu>

    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>

    <v-footer class="pa-3" fixed app>
      <v-spacer></v-spacer>
      <span>&copy; {{ appName }}</span>
    </v-footer>
  </div>
</template>


<script lang="ts">
import { defineComponent } from "vue";
import { appName } from "@/env";

export default defineComponent ({
  name: "Main-app",
  data() {
    return {
      appName: appName,
      mainMenu: [
      { 
        text: 'Dashboard', 
        icon: 'mdi-view-dashboard', 
        route: '/main/dashboard'
      },
      { 
        text: 'Perfil', 
        icon: 'mdi-account', 
        route: '/main/profile/view'
      },
      { 
        text: 'Editar Perfil', 
        icon: 'mdi-pencil', 
        route: '/main/profile/edit'
      },
      { 
        text: 'Cambio Contraseña', 
        icon: 'mdi-key', 
        route: '/main/profile/password'
      }
      ],
      tools: [
      { 
        text: 'Endodoncia', 
        icon: 'mdi-radiology-box', 
        route: '/main/radiografias'
      },
      ],
      adminTools: [
      { 
        text: 'Gestion Usuarios', 
        icon: 'mdi-account-multiple', 
        route: '/main/admin/users/all'
      },
      { 
        text: 'Nuevo Usuario', 
        icon: 'mdi-account-plus', 
        route: '/main/admin/users/create'
      },
      { 
        text: 'Modelos', 
        icon: 'mdi-database', 
        route: {path: '/main/admin/models/all'}
      },
      { 
        text: 'Subir Modelo', 
        icon: 'mdi-database-plus', 
        route: '/main/admin/models/create'
      },
      
      ]
    }
  },
  computed: {
    showDrawer: {
      get: function() {
        return !this.$store.getters.dashboardShowDrawer
      },
      set: function() {
        this.$store.commit(
        "setDashboardShowDrawer",
        !this.$store.getters.dashboardMiniDrawer)
      }
    },
    miniDrawer() {
      return this.$store.getters.dashboardMiniDrawer
    },
    isAdmin() {
      return this.$store.getters.hasAdminAccess
    }
  },
  methods: {    
    setShowDrawer(value:any) {
      this.$store.commit("setDashboardShowDrawer",value)
    },
    switchShowDrawer() {
      console.log("drawer",this.$store.getters.dashboardShowDrawer)
      this.$store.commit(
        "setDashboardShowDrawer",
        !this.$store.getters.dashboardShowDrawer)
      //commitSetDashboardShowDrawer(this.$store, !readDashboardShowDrawer(this.$store));
    },
    switchMiniDrawer() {
      this.$store.commit(
        "setDashboardShowDrawer",
        !this.$store.getters.dashboardMiniDrawer)
      //commitSetDashboardMiniDrawer(this.$store, !readDashboardMiniDrawer(this.$store));
    },
    hasAdminAccess() {
      this.$store.getters.hasAdminAccess
      //return readHasAdminAccess(this.$store);
    },

    logout() {
      //this.$router.resolve({name:"main-admin-models-all"})
      this.$store.dispatch("actionUserLogOut")
      //await dispatchUserLogOut(this.$store);
    }
  } 
})

</script>
