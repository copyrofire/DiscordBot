import discord
from discord.ext import commands

from utils import create_voice_channel


class Activities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.Cog.listener()
        async def on_voice_state_update(self, member, before, after):
            if member.bot:
                return

            if not before.channel:
                print(f"{member.name} joined {after.channel.naem}")

            if before.channel and not after.channel:
                print("User left channel")

            if after.channel is not None:
                if after.channel.name =="create":
                    channel = await create_voice_channel(after.channel.guild, f'{member.name}'.lower(),
                    category_name="VC")

                    if channel is not None:
                        await member.move_to(channel)

def setup(bot):
    bot.add_cog(Activities(bot))
