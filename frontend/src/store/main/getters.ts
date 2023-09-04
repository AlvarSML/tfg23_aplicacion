import { MainState } from "./state";
import { State } from "../state";

export const getters = {
  hasAdminAccess: (state: MainState) => state.userProfile?.is_superuser && state.userProfile?.is_active,
  loginError: (state: MainState) => state.logInError,
  dashboardShowDrawer: (state: MainState) => state.dashboardShowDrawer,
  dashboardMiniDrawer: (state: MainState) => state.dashboardMiniDrawer,
  userProfile: (state: MainState) => state.userProfile,
  token: (state: MainState) => state.token,
  isLoggedIn: (state: MainState) => state.isLoggedIn,
  firstNotification: (state: MainState) => state.notifications?.[0]
};

export default getters;