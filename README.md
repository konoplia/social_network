# Social_network

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
For populating db by fake users and posts use script from root directory **interactive_bot**.  
From container bash run next command:
```sh
python3 interactive_bot.py
```
This bot takes configurations from **main_app.settings**
```sh
# settings for interactive bot
NUMBER_OF_USER = 10
MAX_POSTS_PER_USER = 10
MAX_LIKES_PER_USER = 10
```
and populating db fake users.  
Script has log after running:
```sh
Created 10 users
Created 73 posts
```

## Register and Authentication
For convenience, the API documentation has been implemented in the project.  
After a successful launch of the container, the [endpoint](http://localhost:8000/api/schema/docs/) will be available in the browser.

### Register
Use [register endpoint](http://localhost:8000/api/schema/docs/#/auth/auth_register_create). Push **Try it out** button and enter your data in request body:
```sh
{
  "username": "user",
  "password": "password",
  "email": "user@example.com"
}
```
You should get this server response.
```sh
{
  "success": "User 'user' created successfully"
}
```
### Login
Use [login endpoint](http://127.0.0.1:8000/api/schema/docs/#/auth/auth_register_create). Enter your credentials in request body:
```sh
{
  "username": "user",
  "password": "password",
}
```
You shoul get response with following data:
```sh
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NTg3NTc2NSwiaWF0IjoxNjg1NzAyOTY1LCJqdGkiOiI5OGZkNTBhNTZhYTk0ZDY3YWNjMmM5MDdkZDdlZTA4YyIsInVzZXJfaWQiOjI4fQ._mnDlIXRExvh0SDPiM8JGgJ_n_uRv_U47khd1vXvuuE",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1Nzg5MzY1LCJpYXQiOjE2ODU3MDI5NjUsImp0aSI6IjkyYTY5MjZmYmYyMjQwZjFhMjU0ZWZlMmVhNzRiODEyIiwidXNlcl9pZCI6Mjh9.pd5L_33xd3YNAIeI8O2shf77_cThythRUUnjAVmDzg8"
}
```
Copy "access" value without quotes, and put in the authorization window in the upper right corner. And push **Authorize** button. After that you are authorized user, and can make any request.

## Test
For run tests in container shall run command:
```sh
./manage.py test
```
