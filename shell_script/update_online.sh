#/bin/bash
/usr/bin/rsync --progress -av --exclude="blog_env.conf" /root/src/git_hub/pyweber/* /usr/local/src/myblog/online
