import { ComponentType, ReactElement } from "react";

export type MedicalYear = {
  id: string;
  label: string;
  theory_questions_count: number;
  clinical_cases_count: number;
};

export type MedicalYearsResponse = {
  medical_years: MedicalYear[];
};

export type Subject = {
  id: string;
  name: string;
  theory_questions_count: number;
  clinical_cases_count: number;
};

export type SubjectsResponse = {
  subjects: Subject[];
};

export type MultiSelectType = {
  value: string;
  label: string;
  icon?: React.ComponentType<{ className?: string }>;
};
