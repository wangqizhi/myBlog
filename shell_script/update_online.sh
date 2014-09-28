#/bin/bash
/usr/bin/rsync --progress -av --exclude="blog_env.conf" /root/src/git_hub/pyweber/* /usr/local/src/myblog/online
/usr/bin/python /usr/local/src/myblog/online/index.py >/dev/null 2>&1  &
