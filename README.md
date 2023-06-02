# Telegram Bot for Github File Upload
This is a simple Telegram bot that can upload files from Telegram to a Github repository. It uses Pyrogram, Requests and PyGithub libraries.

## Features
The bot can only be used by the owner of the bot, who is specified by the OWNER_ID environment variable.
The bot can download any document sent to it and upload it to the latest release of a Github repository, which is specified by the GITHUB_REPO_NAME and GITHUB_REPO_RELEASE_TAG_NAME environment variables.
The bot can handle errors and exceptions gracefully and send feedback messages to the owner.

## Installation
Clone this repository or download the main.py file.

Install the required dependencies using `pip install -r requirements.txt`

Create a Telegram bot using BotFather and get its token and username.

Create a Github personal access token with repo scope and get the name of the repository you want to upload files to.

Set the following environment variables:

- API_ID: Your Telegram API ID obtained from https://my.telegram.org
- API_HASH: Your Telegram API hash obtained from https://my.telegram.org
- OWNER_ID: Your Telegram user ID obtained from @userinfobot
- BOT_TOKEN: Your Telegram bot token obtained from BotFather
- BOT_USERNAME: Your Telegram bot username obtained from BotFather
- GITHUB_ACCESS_TOKEN: Your Github personal access token obtained from https://github.com/settings/tokens
- GITHUB_REPO_NAME: Your Github repository name in the format username/repo
- GITHUB_REPO_RELEASE_TAG_NAME: The tag name of the release you want to upload files to, such as latest
Run the bot using python main.py.

## Usage
Send any document to the bot and it will download it and upload it to the Github repository.
You will receive feedback messages from the bot about the progress and status of the file upload.

`--Thanks to Bing ChatGPT for generating this accurate README File`
