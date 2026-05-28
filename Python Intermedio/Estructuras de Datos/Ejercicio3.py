class FolderNode:
    def __init__(self, folder_name):
        self.folder_name = folder_name
        self.left = None
        self.right = None


class FolderBinaryTree:
    def __init__(self, root_folder_name):
        self.root = FolderNode(root_folder_name)

    def add_left(self, parent_node, folder_name):
        if parent_node.left is not None:
            raise Exception(f"{parent_node.folder_name} ya tiene un folder a la izquierda.")

        parent_node.left = FolderNode(folder_name)

        return parent_node.left

    def add_right(self, parent_node, folder_name):
        if parent_node.right is not None:
            raise Exception(f"{parent_node.folder_name} ya tiene un folder a la derecha.")

        parent_node.right = FolderNode(folder_name)

        return parent_node.right

    def print_tree(self):
        if self.root is None:
            print("El Binary Tree está vacío.")
            return

        self._print_node(self.root, 0)

    def _print_node(self, node, level):
        if node is None:
            return

        spaces = "    " * level
        print(spaces + node.folder_name)

        self._print_node(node.left, level + 1)
        self._print_node(node.right, level + 1)


folders = FolderBinaryTree("Root")

documents = folders.add_left(folders.root, "Documents")
downloads = folders.add_right(folders.root, "Downloads")

school = folders.add_left(documents, "School")
work = folders.add_right(documents, "Work")

images = folders.add_left(downloads, "Images")
videos = folders.add_right(downloads, "Videos")

folders.print_tree()