import function
from function import get_todos,write_todos
import PySimpleGUI
import time
import os


if not os.path.exists('todos.txt'):
    with open('todos.txt','w') as file:
        pass

PySimpleGUI.theme('Topanga')
clock = PySimpleGUI.Text('',key='clock')
label = PySimpleGUI.Text("Enter your to-do item")
input_box = PySimpleGUI.InputText(tooltip="Enter a todo",key='todo')
add_buttom = PySimpleGUI.Button('Add')
list_box =PySimpleGUI.Listbox(values =get_todos(), key ='todos_value',
                              enable_events=True , size=(45,10))

edit_button = PySimpleGUI.Button('Edit')

complete_buttom = PySimpleGUI.Button('complete')

exit_button = PySimpleGUI.Button('Exist')


window=PySimpleGUI.Window('My-To-Do-app',
                          layout=[[clock],[label],
                                  [input_box,add_buttom],
                                  [list_box,edit_button],
                                  [complete_buttom,exit_button]],
                          font=('Helviteca',20))

#Reading
while True:
    event,values =window.read(timeout=200)
    window["clock"].update(value=time.strftime('%b %d,%Y %H:%M %S'))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = get_todos()
            new_todos = values['todo'] + '\n'
            todos.append(new_todos)
            write_todos(todos)
            window['todos_value'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos_value'][0]
                new_todo = values['todo']
                todos= get_todos()
                index_number= todos.index(todo_to_edit)
                todos[index_number]= new_todo
                write_todos(todos)
                window['todos_value'].update(values=todos)

            except IndexError:
               PySimpleGUI.popup('select a  value to edit',font=('Helviteca',26))




        case "complete":
            try:
                completed_todos= values['todos_value'][0]
                updated_todos=get_todos()
                updated_todos.remove(completed_todos)
                write_todos(updated_todos)

                window['todos_value'].update(values=updated_todos)

                window['todo'].update(value='')
            except IndexError:
                PySimpleGUI.popup('Select value you completed',font=('Helviteca',25))


        case 'Exist':
            break



        case 'todos_value':
            window['todo'].update(value=values['todos_value'][0])


        case PySimpleGUI.WIN_CLOSED:
            break


window.close()