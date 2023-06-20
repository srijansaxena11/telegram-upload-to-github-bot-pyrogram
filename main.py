from pyrogram import Client, filters
import requests
import os
import base64
from github import Github
from github import InputGitTreeElement

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

owner_id = os.getenv("OWNER_ID")

bot_token = os.getenv("BOT_TOKEN")
bot_username = os.getenv("BOT_USERNAME")

github_access_token = os.getenv("GITHUB_ACCESS_TOKEN")
github_repo_name = os.getenv("GITHUB_REPO_NAME")
# github_repo_branch_name = os.getenv("GITHUB_REPO_BRANCH_NAME")
github_repo_release_tag_name = os.getenv("GITHUB_REPO_RELEASE_TAG_NAME")

commit_message = 'Commit from Telegram Bot'

app = Client(
    bot_username,
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

g = Github(github_access_token)
repo = g.get_repo(github_repo_name)

def is_owner(client, message):
    allowed = False
    user = message.from_user
    if user.id == int(owner_id):
        allowed = True
    return allowed

@app.on_message(filters.command("start"))
async def start_command(client, message):
    if(is_owner(client, message)):
        await message.reply_text("Hello!")
    else:
        await message.reply_text("You are not the owner.")

@app.on_message(filters.document)
async def handle_file_upload(client, message):
    if(is_owner(client, message)):
        try:
            await message.reply_text("Downloading the file now.")
            file_path = await client.download_media(message.document)
            await message.reply_text(f"File downloaded successfully. Now uploading to Github Repository: {github_repo_name}")
            file_name = file_path.split("/")[-1]

            release = repo.get_release(github_repo_release_tag_name)

            release.upload_asset(
                path=file_path,
                content_type="application/octet-stream",
                name=file_name
            )

            os.remove(file_path)
            await message.reply_text("File uploaded successfully.")
        except Exception as e:
            await message.reply_text("Something went wrong:\n"+str(e))
            # await message.reply_text("Backtrace:\n"+str(traceback.format_exc()))
    else:
        await message.reply_text("You are not the owner.")

app.run()
