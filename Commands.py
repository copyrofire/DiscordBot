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
    @commands.has_role('DISCORD_ROLE_HERE')
    async def purge(self, ctx, amount=15):
        await ctx.channel.purge(limit=amount+1)

        channel = self.bot.get_channel(CHANNEL_ID_HERE)
        embed = Embed(title=f"{ctx.author.name} purged: {ctx.channel.name}", description=f"{amount} messages were cleared")
        await channel.send(embed=embed)
        

    @commands.command(pass_context=True)
    async def sjoin(self, ctx, Member = None):
        if Member is None:
            Member = ctx.message.author

        await ctx.send('{0} joined this server at {0.joined_at}'.format(Member))

    @commands.command(pass_context=True)
    async def djoin(self, ctx, Member = None):
        if Member is None:
            Member = ctx.message.author

        await ctx.send('{0} created the discord account at {0.created_at}'.format(Member))


    @commands.command(pass_context=True)
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="Now you can stalk me in real time!")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)                           
                         
                               
    @commands.command(pass_context=True)
    async def help(self, ctx):

        embed = discord.Embed(color = discord.Colour.orange())

        embed.set_author(name='Commands')
        embed.add_field(name='ping', value='How quickly I respond', inline=False)
        embed.add_field(name='uptime', value='Shows how long the Bot has been up and running', inline=False)
        embed.add_field(name='messages', value='Shows messages', inline=False)
        embed.add_field(name='djoin', value='Shows when you joined Discord', inline=False)
        embed.add_field(name='sjoin', value='Shows when you joined this Discord Server', inline=False)
        embed.add_field(name='level', value='Shows what level and how much exp you have.', inline=False)
        embed.add_field(name='purge', value='Deletes 25 messages! (Only usable for mods!)', inline=False)
        embed.add_field(name='warn', value='Warn a user! [example: .warn @copyrofire test] (Only usable for mods!)', inline=False)
        if ctx.channel.name == ("bots"):
            await ctx.send(embed=embed)
        else:
            await ctx.send("Wrong channel, go to #bots or go to jail u rulebreaker!")                           
                               
def setup(bot):
    bot.add_cog(Commands(bot))

    





