# docker pull image
sudo docker build -t curr-serv .
PORT=5002
sudo docker run -p $PORT:$PORT -v $(pwd)/token.txt:/app/token.txt --restart always --name curr_cont -e port=$PORT -d curr-serv