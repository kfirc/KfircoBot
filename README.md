# KfircoBot
My First Telegram Bot, based on self-created TelegramBot framework

### Running in Docker

**Building the docker image:**

Select an IMAGE_NAME for the image, for example - 'kfircobot'
Prepare the Github token for the KfircoBot repository, and the Telegram token for your bot

```console
docker build --build-arg TELEGRAM_TOKEN={{YOUR_TELEGRAM_TOKEN}} --build-arg GITHUB_TOKEN={{YOUR_GITHUB_TOKEN}} -t {{IMAGE_NAME}} .
```

**Running the docker image:**

```console
docker run -t -i --name KfircoBot {{IMAGE_NAME}}
```
