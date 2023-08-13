/* eslint-disable */
/*
  ?
  Operaciones asicronas que aplican la mutacion de un estado
  se recomienda el uso de dispatch
  ! Para llamdas al modulo de API
*/
/*
import { api } from "@/api";
import router from "@/router";
import { getLocalToken, removeLocalToken, saveLocalToken } from "@/utils";
import axios from "axios";
*/
import { getStoreAccessors } from "typesafe-vuex";
import { ActionContext } from "vuex";
import { State } from "../state";
import {} from "./mutations";
import { InferenceState } from "./state";

//type MainContext = ActionContext<InferenceState, State>;

export const actions = {};

// eslint-disable-next-line @typescript-eslint/no-explicit-any
//const { dispatch } = getStoreAccessors<InferenceState | any, State>("");

//export const dispatchCheckApiError = dispatch(actions.actionCheckApiError);
