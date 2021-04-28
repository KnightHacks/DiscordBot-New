FROM python:3.9.0-slim

ENV TZ America/New_York

WORKDIR /home/discordbot/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]
CMD [ "-m", "src" ]
