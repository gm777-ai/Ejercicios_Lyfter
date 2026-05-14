from actions import (
    add_students,
    show_students,
    show_top_students,
    show_general_average,
    delete_student,
    show_failed_students
)

from data import export_students_to_csv, import_students_from_csv


def show_menu():
    print("\n========== Sistema de Control de Estudiantes ==========")
    print("1. Ingresar estudiantes")
    print("2. Ver todos los estudiantes")
    print("3. Ver top 3 estudiantes con mejor promedio")
    print("4. Ver promedio general de todos los estudiantes")
    print("5. Exportar datos a CSV")
    print("6. Importar datos desde CSV")
    print("7. Eliminar estudiante")
    print("8. Ver estudiantes reprobados")
    print("0. Salir")


def get_menu_option():
    valid_options = ["1", "2", "3", "4", "5", "6", "7", "8", "0"]

    while True:
        option = input("Seleccione una opción: ").strip()

        if option in valid_options:
            return option

        print("Opción inválida. Tiene que ser un valor numerico, intente de nuevo.")


def start_menu(students):
    while True:
        show_menu()
        option = get_menu_option()

        if option == "1":
            add_students(students)

        elif option == "2":
            show_students(students)

        elif option == "3":
            show_top_students(students)

        elif option == "4":
            show_general_average(students)

        elif option == "5":
            export_students_to_csv(students)

        elif option == "6":
            import_students_from_csv(students)

        elif option == "7":
            delete_student(students)

        elif option == "8":
            show_failed_students(students)

        elif option == "0":
            print("Gracias por usar el sistema. Hasta luego.")
            break