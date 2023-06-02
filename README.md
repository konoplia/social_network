# social_network

# About App
This django app is a piece of a social network. In which each user can register and log in using JWT authentication. The user can create a post and like or dislike their own and other posts. There are also endpoints for viewing statistics of likes for a certain period and user activity.

# Instalation
## Clone repo on your local machine

```bash
git clone https://github.com/konoplia/social_network.git
```
## Add .env
In root directory, need to create **.env** file.  
In this file, you need to put the secret key, which is held by the author of the project.
In .env:
```bash
SECRET_KEY="django-sectet-key"
```
## Docker run
While in the root of the project, run the following command through the terminal:
```bash
docker build . -t social_network_img 
```
and then
```bash
docker run --name social_network_cont -p 8000:8000 --mount type=bind,source="$(pwd)",target=/code -it  social_network_img
```
for stopping container press ctrl+C in terminal.

For the next run of the container use:
```bash
docker start -i social_network_cont 
```
For stopping container press ctrl+C in terminal.

## Migrations
After starting container need to apply migrations. In terminal:
```bash
docker exec -it social_network_cont bash
```
and
```bash
./manage.py makemigrations
```
and then
```sh
./manage.py migrate
```
## Populating db
## Register and Authentication
## Test
