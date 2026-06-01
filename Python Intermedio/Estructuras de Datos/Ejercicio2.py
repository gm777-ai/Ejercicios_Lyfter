class PersonNode:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.previous = None


class PeopleDeque:
    def __init__(self):
        self.left = None
        self.right = None

    def push_left(self, name):
        new_person = PersonNode(name)

        if self.left is None:
            self.left = new_person
            self.right = new_person
            return

        new_person.next = self.left
        self.left.previous = new_person
        self.left = new_person

    def push_right(self, name):
        new_person = PersonNode(name)

        if self.right is None:
            self.left = new_person
            self.right = new_person
            return

        new_person.previous = self.right
        self.right.next = new_person
        self.right = new_person

    def pop_left(self):
        if self.left is None:
            raise Exception("El deque está vacío. No se puede hacer pop_left.")

        removed_name = self.left.name

        if self.left == self.right:
            self.left = None
            self.right = None
            return removed_name

        self.left = self.left.next
        self.left.previous = None

        return removed_name

    def pop_right(self):
        if self.right is None:
            raise Exception("El deque está vacío. No se puede hacer pop_right.")

        removed_name = self.right.name

        if self.left == self.right:
            self.left = None
            self.right = None
            return removed_name

        self.right = self.right.previous
        self.right.next = None

        return removed_name

    def print_deque(self):
        if self.left is None:
            print("El deque está vacío.")
            return

        current_person = self.left

        print("Personas en el deque:")

        while current_person is not None:
            print(current_person.name)
            current_person = current_person.next


people = PeopleDeque()

people.push_right("Carlos")
people.push_right("Maria")
people.push_left("Ana")
people.push_left("Luis")

people.print_deque()

removed_left = people.pop_left()
print("Persona removida por la izquierda:", removed_left)

removed_right = people.pop_right()
print("Persona removida por la derecha:", removed_right)

people.print_deque()