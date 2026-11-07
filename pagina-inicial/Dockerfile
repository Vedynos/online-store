FROM python:3.12-slim

RUN pip install flask
# posso apagar os COPY e deixar apenas o último!
COPY main.py /main.py
COPY templates /templates
COPY . .

CMD ["python", "main.py"]
