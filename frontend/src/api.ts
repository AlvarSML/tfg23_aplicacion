import axios from "axios";
import { apiUrl } from "@/env";
import { IUserProfile, IUserProfileUpdate, IUserProfileCreate } from "./interfaces";
import Model from "@/types/Model";

function authHeaders(token: string) {
  return {
    headers: {
      Authorization: `Bearer ${token}`
    }
  };
}

export const api = {
  async logInGetToken(username: string, password: string) {
    const params = new URLSearchParams();
    params.append("username", username);
    params.append("password", password);

    return axios.post(`${apiUrl}/api/v1/login/access-token`, params);
  },
  async getMe(token: string) {
    return axios.get<IUserProfile>(`${apiUrl}/api/v1/users/me`, authHeaders(token));
  },
  async updateMe(token: string, data: IUserProfileUpdate) {
    return axios.put<IUserProfile>(
      `${apiUrl}/api/v1/users/me`,
      data,
      authHeaders(token)
    );
  },
  async getUsers(token: string) {
    return axios.get<IUserProfile[]>(`${apiUrl}/api/v1/users/`, authHeaders(token));
  },
  async updateUser(token: string, userId: number, data: IUserProfileUpdate) {
    return axios.put(`${apiUrl}/api/v1/users/${userId}`, data, authHeaders(token));
  },
  async createUser(token: string, data: IUserProfileCreate) {
    return axios.post(`${apiUrl}/api/v1/users/`, data, authHeaders(token));
  },
  async passwordRecovery(email: string) {
    return axios.post(`${apiUrl}/api/v1/password-recovery/${email}`);
  },
  async resetPassword(password: string, token: string) {
    return axios.post(`${apiUrl}/api/v1/reset-password/`, {
      new_password: password,
      token
    });
  },
  // Obtener la segmentacion y las medidas de cada diente
  async getInference(image: File) {
    // eslint-disable-next-line
    console.log("Imagen",image)
    const post = axios.post(
      // eslint-disable-next-line
      `${apiUrl}/api/v1/radiogrfias/subir/`
      // eslint-disable-next-line
      ,{image: image}
      // eslint-disable-next-line
      ,{ headers: { 'Content-Type': 'multipart/form-data' }, responseType: "blob" }

    );
    console.log(post);
    return post;
  },
  async getModels(token: string) {
    return axios.get<Model[]>(`${apiUrl}/api/v1/models/`, authHeaders(token));
  }
};
