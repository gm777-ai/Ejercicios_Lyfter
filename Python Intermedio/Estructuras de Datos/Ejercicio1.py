class BookNode:
    def __init__(self, title):
        self.title = title
        self.next = None


class BookStack:
    def __init__(self):
        self.top = None

    def push(self, title):
        new_book = BookNode(title)

        new_book.next = self.top
        self.top = new_book

        print(f"Libro agregado: {title}")

    def pop(self):
        if self.top is None:
            raise Exception("No hay libros en el stack.")

        removed_book = self.top
        self.top = self.top.next

        return removed_book.title

    def print_stack(self):
        if self.top is None:
            print("El stack de libros está vacío.")
            return

        current_book = self.top

        print("Stack de libros:")

        while current_book is not None:
            print(current_book.title)
            current_book = current_book.next


books = BookStack()

books.push("Python intermedio")
books.push("Programación Orientada a Objetos")
books.push("Estructuras de Datos")

books.print_stack()

removed = books.pop()

print(f"Libro removido: {removed}")

books.print_stack()