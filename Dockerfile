# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /projects

# Prevent caching the following commands
ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache

# Creeate the log dir
RUN mkdir /log

# export environment variables
ARG TELEGRAM_TOKEN
ARG GITHUB_TOKEN
ENV TELEGRAM_TOKEN=${TELEGRAM_TOKEN} LOGGER_PATH=/log/bot.log

# Clone the GitHub Repositories
RUN git clone https://${GITHUB_TOKEN}:x-oauth-basic@github.com/kfirc/TelegramBot.git && \
    git clone https://${GITHUB_TOKEN}:x-oauth-basic@github.com/kfirc/KfircoBot.git

# install dependencies
RUN pip install --upgrade pip && \
    pip install -r KfircoBot/requirements_docker.txt && \
    pip install ./TelegramBot

# command to run on container start
CMD [ "python", "KfircoBot/main.py" ]
