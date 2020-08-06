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
        
    async def on_raw_reaction_add(payload):
        message_id = payload.message_id
        if message_id == 554283977729507358:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

            if payload.emoji.name == "check":
                role = discord.utils.get(guild.roles, name="Yordle City")
            else:
                role = discord.utils.get(guild.roles, name=ayload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user.id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print("done")
                else:
                    print("Member not found")
            else:
                print("Role not found")



if __name__ == '__main__':
    client = MyClient(command_prefix=".")
    client.load_extension("Commands")
    client.run("")
