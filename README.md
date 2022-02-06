# Avto Saransk Tatem
---
## Описание 
Avto Saransk - пример интернет магазина в моем портфолио(клон авито). [Ссылка на сайт](https://avtosaransk.herokuapp.com)
---
## Мотивация создание 
1. Научится работать с параметрами в ссылке.
2. Оточить навыки дизайна.
3. Научится работать с облачным хранилище.
4. Предоставить подобный проект в портфолио.
---
## Инструкция по запуску 
1. Скопируйте репозиторий, и установите зависимость:
```bash
git clone https://github.com/Daniil-7/Tatem-Avto-Saransk.git
cd Tatem-Avto-Saransk
pip install -r requirements.txt
```
2. Зарегистрируйтесь на cloudinary.
3. В файле ./hello/models.py измените имя облака, api ключ и секретный ключ:
```python
cloudinary.config(
  cloud_name = "ваше имя облака",
  api_key = "ваш ключ от api",
  api_secret = "ваш секретный ключ от api"
)
```
4. Создание суперпользователя:
```bash
python manage.py createsuperuser
```
5. Миграция и запуск:
```bash
python manage.py migrate
puthon manage.py runserver
```
6. Создайте новые записи в панели администрации, по ссылке: http://127.0.0.1:8000/admin/login/?next=/admin
7. При диплои проекта не забудьте установить ключ:
файл ./gettingstarted/settings.py:
```python
SECRET_KEY = "ваш ключ"
```
---
## Использованные технологии
1. Python 3.10.2
2. Django 4.0
3. cloudinary 1.29.0
---
## Примечание 
1. [Ссылка на сайт проекта]( https://avtosaransk.herokuapp.com)
2. [Сайт портфолио](https://tatem.pythonanywhere.com)
