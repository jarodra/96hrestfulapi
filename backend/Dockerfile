# Dockerfile backend
FROM python:3.11.1-slim
COPY ./requirements.txt /requirements.txt
WORKDIR /backend
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
RUN python -m pip install --upgrade pip
RUN mkdir /files
COPY . .
EXPOSE 5000
ENV FLASK_APP=app
CMD [ "python", "app.py"]