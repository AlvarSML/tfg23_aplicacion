/* eslint-disable */
/*
  Para permitir cambios de estado
  Solo deberia de hacer falta para los cambios de imagen
*/
import { IUserProfile } from "@/interfaces";
import { RadiografiasState } from "./state";
import { State } from "../state";

const mutations = {
  setImagePreview(state: RadiografiasState, payload: File) {
    state.imagePreview = payload
  },
};

export default mutations

// eslint-disable-next-line @typescript-eslint/no-explicit-any
// Ejemplos
//const { commit } = getStoreAccessors<MainState | any, State>("");

//export const commitSetDashboardMiniDrawer = commit(mutations.setDashboardMiniDrawer);
