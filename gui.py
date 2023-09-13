import time
from modules import functions
import PySimpleGUI as sg

clock = sg.Text("", key="clock")
label = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip="Enter Todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, delete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("DATE: %b%d,%Y   TIME: %H:%M:%S"))

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window["todos"].update(values=todos)

    elif event == "Edit":
        try:
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window['todo'].update(value="")
        except IndexError:
            sg.popup("Please select a Todo first", font=('Helvetica', 20))

    elif event == "Delete":
        try:
            todo_to_delete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_delete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        except IndexError:
            sg.popup("Please select a Todo first", font=('Helvetica', 20))

    elif event == "Exit":
        break
    elif event == "todos":
        window["todo"].update(value=values["todos"][0])

    elif event == sg.WIN_CLOSED:
        break

window.close()
