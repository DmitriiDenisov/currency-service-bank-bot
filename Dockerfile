FROM python:3
COPY . .
RUN pip install flask requests
ENTRYPOINT ["python3", "get_rates.py"]