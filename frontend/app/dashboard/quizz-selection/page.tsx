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
  const [medicalYears, setMedicalYears] = useState<MedicalYear[]>([]);
  const [selectedSubject, setSelectedSubject] = useState<string>("");
  const [subjects, setSubjects] = useState<MultiSelectType[]>([]);

  useEffect(() => {
    fetchMedicalYears().then(setMedicalYears);
  }, []);

  function handleMedicalYearSelection(medicalYear: string) {
    setSelectedSubject("");
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

      <div className="flex flex-col items-start w-[250px]">
        <label className="mb-1 text-sm font-medium text-gray-700">
          Subject(s)
        </label>
        <Select onValueChange={setSelectedSubject}>
          <SelectTrigger className="w-full">
            <SelectValue placeholder="Select Subject" />
          </SelectTrigger>
          <SelectContent>
            {subjects.map((subject) => (
              <SelectItem key={subject?.value} value={subject?.value}>
                {subject?.label}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>
    </form>
  );
}
