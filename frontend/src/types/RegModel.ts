import { Model, CreateModel } from "./Model";

export interface RegModel extends Model {
  rmse: number;
}

export interface CreateRegModel extends CreateModel {
  rmse: number;
}
