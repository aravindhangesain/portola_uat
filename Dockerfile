# pull official base image
# FROM python:3.8.0-alpine

# consider slim due to: https://github.com/docker-library/python/issues/381
FROM python:3.11
EXPOSE 8000

# set work directory
WORKDIR /usr/src/Portola

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/Portola/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/Portola/
# CMD ["gunicorn", "-b", "0.0.0.0:8000", "--workers=4", "backend.wsgi:application", "--timeout", "1200", "--access-logfile", "-", "--error-logfile", "-"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
