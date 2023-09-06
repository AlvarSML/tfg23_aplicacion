import { IUserProfile } from "@/interfaces";
import { MainState, AppNotification } from "./state";
import { State } from "../state";

export const mutations = {
  setToken(state: MainState, payload: string): void {
    state.token = payload;
    localStorage.setItem('token', payload);
  },
  setLoggedIn(state: MainState, payload: boolean): void {
    state.isLoggedIn = payload;
  },
  setLogInError(state: MainState, payload: boolean): void {
    state.logInError = payload;
  },
  setUserProfile(state: MainState, payload: IUserProfile): void {
    state.userProfile = payload;
  },
  setDashboardMiniDrawer(state: MainState, payload: boolean): void {
    state.dashboardMiniDrawer = payload;
  },
  setDashboardShowDrawer(state: MainState, payload: boolean): void {
    state.dashboardShowDrawer = payload;
  },
  addNotification(state: MainState, payload: AppNotification): void {
    state.notifications.push(payload);
  },
  removeNotification(state: MainState, payload: AppNotification): void {
    state.notifications = state.notifications.filter((notification) => notification !== payload);
  },
};

export default mutations;
