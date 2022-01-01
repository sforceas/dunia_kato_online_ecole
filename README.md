# Dunia Kato Online E-cole
Online e-learning platform from Dunia Kato Senegal.

## Stack

### Frontend
- HTML 5
- CSS 3
- JavaScript
- React.js

### Backend (API REST)
- Python 3.10
- Django 4.0

## DDBB
- PostgreSQL 13.4

### Deployment
- Docker 20.10.11

## Folder structure
From: https://medium.com/@gagansh7171/dockerize-your-django-and-react-app-68a7b73ab6e9
```
├──frontend  
| ├──public/   
| ├─src/  
| ├──Dockerfile          //Dockerfile for frontend image  
| ├──package.json  
| └──package-lock.json  
├──dks_ecole  
| ├──bug/  
| ├──media/  
| ├──dks_ecole/  
| ├──static/  
| ├──Dockerfile         //Dockerfile for backend image  
| ├──check_db.py  
| ├──entrypoint.sh  
| ├──manage.py  
| ├──requirements.txt  
| └──settings.ini  
└──docker-compose.yaml  //for running multi-conatiner application
```
