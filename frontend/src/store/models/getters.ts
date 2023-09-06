/*
  ?
  Solo para almacenar los getter para elemetos complejos
*/

import { ModelState } from "./state";

export const getters = {
  getModels: (state: ModelState) => state.models,
  getRegModels: (state: ModelState) => state.reg_models,
  getSegModels: (state: ModelState) => state.seg_models,
  getUploadRegModel: (state: ModelState) => state.upload_reg_model,
  getUploadSegModel: (state: ModelState) => state.upload_seg_model,
  getRegActive: (state: ModelState) => state.active_reg,
  getSegActive: (state: ModelState) => state.active_seg,
};

