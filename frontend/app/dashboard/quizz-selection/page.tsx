import { fetchMedicalYears } from "@/app/lib/api";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

export default async function QuizzSelection() {
  const medicalYears = await fetchMedicalYears();

  return (
    <>
      <Select>
        <SelectTrigger className="w-[180px]">
          <SelectValue placeholder="Select Medical Year" />
        </SelectTrigger>
        <SelectContent>
          {medicalYears.map((year) => (
            <SelectItem key={year?.id} value={year?.id}>
              {year?.label}
            </SelectItem>
          ))}
        </SelectContent>
      </Select>
    </>
  );
}
