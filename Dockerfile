FROM python:3.9-slim

ENV TZ America/New_York

WORKDIR /home/discordbot/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python3" ]
CMD [ "-m", "src" ]
