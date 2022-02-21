from utils.languageembed import languageEmbed
import settings
import nextcord
import aiohttp
from nextcord.ext import commands


class Anime(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot

    @commands.command()
    async def feed(self, ctx: commands.Context, member: nextcord.Member = None):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://nekos.life/api/v2/img/feed") as r:
                    r = await r.json()
                    embed = nextcord.Embed(colour=0xFC7EF5, title="feed")
                    url = r["url"]
                    embed.set_image(url=url)
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = (
                        await ctx.send(embed=embed)
                        if member is None
                        else await ctx.send(f"{member.mention}", embed=embed)
                    )
                    await message.add_reaction("❤️")

    @commands.command()
    async def tickle(self, ctx: commands.Context, member: nextcord.Member = None):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://nekos.life/api/v2/img/tickle") as r:
                    r = await r.json()
                    embed = nextcord.Embed(colour=0xFC7EF5, title="tickle")
                    url = r["url"]
                    embed.set_image(url=url)
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = (
                        await ctx.send(embed=embed)
                        if member is None
                        else await ctx.send(f"{member.mention}", embed=embed)
                    )
                    await message.add_reaction("❤️")

    @commands.command()
    async def slap(self, ctx: commands.Context, member: nextcord.Member = None):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://nekos.life/api/v2/img/slap") as r:
                    r = await r.json()
                    embed = nextcord.Embed(colour=0xFC7EF5, title="slap")
                    url = r["url"]
                    embed.set_image(url=url)
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = (
                        await ctx.send(embed=embed)
                        if member is None
                        else await ctx.send(f"{member.mention}", embed=embed)
                    )
                    await message.add_reaction("❤️")

    @commands.command()
    async def hug(self, ctx: commands.Context, member: nextcord.Member = None):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://nekos.life/api/v2/img/hug") as r:
                    r = await r.json()
                    embed = nextcord.Embed(colour=0xFC7EF5, title="hug")
                    url = r["url"]
                    embed.set_image(url=url)
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = (
                        await ctx.send(embed=embed)
                        if member is None
                        else await ctx.send(f"{member.mention}", embed=embed)
                    )
                    await message.add_reaction("❤️")

    @commands.command()
    async def smug(self, ctx: commands.Context, member: nextcord.Member = None):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://nekos.life/api/v2/img/smug") as r:
                    r = await r.json()
                    embed = nextcord.Embed(colour=0xFC7EF5, title="smug")
                    url = r["url"]
                    embed.set_image(url=url)
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = (
                        await ctx.send(embed=embed)
                        if member is None
                        else await ctx.send(f"{member.mention}", embed=embed)
                    )
                    await message.add_reaction("❤️")

    @commands.command()
    async def pat(self, ctx: commands.Context, member: nextcord.Member = None):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://nekos.life/api/v2/img/pat") as r:
                    r = await r.json()
                    embed = nextcord.Embed(colour=0xFC7EF5, title="pat")
                    url = r["url"]
                    embed.set_image(url=url)
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = (
                        await ctx.send(embed=embed)
                        if member is None
                        else await ctx.send(f"{member.mention}", embed=embed)
                    )
                    await message.add_reaction("❤️")

    @commands.command()
    async def kiss(self, ctx, member: nextcord.Member = None):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://nekos.life/api/v2/img/kiss") as r:
                    r = await r.json()
                    embed = nextcord.Embed(colour=0xFC7EF5, title="kiss")
                    url = r["url"]
                    embed.set_image(url=url)
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = (
                        await ctx.send(embed=embed)
                        if member is None
                        else await ctx.send(f"{member.mention}", embed=embed)
                    )
                    await message.add_reaction("❤️")


def setup(bot: commands.Bot):
    bot.add_cog(Anime(bot))
