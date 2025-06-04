export async function fetchMedicalYears() {
  try {
    const medicalYears = await fetch("http://127.0.0.1:8000/medical_years/");
    const medicalYearsJsonResponse = await medicalYears.json();
    const medicalYearsList = medicalYearsJsonResponse?.medical_years;
    return medicalYearsList;
  } catch (error) {
    console.error("Somthing went wrong in the Server", error);
    throw new Error("Failed to fetch Medical Years");
  }
}
