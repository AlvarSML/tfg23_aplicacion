export interface Model {
  id: number;
  name: string;
  short_desc: string;
  model_description: string | null;
}

export interface CreateModel {
  name: string;
  short_desc: string;
  model_description: string | null;
  model_file: File
}

