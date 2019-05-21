#!/bin/bash

echo "=> make init.sh"
echo '#!/bin/bash' > init.sh
echo "export ZZOVLOG_SECRET_KEY='$ZZOVLOG_SECRET_KEY'" >> init.sh
echo "export ZZOVLOG_DEBUG=$ZZOVLOG_DEBUG" >> init.sh
echo "export ZZOVLOG_DB_USER='$ZZOVLOG_DB_USER'" >> init.sh
echo "export ZZOVLOG_DB_PASSWORD='$ZZOVLOG_DB_PASSWORD'" >> init.sh
echo "export ZZOVLOG_DB_HOST='$ZZOVLOG_DB_HOST'" >> init.sh
echo "export ZZOVLOG_DB_PORT='$ZZOVLOG_DB_PORT'" >> init.sh

echo "=> build image zzovlog"
sudo docker build -t zzovlog .

echo "=> remove local init.sh"
rm init.sh

echo "=> stop and remove container zzovlog"
sudo docker stop zzovlog
sudo docker container prune

echo "=> run container zzovlog"
sudo docker run --name zzovlog -h zzovlog -d -p 8000:80 zzovlog:latest
