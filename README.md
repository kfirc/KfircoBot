# KfircoBot
My First Telegram Bot, based on self-created TelegramBot framework

### running in Docker
docker build -t kfircobot .
&& docker run
--env TELEGRAM_TOKEN={{YOUR_TELEGRAM_TOKEN}}
--env GITHUB_TOKEN={{YOUR_GITHUB_TOKEN}}
--name KfircoBot
kfircobot
