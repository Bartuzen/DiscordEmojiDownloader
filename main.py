import discord
import requests
import shutil

token = ""
guild_id = 123456789


def download_image(url, name):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'}
    extension = url[-3:]
    response = requests.get(url, stream=True, headers=headers)
    with open(f"images\\{name}.{extension}", 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)


class Bot(discord.Client):
    async def on_ready(self):
        print("Started")
        guild = self.get_guild(guild_id)
        emojis = guild.emojis
        for each in emojis:
            if each.animated:
                download_image(f"https://cdn.discordapp.com/emojis/{each.id}.gif", each.name)
            else:
                download_image(f"https://cdn.discordapp.com/emojis/{each.id}.png", each.name)
        print("Finished")


bot = Bot()
bot.run(token, bot=False)
