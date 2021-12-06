My notes:


===== DOCKER ===== docker~=20.10.8
install docker
docker version - see docker version
docker-compose version - see docker-compose version
sudo chmod 666 /var/run/docker.sock - comand for work docker
docker pull python - install python images
docker image ls

VIEWS
docker images - see all docker images
docker ps - see what container starts
docker ps -a - see all work and close containers 

CREATE
Must create dockerfile with fields (file name 'dockerfile' in Folder with project) : 
FROM python  - what images we use
RUN mkdir -p /user/src/app - (RUN) what we do, (mkdir -p) create folder 
WORKDIR /app - this work folder
COPY  . . - copy from (.) auer computer to (.) container
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8080
ENV TZ Europe/Kiev - Переменная окружения, временная зона
CMD ["python", "index.py"] - (or ENTRYPOINT ["python", "index.py"]) what we do when project start('start command Python'
and 'run index.py')

docker build -t testname . - create new docker image with name 'testname' in this directory '.'
docker run --name newname - change name of container on 'newname'

DELETE
docker rm -vf $(docker ps -aq) - delete all containers (first)
docker rmi -f $(docker images -aq) - delete all images (second)
docker rm testname - dell 'testname' images
docker rmi <your-image-id> - dell 1 2 3 images

RUN
docker run testname - start docker with name 'testname'
docker run testname (-d) - run docker 'testname' (-d - start in fon)
docker run --name testname -d --rm name - run container 'name' with imagename 'testname' and dell after exit
docker run --rm --name name -p 8080:8080 web-hello -** run container with name 'name' create from images name 'web-hello' 
and dell after exit
docker run --rm --name name -p 8080:8080 -e TZ=Europe/Kiev web-hello - **(-e TZ=Europe/Kiev - add date time in code)

SWITCH DIRECTORY
variant 1)
-v /home/warex/PycharmProjects/impression/media:/user/src/app/media web-hello - add folder in project:add folder in 
container and ('web-hello' - name of image)
variant 2)
docker volume ls - see all volume container
docker volume create testname - create volume container 'testname'
-v testname:/user/src/app/media web-hello - add folder in project:add folder in 
container and ('web-hello' - name of image)

STOP
docker stop newname - stop docker container 'newname'
docker-compose down

INSTALL REQUIREMENTS
pip install --no-cache-dir -r requirements.txt - Install all requirements
(55:20 min)


===== DJANGO REST FRAMEWORK =====
pip3 install djangorestframework - install django REST Framework
django-admin startapp api - create API app
register REST and API in INSTALLED_APPS:
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api.apps.ApiConfig',
]


===== PYTHON PROJECT =====
pwd - way of directory like /home/warex/.../
python3 --version
pip3 install python (import django in test.py) - install django with pycharm and test it
print(django.get_version()) - check django version
print('hello world') - test django works
django-admin startproject impression - create new app django
cd impression - go to main folder
python3 manage.py startapp mainimapp - create main app
register App 'mainimapp' in sittings in INSTALLED_APPS
python3 manage.py makemigrations - Django использует миграции для переноса изменений в моделях (добавление поля, удаление модели и т.д.) на структуру базы данных.
python3 manage.py migrate - Start migrate
python3 manage.py migrate mainapp zero - dell all migrations
python3 manage.py migrate mainapp 0002 - dell 0002 migration
admin.site.register(Users) - register models in admin.py
python3 manage.py createsuperuser - create Super User
python3 manage.py runserver - run server 
create models in mainapp, file models.py

pip3 install pillow - install for using models.ImageField fore pictures
pip3 install requests - for requests
pip3 install -r requirements.txt - for install requests
pip freeze | xargs pip uninstall -y - for dell requests

pip3 freeze - Чтобы получить список пакетов в проекте выполняем команду
pip3 freeze > requirements.txt - Для записи вывода в requirements.txt, Команду выполняем в корне проекта. 


===== REACT ===== 
npx create-react-app name_of_app - create React app
cd name_of_app - go to folder React app
npm start - start React app
setupTests.js, reportWebVitals.js, logo.svg, index.css, App.test.js - dell it in folder name_of_app
import logo from './logo.svg'; and <header className="App-header">...</header> - dell it in file App.js
reportWebVitals(); and import reportWebVitals from './reportWebVitals'; and import './index.css'; - dell it in index.js
App.css - dell all information
