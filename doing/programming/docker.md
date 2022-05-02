## Brief introduction
Docker creates isolated enviroments to run a pretty specific task. A container is not a full VM because it does not have the kernel of the OS, containers share kernels between them. An image is a template where we declare the properties of our container, we need to `run`it to create the container. The image is defined using Dockerfile, in it we write the neccesary steps to `build` our image, and then we `run` the image to set up the container. Usually the Dockerfile document calls a previous image already built and defines the new image on top of it. 

## Practical example
Let's suppose that we want to deploy the simplest web application, which should be write like:
```{php, webapp, eval=False}
<?php
echo "Hello World!"
```

So we are in our project folder and we save that file as `index.php` in a new folder called `src`. Now we need a web server to deploy this application so we are going to build a Docker container for that. To do this we have to create a `Dockerfile` that we will save with the `src` folder. To build this `Dockerfile` we can go to Dockerhub and check for the best `php` image to deploy our app, after doing this we can write the file.
```{docker, image, eval=False}
FROM php:7.0-apache
COPY src/ /var/www/html/ #this is pretty specific for this Docker image
EXPOSE 80 # The port we want to expose in our container
```

So our folders structure looks as simple as:
```{txt, structure, eval=False}
project
|___Dockerfile
|___src
    |___index.php
```

And now we can go to our sell and write:
```{bash, commands, eval=False}
cd path/to/our/project/
docker build -t hello-world . # -t let us give it a name
docker run -p 80:80 hello-world # -p connects port 80 from the host to port 80 in the container
```

We can go into our localhost:80 location and watch our application running. Not really impressive to be honest. 
It's not hard to find a massive pain, if we go to our `index.php` file and make any change, our docker container won't take care of it. To avoid this behaviour we can mount a local directory on our computer as a volume inside the container (we have also persistent volumes that we can use in docker containers). To do this.
```{bash, bettercommands, eval=False}
docker run -p 80:80 -v /Absolute/path/to/our/local/folder/:/var/www/html/ hello-world
```

And the changes that we made in our `index.php` file are shown inmediately in localhost:80. GREAT!
