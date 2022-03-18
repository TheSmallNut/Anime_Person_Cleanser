from discord.ext import commands
import discord
import os


class cog1(commands.Cog, name="cog1"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", aliases=[])
    @commands.cooldown(1, 10, commands.BucketType.guild)
    @commands.has_permissions()
    async def _ping(self, ctx: commands.Context):
        em = discord.Embed(
            title=f'Pong! {round(self.bot.latency * 1000)}ms', color=0x00ff00)
        await ctx.send(embed=em)

    @_ping.error
    async def _ping_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=f"Slow it down!",
                                  description=f"Try again in {error.retry_after:.2f}s.", color=0xff0000)
            await ctx.send(embed=embed)


def setup(bot):
    print("cog1 Cog Loaded")
    bot.add_cog(cog1(bot))


def teardown(bot):
    print("cog1 Cog Unloaded")
