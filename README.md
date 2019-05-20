# zzovlog
The backend of zzovlog
## 개발환경
- Python3.7, Django, Django Rest Framework 기반
- CORS error 해결을 위해 [django-cors-headers](https://github.com/ottoyiu/django-cors-headers)도 이용함
- Apache + mod_wsgi
## Dockerfile
httpd(apache) 이미지 위에 python이랑 mod_wsgi 설치하려고 했는데 httpd:latest 이미지에서 apt-get으로 python3.5 이상 설치가 안되고 gcc 등 python이 제대로 동작하기 위해 필요한 환경 설치하는데만 한세월 걸릴 것 같아서 python 이미지 기반으로 변경함. 요 위에다 apache, mod_wsgi 깔고 돌리는 게 훨씬 쉬울듯.
## 참고
- [python - Docker Hub](https://hub.docker.com/_/python?tab=description)
- [httpd - Docker Hub](https://hub.docker.com/_/httpd)
- [pip install mod_wsgi](https://pypi.org/project/mod_wsgi/)
- [How to use Django with Apache and mod_wsgi](https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/modwsgi/)
- [official mod_wsgi documentation](https://modwsgi.readthedocs.io/en/develop/)
- [Docker container networking](https://docs.docker.com/v17.09/engine/userguide/networking/)
