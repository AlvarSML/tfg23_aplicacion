import { SegModel } from "./SegModel";
import { RegModel } from "./RegModel";

export interface State {
  reg_model: RegModel;
  seg_model: SegModel;
  changed_by: number;
  created_date: Date;
}