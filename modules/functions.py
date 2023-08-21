def get_todos(filepath="./files/todos.txt"):
    """
    Reads a text file and returns the to-do items
    as a list. the path of the text file given as the
    parameter "filepath"
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="./files/todos.txt"):
    """
    Writes the to-do items in the text file.
    the path of the text file given as the
    parameter "filepath"
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

