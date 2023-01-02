import streamlit as st
import functions
import os
if not os.path.exists('todos.txt'):
    with open("todos.txt", 'w') as file:
        pass

todos = functions.read_file('todos.txt')

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo+'\n')
    functions.write_file(todos)


st.title("My Todo App")
st.subheader("This app is built to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=' ', placeholder="Add new todo....", on_change=add_todo, key='new_todo')

st.session_state