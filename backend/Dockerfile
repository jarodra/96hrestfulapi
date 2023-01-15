# Dockerfile backend
FROM python:3.11.1-slim
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
RUN python -m pip install --upgrade pip
ENV FLASK_APP=app
EXPOSE 5000
COPY . .
CMD [ "python", "app.py"]