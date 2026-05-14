import csv
import os

from actions import (
    SUBJECTS,
    normalize_name,
    normalize_section,
    is_valid_name,
    is_valid_section,
    student_exists
)


CSV_FILE_NAME = "students.csv"


def export_students_to_csv(students):
    if len(students) == 0:
        print("No hay estudiantes para exportar.")
        return

    fieldnames = ["full_name", "section"] + list(SUBJECTS.keys())

    try:
        with open(CSV_FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for student in students:
                writer.writerow(student)

        print(f"Datos exportados correctamente al archivo {CSV_FILE_NAME}.")

    except PermissionError:
        print("No se pudo exportar el archivo porque no hay permisos suficientes.")

    except Exception as error:
        print(f"Ocurrió un error al exportar los datos: {error}")


def is_valid_imported_grade(value):
    try:
        grade = float(value)
        return 0 <= grade <= 100

    except ValueError:
        return False


def import_students_from_csv(students):
    if not os.path.exists(CSV_FILE_NAME):
        print("No existe un archivo CSV previamente exportado.")
        return

    fieldnames = ["full_name", "section"] + list(SUBJECTS.keys())

    imported_count = 0
    skipped_count = 0

    try:
        with open(CSV_FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames != fieldnames:
                print("El archivo CSV no tiene el formato correcto.")
                return

            for row in reader:
                full_name = normalize_name(row["full_name"])
                section = normalize_section(row["section"])

                if not is_valid_name(full_name):
                    skipped_count += 1
                    continue

                if not is_valid_section(section):
                    skipped_count += 1
                    continue

                if student_exists(students, full_name, section):
                    skipped_count += 1
                    continue

                valid_grades = True
                student = {
                    "full_name": full_name,
                    "section": section
                }

                for subject_key in SUBJECTS.keys():
                    if is_valid_imported_grade(row[subject_key]):
                        student[subject_key] = float(row[subject_key])
                    else:
                        valid_grades = False
                        break

                if valid_grades:
                    students.append(student)
                    imported_count += 1
                else:
                    skipped_count += 1

        print(f"Importación finalizada.")
        print(f"Estudiantes importados: {imported_count}")
        print(f"Registros omitidos: {skipped_count}")

    except PermissionError:
        print("No se pudo importar el archivo porque no hay permisos suficientes.")

    except Exception as error:
        print(f"Ocurrió un error al importar los datos: {error}")