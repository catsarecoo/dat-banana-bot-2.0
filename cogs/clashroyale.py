import discord
import sys
import os
import io
import clashroyale
from discord.ext import commands


class clashroyale:
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    async def crprofile(self, ctx, crtag:str):
        """Shows CR stats for you! Usage: *crprofile [tag]"""
        client = clashroyale.Client("607d4e53a8b643f1bbb7837bacb7ec3c4706bc9420b34377a869d8048500f998", is_async=True)
        profile = await client.get_player(crtag)
        color = discord.Color(value=0xf1f442)
        em = discord.Embed(color=color, title=profile.name)
        em.description = f"#{profile.tag}"
        em.add_field(name='Trophies', value=profile.trophies)
        em.add_field(name='Personal Best', value=profile.stats.max_trophies)
        em.add_field(name='XP Level', value=profile.stats.level)
        em.add_field(name='Arena', value=profile.arena.name)
        em.add_field(name='Wins/Losses/Draws', value=record)
        em.add_field(name='Win Rate', value=f"{(profile.games.wins / (profile.games.wins + profile.games.losses) * 100):.3f}%")
        