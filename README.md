# zzovlog
The backend of zzovlog
## 개발환경
- Python3.7, Django, Django Rest Framework 기반
- CORS error 해결을 위해 [django-cors-headers](https://github.com/ottoyiu/django-cors-headers)도 이용함
- Apache + mod_wsgi
## 환경변수
```bash
# django-admin startproject로 프로젝트 생성시 settings.py에 생기는 보안키. 참고항목 링크 참고.
ZZOVLOG_SECRET_KEY

# settings.py의 DEBUG 변수값. Production 환경에선 False로 설정해줘야 한다.
ZZOVLOG_DEBUG

# settings.py의 DATABASES 설정값. 사용하는 DB의 호스트, 포트, 사용자 및 비밀번호 정보들을 넣어준다.
ZZOVLOG_DB_USER
ZZOVLOG_DB_PASSWORD
ZZOVLOG_DB_HOST
ZZOVLOG_DB_PORT
```
## Dockerfile
httpd(apache) 이미지 위에 python이랑 mod_wsgi 설치하려고 했는데 httpd:latest 이미지에서 apt-get으로 python3.5 이상 설치가 안되고 gcc 등 python이 제대로 동작하기 위해 필요한 환경 설치하는데만 한세월 걸릴 것 같아서 python 이미지 기반으로 변경함. 요 위에다 apache, mod_wsgi 깔고 돌리는 게 훨씬 쉬울듯.
## docker-entrypoint.sh
Docker container가 실행(run)될 때 Dockerfile의 ENTRYPOINT, CMD 명령어 부분이 실행되는데 ENTRYPOINT에서 실행하고 싶은 명령어를 모아놓은 shell script file의 컨벤션 이름이 docker-entrypoint.sh.
이 프로젝트에선 django-rest-framework 및 django framework에서 쓰이는 static file들을 collect하고 db에 blog/models.py 및 framework에서 정의된 모델들을 db table로 migration 하는 데 쓰인다.
## 참고
- [python - Docker Hub](https://hub.docker.com/_/python?tab=description)
- [httpd - Docker Hub](https://hub.docker.com/_/httpd)
- [pip install mod_wsgi](https://pypi.org/project/mod_wsgi/)
- [How to use Django with Apache and mod_wsgi](https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/modwsgi/)
- [official mod_wsgi documentation](https://modwsgi.readthedocs.io/en/develop/)
- [Docker container networking](https://docs.docker.com/v17.09/engine/userguide/networking/)
- [Django - settings.py 의 SECRET_KEY 변경 및 분리하기](https://wayhome25.github.io/django/2017/07/11/django-settings-secret-key/)
