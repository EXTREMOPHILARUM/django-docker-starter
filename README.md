# Django-docker-starter

gunicorn + nginx + postgres + redis + celery + docker
### demo API
* `/`：member
* `/addmember/<name>`：by postgres
* `/add/<int>/<int>`：by celery

### to load and run
    chmod +x load.sh run.sh
    ./load.sh
    ./run.sh
