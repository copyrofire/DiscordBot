import commands
from discord.ext import commands
import ctx as ctx
    
    
#@commands.Cog.listener()
class Commands(commands.Cog, name='Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong! \n{round(self.client.latency * 1000)}ms")

def setup(bot):
    bot.add_cog(Commands(bot))

    





