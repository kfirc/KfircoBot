# KfircoBot
My First Telegram Bot, based on self-created TelegramBot framework

### Running in Docker

**Building the docker image:**

Select an IMAGE_NAME for the image, for example - 'kfircobot'
```console
docker build -t {{IMAGE_NAME}} .
```

**Running the docker image:**

Prepare the Github token for the KfircoBot repository, and the Telegram token for your bot

```console
docker run -t -i
--env TELEGRAM_TOKEN={{YOUR_TELEGRAM_TOKEN}}
--env GITHUB_TOKEN={{YOUR_GITHUB_TOKEN}}
--name KfircoBot
{{IMAGE_NAME}}
```
