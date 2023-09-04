/*
  Elemento unico donde se guarda el estado de los datos
  Propio de Vuex, cada elemento puede tener su propio estado
*/

export interface RadiografiasState {
  image: File | null;
  imageUrl: string;
  modelSegmentation: string;
  modelRegression: string;
  imagePreview: File | null;
  imageProcessed: File | null;
}
