docker run -d --name redis new_django-docker-starter_redis_1 redis-server
docker run -d --name db new_django-docker-starter_db_1 postgres
docker run -d --name worker --link redis new_django-docker-starter_worker_1
docker run -d -p 8000:8000 --name web --link db --link redis new_django-docker-starter_web_1 python manage.py runserver 0.0.0.0:8000
