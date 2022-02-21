import nextcord
import aiohttp
import settings
from utils.languageembed import languageEmbed
from nextcord.ext import commands


class Proxy(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot

    @commands.command()
    async def gethttp(self, ctx: commands.Context):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            url = (
                "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt"
            )
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    r = await r.text()
            with open("data/http.txt", "w") as file:
                file.write(r)
            f = nextcord.File("data/http.txt", filename="http.txt")
            await ctx.send(file=f)

    @commands.command()
    async def gethttps(self, ctx: commands.Context):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            url = (
                "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt"
            )
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    r = await r.text()
            with open("data/https.txt", "w") as file:
                file.write(r)
            file = nextcord.File("data/https.txt", filename="https.txt")
            await ctx.send(file=file)

    @commands.command()
    async def getproxy(self, ctx: commands.Context):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            url = (
                "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt"
            )
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    r = await r.text()
            with open("data/proxy.txt", "w") as file:
                file.write(r)
            f = nextcord.File("data/proxy.txt", filename="proxy.txt")
            await ctx.send(file=f)

    @commands.command()
    async def getsock4(self, ctx: commands.Context):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            url = "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    r = await r.text()
            with open("data/sock4.txt", "w") as file:
                file.write(r)
            file = nextcord.File("data/sock4.txt", filename="sock4.txt")
            await ctx.send(file=file)

    @commands.command()
    async def getsock5(self, ctx: commands.Context):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            url = "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    r = await r.text()
            with open("data/sock5.txt", "w") as file:
                file.write(r)
            f = nextcord.File("data/sock5.txt", filename="data/sock5.txt")
            await ctx.send(file=f)


def setup(bot: commands.Bot):
    bot.add_cog(Proxy(bot))
