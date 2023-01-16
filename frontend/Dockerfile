# Dockerfile frontend
FROM ubuntu
RUN apt-get -y update && apt-get -y install nginx
COPY . /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/sites-available/default
EXPOSE 8080
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]