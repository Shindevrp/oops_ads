class Task:
    def __init__(self,task_id,title,descripation,due_data,priority,is_completed):
        self.task_id=task_id
        self.title=title
        self.descripation=descripation
        self.due_data=due_data
        self.priority=priority
        self.is_completed=is_completed
    def mark_completed(self):
        self.is_completed = True
    def update_task(self,title,descripation,due_date,priority):
        self.title = title
        self.description = descripation
        self.due_date = due_date
        self.priority = priority
    def get_task_details(self):
        pass
class ToDoList:
    def __init__(self,tasks):
        self.tasks=[]
        # self.dataBase=[]
    def add_task(self,task_id,title,descripation,due_data,priority,is_completed):
        s=Task(task_id,title,descripation,due_data,priority,is_completed)
        self.tasks.append(s)

    def remove_task(self,task,task_i):
        # for Task in self.dataBase:
        #     if task_id in 
        pass
    def get_all_tasks(self):
        for task in self.dataBase:
            print(f"All Tasks:{task}")
    def get_pending_tasks(self):
        print("Pending Tasks:")
        for task in self.tasks:
            if not task.is_completed:
                print(task)
        print()
    def sort_tasks(self):
        pass
    def search_tasks(self,keyword):
        # for task in self.dataBase:
        #     # if keyword==task:
            #     print(f"search_tasks "{keyword}"")
 






try:
    todo = ToDoList()
    while True:
        i = input().strip()
        if not i:
            break
        cmd = i.split("(")
        action = cmd[0].strip()
        params = eval("(" + cmd[1]) if len(cmd) > 1 else ()

        if action == "add_task":
            todo.add_task(*params)
        elif action == "get_all_tasks":
            todo.get_all_tasks()
        elif action == "mark_completed":
            todo.mark_completed(*params)
        elif action == "get_completed_tasks":
            todo.get_completed_tasks()
        elif action == "remove_task":
            todo.remove_task(*params)
        elif action == "update_task":
            todo.update_task(*params)
        elif action == "get_pending_tasks":
            todo.get_pending_tasks()
        elif action == "sort_tasks":
            todo.sort_tasks(*params)
        elif action == "search_tasks":
            todo.search_tasks(*params)
except EOFError:
    pass







# while True:
#     try:
#         todo = ToDoList()
#         i=input().split(")")
#         i=
#         if i==" ":
#             break
#         if 

#     except EOFError:
#         break


