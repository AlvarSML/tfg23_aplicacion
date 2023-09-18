// 
import { api } from "@/api";

import { ActionContext } from "vuex";
import { IUserProfileCreate, IUserProfileUpdate } from "@/interfaces";
import { State } from "../state";
import { AdminState } from "./state";


type MainContext = ActionContext<AdminState, State>;

export const actions = {
  async actionGetUsers(context: MainContext) {
    try {
      const response = await api.getUsers(context.rootState.main.token);
      if (response) {
        context.commit("setUsers", response.data);      }
    } catch (error) {
      await context.dispatch("checkApiError",error); 
    }
  },
  async actionUpdateUser(
    context: MainContext,
    payload: { id: number; user: IUserProfileUpdate }
  ) {
    try {
      const loadingNotification = { content: "saving", showProgress: true };
      //commitAddNotification(context, loadingNotification);
      context.commit("addNotification",loadingNotification)
      const response = (
        await Promise.all([
          api.updateUser(context.rootState.main.token, payload.id, payload.user),
          await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500))
        ])
      )[0];
      //commitSetUsers(context, response.data);
      context.commit("setUser", response.data)

      //commitRemoveNotification(context, loadingNotification);
      context.commit("removeNotification",loadingNotification)

      /*
      commitAddNotification(context, {
        content: "User successfully updated",
        color: "success"
      });
      */
      context.commit("AddNotification",{
        content: "User successfully updated",
        color: "success"
      })


    } catch (error) {
      //await dispatchCheckApiError(context, error);
      await context.dispatch("checkApiError",error); 
    }
  },
  async actionCreateUser(context: MainContext, payload: IUserProfileCreate) {
    console.log("createuser", payload)
    try {
      const loadingNotification = { content: "saving", showProgress: true };
      context.commit("addNotification",loadingNotification);
      //commitAddNotification(context, loadingNotification);
      const response = (
        await Promise.all([
          api.createUser(context.rootState.main.token, payload),
          await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500))
        ])
      )[0];
      context.commit("setUser", response.data)
      context.commit("removeNotification",loadingNotification)
      context.commit("AddNotification",{
        content: "User successfully created",
        color: "success"
      })

    } catch (error) {
      //await dispatchCheckApiError(context, error);
      await context.dispatch("checkApiError",error); 
    }
  }
};

export default actions;
