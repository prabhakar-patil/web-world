# web-world

Host: Ubuntu 1804

## web-server
docker container running nginx web server.
Modify the root for web server and create your static pages.

0. docker pull nginx
1. mkdir -p ~/docker-nginx/html
2. cat > ~/docker-nginx/html/index.html << EOF
<html>
  <body>
     <h1>Hello World!</h1>
  </body>
</html>
EOF
3. cd web-server
4. ./nginx-run.sh

## web-client
There are multiple ways you can connect to web-server. You can write your own web-client too.

### web-client1: web-browser
URL- http://localhost:5000

### web-client2 : telenet
1. telnet localhost 5000
2. Make HTTP request
GET / HTTP/1.1
host: localhost

3. Enter two times and you will get HTTP response

### web-client3: python
Python code is there in web-client