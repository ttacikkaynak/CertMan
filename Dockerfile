FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /appdata/projects/dashboard
WORKDIR /appdata/projects/dashboard
ADD requirements.txt /appdata/projects/dashboard
RUN pip install -r requirements.txt
ADD . /appdata/projects/dashboard