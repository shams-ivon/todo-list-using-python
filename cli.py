from modules import functions
import time

now = time.strftime("DATE: %b%d,%Y   TIME: %H:%M:%S")
print(now)

while True:
    user_actions = input("Type 'add' or 'show' or 'edit' or 'delete': ")
    user_actions = user_actions.strip()

    if user_actions.startswith("add"):
        todo = user_actions[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_actions.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            todo = f"{index + 1}. {item}"
            print(todo)

    elif user_actions.startswith("edit"):
        try:
            index = int(user_actions[5:])
            index = index - 1

            new_todo = input(f"Update the todo at serial no. {index + 1} : ")

            todos = functions.get_todos()

            todos[index] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Enter the serial number of the task you want to edit after the word 'edit'")

    elif user_actions.startswith("delete"):
        try:
            index = int(user_actions[7:])
            index = index - 1

            todos = functions.get_todos()

            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list"
            print(message)
        except IndexError:
            print("Todo with this serial does not exist!")

    elif user_actions.startswith("exit"):
        break

    else:
        print("Not a valid command!")

print("Terminated")
