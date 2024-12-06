 
import os
import sys
import subprocess

def test_word_counter():
    # Создаем тестовый файл
    with open('test_input.txt', 'w', encoding='utf-8') as f:
        f.write("Привет мир! Привет, Питон. Привет, программирование...")
    
    # Запускаем скрипт
    subprocess.run([sys.executable, 'word_counter.py', 'test_input.txt'])
    
    # Проверяем создание файлов
    assert os.path.exists('result/test_input.txt_words.txt')
    assert os.path.exists('result/test_input.txt_stat.txt')
    
    # Проверяем содержимое файла со словами
    with open('result/test_input.txt_words.txt', 'r', encoding='utf-8') as f:
        words_content = f.read()
        assert 'привет' in words_content
        assert 'мир' in words_content
    
    # Очистка
    os.remove('test_input.txt')
    os.remove('result/test_input.txt_words.txt')
    os.remove('result/test_input.txt_stat.txt')

if __name__ == '__main__':
    test_word_counter()
    print("Тест успешно пройден!")
