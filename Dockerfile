FROM python:3
COPY . /app
WORKDIR /app
RUN pip install flask requests wtforms
ENTRYPOINT ["python3", "get_rates.py"]
