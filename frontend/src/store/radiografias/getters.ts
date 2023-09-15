/*
  ?
  Solo para almacenar los getter para elemetos complejos
*/
//import { InferenceState } from "./state";
//import { getStoreAccessors } from "vuex-typescript";
//import { State } from "../state";

import { RadiografiasState } from "./state";
import { State } from "../state";

export const getters = {
  imageProcessed: (state: RadiografiasState) => state.imageProcessed,
  imagePreview: (state: RadiografiasState) => state.imagePreview,
};

//const { read } = getStoreAccessors<MainState, State>("");

//export const readDashboardMiniDrawer = read(getters.dashboardMiniDrawer);
