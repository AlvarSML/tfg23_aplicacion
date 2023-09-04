/**
 * ? Crea el modulo principal agrupoandolo todo
 * tr://vuex.vuejs.org/guide/modules.html
 */

import mutations from "./mutations";
import { getters } from "./getters";
import { actions } from "./actions";
import { RadiografiasState } from "./state";

const defaultState: RadiografiasState = {
  image: null,
  imagePreview: null,
  imageProcessed: null,
  imageUrl: "",
  modelSegmentation: "seg.onnx",
  modelRegression: "reg.onnx"
};

export const radiografias = {
  state: defaultState,
  mutations: mutations,
  actions: actions,
  getters: getters
};
