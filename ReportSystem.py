from discord.ext import commands
from discord import Embed
import asyncio
import json
import time
import os
import ctx as ctx
import discord, datetime, time
from discord.ext.commands import bot
import Database


class ReportSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, user : discord.Member, *, reason:str):
        Database.add_one("User", "discord.Member", "reason")




    #    with open('reports.json', encoding='utf-8') as f:
    #        try:
    #            report = json.load(f)
    #        except ValueError:
    #            report = {}
    #            report['users'] = []
    #    if not reason:
    #        await ctx.send("Please provide a reason")
    #    #return #below code won't be executed
    #    reason = ''.join(reason)
    #    for current_user in report['users']:
    #        if current_user['id'] == user.id:
    #            current_user['reasons'].append(reason)
    #        break
    #    else:
    #        report['users'].append({
    #        'id': user.id,
    #        'reasons': [reason, ]
    #        })
    #    with open('reports.json','w') as f:
    #        json.dump(report,f, indent=3)
    #        await ctx.send(f"{user.name} has been successfully reported!")

    #@commands.command(pass_context = True)
    #async def warnings(self, ctx,user:discord.User):
    #    with open('reports.json', encoding='utf-8') as f:
    #        try:
    #            report = json.load(f)
    #        except ValueError:
    #            report = {}
    #            report['users'] = []
    #    for current_user in report['users']:
    #        if user.id == current_user['id']:
    #            await ctx.send(f"{user.name} has been reported {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}")
    #        break
    #    else:
    #        await ctx.send(f"{user.name} has never been reported")  

    #@warn.error
    #async def warn_error(self, error, ctx):
    #    if isinstance(error, commands.MissingRole):
    #        await ctx.send("Okay +1 warning for you, for trying to use a command u are not allowed to use!")



def setup(bot):
    bot.add_cog(ReportSystem(bot))
