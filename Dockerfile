FROM python:3

RUN mkdir -p /app/rps

WORKDIR /app/rps

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD [ "python", "./main.py" ]