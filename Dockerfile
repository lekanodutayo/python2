FROM python:3.13.6

WORKDIR /app

COPY . . 

RUN pip install  requests

CMD ["python", "assign1.py"]