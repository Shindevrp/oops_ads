class TaskItem:
    def __init__(self, item_id, name, details, deadline, priority):
        self.item_id = item_id
        self.name = name
        self.details = details
        self.deadline = deadline
        self.priority = priority
        self.is_done = False

    def completed_task(self):
        self.is_done = True

    def update_task(self, item_id, name, details, deadline, priority):
        self.item_id = item_id
        self.name = name
        self.details = details
        self.deadline = deadline
        self.priority = priority

    def display_task(self):
        if self.is_done:
            status = "Completed"
        else:
            status = "Pending"
        return f"{self.item_id}. [{status}] {self.name} - Due: {self.deadline}, Priority: {self.priority}"


class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self, task_info):
        item_id, name, details, deadline, priority = map(str, task_info)
        task = TaskItem(item_id, name, details, deadline, priority)
        self.task_list.append(task)

    def remove_task(self, item_id):
        new_list = []
        for task in self.task_list:
            if task.item_id != str(item_id):
                new_list.append(task)
        self.task_list = new_list

    def get_all_tasks(self):
        all_tasks = []
        for task in self.task_list:
            all_tasks.append(task.display_task())
        return all_tasks

    def get_pending_tasks(self):
        pending_tasks = []
        for task in self.task_list:
            if not task.is_done:
                pending_tasks.append(task.display_task())
        return pending_tasks

    def get_completed_tasks(self):
        completed_tasks = []
        for task in self.task_list:
            # print("l")
            # print(task.display_task)
            # print(task.is_done)
            if task.is_done:
                # print("K")
                completed_tasks.append(task.display_task())
        return completed_tasks

    def sort(self, criteria):
        # print(criteria)
        if criteria == "due_date":
            self.task_list.sort(key=lambda task: task.deadline)
        elif criteria == "priority":
            self.task_list.sort(key=lambda task: task.priority)

    def retrive_tasks(self, search_term):
        search_term = search_term.lower()
        searched_tasks = []
        for task in self.task_list:
            if search_term in task.name.lower() or search_term in task.details.lower():
                searched_tasks.append(task.display_task())
        return searched_tasks


def manage_task_manager():
    task_mgmt = TaskManager()

    while True:
        try:
            command = input().strip()
            # print(command)
            if command.startswith("add_task"):
                task_info = eval(command.split("add_task")[1])
                task_mgmt.add_task(task_info)

            elif command.startswith("update_task"):
                task_info = eval(command.split("update_task")[1])
                for task in task_mgmt.task_list:
                    if task.item_id == str(task_info[0]):
                        task.update_task(*task_info)

            elif command.startswith("get_all_tasks"):
                print("All Tasks:")
                for task in task_mgmt.get_all_tasks():
                    print(task)
                print()

            elif command.startswith("get_completed_tasks"):
                print("Completed Tasks:")
                # print("h")
                for task in task_mgmt.get_completed_tasks():
                    print(task)
                print()

            elif command.startswith("get_pending_tasks"):
                print("Pending Tasks:")
                for task in task_mgmt.get_pending_tasks():
                    print(task)
                print()

            elif command.startswith("mark_completed"):
                item_id = int(eval(command.split("mark_completed")[1]))
                for task in task_mgmt.task_list:
                    # print(task)
                    if task.item_id == str(item_id):
                        task.completed_task()

            elif command.startswith("remove_task"):
                item_id = eval(command.split("remove_task")[1])
                task_mgmt.remove_task(item_id)

            elif command.startswith("sort_tasks"):
                condition = eval(command.split("sort_tasks")[1])
                task_mgmt.sort(condition)
                print("All Tasks:")
                for task in task_mgmt.get_all_tasks():
                    print(task)
                print()

            elif command.startswith("search_tasks"):
                term = eval(command.split("search_tasks")[1])
                print(f"Search Results for: {term}")
                for result in task_mgmt.retrive_tasks(term):
                    print(result)
                print()

        except:
            break


if __name__ == "__main__":
    manage_task_manager()
