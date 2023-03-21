class Stack:
    def __init__(self):
        self.__st = list()

    def __str__(self):
        # return f'{self.__st}'
        return '; '.join(self.__st)

    def push(self, elem):
        self.__st.append(elem)

    def pop(self):
        if len(self.__st) == 0:
            return None
        else:
            return self.__st.pop()


class TaskManager:

    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = list()
        if self.task:
            for i_prior in sorted(self.task.keys()):
                display.append(f'{i_prior} {self.task[i_prior]}')
        return '\n'.join(display)

    def new_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
print(manager.task)
#
# Результат:
# 1 отдохнуть
# 2 поесть; сдать дз
# 4 сделать уборку; помыть посуду