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
import { RadiografiasState } from "./state";
import { api } from "@/api";

type InferenceContext = ActionContext<RadiografiasState, State>;

export const actions = {
  async actionInference(
    context: InferenceContext,
    payload: {image: File}
  ) {

    try {
      const response = await api.getInference(payload.image).then((response)=>{
        context.commit("setImageProcessed",response.data)
        console.log("response", response.data)
      });
    } catch (err) {
      console.error(err)
    }    
  },
};
