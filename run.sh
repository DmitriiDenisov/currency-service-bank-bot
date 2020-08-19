# docker pull image
# docker build -t test_image .
sudo docker pull dmitrydenisov/curr-serv
PORT=5002
sudo docker run -p $PORT:$PORT -v $(pwd)/token.txt:/app/token.txt --restart always --name curr_cont -e port=$PORT -d dmitrydenisov/curr-serv
# sudo docker run -p 1000:1000   -v $(pwd)/token.txt:/app/token.txt --restart always -e port=1000 -d test_image