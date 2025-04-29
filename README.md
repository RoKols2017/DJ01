# 🧪 Учебный Django-проект: Многостраничный сайт

Простой учебный проект на Django с 3 статичными страницами: **главная**, **страница данных** и **тестовая страница**, каждая оформлена в отдельном шаблоне с навигацией.

## 🚀 Стек технологий

- ```Python 3.13````
- ```Django 5.2````

## 🛠️ Установка

1. Клонируй репозиторий:
   ```
   git clone https://github.com/your-username/learn_project.git
   cd learn_project
   ```

2. Создай виртуальное окружение:
   ```
   python -m venv .venv
   source .venv/bin/activate       # Linux/macOS
   .venv\Scripts\activate          # Windows
   ```

3. Установи Django:
   ```
   pip install django
   ```

4. Применить миграции:
   ```
   python manage.py migrate
   ```

5. Запусти сервер:
   ```
   python manage.py runserver
   ```

## 🌐 Доступные маршруты

- `````` — главная страница (`home.html`)
- ```/data``` — страница данных (`data.html`)
- ```/page3``` — тестовая страница (`test.html`)

## 📁 Структура проекта

```
learn_project/
├── pages/
│   ├── templates/
│   │   └── pages/
│   │       ├── home.html
│   │       ├── data.html
│   │       └── test.html
│   ├── urls.py
│   └── views.py
├── learn_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── manage.py
```

## ✨ Особенности

- Простая маршрутизация через ```pages/urls.py````
- Шаблоны HTML хранятся в ```templates/pages``` директории
- На страницах /data и /page3 есть ссылка «← На главную»
- Идеален для начала изучения Django

## 📄 Лицензия

Проект предназначен для обучения. Используй, изменяй и улучшай как хочешь!

