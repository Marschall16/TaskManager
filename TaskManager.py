def save_to_file(self, filename: str = "tasks.json"):
"""Сохраняет задачи в JSON файл"""
try:
data = []
for task in self.__tasks:
task_data = {
'type': 'Important' if isinstance(task, ImportantTask) else 'Regu
lar',
'title': task.title,
'description': task.description,
'priority': task.priority,
'completed': task.completed,
'created_at': task.created_at.isoformat() if task.created_at else
None,
'completed_at': task.completed_at.isoformat() if task.completed_a
t else None
}
# Добавляем специфичные для ImportantTask поля
if isinstance(task, ImportantTask):
task_data['deadline'] = task.deadline
data.append(task_data)
with open(filename, 'w', encoding='utf-8') as f:
json.dump(data, f, ensure_ascii=False, indent=2)
print(f"✓ Задачи сохранены в файл {filename}")
except PermissionError:
print(f"✗ Нет прав для записи в файл {filename}")
except Exception as e:
print(f"✗ Ошибка при сохранении: {e}")
@classmethod
def load_from_file(cls, name: str, filename: str = "tasks.json"):
"""
Загружает задачи из JSON файла
Args:
name: Название менеджера задач
filename: Имя файла
"""
manager = cls(name)
try:
with open(filename, 'r', encoding='utf-8') as f:
data = json.load(f)
for item in data:
try:
if item['type'] == 'Important':
task = ImportantTask(
item['title'],
item['description'],
item.get('deadline', 'не указан')
)
else:
task = Task(
item['title'],
item['description'],
item['priority']
)
# Восстанавливаем состояние
if item['completed']:
task._Task__completed = true
if item['completed_at']:
task._Task__completed_at = datetime.fromisoformat(item['c
ompleted_at'])
manager._TaskManager__tasks.append(task)
except Exception as e:
print(f"✗ Ошибка при загрузке задачи {item.get('title', 'unknown
')}: {e}")
continue
print(f"✓ Загружено {len(manager)} задач из файла {filename}")
except FileNotFoundError:
print(f"✗ Файл {filename} не найден")
except json.JSONDecodeError:
print(f"✗ Ошибка формата JSON в файле {filename}")
except Exception as e:
print(f"✗ Ошибка при загрузке: {e}")
return manager