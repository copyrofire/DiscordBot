from discord.ext import commands

from settings import *

async def create_voice_channel(guild, channel_name, category_name="VOICECHANNELS", user_limit=None):

    category = get_category_by_name(guild, category_name)
    await guild.create_voice_channel(channel_name, category=category, user_limit=user_limit)
    channel = get_channel_by_name(guild, channel_name)
    return channel

def get_channel_by_name(guild, channel_name):

    channel = None
    for c in guild.channels:
        if c.name == channel_name.lower():
            channel = c
            break
    return category
