import sys  # Модуль для работы с аргументами командной строки
import os  # Модуль для работы с файловой системой
import shutil  # Модуль для копирования файлов
from collections import defaultdict  # Импорт defaultdict для удобного счёта повторяющихся файлов

input_dir = sys.argv[1]  # Путь к входной директории передаётся первым аргументом
output_dir = sys.argv[2]  # Путь к выходной директории передаётся вторым аргументом

try:
    max_depth = int(sys.argv[3])  # Пробуем получить максимальную глубину обхода
except (IndexError, ValueError):
    max_depth = None  # Если аргумент не указан или некорректен, глубина не ограничена

os.makedirs(output_dir, exist_ok=True)  # Создаём выходную директорию, если её ещё нет

name_counts = defaultdict(int)  # Словарь для подсчёта количества файлов с одинаковыми именами

def relative_depth(root, path):
    return os.path.relpath(path, root).count(os.sep)  # Вычисляем глубину относительно корня

for current_root, dirs, files in os.walk(input_dir):  # Обходим все папки и файлы внутри input_dir
    if max_depth is not None and relative_depth(input_dir, current_root) >= max_depth:
        dirs[:] = []  # Если глубина превышает допустимую, останавливаем обход вглубь
        continue  # Переходим к следующей итерации

    for file in files:  # Проходим по каждому файлу в текущей директории
        full_path = os.path.join(current_root, file)  # Полный путь к файлу
        base_name, ext = os.path.splitext(file)  # Разделяем имя файла и его расширение
        count = name_counts[file]  # Сколько раз уже встречался файл с таким именем

        if count == 0:
            new_name = file  # Если файл первый раз, имя остаётся без изменений
        else:
            new_name = f"{base_name}{count}{ext}"  # Если имя уже встречалось, добавляем число к имени

        name_counts[file] += 1  # Увеличиваем счётчик для этого имени

        destination = os.path.join(output_dir, new_name)  # Куда копировать файл в output_dir
        shutil.copy2(full_path, destination)  # Копируем файл с сохранением метаданных