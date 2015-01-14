#/bin/bash
/usr/bin/rsync --progress -av --exclude="blog_env.conf" --exclude="myUwsgi.ini" /root/src/git_hub/pyweber/* /usr/local/src/myblog/test
PID=`netstat -anlpt |grep 3032 |awk -F '/' '{print $1}'|awk -F ' ' '{print $7}'`
/bin/kill -9 $PID
/usr/local/python2.7.8/bin/uwsgi /usr/local/src/myblog/test/conf/myUwsgi.ini 2>&1 >/tmp/testWeb.log &