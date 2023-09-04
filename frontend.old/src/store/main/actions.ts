import { api } from "@/api";
import router from "@/router";
import { getLocalToken, removeLocalToken, saveLocalToken } from "@/utils";
import axios from "axios";
//import { getStoreAccessors } from "vuex-typescript";
import { ActionContext } from "vuex";
import { State } from "../state";
/*
import {
  commitAddNotification,
  commitRemoveNotification,
  commitSetLoggedIn,
  commitSetLogInError,
  commitSetToken,
  commitSetUserProfile
} from "./mutations";
*/
import mutations from "./mutations";
import { AppNotification, MainState } from "./state";

type MainContext = ActionContext<MainState, State>;

const actions = {
  async actionLogIn(
    context: MainContext,
    payload: { username: string; password: string }
  ) {
    try {
      const response = await api.logInGetToken(payload.username, payload.password);
      const token = response.data.access_token;
      if (token) {
        saveLocalToken(token);
        mutations.setToken(context, token);
        commitSetLoggedIn(context, true);
        commitSetLogInError(context, false);
        await this.actionGetUserProfile(context);
        await this.actionRouteLoggedIn();
        commitAddNotification(context, { content: "Logged in", color: "success" });
      } else {
        await this.actionLogOut(context);
      }
    } catch (err) {
      commitSetLogInError(context, true);
      await this.actionLogOut(context);
    }
  },
  async actionGetUserProfile(context: MainContext) {
    try {
      const response = await api.getMe(context.state.token);
      if (response.data) {
        commitSetUserProfile(context, response.data);
      }
    } catch (error) {
      await this.actionCheckApiError(context, error);
    }
  },
  async actionUpdateUserProfile(context: MainContext, payload) {
    try {
      const loadingNotification = { content: "saving", showProgress: true };
      commitAddNotification(context, loadingNotification);
      const response = (
        await Promise.all([
          api.updateMe(context.state.token, payload),
          await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500))
        ])
      )[0];
      commitSetUserProfile(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        content: "Profile successfully updated",
        color: "success"
      });
    } catch (error) {
      await this.actionCheckApiError(context, error);
    }
  },
  async actionCheckLoggedIn(context: MainContext) {
    if (!context.state.isLoggedIn) {
      let token = context.state.token;
      if (!token) {
        const localToken = getLocalToken();
        if (localToken) {
          commitSetToken(context, localToken);
          token = localToken;
        }
      }
      if (token) {
        try {
          const response = await api.getMe(token);
          commitSetLoggedIn(context, true);
          commitSetUserProfile(context, response.data);
        } catch (error) {
          await this.actionRemoveLogIn(context);
        }
      } else {
        await this.actionRemoveLogIn(context);
      }
    }
  },
  async actionRemoveLogIn(context: MainContext) {
    removeLocalToken();
    commitSetToken(context, "");
    commitSetLoggedIn(context, false);
  },
  async actionLogOut(context: MainContext) {
    await this.actionRemoveLogIn(context);
    await this.actionRouteLogOut();
  },
  async actionUserLogOut(context: MainContext) {
    await this.actionLogOut(context);
    commitAddNotification(context, { content: "Logged out", color: "success" });
  },
  actionRouteLogOut() {
    if (router.currentRoute.path !== "/login") {
      router.push("/login");
    }
  },
  async actionCheckApiError(context: MainContext, payload: unknown) {
    if (axios.isAxiosError(payload)) {
      if (payload.response?.status === 401) {
        await this.actionLogOut(context);
      }
    }
  },
  actionRouteLoggedIn() {
    if (router.currentRoute.path === "/login" || router.currentRoute.path === "/") {
      router.push("/main");
    }
  },
  async removeNotification(
    context: MainContext,
    payload: { notification: AppNotification; timeout: number }
  ) {
    return new Promise((resolve, _) => {
      setTimeout(() => {
        commitRemoveNotification(context, payload.notification);
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
      commitAddNotification(context, loadingNotification);
      await Promise.all([
        api.passwordRecovery(payload.username),
        await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500))
      ]);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        content: "Password recovery email sent",
        color: "success"
      });
      await this.actionLogOut(context);
    } catch (error) {
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, { color: "error", content: "Incorrect username" });
    }
  },
  async resetPassword(
    context: MainContext,
    payload: { password: string; token: string }
  ) {
    const loadingNotification = { content: "Resetting password", showProgress: true };
    try {
      commitAddNotification(context, loadingNotification);
      await Promise.all([
        api.resetPassword(payload.password, payload.token),
        await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500))
      ]);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        content: "Password successfully reset",
        color: "success"
      });
      await this.actionLogOut(context);
    } catch (error) {
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        color: "error",
        content: "Error resetting password"
      });
    }
  }
};

// eslint-disable-next-line @typescript-eslint/no-explicit-any
// const { this.action } = getStoreAccessors<MainState | any, State>("");
/*
export const dispatchCheckApiError = dispatch(actions.actionCheckApiError);
export const dispatchCheckLoggedIn = dispatch(actions.actionCheckLoggedIn);
export const dispatchGetUserProfile = dispatch(actions.actionGetUserProfile);
export const dispatchLogIn = dispatch(actions.actionLogIn);
export const dispatchLogOut = dispatch(actions.actionLogOut);
export const dispatchUserLogOut = dispatch(actions.actionUserLogOut);
export const dispatchRemoveLogIn = dispatch(actions.actionRemoveLogIn);
export const dispatchRouteLoggedIn = dispatch(actions.actionRouteLoggedIn);
export const dispatchRouteLogOut = dispatch(actions.actionRouteLogOut);
export const dispatchUpdateUserProfile = dispatch(actions.actionUpdateUserProfile);
export const dispatchRemoveNotification = dispatch(actions.removeNotification);
export const dispatchPasswordRecovery = dispatch(actions.passwordRecovery);
export const dispatchResetPassword = dispatch(actions.resetPassword);
*/
export default actions