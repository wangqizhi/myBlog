#/bin/bash
/usr/bin/rsync --progress -av --exclude="blog_env.conf" /root/src/git_hub/pyweber/* /usr/local/src/myblog/online
PID=`/bin/ps -ef |grep [p]ython |awk -F " " '{printf $2}'`
/bin/kill $PID
/usr/bin/python /usr/local/src/myblog/online/index.py 9999 >/dev/null 2>&1  &
