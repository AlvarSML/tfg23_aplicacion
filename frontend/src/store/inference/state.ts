/*
  Elemento unico donde se guarda el estado de los datos
  Propio de Vuex, cada elemento puede tener su propio estado
*/
//import { IUserProfile } from "@/interfaces";

export interface InferenceState {
  image: File | null,
  model: string
}
