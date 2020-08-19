# docker pull image
# docker build -t test_image .

# Pull image
sudo docker pull dmitrydenisov/curr-serv
PORT=5002
# Docker run container
sudo docker run -p $PORT:$PORT -v $(pwd)/token.txt:/app/token.txt --restart always --name curr_cont -e port=$PORT -d dmitrydenisov/curr-serv