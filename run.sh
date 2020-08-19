# Pull image
sudo docker pull dmitrydenisov/curr-serv

# If pull does not work (for example, repo was deleted) then:
# docker build -t curr-serv .

# Rename iamge
sudo docker image tag dmitrydenisov/curr-serv:latest curr-serv:latest
sudo docker rmi dmitrydenisov/curr-serv

# Define port
PORT=5002

# Docker run container
sudo docker run -p $PORT:$PORT -v $(pwd)/token.txt:/app/token.txt --restart always --name curr_cont -e port=$PORT -d curr-serv