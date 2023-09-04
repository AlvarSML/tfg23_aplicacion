/*
  ?
  Solo para almacenar los getter para elemetos complejos
*/

import { ModelState } from "./state";

export const getters = {
  getModels: (state: ModelState) => state.models,
  getRegModels: (state: ModelState) => state.reg_models,
  getSegModels: (state: ModelState) => state.seg_models,
};

