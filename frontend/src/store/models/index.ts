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
  seg_models: [],
  active_reg: 0,
  active_seg: 0
};

export const models = {
  state: defaultState,
  mutations: mutations,
  actions: actions,
  getters: getters
};
