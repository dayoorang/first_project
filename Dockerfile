FROM python:3.9.0

WORKDIR /home/

RUN echo "asdfasdaasdfasdfsasdfdffdf"

RUN git clone https://github.com/yangsunkang/first_project.git

WORKDIR /home/first_project/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient


EXPOSE 8000

CMD ["bash","-c","python manage.py collectstatic --noinput --settings=first_project.settings.deploy && python manage.py migrate --settings=first_project.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=first_project.settings.deploy first_project.wsgi --bind 0.0.0.0:8000"]