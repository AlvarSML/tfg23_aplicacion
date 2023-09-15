import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '.@/views/HomeView.vue'
import RouterComponent from '@/router'
import { store } from "@/store"

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    component: () => import(/* webpackChunkName: "start" */ "@/views/main/Start.vue"),
    redirect: { name: 'login' },
    children: [
      {
        path: "login",
        name: "login",
        component: () => import(/* webpackChunkName: "login" */ "@/views/Login.vue")
      },
      {
        path: "recover-password",
        component: () =>
          import(
            /* webpackChunkName: "recover-password" */ "@/views/PasswordRecovery.vue"
          )
      },
      {
        path: "reset-password",
        component: () =>
          import(/* webpackChunkName: "reset-password" */ "@/views/ResetPassword.vue")
      },
      {
        path: "main",
        component: () =>
          import(/* webpackChunkName: "main" */ "@/views/main/Main.vue"),
        meta: {
          requiresAuth: true
        },
        children: [
          {
            path: "dashboard",
            component: () =>
              import(
                /* webpackChunkName: "main-dashboard" */ "@/views/main/Dashboard.vue"
              )
          },
          {
            path: "profile",
            //component: RouterComponent,
            redirect: "profile/view",
            children: [
              {
                path: "view",
                component: () =>
                  import(
                    /* webpackChunkName: "main-profile" */ "@/views/main/profile/UserProfile.vue"
                  )
              },
              {
                path: "edit",
                component: () =>
                  import(
                    /* webpackChunkName: "main-profile-edit" */ "@/views/main/profile/UserProfileEdit.vue"
                  )
              },
              {
                path: "password",
                component: () =>
                  import(
                    /* webpackChunkName: "main-profile-password" */ "@/views/main/profile/UserProfileEditPassword.vue"
                  )
              }
            ]
          },
          {
            path: "admin",
            component: () =>
              import(
                /* webpackChunkName: "main-admin" */ "@/views/main/admin/Admin.vue"
              ),
            redirect: "admin/users/all",
            children: [
              {
                path: "users",
                redirect: "users/all"
              },
              {
                path: "users/all",
                component: () =>
                  import(
                    /* webpackChunkName: "main-admin-users" */ "@/views/main/admin/AdminUsers.vue"
                  )
              },
              {
                path: "users/edit/:id",
                name: "main-admin-users-edit",
                component: () =>
                  import(
                    /* webpackChunkName: "main-admin-users-edit" */ "@/views/main/admin/EditUser.vue"
                  )
              },
              {
                path: "users/create",
                name: "main-admin-users-create",
                component: () =>
                  import(
                    /* webpackChunkName: "main-admin-users-create" */ "@/views/main/admin/CreateUser.vue"
                  )
              },
              {
                path: "models",
                name: "main-admin-models",
                component: () =>
                  import(
                    /* webpackChunkName: "main-admin-users-create" */ "@/views/main/models/Models.vue"
                  )
              },
              {
                path: "models/all",
                name: "main-admin-models-all",
                component: () =>
                  import(
                    /* webpackChunkName: "main-admin-users-create" */ "@/views/main/models/Models.vue"
                  )
              },
              {
                path: "models/create",
                name: "main-admin-models-create",
                component: () =>
                  import(
                    /* webpackChunkName: "main-admin-users-create" */ "@/views/main/models/CreateRegModel.vue"
                  )
              }
            ]
          },
          {
            path: "radiografias",
            name: "radiografias",
            component: () =>
              import(/* webpackChunkName: "Radiografias" */ "@/views/Radiografias.vue")
          }
        ]
      }
    ]
  },
  {
    path: "/*",
    redirect: "/"
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// Global navigation guard, sustituye a los anteriores
console.log("loguado", store.getters.isLoggedIn)

router.beforeEach(async (to, from) => {
  await store.dispatch("actionCheckLoggedIn");
})

export default router
