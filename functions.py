FILE = 'todos.txt'


def read_file(filepath=FILE):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_file(todos_list, filepath=FILE):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_list)
