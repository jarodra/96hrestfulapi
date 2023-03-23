# 96hrestfulapi

RESTFUL front and backend APIs.

**Backend routes**:

| Name | Methods | Description |
| ---- | ---- | ----------- |
| `/upload_images` | POST | uploads a img file (allowed formats: jpg, jpeg and png) |
| `/analyse_image/id` | GET | returns the width and height of the image specified on the id |
| `/list_images` | GET | returns a list of the images saved in the container |

## Deployment

_First, clone the repository_

```
git clone https://github.com/Durgrim/96hrestfulapi
```
_To deploy the microservices introduce the following code:_

```
cd 96hrestfulapi
docker-compose build
docker-compose up -d
```
or use the Jenkinsfile.

_Access the user documentation frontend in the address `127.0.0.1:8080`_

## Used technologies

* [Python](https://www.python.org)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/) 
* [Javascript](https://www.javascript.com)
* [HTML](https://html.spec.whatwg.org)
* [CSS](https://www.w3.org/TR/CSS/#css)
* [Docker](https://www.docker.com)
* [Git](https://git-scm.com)
* [Bootstrap](https://getbootstrap.com)
* [jQuery](https://jquery.com/)
* [nginx](https://www.nginx.com/)
* [Visual Studio Code](https://code.visualstudio.com)
* [Postman](https://www.postman.com)

## Development planning

This is going to be the initial planning for the development of both applications.

- [X] Preparation
  - [X] Flask
    - [x] Routing
    - [X] Uploading files
  - [X] nginx
- [X] Structure
  - [X] Backend
    - [X] upload_image function
    - [X] Wrong url
    - [X] list_images function
    - [X] analyse_image function
  - [X] Frontend
    - [X] HTML 
    - [X] Javascript
    - [X] CSS / Bootstrap
  - [X] Dockerizing
    - [X] Docker Compose
      - [X] Frontend app
      - [X] Backend app
      - [X] Simultaneusly

## Author ✒️

- [**Javier Rodrigo**](https://github.com/durgrim)
