#git_automation_with_python


This is a pthon script used to automate the creation of github repos,
and clone said repo to your local machine. 

This program uses GitHub api 

to use program create a personal access token 

settings > Developer settings > personal access token

Create an enviroment variable called "GIT_TOKEN"

```
export GIT_TOKEN=<your_personal_access_token>
```

The program takes 3 commandline arguments 

--name or -n = the name of the repo to create (required)

--user or -u = your github username (required)

--private or -p : flag to specify if the repo should be private or public (optional)

ex
```
python3 create_repo.py --name <repo_name> --user <user_name> --private
``` 

after creating the repo in github, the program will create a new directory
from your current location and init the repo there. 
