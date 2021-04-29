FROM python:3.9-slim
LABEL maintainer "webmaster@knighthacks.org"

ENV TZ America/New_York

RUN python3 -m pip install --upgrade pip \
    && groupadd -r knighthacks \
    && useradd --no-log-init -r -g knighthacks discordbot \
    && mkdir -p /home/discordbot/app \
    && chown -R discordbot:knighthacks /home/discordbot

WORKDIR /home/discordbot/app

COPY requirements.txt .

USER discordbot:knighthacks

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=discordbot:knighthacks . .

ENTRYPOINT [ "python3" ]
CMD [ "-m", "src" ]
