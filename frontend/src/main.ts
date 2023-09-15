import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { store } from './store'
//import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css'
import { VDataTable,
        VDataTableServer,
        VDataTableVirtual,
        } from 'vuetify/labs/VDataTable'



const vuetify = createVuetify({
  components: { ...components, VDataTable, VDataTableServer,
    VDataTableVirtual },
  directives,
})

loadFonts()

createApp(App)
  .use(router)
  .use(store)
  .use(vuetify)
  .mount('#app')
