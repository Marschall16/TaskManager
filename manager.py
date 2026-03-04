import json
from datetime import datetime
from task import Task, ImportantTask

class TaskManager:
    """Класс для управления списком задач"""

    def __init__(self, name: str):
        """
        Конструктор класса TaskManager
        Args:
            name: Название менеджера задач
        """
        self.__name = name
        self.__tasks = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name.strip()) > 0:
            self.__name = new_name
        else:
            raise ValueError("Название не может быть пустым")

    def add_task(self, task: Task):
        """Добавление задачи с обработкой ошибок"""
        try:
            if not isinstance(task, Task):
                raise TypeError("Можно добавлять только объекты класса Task")

            # Проверяем, нет ли уже задачи с таким названием
            for existing_task in self.__tasks:
                if existing_task.title.lower() == task.title.lower():
                    raise ValueError(f"Задача '{task.title}' уже существует")

            self.__tasks.append(task)
            print(f"✓ Задача '{task.title}' добавлена в {self.__name}")
        except TypeError as e:
            print(f"✗ Ошибка типа: {e}")
        except ValueError as e:
            print(f"✗ Ошибка значения: {e}")
        except Exception as e:
            print(f"✗ Непредвиденная ошибка: {e}")

    def remove_task(self, title: str):
        """Удаление задачи по названию"""
        for i, task in enumerate(self.__tasks):
            if task.title.lower() == title.lower():
                removed = self.__tasks.pop(i)
                print(f"Задача '{removed.title}' удалена")
                return True
        print(f"Задача '{title}' не найдена")
        return False

    def find_tasks(self, keyword: str):
        """Поиск задач по ключевому слову"""
        found = []
        for task in self.__tasks:
            if (keyword.lower() in task.title.lower() or
                    keyword.lower() in task.description.lower()):
                found.append(task)
        return found

    def get_tasks_by_priority(self, priority: str):
        """Получение задач по приоритету"""
        return [task for task in self.__tasks if task.priority == priority]

    def get_completed_tasks(self):
        """Получение выполненных задач"""
        return [task for task in self.__tasks if task.completed]

    def get_pending_tasks(self):
        """Получение невыполненных задач"""
        return [task for task in self.__tasks if not task.completed]

    def show_all_tasks(self):
        """Показать все задачи"""
        if not self.__tasks:
            print("Список задач пуст")
            return
        print(f"\n=== {self.__name} - Все задачи ===\n")
        for i, task in enumerate(self.__tasks, 1):
            print(f"{i}. {task}")

    def get_task_by_index(self, index: int):
        """Получение задачи по индексу с обработкой ошибок"""
        try:
            if not isinstance(index, int):
                raise TypeError("Индекс должен быть целым числом")
            if index < 0:
                raise IndexError("Индекс не может быть отрицательным")
            return self.__tasks[index]
        except IndexError:
            print(f"✗ Задача с индексом {index} не найдена")
            return None
        except TypeError as e:
            print(f"✗ {e}")
            return None

    def __len__(self):
        """Возвращает количество задач"""
        return len(self.__tasks)

    def __getitem__(self, index):
        """Позволяет обращаться по индексу: manager[0]"""
        return self.get_task_by_index(index)

    def __contains__(self, title):
        """Позволяет использовать 'in': if 'Купить' in manager"""
        return any(task.title.lower() == title.lower() for task in self.__tasks)

    def __str__(self):
        """Статистика по задачам"""
        total = len(self.__tasks)
        completed = len(self.get_completed_tasks())
        pending = total - completed
        return f"{self.__name}: всего {total} задач (выполнено: {completed}, осталось: {pending})"