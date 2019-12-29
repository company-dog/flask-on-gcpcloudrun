FROM python:3.8

ENV LC_ALL=C.UTF-8 \
  LANG=C.UTF-8 \
  PORT=8888

WORKDIR /app
COPY . .

RUN pip install pipenv
RUN pipenv lock -r > requirements.txt && pip install -r requirements.txt

CMD ["python", "src/app.py"]
EXPOSE 8888
