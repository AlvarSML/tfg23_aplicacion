import { mutations } from "./mutations";
import { getters } from "./getters";
import { actions } from "./actions";
import { InferenceState } from "./state";

const defaultState: InferenceState = {
  image: null
};

export const mainModule = {
  state: defaultState,
  mutations,
  actions,
  getters
};
