from discord.ext import commands
    

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"pong! \n{round(self.bot.latency * 1000)}ms")
        
    @commands.command()
    async def maintenanceP(self, ctx):
        await ctx.message.delete()
        await ctx.send("Time for me to Level Up! I am going Offline to apply an Update! During this time users can not gain exp or level up!")

    @commands.command()
    async def maintenanceNP(self, ctx):
        await ctx.message.delete()
        await ctx.send("Something is not right with me, therefore i am going Offline for an indefinite time! Remember no exp gain or level up can happen while i am Offline!")

    @commands.command()
    async def messages(self, ctx):
        mesg = await ctx.send('Calculating...')
        counter = 0
        async for msg in cached_messages(message.channel, limit=9999999):
            if msg.author == message.author:
                counter += 1
        await message.edit(mesg, '{} has {} messages in {}.'.format(message.author, str(counter), message.channel))
        
    @commands.command()
    async def messages(self, ctx):
        mesg = await ctx.send('Calculating...')
        counter = 0
        async for msg in cached_messages(message.channel, limit=9999999):
            if msg.author == message.author:
                counter += 1
        await message.edit(mesg, '{} has {} messages in {}.'.format(message.author, str(counter), message.channel))

    @commands.command()
    @commands.has_role('Yordle Commaders')
    async def purge(self, ctx, amount=15):
        await ctx.channel.purge(limit=amount+1)

        channel = self.bot.get_channel(737219743143952404)
        embed = Embed(title=f"{ctx.author.name} purged: {ctx.channel.name}", description=f"{amount} messages were cleared")
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Commands(bot))

    





