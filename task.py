from datetime import datetime

class Task:
    """Класс, представляющий задачу"""

    def __init__(self, title: str, description: str = "", priority: str = "средний"):
        """
        Конструктор класса Task
        Args:
            title: Название задачи
            description: Описание задачи
            priority: Приоритет (низкий, средний, высокий)
        """
        self.__title = title
        self.__description = description
        self.__priority = priority
        self.__completed = False
        self.__created_at = datetime.now()
        self.__completed_at = None

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and len(new_title.strip()) > 0:
            self.__title = new_title
        else:
            raise ValueError("Название задачи не может быть пустым")

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        if isinstance(new_description, str):
            self.__description = new_description
        else:
            raise ValueError("Описание должно быть строкой")

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, new_priority):
        valid_priorities = ["низкий", "средний", "высокий"]
        if new_priority in valid_priorities:
            self.__priority = new_priority
        else:
            raise ValueError(f"Приоритет должен быть одним из: {valid_priorities}")

    @property
    def completed(self):
        return self.__completed

    @property
    def created_at(self):
        return self.__created_at

    @property
    def completed_at(self):
        return self.__completed_at

    def mark_completed(self):
        """Отметить задачу как выполненную"""
        if not self.__completed:
            self.__completed = True        # исправлено true -> True
            self.__completed_at = datetime.now()
            print(f"Задача '{self.__title}' отмечена как выполненная")
        else:
            print(f"Задача '{self.__title}' уже была выполнена")

    def __str__(self):
        """Магический метод для строкового представления задачи"""
        status = "✓" if self.__completed else "○"
        priority_symbol = {
            "низкий": "⬇️",
            "средний": "➡️",
            "высокий": "⬆️"
        }.get(self.__priority, "")
        # исправлен срез [:3 0] -> [:30]
        return f"{status} [{priority_symbol}] {self.__title} - {self.__description[:30]}..."

    def get_info(self):
        """Полная информация о задаче"""
        info = f"Задача: {self.__title}\n"
        info += f"Описание: {self.__description}\n"
        info += f"Приоритет: {self.__priority}\n"
        info += f"Создана: {self.__created_at.strftime('%d.%m.%Y %H:%M')}\n"
        if self.__completed:
            info += f"Выполнена: {self.__completed_at.strftime('%d.%m.%Y %H:%M')}"
        else:
            info += "Статус: Не выполнена"
        return info

from task import Task

class ImportantTask(Task):
    """Класс для важных задач (наследник Task)"""

    def __init__(self, title: str, description: str = "", deadline: str = "сегодня"):
        """
        Конструктор важной задачи
        Args:
            title: Название задачи
            description: Описание
            deadline: Дедлайн
        """
        # Вызываем конструктор родителя с приоритетом "высокий"
        super().__init__(title, description, priority="высокий")
        self.__deadline = deadline
        self.__reminder_set = False  # исправлено false -> False

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, new_deadline):
        if isinstance(new_deadline, str) and len(new_deadline.strip()) > 0:
            self.__deadline = new_deadline
        else:
            raise ValueError("Дедлайн не может быть пустым")

    def set_reminder(self):
        """Установить напоминание"""
        self.__reminder_set = True   # исправлено true -> True
        print(f"🔔 Напоминание установлено для задачи '{self.title}'")

    # Переопределяем метод __str__
    def __str__(self):
        """Переопределенный метод для важных задач"""
        base_str = super().__str__()
        reminder = "🔔" if self.__reminder_set else "⏰"
        return f"{base_str} [Дедлайн: {self.__deadline}] {reminder}"

    # Переопределяем метод get_info
    def get_info(self):
        """Расширенная информация для важной задачи"""
        base_info = super().get_info()
        base_info += f"\nДедлайн: {self.__deadline}"
        base_info += f"\nНапоминание: {'установлено' if self.__reminder_set else 'не установлено'}"
        return base_info