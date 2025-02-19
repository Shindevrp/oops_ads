class Task:
    def __init__(self,task_id,title,descripation,due_data,priority,is_completed):
        self.task_id=task_id
        self.title=title
        self.descripation=descripation
        self.due_data=due_data
        self.priority=priority
        self.is_completed=is_completed
    def mark_completed(self):
        pass
    def update_task(self,title,descripation,due_date,priority):
        pass
    def get_task_details(self):
        pass
class ToDoList:
    def __init__(self,tasks):
        self.tasks=tasks
        self.dataBase=[]
    def add_task(self,task_id,title,descripation,due_data,priority,is_completed):
        s=Task(task_id,title,descripation,due_data,priority,is_completed)
        self.dataBase.append(s)

    def remove_task(self,task,task_i):
        # for Task in self.dataBase:
        #     if task_id in 
        pass
    def get_all_tasks(self):
        for task in self.dataBase:
            print(f"All Tasks:{task}")
    def get_pending_tasks(self):
        pass
    def sort_tasks(self):
        pass
    def search_tasks(self,keyword):
        for task in self.dataBase:
            if keyword==task:
    print(f"search_tasks "{keyword}"")

try:
    todo = ToDoList()
    pass
except EOFError:
    pass


