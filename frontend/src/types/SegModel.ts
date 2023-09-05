import { Model, CreateModel } from "./Model";

export interface SegModel extends Model {
  iou: number;
}

export interface CreateSegModel extends CreateModel {
  iou: number;
}

