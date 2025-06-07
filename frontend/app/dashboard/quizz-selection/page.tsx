"use client";

import React, { useEffect, useState } from "react";
import {
  Select,
  SelectTrigger,
  SelectValue,
  SelectContent,
  SelectItem,
} from "@/components/ui/select";
import { MultiSelect } from "@/components/multi-select";
import { fetchChapters, fetchMedicalYears, fetchSubjects } from "@/lib/api";
import {
  MedicalYear,
  MultiSelectType,
  Subject,
} from "../../../lib/definitions";

export default function QuizzSelection() {
  const [selectedMedicalYear, setSelectedMedicalYear] = useState<string>("");
  const [selectedSubjects, setSelectedSubjects] = useState<string[]>([]);
  const [medicalYears, setMedicalYears] = useState<MedicalYear[]>([]);
  const [subjects, setSubjects] = useState<MultiSelectType[]>([]);

  useEffect(() => {
    fetchMedicalYears().then(setMedicalYears);
  }, []);

  function handleMedicalYearSelection(medicalYear) {
    setSelectedSubjects([]);
    setSelectedMedicalYear(medicalYear);
    fetchSubjects(medicalYear).then((subjects) => {
      const labledSubjects = subjects.map((subject: Subject) => {
        return {
          label: subject.name,
          value: subject.id,
        };
      });
      setSubjects(labledSubjects);
    });
  }

  // when a medical Year is selected
  /*
  useEffect(() => {

    console.log(selectedSubjects);
    // reset the list of selected subjects
    setSelectedSubjects([]);
    console.log(selectedSubjects);

    // fetch the new subjects after selecting the medical year
    fetchSubjects(selectedMedicalYear).then((subjects) => {
      const labledSubjects = subjects.map((subject: Subject) => {
        return {
          label: subject.name,
          value: subject.id,
        };
      });
      setSubjects(labledSubjects);
    });
  }, [selectedMedicalYear]);
  */

  return (
    <form className="flex flex-col items-center gap-6 mt-10">
      {/* Medical Year */}
      <div className="flex flex-col items-start w-[250px]">
        <label className="mb-1 text-sm font-medium text-gray-700">
          Medical Year
        </label>
        <Select onValueChange={handleMedicalYearSelection}>
          <SelectTrigger className="w-full">
            <SelectValue placeholder="Select Medical Year" />
          </SelectTrigger>
          <SelectContent>
            {medicalYears.map((year) => (
              <SelectItem key={year.id} value={year.id}>
                {year.label}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>

      {/* Subjects */}
      <div className="flex flex-col items-start w-[250px]">
        <label className="mb-1 text-sm font-medium text-gray-700">
          Subject(s)
        </label>
        <MultiSelect
          options={subjects}
          onValueChange={setSelectedSubjects}
          value={selectedSubjects}
          placeholder="Select Subject(s)"
        />
      </div>
    </form>
  );
}
