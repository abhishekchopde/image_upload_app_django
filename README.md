# Containerizing a django application using Dockers
<img src="/logos/docker_logo.png" alt="Docker" title="Docker" /> 
	
This API enables a user to upload an image and store its metadata to the mongodb  database. Docker files and docker-compose files are present along with the code which we will use to containerize the applciation.

## Installations

#### Django
Create a new conda environment. And install using env.yml file or requirements.txt file. \
**Python: 3.6.9**

I am using conda environment as my python environment. Fell free to use python virtual environment if you want.
Just make sure you do required changes to the Dockerfile for installations and env activation etc. It should be pretty easy.

```(your_conda_env)$ pip install -r requirements.txt```

**Note -** If the app throws pymongo error; uninstall bson and pymongo and just reinstall pymongo. It will install the required bson version.
#### Docker
- [Docker official Installation Guide](https://docs.docker.com/engine/install/ubuntu/)
- [Docker Compose](https://docs.docker.com/compose/install/)

#### Mongodb
- [MongoDB CE (Ubuntu)](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/) - you can also look for other distributions available through Mongo

## Usage
Once all the installations are done. Lets start with running an application on your system first. For that you will need to install MongoDB on your host machine. 

Make sure you change host for Mongodb in settings.py file to localhost while running onn host machine.
```
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'test',
        'HOST': MONGODB_TEST_HOST,
        'PORT': 27017,
    }
}
# Dont forget to export env_var.sh file to have required ENV vars in your environment while running locally.
```
Now the first lets do migrations for our models. I have already included the migrations in the repo. You are free to redo them if you choose to rename the database or anything else.
Make sure you are inside your python environment and you have initiated your mongodb.

```
$ python manage.py makemigrations
$ python manage.py migrate
```
By these steps, a database with specified name (in settings.py) is created in your mongodb. You can use mongo shell and check if it has been created.

Woahh! Our app is ready to run now.

```
$ python manage.py runserver 0.0.0.0:9049
```

This should get your app running and live. You can test uploading any images and check if the changes are reflecting the database.

## Containerzing

Now its time to containerize the application and run it inside docker containers. Go through the Dockerfile and docker-compose.yml file to have an idea about how to configure these containers for your application. For deeper understanding on docker and docker-compose, visit my blog on medium:
***[Containerizing a django application using Docker and Docker Compose](https://medium.com/@logan_14/containerizing-a-django-application-using-dockers-c18cdc9a838e)***

```$ docker-compose up -d```

'-d' flag will help you run your containers and compose in detached mode(daemoning). You can check if the containers are running by,

To list all the containers which are up at the moment

``` $ docker ps```


Hope this helps. Thanks!!
