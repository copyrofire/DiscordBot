import discord
from discord.ext.commands import Bot


class MyClient(Bot):
    #Log in
    async def on_ready(self):
        await client.change_presence(status=discord.Status.idle, activity=discord.Game("Version 0.0.3"))
        print("I am ready senpai")

    async def on_typing(self, channel , user, when):
        print(str(user) + " is typing in: " + str(channel) + str(when))

    async def on_message_delete(self, message):
        channel = client.get_channel(737219743143952404)
        await channel.send(str(message.author) + " deleted message: " + message.content)

    async def on_message_edit(self, before, after):
        channel = client.get_channel(737219743143952404)
        if before.content != after.content:
            await channel.send(" Changed message: " + before.content + " --to--> " + after.content)
        else:
            return


if __name__ == '__main__':
    client = MyClient(command_prefix=".")
    client.load_extension("Commands")
    client.run("")
