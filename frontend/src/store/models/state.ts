/*
  Elemento unico donde se guarda el estado de los datos
  Propio de Vuex, cada elemento puede tener su propio estado
*/
import { Model } from "@/types/Model"
import { RegModel } from "@/types/RegModel"
import { SegModel } from "@/types/SegModel"

export interface ModelState {
  models?: Model[];
  reg_models?: RegModel[];
  seg_models?: SegModel[];
  upload_reg_model?: File;
  upload_seg_model?: File;
}
