Hello,Python World!
#nginx.conf


<code>
        
        upstream pygogo {
            server 127.0.0.1:8080;
        }
        server {
            listen       80;
            server_name  wangqizhi.info *.wangqizhi.info 42.96.204.212;
            location ~ \.py {
                deny all;
            }
            location ~ \.(gif|jpg|png|js|css|html)$ {
    		  root /usr/local/src/web;
    		  index index.html;
    	    }
            location / {
                proxy_pass http://pygogo;
    	    proxy_set_header Host $host;
            }
    
            error_page	404	/404_page.html;
    	    location = /404_page.html{
    		    root /usr/local/src/web;
    	    }
    
            error_page   500 502 503 504  /50x_page.html;
            location = /50x_page.html {
     		root /usr/local/src/web;
            }
        }
</code>
