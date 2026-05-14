import re


SUBJECTS = {
    "spanish": "Español",
    "english": "Inglés",
    "social_studies": "Sociales",
    "science": "Ciencias"
}


def normalize_name(full_name):
    return " ".join(full_name.strip().split())


def normalize_section(section):
    return section.strip().upper()


def is_valid_name(full_name):
    full_name = normalize_name(full_name)

    if full_name == "":
        return False

    if any(character.isdigit() for character in full_name):
        return False

    if not any(character.isalpha() for character in full_name):
        return False

    return True


def is_valid_section(section):
    section = normalize_section(section)
    pattern = r"^(1[0-2]|[1-9])[A-Z]$"

    return re.match(pattern, section) is not None


def student_exists(students, full_name, section):
    full_name = normalize_name(full_name).lower()
    section = normalize_section(section)

    for student in students:
        if student["full_name"].lower() == full_name and student["section"] == section:
            return True

    return False


def get_valid_name():
    while True:
        full_name = input("Ingrese el nombre completo del estudiante: ")
        full_name = normalize_name(full_name)

        if is_valid_name(full_name):
            return full_name

        print("Nombre inválido. No puede estar vacío ni contener números.")


def get_valid_section():
    while True:
        section = input("Ingrese la sección del estudiante, por ejemplo 11B: ")
        section = normalize_section(section)

        if is_valid_section(section):
            return section

        print("Sección inválida. Use un formato como 10A, 11B o 12C.")


def get_valid_grade(subject_name):
    while True:
        try:
            grade = float(input(f"Ingrese la nota de {subject_name}: "))

            if 0 <= grade <= 100:
                return grade

            print("La nota debe estar entre 0 y 100.")

        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")


def get_valid_student_info(students):
    while True:
        full_name = get_valid_name()
        section = get_valid_section()

        if not student_exists(students, full_name, section):
            break

        print("Ese estudiante ya existe. No se permiten estudiantes duplicados.")

    student = {
        "full_name": full_name,
        "section": section
    }

    for subject_key, subject_name in SUBJECTS.items():
        student[subject_key] = get_valid_grade(subject_name)

    return student


def get_valid_student_amount():
    while True:
        try:
            amount = int(input("¿Cuántos estudiantes desea ingresar?: "))

            if amount > 0:
                return amount

            print("Debe ingresar un número mayor que cero.")

        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")


def add_students(students):
    amount = get_valid_student_amount()

    for index in range(amount):
        print(f"\nIngresando estudiante #{index + 1}")
        student = get_valid_student_info(students)
        students.append(student)
        print("Estudiante agregado correctamente.")


def calculate_average(student):
    total = 0

    for subject_key in SUBJECTS.keys():
        total += student[subject_key]

    return total / len(SUBJECTS)


def format_grade(grade):
    if grade == int(grade):
        return str(int(grade))

    return f"{grade:.2f}"


def show_students(students):
    if len(students) == 0:
        print("No hay estudiantes registrados.")
        return

    print("\n========== Lista de Estudiantes ==========")

    for index, student in enumerate(students, start=1):
        print(f"\nEstudiante #{index}")
        print(f"Nombre completo: {student['full_name']}")
        print(f"Sección: {student['section']}")

        for subject_key, subject_name in SUBJECTS.items():
            print(f"{subject_name}: {format_grade(student[subject_key])}")

        average = calculate_average(student)
        print(f"Promedio: {average:.2f}")


def show_top_students(students):
    if len(students) == 0:
        print("No hay estudiantes registrados.")
        return

    sorted_students = sorted(
        students,
        key=calculate_average,
        reverse=True
    )

    top_students = sorted_students[:3]

    print("\n========== Top 3 Estudiantes ==========")

    for position, student in enumerate(top_students, start=1):
        average = calculate_average(student)

        print(f"\nPuesto #{position}")
        print(f"Nombre completo: {student['full_name']}")
        print(f"Sección: {student['section']}")
        print(f"Promedio: {average:.2f}")


def show_general_average(students):
    if len(students) == 0:
        print("No hay estudiantes registrados.")
        return

    total_average = 0

    for student in students:
        total_average += calculate_average(student)

    general_average = total_average / len(students)

    print(f"El promedio general de todos los estudiantes es: {general_average:.2f}")


def delete_student(students):
    if len(students) == 0:
        print("No hay estudiantes registrados.")
        return

    full_name = get_valid_name()
    section = get_valid_section()

    for student in students:
        if student["full_name"].lower() == full_name.lower() and student["section"] == section:
            print("\nEstudiante encontrado:")
            print(f"Nombre completo: {student['full_name']}")
            print(f"Sección: {student['section']}")

            confirmation = input("¿Está seguro de que desea eliminarlo? S/N: ").strip().lower()

            if confirmation == "s":
                students.remove(student)
                print("Estudiante eliminado correctamente.")
            else:
                print("Eliminación cancelada.")

            return

    print("No se encontró un estudiante con ese nombre y sección.")


def show_failed_students(students):
    if len(students) == 0:
        print("No hay estudiantes registrados.")
        return

    failed_students = []

    for student in students:
        failed_subjects = {}

        for subject_key, subject_name in SUBJECTS.items():
            if student[subject_key] < 60:
                failed_subjects[subject_name] = student[subject_key]

        if len(failed_subjects) > 0:
            failed_students.append({
                "full_name": student["full_name"],
                "section": student["section"],
                "failed_subjects": failed_subjects
            })

    if len(failed_students) == 0:
        print("No hay estudiantes reprobados.")
        return

    print("\n========== Estudiantes Reprobados ==========")

    for student in failed_students:
        print(f"\nNombre completo: {student['full_name']}")
        print(f"Sección: {student['section']}")
        print("Materias reprobadas:")

        for subject_name, grade in student["failed_subjects"].items():
            print(f"{subject_name}: {format_grade(grade)}")