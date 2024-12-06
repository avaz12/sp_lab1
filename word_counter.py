import sys
import re
from typing import List

def read_file(filename: str) -> str:
    """Читает содержимое файла."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
        sys.exit(1)

def preprocess_text(text: str) -> List[str]:
    """Обрабатывает текст: удаляет пунктуацию, переводит в нижний регистр."""
    text = text.lower()  # Переводим в нижний регистр
    text = re.sub(r'[^\w\s]', '', text)  # Удаляем пунктуацию
    return text.split()  # Разделяем на слова

def main():
    # Проверяем аргументы командной строки
    if len(sys.argv) < 2:
        print("Использование: python word_counter.py <имя_файла>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    
    # Читаем файл
    text = read_file(input_filename)
    
    # Обрабатываем текст
    words = preprocess_text(text)
    
    print(f"Обработано слов: {len(words)}")

if __name__ == "__main__":
    main()
