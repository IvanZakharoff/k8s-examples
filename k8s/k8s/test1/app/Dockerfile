FROM python:3.12.0

WORKDIR /src

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY main.py ./main.py
COPY db.py ./db.py

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0"]

EXPOSE 5000