/* eslint-disable */
/*
  Para permitir cambios de estado
  Solo deberia de hacer falta para los cambios de imagen
*/
import { Model } from "@/types/Model";
import { ModelState } from "./state";
import { State } from "../state";

const mutations = {
  setUploadRegModel(state: ModelState, payload: File) {
    state.upload_reg_model = payload;
  },
  setUploadSegModel(state: ModelState, payload: File) {
    state.upload_seg_model = payload;
  },
};

export default mutations

// eslint-disable-next-line @typescript-eslint/no-explicit-any
// Ejemplos
//const { commit } = getStoreAccessors<MainState | any, State>("");

//export const commitSetDashboardMiniDrawer = commit(mutations.setDashboardMiniDrawer);
