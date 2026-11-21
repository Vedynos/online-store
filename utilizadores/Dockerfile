FROM python:3.12-slim

RUN pip install flask

COPY main.py /main.py
COPY templates /templates
COPY . .

CMD [ "python" , "main.py" ]