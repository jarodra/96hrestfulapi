# Dockerfile frontend
FROM ubuntu
RUN apt-get -y update && apt-get -y install nginx
VOLUME /usr/share/nginx/html
VOLUME /etc/nginx
COPY index.html /usr/share/nginx/html/index.html
COPY js/ /usr/share/nginx/html/js/
COPY nginx.conf /etc/nginx/sites-available/default
EXPOSE 8080
#RUN chown www-data /usr/share/nginx/html/
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]