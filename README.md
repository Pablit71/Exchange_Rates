# Exchange Rates

Exchange Rates - это проект на Django, который предоставляет функциональность для работы с обменными курсами валют.

## Основные компоненты

- `Exchange_Rates`: Директория с настройками проекта.
- `currency_app`: Директория с приложением для работы с валютами.
- `db.sqlite3`: Файл базы данных SQLite.
- `manage.py`: Скрипт для управления проектом Django.

## Установка

Следуйте этим шагам, чтобы установить проект локально:

1. Клонируйте репозиторий:
   `
   git clone https://github.com/Pablit71/Exchange_Rates.git
   `

2. Перейдите в директорию проекта:
   `
   cd Exchange_Rates`

3. Установите зависимости из файла requirements.txt:
   `pip install -r requirements.txt`

5. Выполните миграции базы данных:`
   python manage.py migrate`

6. Запустите команду для запроса к сайту:
`python manage.py get_rates.py`

7. Запустите сервер разработки:
   `python manage.py runserver`

## Использование

После установки вы можете открыть веб-браузер и перейти по адресу `http://localhost:8000/show_rates?date=YYYY-MM-DD`,(где YYYY-MM-DD - указываете нужную вам дату) чтобы начать работу с приложением.

