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

import { ActionContext } from "vuex";
import { State } from "../state";
import {} from "./mutations";
import { ModelState } from "./state";
import { api } from "@/api";
import { CreateRegModel, RegModel } from "@/types/RegModel";
import { CreateSegModel, SegModel } from "@/types/SegModel";

type ModelContext = ActionContext<ModelState ,State>;

export const actions = {
  async getModels(context: ModelContext) {
    const response = await api.getModels(context.rootState.main.token);
    context.state.models = response.data
  },
  async uploadRegModel(context: ModelContext, data: CreateRegModel) {
    const response = await api.createRegModel(context.rootState.main.token, data)
    console.log(response)
  },
  async uploadSegModel(context: ModelContext, data: CreateSegModel) {
    const response = await api.createSegModel(context.rootState.main.token, data)
    console.log(response)
  },
};
