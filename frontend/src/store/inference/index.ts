/**
 * ? Crea el modulo principal agrupoandolo todo
 * tr://vuex.vuejs.org/guide/modules.html
 */

import { mutations } from "./mutations";
import { getters } from "./getters";
import { actions } from "./actions";
import { InferenceState } from "./state";

const defaultState: InferenceState = {
  image: null,
  imageUrl: "",
  modelSegmentation: "seg.onnx",
  modelRegression: "reg.onnx"
};

export const inferenceModule = {
  state: defaultState,
  mutatios: mutations,
  actions: actions,
  getters: getters
};
