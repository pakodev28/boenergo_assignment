## ТЗ

Задания ниже нужно выполнить используя любой веб-фреймворк Python (Flask, FastApi, Django) и любую базу данных. Результат выполнения задач нужно опубликовать на Github, Gitlab или Bitbucket, и прислать ссылку на опубликованный код.

### Первое задание

Напишите сервис, который будет находить корни квадратного уравнения *ax^2 + bx + c = 0*. Самостоятельно определите наиболее оптимальную структуру возвращаемых данных.
В качестве входных данных в сервис передаются значения *a, b, c*.

### Второе задание

Есть группа из 100 предметов. Предметы могут быть синего, зелёного и красного цвета. Известно, что предметов синего цвета сильно больше, чем предметов зелёного цвета, а предметов зелёного цвета немного больше, чем предметов красного цвета. Напишите сервис, который будет принимать номер предмета и пытаться угадать его цвет. Логику работы сервиса определите самостоятельно.



## Как развернуть проект из файла docker-compose(используется gunicorn и postgresql):
1. Склонировать проект, настроить .env файл:
    ```
    git clone git@github.com:pakodev28/boenergo_assignment.git
    ```
    ```
    cd boenergo_assignment
    ```
    ```
    cp .env.example .env
    ```
2. для запуска контейнеров:
    ```
    docker-compose up -d --build
    ```
3. Далее выполните следующие команды:
    ```
    docker-compose exec web python manage.py migrate --noinput
    ```
    ```
    docker-compose exec web python manage.py collectstatic --noinput
    ```
    Создайте суперюзера, если хотите пользоваться админкой ->
    ```
    docker-compose exec web python manage.py createsuperuser
    ```

## Доступные эндпоинты:
   Эндпоинт для генерации множества цветов с редиректом на сираницу угадывания цвета по номеру ->
    
    
    http://localhost/predictor/create_colors/
    
   Эндпоинт для решения квадратных уравнений ->
   
<<<<<<< HEAD
    http://localhost/quadratic_equations/find_quadratic_equation_roots/
=======
    http://localhost/quadratic_equations/find_quadratic_equation_roots/
>>>>>>> 53c19204163c00a1cb4d43206ebc2ad72439b7d8
