/* Creacion de la store */
import { createStore } from 'vuex'

/* legacy */
import Vue from "vue";

import { mainModule } from "./main";
import { State } from "./state";
import { adminModule } from "./admin";
import { inferenceModule } from "./inference";


export const store = createStore ({
  modules: {
    main: mainModule,
    admin: adminModule,
    inference: inferenceModule
  }
})


