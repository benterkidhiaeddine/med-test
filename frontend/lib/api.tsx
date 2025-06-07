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

export async function fetchSubjects(medicalYearId) {
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/medical_years/${medicalYearId}/subjects/`
    );
    const json = await response.json();
    const subjectsList = json?.subjects || json; // adjust this if your API wraps it in a key
    console.log(subjectsList);
    return subjectsList;
  } catch (error) {
    console.error("Something went wrong while fetching subjects:", error);
    throw new Error("Failed to fetch Subjects for the selected Medical Year");
  }
}

export async function fetchChapters(subjectId) {
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/subjects/${subjectId}/chapters/`
    );
    const json = await response.json();
    const chaptersList = json?.chapters || json; // adjust this if the API wraps it differently
    return chaptersList;
  } catch (error) {
    console.error("Something went wrong while fetching chapters:", error);
    throw new Error("Failed to fetch Chapters for the selected Subject");
  }
}

export async function fetchCourses(chapterId) {
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/chapters/${chapterId}/courses/`
    );
    const json = await response.json();
    const coursesList = json?.courses || json; // Adjust if your API wraps data under a specific key
    return coursesList;
  } catch (error) {
    console.error("Something went wrong while fetching courses:", error);
    throw new Error("Failed to fetch Courses for the selected Chapter");
  }
}

export async function fetchCourseYears(courseIds) {
  try {
    const response = await fetch(
      "http://127.0.0.1:8000/courses/available_years/",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ course_id_list: courseIds }),
      }
    );

    if (!response.ok) {
      throw new Error(`Server responded with status ${response.status}`);
    }

    const json = await response.json();
    const availableYears = json?.available_years || json; // adjust if your API wraps it differently
    return availableYears;
  } catch (error) {
    console.error(
      "Something went wrong while fetching available years:",
      error
    );
    throw new Error("Failed to fetch Available Years for selected Courses");
  }
}
