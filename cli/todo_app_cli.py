# define functionalities
def header():
    print(" _____________________________________________________________________________________")
    print("                                    TODO LIST APP                                    ")
    print("                     A CLI based Todo-List App built with Python                     ")
    print("                               Author: Golam Afif Ahnaf                              ")
    print("                            www.github.com/golamafifahnaf                            ")
    print(" _____________________________________________________________________________________")
    print("                         << Command words for your prompt >>                         ")
    manual()
    print(" _____________________________________________________________________________________")

def manual():
    print(" >> 'ADD'      - Add a new task (ADD <Your_Task>). Ex: ADD Do the homework.")
    print(" >> 'DELETE'   - Delete a task (DELETE <Task_Number>). Ex: DELETE 2")
    print(" >> 'COMPLETE' - Select the completed task (COMPLETE <Task_Number>). Ex: COMPLETE 3")
    print(" >> 'UPDATE'   - Rewrite a task (UPDATE <task_number>). Ex: UPDATE 1")
    print(" >> 'SHOW'     - Show all tasks.")
    print(" >> 'HELP'     - Show the command words.")
    print(" >> 'END'      - Close the app. All remaining tasks will be removed.")

def show_task(todo_list):
    if not todo_list:
        return " >> There is no task in the list."
    else:
        result = []
        for i in range(len(todo_list)):
            result.append(f"    <{i+1}> {todo_list[i]}")
        return "\n".join(result)

def add_task(val):
    task = val.strip()

    if not task:
        return {
            "done"  : False,
            "msg"   : "Invalid Task!",
            "tasks" : None
        }
    
    todo_list.append(task)

    return {
        "done"  : True,
        "msg"   : "Task added successfully!",
        "tasks" : todo_list.copy()
    }

def complete_task(val):
    try:
        task_num = int(val.strip())
    except ValueError:
        return {
            "done"  : False,
            "msg"   : "Invalid input! Task number must be an integer.",
            "tasks" : None
        }
        
    if len(todo_list) == 0:
        return {
            "done"  : False,
            "msg"   : "There is no task in the list.",
            "tasks" : None
        }
    elif task_num not in range(1, len(todo_list) + 1):
        return {
            "done"  : False,
            "msg"   : "Invalid task no.! Please select a valid task you want to complete!",
            "tasks" : todo_list.copy()
        }
    else:
        todo_list.pop(task_num - 1)
        return {
            "done"  : True,
            "msg"   : f"Task - {task_num} completed successfully!",
            "tasks" : todo_list.copy()
        }

def delete_task(val):
    try:
        task_num = int(val.strip())
    except ValueError:
        return {
            "done"  : False,
            "msg"   : "Invalid input! Task number must be an integer.",
            "tasks" : None
        }
        
    if len(todo_list) == 0:
        return {
            "done"  : False,
            "msg"   : "There is no task in the list.",
            "tasks" : None
        }
    elif task_num not in range(1, len(todo_list) + 1):
        return {
            "done"  : False,
            "msg"   : "Invalid task no.! Please select a valid task you want to delete!",
            "tasks" : todo_list.copy()
        }
    else:
        todo_list.pop(task_num - 1)

        return {
            "done"  : True,
            "msg"   : f"Task - {task_num} deleted successfully!",
            "tasks" : todo_list.copy()
        }

def update_task(val):
    try:
        task_num = int(val.strip())
    except ValueError:
        return {
            "done"  : False,
            "msg"   : "Invalid input! Task number must be an integer.",
            "tasks" : None
        }

    if len(todo_list) == 0:
        return {
            "done"  : False,
            "msg"   : "There is no task in the list.",
            "tasks" : None
        }
    elif task_num not in range(1, len(todo_list) + 1):
        return {
            "done"  : False,
            "msg"   : "Invalid task no.! Please select a valid task you want to update!",
            "tasks" : todo_list.copy()
        }
    else:
        while True:
            updated_task = input(" >> Updated task >> ").strip()
            if updated_task:
                todo_list[task_num - 1] = updated_task
                return {
                    "done"  : True,
                    "msg"   : f"Task - {task_num} updated successfully!",
                    "tasks" : todo_list.copy()
                }
            else:
                return {
                    "done"  : False,
                    "msg"   : "Task cannot be empty. Please write something!",
                    "tasks" : todo_list.copy()
                }

def footer():
    print(" >> Thanks for using me. I hope you've completed your tasks. See you again!          ")
    print("_____________________________________________________________________________________")

def main():
    header()
    while True:
        command = input(" >> ").strip().split(maxsplit=1)
        cmd = command[0]
        val = command[1] if len(command) > 1 else ""

        if not cmd:
            print(" >> Error! Please write something!")

        elif cmd == "SHOW":
            print(show_task(todo_list))

        elif cmd == "ADD":
            result = add_task(val)
            print(" >>", result["msg"])
            if result["done"] == True:
                print(" >> Updated Task List:")
                print(show_task(result["tasks"]))

        elif cmd == "COMPLETE":
            result = complete_task(val)
            print(" >>", result["msg"])
            if result["done"] == True:
                print(" >> Updated Task List:")
                print(show_task(result["tasks"]))

        elif cmd == "DELETE":
            result = delete_task(val)
            print(" >>", result["msg"])
            if result["done"] == True:
                print(" >> Updated Task List:")
                print(show_task(result["tasks"]))

        elif cmd == "UPDATE":
            result = update_task(val)
            print(" >>", result["msg"])
            if result["done"] == True:
                print(" >> Updated Task List:")
                print(show_task(result["tasks"]))

        elif cmd == "HELP":
            manual()

        elif cmd == "END":
            footer()
            break

        else:
            print(" >> Unknown Command!")

# Main App
todo_list = []
main()