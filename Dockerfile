FROM python:3-alpine
COPY . /app
WORKDIR /app
RUN pip install flask requests wtforms
ENTRYPOINT ["python3", "get_rates.py"]
