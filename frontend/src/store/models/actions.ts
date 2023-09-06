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
  async getRegModels(context: ModelContext) {
    const response = await api.getRegModels(context.rootState.main.token);
    context.state.reg_models = response.data
  },
  async getSegModels(context: ModelContext) {
    const response = await api.getSegModels(context.rootState.main.token);
    context.state.seg_models = response.data
  },
  async uploadRegModel(context: ModelContext, data: CreateRegModel) {
    const response = await api.createRegModel(context.rootState.main.token, data)
    console.log(response)
  },
  async uploadSegModel(context: ModelContext, data: CreateSegModel) {
    const response = await api.createSegModel(context.rootState.main.token, data)
    console.log(response)
  },
  async getState(context: ModelContext) {
    const response = await api.getState(context.rootState.main.token)
    context.state.active_reg = response.data.reg_model.id;
    context.state.active_seg = response.data.seg_model.id;
  },
  async updateStateReg(context: ModelContext, data:number) {
    const response = await api.updateStateReg(context.rootState.main.token, data)
    context.dispatch("getState")
  },
  async updateStateSeg(context: ModelContext, data:number) {
    const response = await api.updateStateSeg(context.rootState.main.token, data)
    context.dispatch("getState")
  }
  
};
