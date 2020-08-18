# docker pull image
sudo docker pull dmitrydenisov/curr-serv
PORT=5002
sudo docker run -p $PORT:$PORT -v $(pwd)/token.txt:/app/token.txt --restart always --name curr_cont -e port=$PORT curr-serv