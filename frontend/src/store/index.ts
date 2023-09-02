/* Creacion de la store */

import Vue from "vue";
import Vuex, { StoreOptions } from "vuex";

import { mainModule } from "./main";
import { State } from "./state";
import { adminModule } from "./admin";
import { inferenceModule } from "./inference";

Vue.use(Vuex);

const storeOptions: StoreOptions<State> = {
  modules: {
    main: mainModule,
    admin: adminModule,
    inference: inferenceModule
  }
};

export default new Vuex.Store<State>(storeOptions);
