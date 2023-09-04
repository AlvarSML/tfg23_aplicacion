import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '.@/views/HomeView.vue'
import RouterComponent from '@/router'
import { store } from "@/store"

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    component: () => import(/* webpackChunkName: "start" */ "@/views/main/Start.vue"),
    children: [
      {
        path: "login",
        name: "login",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
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
          requiresAuth: false
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
            meta: {
              requiresAdmin: true
            },
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
console.log(store)
router.beforeEach((to, from, next) => {
  // Si necesita estar logueado
  if (to.meta.requiresAuth) {
    // Si no está logueado, redirige a login
    if (store) {
      console.log("no logueado")
      next({ name: "login" });
    } else {
      // Si está logueado, continua con el ruteo
      next();
    }
  } else {
    // Si no necesita estar logueado, continua con el ruteo
    next();
  }
});

export default router
