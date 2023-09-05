/**
 * ? Crea el modulo principal agrupoandolo todo
 * tr://vuex.vuejs.org/guide/modules.html
 */

import mutations from "./mutations";
import { getters } from "./getters";
import { actions } from "./actions";
import { ModelState } from "./state";

const defaultState: ModelState = {
  models: [],
  reg_models: [],
  seg_models: []
};

export const models = {
  state: defaultState,
  mutations: mutations,
  actions: actions,
  getters: getters
};
