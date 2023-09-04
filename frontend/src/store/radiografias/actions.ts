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
        //context.state.imageUrl = URL.createObjectURL(blob);
        console.log("Response",response.data)
        context.state.imageUrl = URL.createObjectURL(response.data);
        context.state.imageProcessed = response.data
    })
      
      console.log(context.state.imageUrl)
    } catch (err) {
      console.error(err)
    } finally {

    }

    
  },
};
