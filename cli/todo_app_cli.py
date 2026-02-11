from storage import load_tasks, save_tasks
from colorama import Fore, Style, init
init(autoreset=True)

### UI Section

# Header Design
def header():
    print(Style.DIM + ' *'*40)
    print(f"{Style.BRIGHT}{Fore.MAGENTA}                                      TODO-APP")
    print(f"                   A Command based Todo-List CLI built with Python")
    print(f"                               Author: Golam Afif Ahnaf")
    print(f"{Fore.CYAN}                            www.github.com/golamafifahnaf")
    print(Style.DIM + ' *'*40)
    print(f"{Fore.MAGENTA}                                 << COMMAND WORDS >>")
    manual()
    print(Style.DIM + ' *'*40)

def manual():
    print(f"{Style.BRIGHT}{Fore.YELLOW}                         ⚠️   Commands are case-sensitive! ⚠️")
    print(f" >> {Style.BRIGHT}{Fore.YELLOW}'ADD'{Style.RESET_ALL}      -  Add a new task (ADD <Your_Task>). Ex: ADD Do the homework.")
    print(f" >> {Style.BRIGHT}{Fore.YELLOW}'DONE'{Style.RESET_ALL}     -  Mark a task as Completed (DONE <Task_Number>). Ex: DONE 3")
    print(f" >> {Style.BRIGHT}{Fore.YELLOW}'DONE ALL'{Style.RESET_ALL} -  Mark all task(s) as Completed.")
    print(f" >> {Style.BRIGHT}{Fore.YELLOW}'UPDATE'{Style.RESET_ALL}   -  Rewrite a task (UPDATE <task_number>). Ex: UPDATE 1")
    print(f" >> {Style.BRIGHT}{Fore.YELLOW}'DLT'{Style.RESET_ALL}      -  Delete a task (DLT <Task_Number>). Ex: DLT 2")
    print(f" >> {Style.BRIGHT}{Fore.YELLOW}'DLT ALL'{Style.RESET_ALL}  -  Delete all task(s).")
    print(f" >> {Style.BRIGHT}{Fore.YELLOW}'DLT DONE'{Style.RESET_ALL} -  Delete completed task(s).")
    print(f" >> {Style.BRIGHT}{Fore.YELLOW}'SHOW'{Style.RESET_ALL}     -  Show all tasks.")
    print(f" >> {Style.BRIGHT}{Fore.YELLOW}'HELP'{Style.RESET_ALL}     -  Show the command words and their usecase.")
    print(f" >> {Style.BRIGHT}{Fore.YELLOW}'END'{Style.RESET_ALL}      -  Close the app.")

def footer():
    task_remaining = len([task for task in todo_list if not task["done"]])
    if task_remaining > 0:
        print(Style.BRIGHT + Fore.GREEN + " Your tasks are safely saved.💾")
        print(Style.BRIGHT + Fore.YELLOW + " Have a nice day! See you again!👋")
    else:
        print(Style.BRIGHT + Fore.YELLOW + "\n Have a nice day! See you again!👋")
    print(Style.DIM + ' *'*40)

def show_task(todo_list):
    if not todo_list:
        return f" >> {Fore.YELLOW}There is no task in the list."
    else:
        result = []
        for i in range(len(todo_list)):
            result.append(f'    {i+1}.{"✅" if todo_list[i]["done"] else "⏳"} {todo_list[i]["task"] if not todo_list[i]["done"] else Style.DIM + todo_list[i]["task"] + Style.RESET_ALL}')
        return "\n".join(result)

def add_task(val):
    task = val.strip()

    if not task:
        return {
            "done"  : False,
            "msg"   : "Invalid Task!",
            "tasks" : None
        }
    
    todo_list.append({"task" : task, "done" : False})
    save_tasks(todo_list)

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
    elif todo_list[task_num - 1]["done"]:
        return {
            "done": False,
            "msg": "Task already completed!",
            "tasks": todo_list.copy()
        }
    else:
        todo_list[task_num - 1]["done"] = True
        save_tasks(todo_list)

        return {
            "done"  : True,
            "msg"   : f"Task - {task_num} completed successfully!",
            "tasks" : todo_list.copy()
        }
    
def complete_all():
    global todo_list

    if len(todo_list) == 0:
        return {
            "done"  : False,
            "msg"   : "There is no task in the list.",
            "tasks" : None
        }
    
    updated_count = 0

    for task in todo_list:
        if not task["done"]:
            task["done"] = True
            updated_count += 1

    if updated_count == 0:
        return {
            "done": False,
            "msg": "All tasks are already completed.",
            "tasks": todo_list.copy()
        }

    save_tasks(todo_list)

    return {
        "done": True,
        "msg": "All task(s) marked as completed.",
        "tasks": todo_list.copy()
    }
    
def delete_completed():
    global todo_list

    if len(todo_list) == 0:
        return {
            "done"  : False,
            "msg"   : "There is no task in the list.",
            "tasks" : None
        }
    
    total_tasks = len(todo_list)
    todo_list = [task for task in todo_list if not task["done"]]
    total_completed = total_tasks - len(todo_list)

    if total_completed == 0:
        return {
            "done": False,
            "msg": "No completed tasks to delete.",
            "tasks": todo_list.copy()
        }
    
    save_tasks(todo_list)

    return {
        "done"  : True,
        "msg"   : f"{total_completed} completed task(s) deleted successfully.",
        "tasks" : todo_list.copy()
    }

def delete_all():
    global todo_list

    if len(todo_list) == 0:
        return {
            "done"  : False,
            "msg"   : "There is no task in the list.",
            "tasks" : None
        }
    
    todo_list = []
    save_tasks(todo_list)

    return {
        "done"  : True,
        "msg"   : "All task(s) deleted successfully.",
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
        save_tasks(todo_list)

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
    elif todo_list[task_num - 1]["done"]:
        return {
            "done"  : False,
            "msg"   : "You cannot update a completed task!",
            "tasks" : todo_list.copy()
        }
    else:
        while True:
            updated_task = input(" >> Updated task >> ").strip()
            if updated_task:
                todo_list[task_num - 1]["task"] = updated_task
                save_tasks(todo_list)

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

def main():
    header()
    while True:
        command = input(" >> ").strip().split(maxsplit=1)

        if not command:
            print(f" >> {Fore.RED}Error! Please write something!")
            continue

        cmd = command[0]
        val = command[1] if len(command) == 2 else ""

        if len(command) == 1 and cmd == "SHOW":
            print(show_task(todo_list))

        elif cmd == "ADD":
            result = add_task(val)
            print(f" >> {Fore.YELLOW}{result['msg']}")
            if result["done"] == True:
                print(" >> Updated Task List:")
                print(show_task(result["tasks"]))

        elif cmd == "DONE":
            if len(command) == 2 and  val == "ALL":
                result = complete_all()
            else:
                result = complete_task(val)

            print(f" >> {Fore.YELLOW}{result['msg']}")
            if result["done"] == True:
                print(" >> Updated Task List:")
                print(show_task(result["tasks"]))

        elif cmd == "DLT":
            if len(command) == 2 and  val == "DONE":
                result = delete_completed()
            elif len(command) == 2 and  val == "ALL":
                result = delete_all()
            else:
                result = delete_task(val)

            print(f" >> {Fore.YELLOW}{result['msg']}")
            if result["done"] == True:
                print(" >> Updated Task List:")
                print(show_task(result["tasks"]))

        elif cmd == "UPDATE":
            result = update_task(val)
            print(f" >> {Fore.YELLOW}{result['msg']}")
            if result["done"] == True:
                print(" >> Updated Task List:")
                print(show_task(result["tasks"]))

        elif cmd == "HELP":
            manual()

        elif cmd == "END":
            footer()
            break

        else:
            print(f" >> {Fore.RED}Unknown Command!")

# Main App
todo_list = load_tasks()
main()