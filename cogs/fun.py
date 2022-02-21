import nextcord
import random
import datetime
import aiohttp
from nextcord.ext.commands.core import command
from utils.languageembed import languageEmbed
import settings
import asyncpraw
from nextcord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot

    @commands.command(aliases=["subreddit", "reddit"])
    async def sreddit(self, ctx: commands.Context, subreddit):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = languageserver["Language"]

            if server_language == "Thai":
                subreddit = await settings.reddit.subreddit(subreddit)
                all_subs = []
                async for submission in subreddit.hot(limit=10):
                    all_subs.append(submission)

                random_sub = random.choice(all_subs)
                title = random_sub.title
                url = random_sub.url

                if random_sub.over_18:
                    if ctx.channel.is_nsfw():
                        embed = nextcord.Embed(
                            colour=0x00FFFF,
                            title=f"{title}",
                            description=f"ที่มาของรูปคือ subreddit r/{subreddit}",
                        )

                        embed.set_image(url=url)
                        embed.set_footer(text=f"┗Requested by {ctx.author}")
                        embed.timestamp = datetime.datetime.utcnow()

                        message = await ctx.send(embed=embed)
                        await message.add_reaction("✨")

                    else:
                        embed = nextcord.Embed(
                            colour=0x983925,
                            title=f"NSFW",
                            description=f"คุณไม่สามารถค้นหา subreddit ที่ 18+ ในช่องเเชทนี้ได้ โปรดใช้ในห้อง NSFW เท่านั้น",
                        )

                        embed.set_footer(text=f"┗Requested by {ctx.author}")
                        embed.timestamp = datetime.datetime.utcnow()

                        message = await ctx.send(embed=embed)
                        await message.add_reaction("✨")

                else:
                    embed = nextcord.Embed(
                        colour=0x00FFFF,
                        title=f"{title}",
                        description=f"ที่มาของรูปคือ subreddit r/{subreddit}",
                    )

                    embed.set_image(url=url)
                    embed.set_footer(text=f"┗Requested by {ctx.author}")
                    embed.timestamp = datetime.datetime.utcnow()

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("✨")

            if server_language == "English":
                subreddit = await settings.reddit.subreddit(subreddit)
                all_subs = []

                async for submission in subreddit.hot(limit=10):
                    all_subs.append(submission)

                random_sub = random.choice(all_subs)
                title = random_sub.title
                url = random_sub.url

                if random_sub.over_18:
                    if ctx.channel.is_nsfw():
                        embed = nextcord.Embed(
                            colour=0x00FFFF,
                            title=f"{title}",
                            description=f"Source : subreddit r/{subreddit}",
                        )

                        embed.set_image(url=url)
                        embed.set_footer(text=f"┗Requested by {ctx.author}")
                        embed.timestamp = datetime.datetime.utcnow()

                        message = await ctx.send(embed=embed)
                        await message.add_reaction("✨")

                    else:
                        embed = nextcord.Embed(
                            colour=0x983925,
                            title=f"NSFW",
                            description=f"unable to search subreddit which is 18+ in this text channel please use this in NSFW channel",
                        )
                        embed.set_footer(text=f"┗Requested by {ctx.author}")
                        embed.timestamp = datetime.datetime.utcnow()

                        message = await ctx.send(embed=embed)
                        await message.add_reaction("✨")

                else:
                    embed = nextcord.Embed(
                        colour=0x00FFFF,
                        title=f"{title}",
                        description=f"Source : subreddit r/{subreddit}",
                    )

                    embed.set_image(url=url)
                    embed.set_footer(text=f"┗Requested by {ctx.author}")
                    embed.timestamp = datetime.datetime.utcnow()

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("✨")

    @sreddit.error
    async def sreddit_error(self, ctx: commands.Context, error):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = languageserver["Language"]

            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` กรุณาระบุsubreddit ที่ต้องการ ``{settings.COMMAND_PREFIX}sreddit (subreddit)``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` please specify a subreddit ``{settings.COMMAND_PREFIX}sreddit (subreddit)``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

    @commands.command()
    async def slim(self, ctx: commands.Context):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = languageserver["Language"]

            if server_language == "Thai":
                lines = open("data/slim.txt", encoding="utf8").read().splitlines()
                slimrandom = random.choice(lines)

                embed = nextcord.Embed(
                    colour=0xFFE852,
                    title="คําพูดสลิ่ม",
                    description=f"```{slimrandom}```",
                )

                embed.set_thumbnail(
                    url="https://smilewinbot.web.app/assets/image/host/slim.png"
                )
                embed.set_footer(text=f"┗Requested by {ctx.author}")

                message = await ctx.send(embed=embed)
                await message.add_reaction("🐃")

            else:
                pass

    @commands.command()
    async def quote(self, ctx: commands.Context):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = languageserver["Language"]

            if server_language == "Thai":
                lines = open("data/quote.txt", encoding="utf8").read().splitlines()
                quoterandom = random.choice(lines)
                embed = nextcord.Embed(
                    colour=0xFFE852,
                    title="คําคม",
                    description=f"```fix\n{quoterandom}```",
                )

                embed.set_thumbnail(
                    url="https://smilewinbot.web.app/assets/image/host/quote.png"
                )
                embed.set_footer(text=f"┗Requested by {ctx.author}")

                message = await ctx.send(embed=embed)
                await message.add_reaction("❤️")

            else:
                pass

    @commands.command()
    async def roll(self, ctx: commands.Context):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = languageserver["Language"]
            num = [
                "1",
                "2",
                "3",
                "4 ",
                "5",
                "6",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
            ]
            x = random.choice(num)
            url = f"https://www.calculator.net/img/dice{x}.png"

            if server_language == "Thai":
                embed = nextcord.Embed(colour=0x00FFFF, title="🎲 ทอยลูกเต่า")
                embed.set_image(url=url)
                embed.set_footer(text=f"┗Requested by {ctx.author}")

                message = await ctx.send(embed=embed)
                await message.add_reaction("🎲")

            if server_language == "English":
                embed = nextcord.Embed(colour=0x00FFFF, title="🎲 Dice")
                embed.set_image(url=url)
                embed.set_footer(text=f"┗Requested by {ctx.author}")

                message = await ctx.send(embed=embed)
                await message.add_reaction("🎲")

    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx: commands.Context, *, question):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = languageserver["Language"]

            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://8ball.delegator.com/magic/JSON/{question}"
                ) as r:
                    r = await r.json()

            answer = r["magic"]["answer"]
            ask = r["magic"]["question"]
            percent = r["magic"]["type"]

            if server_language == "Thai":
                embed = nextcord.Embed(
                    colour=0x00FFFF,
                    title="🎱 8ball",
                    description=f"""```
    คําถาม : {ask}
    คําตอบ : {answer}
    ความน่าจะเป็น : {percent}```""",
                )
                embed.set_footer(text=f"┗Requested by {ctx.author}")
                message = await ctx.send(embed=embed)
                await message.add_reaction("🎱")

            if server_language == "English":
                embed = nextcord.Embed(
                    colour=0x00FFFF,
                    title="🎱 8ball",
                    description=f"""```
    Question : {ask}
    Respond : {answer}
    Probability : {percent}```""",
                )
                embed.set_footer(text=f"┗Requested by {ctx.author}")
                message = await ctx.send(embed=embed)
                await message.add_reaction("🎱")

    @_8ball.error
    async def _8ball_error(self, ctx: commands.Context, error):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = languageserver["Language"]

            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` จะต้องพิมสิ่งที่จะถาม ``{settings.COMMAND_PREFIX}8ball [คําถาม]``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` need to specify what video to ask ``{settings.COMMAND_PREFIX}8ball [question]``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

    @commands.command()
    async def meme(self, ctx: commands.Context):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://some-random-api.ml/meme") as r:
                    r = await r.json()
                    url = r["image"]
                    cap = r["caption"]

                    embed = nextcord.Embed(colour=0x00FFFF, title=f"{cap}")
                    embed.set_image(url=url)
                    message = await ctx.send(embed=embed)
                    await message.add_reaction("😂")


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
