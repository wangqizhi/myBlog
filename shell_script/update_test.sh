#/bin/bash
/usr/bin/rsync --progress -av --exclude="blog_env.conf" --exclude="myUwsgi.ini" /root/src/git_hub/pyweber/* /usr/local/src/myblog/test
# PID=`/bin/ps -ef |grep [p]ython |awk -F " " '{printf $2}'`
# /bin/kill $PID
# /usr/bin/python /usr/local/src/myblog/online/index.py 9999 >/dev/null 2>&1  &
