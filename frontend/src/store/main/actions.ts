// 
import { api } from "@/api";
// 
import router from "@/router";
import { ActionContext } from "vuex";
import { State } from "../state";
import axios from "axios";
// 
import { getLocalToken, saveLocalToken, removeLocalToken } from "@/utils"

import { AppNotification, MainState } from "./state";

type MainContext = ActionContext<MainState, State>;

export const actions = {
  async actionGetUserProfile(context: MainContext) {
    try {
      const response = await api.getMe(context.state.token);
      if (response.data) {
        await context.commit("setUserProfile", response.data);
      }
    } catch (error) {
      context.dispatch("actionCheckApiError",error);
    }
  },
  async actionUpdateUserProfile(context: MainContext, payload: any) {
    try {
      const loadingNotification = { content: "saving", showProgress: true };
      await context.commit("addNotification", loadingNotification);
      const response = (
        await Promise.all([
          api.updateMe(context.state.token, payload),
          await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500))
        ])
      )[0];
      await context.commit("setUserProfile", response.data);
      await context.commit("removeNotification", loadingNotification);
      await context.commit("addNotification", {
        content: "Profile successfully updated",
        color: "success"
      });
    } catch (error) {
      await context.dispatch("actionCheckApiError",error);
    }
  },
  async actionCheckLoggedIn(context: MainContext) {
    if (!context.state.isLoggedIn) {
      let token = context.state.token;
      if (!token) {
        const localToken = getLocalToken();
        if (localToken) {
          await context.commit("setToken", localToken);
          token = localToken;
        }
      }
      if (token) {
        try {
          const response = await api.getMe(token);
          await context.commit("setLoggedIn", true);
          await context.commit("setUserProfile", response.data);
        } catch (error) {
          await context.dispatch("actionRemoveLogIn");
        }
      } else {
        await context.dispatch("actionRemoveLogIn");
      }
    }
  },
  async actionRemoveLogIn(context: MainContext) {
    removeLocalToken();
    context.commit("setToken", "");
    context.commit("setLoggedIn", false);
  },
  async actionLogOut(context: MainContext) {
    await context.dispatch("actionRemoveLogIn");
    await context.dispatch("actionRouteLogOut");
  },
  async actionUserLogOut(context: MainContext) {
    await context.dispatch("actionLogOut");
    await context.commit("addNotification", { content: "Logged out", color: "success" });
  },
  actionRouteLogOut() {
    console.log("TODO")
    
  },
  async actionCheckApiError(context: MainContext, payload: any) {
    if (axios.isAxiosError(payload)) {
      if (payload.response?.status === 401) {
        await context.dispatch("actionLogOut");
      }
    }
  },
  actionRouteLoggedIn() {
    console.log(router)
    if (router.currentRoute.value.path === "/login" || router.currentRoute.value.path === "/") {
      router.push("/main/dashboard");
    }

  },
  async removeNotification(
    context: MainContext,
    payload: { notification: AppNotification; timeout: number }
  ) {
    return new Promise((resolve, _) => {
      setTimeout(() => {
        context.commit("removeNotification", payload.notification);
        resolve(true);
      }, payload.timeout);
    });
  },
  async passwordRecovery(context: MainContext, payload: { username: string }) {
    const loadingNotification = {
      content: "Sending password recovery email",
      showProgress: true
    };
    try {
      await context.commit("addNotification", loadingNotification);
      await Promise.all([
        api.passwordRecovery(payload.username),
        await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500))
      ]);
      await context.commit("removeNotification", loadingNotification);
      await context.commit("addNotification", {
        content: "Password recovery email sent",
        color: "success"
      });
      await context.dispatch("actionLogOut");
    } catch (error) {
      await context.commit("removeNotification", loadingNotification);
      await context.commit("addNotification", { color: "error", content: "Incorrect username" });
    }
  },
  async resetPassword(
    context: MainContext,
    payload: { password: string; token: string }
  ) {
    const loadingNotification = { content: "Resetting password", showProgress: true };
    try {
      await context.commit("addNotification", loadingNotification);
      await Promise.all([
        api.resetPassword(payload.password, payload.token),
        await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500))
      ]);
      await context.commit("removeNotification", loadingNotification);
      await context.commit("addNotification", {
        content: "Password successfully reset",
        color: "success"
      });
      await context.dispatch("actionLogOut");
    } catch (error) {
      await context.commit("removeNotification", loadingNotification);
      await context.commit("addNotification", {
        color: "error",
        content: "Error resetting password"
      });
    }
  },
  async actionLogIn(
    context: MainContext,
    payload: { username: string; password: string }    
  ) {
    try {
      const response = await api.logInGetToken(payload.username, payload.password);
      const token = response.data.access_token;
      if (token) {
        await context.commit("setToken", token);
        await context.commit("setLoggedIn", true);
        await context.commit("setLogInError", false);
        context.dispatch("actionGetUserProfile");
        context.dispatch("actionRouteLoggedIn");
        await context.commit("addNotification", { content: "Logged in", color: "success" });
      } else {
        await context.dispatch("actionLogOut");
      }
    } catch (err) {
      console.log()
      context.commit("setLogInError", true);
      await context.dispatch("actionLogOut")

    }
  }
};

export default actions;
  
