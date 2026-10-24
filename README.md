# Заметки (Notes)

Простое Django-приложение для создания, просмотра и удаления заметок.

## Возможности

- Список всех заметок
- Создание заметки (заголовок + текст)
- Просмотр отдельной заметки
- Редактирование заметки
- Удаление заметки с подтверждением

## Технологии

- Django 5.0
- SQLite (база данных по умолчанию)
- Bootstrap 5 (через CDN)
- Git

## Запуск

```bash
# 1. Клонировать репозиторий
git clone <ссылка-на-репозиторий>
cd notes-app

# 2. Создать и активировать виртуальное окружение
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Применить миграции
python manage.py migrate

# 5. Запустить сервер
python manage.py runserver
```

Открыть http://127.0.0.1:8000/

## Структура проекта

```
notes-app/
├── config/
│   ├── settings.py
│   └── urls.py
├── notes/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── templates/
│   └── notes/
│       ├── list.html
│       ├── create.html
│       ├── detail.html
│       ├── edit.html
│       └── delete.html
├── .gitignore
├── requirements.txt
└── manage.py
```

## Ветки

Работа велась в отдельных ветках, которые затем слились в `main`:

- `feature/notes-list` — список заметок
- `feature/notes-create` — создание заметки
- `feature/notes-detail` — просмотр заметки
- `feature/notes-delete` — удаление заметки
- `feature/notes-edit` — редактирование заметки (дополнительное задание)
