import asyncio
import json
import DiscordBot
import ctx as ctx
import discord
from discord.ext import commands
from discord.ext.commands import bot

class Levels(commands.Cog, name='Levels'):
    def __init__(self, bot):
        self.bot = bot

        self.bot.loop.create_task(self.save_users())

        with open(r"C:\Users\Administrator\Source\Repos\DiscordBot\DiscordBot\exp.json", "r") as f:
            self.users = json.load(f)
           
        self.bot.loop.create_task(self.save_users())

    async def save_users(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
           # while not self.client.is_closed():
                json.dump(self.users, open(r"C:\Users\Administrator\Source\Repos\DiscordBot\DiscordBot\exp.json", "w"), indent=4)

                await asyncio.sleep(10)

    def lvl_up(self, author_id):
        cur_xp = self.users[author_id]['exp']
        cur_lvl = self.users[author_id]['level']

        if cur_xp >= round((4 * (cur_lvl ** 3)) / 5):
            self.users[author_id]['level'] += 1
            return  True
        else:
            return  False
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        author_id = str(message.author.id)

        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]['level'] = 1
            self.users[author_id]['exp'] = 0

        self.users[author_id]['exp'] += 2

        if self.lvl_up(author_id):
            await message.channel.send(f"{message.author.mention} is now level {self.users[author_id]['level']}")

    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send("Member doesn't have a level")
        else:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f"level - {member}", icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Level", value=self.users[member_id]['level'])
            embed.add_field(name="XP", value=self.users[member_id]['exp'])

            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Levels(client))

