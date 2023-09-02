/* eslint-disable */
/*
  Para permitir cambios de estado
  Solo deberia de hacer falta para los cambios de imagen
*/
import { IUserProfile } from "@/interfaces";
import { InferenceState } from "./state";
import { getStoreAccessors } from "vuex-typescript";
import { State } from "../state";

export const mutations = {
  
};

// eslint-disable-next-line @typescript-eslint/no-explicit-any
// Ejemplos
//const { commit } = getStoreAccessors<MainState | any, State>("");

//export const commitSetDashboardMiniDrawer = commit(mutations.setDashboardMiniDrawer);
