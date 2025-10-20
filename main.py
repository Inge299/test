import subprocess

def git_config_list():
    # Выполняем команду git config --global --list
    result = subprocess.run(
        ['git', 'config', '--global', '--list'],
        capture_output=True,  # Перехватываем вывод
        text=True,  # Возвращаем строку (а не байты)
        encoding='utf-8'  # Указываем кодировку
    )

    # Выводим результат
    print(result.stdout)

    # Если есть ошибка - выводим и её
    if result.stderr:
        print("Ошибка:", result.stderr)

git_config_list()

if __name__ == '__main__':
    git_config_list()