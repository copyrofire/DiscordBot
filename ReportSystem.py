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





def setup(bot):
    bot.add_cog(ReportSystem(bot))
