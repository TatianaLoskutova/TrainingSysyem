ОПИСАНИЕ ПРОЕКТА

Проект Тестовое задание Backend/Django. Построение системы для обучения.

Разработчик проекта: Лоскутова Татьяна (Loskutova Tatiana)

Назначение проекта

Данный проект представляет собой API для работы с системой обучения. Он предоставляет возможность получать список продуктов, доступных для покупки, которое бы включало в себя основную информацию о продукте и количество уроков, которые принадлежат продукту. Выведение списка уроков по конкретному продукту к которому пользователь имеет доступ. Отображает статистику по продуктам. 


Технологический стек

Python - основной язык программирования.

Django - фреймворк для разработки веб-приложений.

Django REST framework - инструмент для создания веб-API на основе Django.

GIT - система контроля версий проекта

Как запустить проект:
1) Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/TatianaLoskutova/TrainingSysyem

cd trainingsystem

2) Создать и активировать виртуальное окружение:

python -m venv venv

venv/Scripts/activate

3) Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip

pip install -r requirements.txt

4) Выполнить миграции:

python manage.py migrate

5) Запустить проект:

python manage.py runserver
