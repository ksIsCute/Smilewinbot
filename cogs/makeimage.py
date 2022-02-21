import nextcord
import settings
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from utils.languageembed import languageEmbed
import random
from io import BytesIO
from pathlib import Path
from random import choice
from captcha.image import ImageCaptcha
from nextcord.ext import commands


class MakeImage(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot

    @commands.command()
    async def love(self, ctx: commands.Context, member: nextcord.Member = None):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = languageserver["Language"]

            if server_language == "Thai":
                if not Path("image/template.png").exists():
                    img = Image.new("RGB", (256, 128), color=(253, 254, 254))
                    img.save("image/template.png")

                else:
                    pass

                if not Path("arial.ttf").exists():
                    dirname = os.path.dirname(os.path.abspath(__file__))
                    fontfile = os.path.join(dirname, "arial.ttf")

                else:
                    fontfile = "arial.ttf"

                font = ImageFont.truetype(fontfile, 15)

                if member is None:
                    memberonly = [
                        member for member in ctx.guild.members if not member.bot
                    ]
                    member = choice(memberonly)
                    template = Image.open("image/template.png")
                    heart = Image.open("image/heart.png")
                    authorasset = ctx.author.avatar.with_size(128)
                    authordata = BytesIO(await authorasset.read())
                    authorpfp = Image.open(authordata)

                    n = random.randint(1, 100)
                    love = f"{n} %"
                    heart = heart.resize((42, 42))
                    draw = ImageDraw.Draw(heart)
                    draw.text((10, 10), love, font=font)

                    memberasset = member.avatar.with_size(128)
                    memberdata = BytesIO(await memberasset.read())
                    memberpfp = Image.open(memberdata)

                    authorpfp = authorpfp.resize((128, 128))
                    memberpfp = memberpfp.resize((128, 128))

                    obj = BytesIO()
                    width = (template.width - heart.width) // 2
                    height = (template.height - heart.height) // 2
                    template.paste(authorpfp, (0, 0))
                    template.paste(memberpfp, (128, 0))
                    template.paste(heart, (width, height), heart)
                    template.save(obj, format="PNG")
                    obj.seek(0)
                    file = nextcord.File(obj, filename="love.png")
                    embed = nextcord.Embed(
                        colour=0x00FFFF,
                        description=f"{ctx.author.mention}  💖  ``{member}``",
                    )
                    embed.set_image(url="attachment://love.png")
                    embed.set_footer(text=f"┗Requested by {ctx.author}")
                    await ctx.send(embed=embed, file=file)

                else:
                    template = Image.open("image/template.png")
                    heart = Image.open("image/heart.png")
                    authorasset = ctx.author.avatar.with_size(128)
                    authordata = BytesIO(await authorasset.read())
                    authorpfp = Image.open(authordata)

                    n = random.randint(1, 100)
                    love = f"{n} %"
                    heart = heart.resize((42, 42))
                    draw = ImageDraw.Draw(heart)
                    draw.text((10, 10), love, font=font)

                    memberasset = member.avatar.with_size(128)
                    memberdata = BytesIO(await memberasset.read())
                    memberpfp = Image.open(memberdata)

                    authorpfp = authorpfp.resize((128, 128))
                    memberpfp = memberpfp.resize((128, 128))
                    heart = heart.resize((42, 42))

                    obj = BytesIO()
                    width = (template.width - heart.width) // 2
                    height = (template.height - heart.height) // 2
                    template.paste(authorpfp, (0, 0))
                    template.paste(memberpfp, (128, 0))
                    template.paste(heart, (width, height), heart)
                    template.save(obj, format="PNG")
                    obj.seek(0)
                    file = nextcord.File(obj, filename="love.png")
                    embed = nextcord.Embed(
                        colour=0x00FFFF,
                        description=f"{ctx.author.mention}  💖  ``{member}``",
                    )
                    embed.set_image(url="attachment://love.png")
                    embed.set_footer(text=f"┗Requested by {ctx.author}")
                    await ctx.send(embed=embed, file=file)

            if server_language == "English":
                if not Path("image/template.png").exists():
                    img = Image.new("RGB", (256, 128), color=(253, 254, 254))
                    img.save("image/template.png")

                else:
                    pass

                if not Path("arial.ttf").exists():
                    dirname = os.path.dirname(os.path.abspath(__file__))
                    fontfile = os.path.join(dirname, "arial.ttf")

                else:
                    fontfile = "arial.ttf"

                font = ImageFont.truetype(fontfile, 15)

                if member is None:
                    memberonly = [
                        member for member in ctx.guild.members if not member.bot
                    ]
                    member = choice(memberonly)
                    template = Image.open("image/template.png")
                    heart = Image.open("image/heart.png")
                    authorasset = ctx.author.avatar.with_size(128)
                    authordata = BytesIO(await authorasset.read())
                    authorpfp = Image.open(authordata)

                    n = random.randint(1, 100)
                    love = f"{n} %"
                    heart = heart.resize((42, 42))
                    draw = ImageDraw.Draw(heart)
                    draw.text((10, 10), love, font=font)
                    memberasset = member.avatar.with_size(128)
                    memberdata = BytesIO(await memberasset.read())
                    memberpfp = Image.open(memberdata)

                    authorpfp = authorpfp.resize((128, 128))
                    memberpfp = memberpfp.resize((128, 128))

                    obj = BytesIO()
                    width = (template.width - heart.width) // 2
                    height = (template.height - heart.height) // 2
                    template.paste(authorpfp, (0, 0))
                    template.paste(memberpfp, (128, 0))
                    template.paste(heart, (width, height), heart)
                    template.save(obj, format="PNG")
                    obj.seek(0)
                    file = nextcord.File(obj, filename="love.png")
                    embed = nextcord.Embed(
                        colour=0x00FFFF,
                        description=f"{ctx.author.mention}  💖  ``{member}``",
                    )
                    embed.set_image(url="attachment://love.png")
                    embed.set_footer(text=f"┗Requested by {ctx.author}")
                    await ctx.send(embed=embed, file=file)

                else:
                    template = Image.open("image/template.png")
                    heart = Image.open("image/heart.png")
                    authorasset = ctx.author.avatar.with_size(128)
                    authordata = BytesIO(await authorasset.read())
                    authorpfp = Image.open(authordata)

                    n = random.randint(1, 100)
                    love = f"{n} %"
                    heart = heart.resize((42, 42))
                    draw = ImageDraw.Draw(heart)
                    draw.text((10, 10), love, font=font)

                    memberasset = member.avatar.with_size(128)
                    memberdata = BytesIO(await memberasset.read())
                    memberpfp = Image.open(memberdata)

                    authorpfp = authorpfp.resize((128, 128))
                    memberpfp = memberpfp.resize((128, 128))
                    heart = heart.resize((42, 42))

                    obj = BytesIO()
                    width = (template.width - heart.width) // 2
                    height = (template.height - heart.height) // 2
                    template.paste(authorpfp, (0, 0))
                    template.paste(memberpfp, (128, 0))
                    template.paste(heart, (width, height), heart)
                    template.save(obj, format="PNG")
                    obj.seek(0)
                    file = nextcord.File(obj, filename="love.png")
                    embed = nextcord.Embed(
                        colour=0x00FFFF,
                        description=f"{ctx.author.mention}  💖  ``{member}``",
                    )
                    embed.set_image(url="attachment://love.png")
                    embed.set_footer(text=f"┗Requested by {ctx.author}")
                    await ctx.send(embed=embed, file=file)

    @commands.command()
    async def lover(
        self,
        ctx: commands.Context,
        member1: nextcord.Member = None,
        member2: nextcord.Member = None,
    ):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = languageserver["Language"]

            if server_language == "Thai":
                if not Path("image/template.png").exists():
                    img = Image.new("RGB", (256, 128), color=(253, 254, 254))
                    img.save("image/template.png")

                else:
                    pass

                if not Path("arial.ttf").exists():
                    dirname = os.path.dirname(os.path.abspath(__file__))
                    fontfile = os.path.join(dirname, "arial.ttf")

                else:
                    fontfile = "arial.ttf"

                font = ImageFont.truetype(fontfile, 15)

                if member1 is None:
                    memberonly1 = [
                        member for member in ctx.guild.members if not member.bot
                    ]
                    member1 = choice(memberonly1)
                    memberonly2 = [
                        member
                        for member in ctx.guild.members
                        if not member.bot and member != member1
                    ]
                    member2 = choice(memberonly2)
                    template = Image.open("image/template.png")
                    heart = Image.open("image/heart.png")
                    member1asset = member1.avatar.with_size(128)
                    member1data = BytesIO(await member1asset.read())
                    member1pfp = Image.open(member1data)

                    n = random.randint(1, 100)
                    love = f"{n} %"
                    heart = heart.resize((42, 42))
                    draw = ImageDraw.Draw(heart)
                    draw.text((10, 10), love, font=font)

                    member2asset = member2.avatar.with_size(128)
                    member2data = BytesIO(await member2asset.read())
                    member2pfp = Image.open(member2data)

                    member1pfp = member1pfp.resize((128, 128))
                    member2pfp = member2pfp.resize((128, 128))

                    obj = BytesIO()
                    width = (template.width - heart.width) // 2
                    height = (template.height - heart.height) // 2
                    template.paste(member1pfp, (0, 0))
                    template.paste(member2pfp, (128, 0))
                    template.paste(heart, (width, height), heart)
                    template.save(obj, format="PNG")
                    obj.seek(0)
                    file = nextcord.File(obj, filename="love.png")
                    embed = nextcord.Embed(
                        colour=0x00FFFF, description=f"``{member1}``  💖  ``{member2}``"
                    )
                    embed.set_image(url="attachment://love.png")
                    embed.set_footer(text=f"┗Requested by {ctx.author}")
                    await ctx.send(embed=embed, file=file)

                elif member2 is None:
                    memberonly = [
                        member for member in ctx.guild.members if not member.bot
                    ]
                    member2 = choice(memberonly)
                    template = Image.open("image/template.png")
                    heart = Image.open("image/heart.png")
                    member2asset = member2.avatar.with_size(128)
                    member2data = BytesIO(await member2asset.read())
                    member2pfp = Image.open(member2data)

                    n = random.randint(1, 100)
                    love = f"{n} %"
                    heart = heart.resize((42, 42))
                    draw = ImageDraw.Draw(heart)
                    draw.text((10, 10), love, font=font)

                    member1asset = member1.avatar.with_size(128)
                    member1data = BytesIO(await member1asset.read())
                    member1pfp = Image.open(member1data)

                    member1pfp = member1pfp.resize((128, 128))
                    member2pfp = member2pfp.resize((128, 128))

                    obj = BytesIO()
                    width = (template.width - heart.width) // 2
                    height = (template.height - heart.height) // 2
                    template.paste(member1pfp, (0, 0))
                    template.paste(member2pfp, (128, 0))
                    template.paste(heart, (width, height), heart)
                    template.save(obj, format="PNG")
                    obj.seek(0)
                    file = nextcord.File(obj, filename="love.png")
                    embed = nextcord.Embed(
                        colour=0x00FFFF, description=f"``{member1}``  💖  ``{member2}``"
                    )
                    embed.set_image(url="attachment://love.png")
                    embed.set_footer(text=f"┗Requested by {ctx.author}")
                    await ctx.send(embed=embed, file=file)

                else:
                    template = Image.open("image/template.png")
                    heart = Image.open("image/heart.png")
                    member1asset = member1.avatar.with_size(128)
                    member1data = BytesIO(await member1asset.read())
                    member1pfp = Image.open(member1data)

                    n = random.randint(1, 100)
                    love = f"{n} %"
                    heart = heart.resize((42, 42))
                    draw = ImageDraw.Draw(heart)
                    draw.text((10, 10), love, font=font)

                    member2asset = member2.avatar.with_size(128)
                    member2data = BytesIO(await member2asset.read())
                    member2pfp = Image.open(member2data)

                    member1pfp = member1pfp.resize((128, 128))
                    member2pfp = member2pfp.resize((128, 128))

                    obj = BytesIO()
                    width = (template.width - heart.width) // 2
                    height = (template.height - heart.height) // 2
                    template.paste(member1pfp, (0, 0))
                    template.paste(member2pfp, (128, 0))
                    template.paste(heart, (width, height), heart)
                    template.save(obj, format="PNG")
                    obj.seek(0)
                    file = nextcord.File(obj, filename="love.png")
                    embed = nextcord.Embed(
                        colour=0x00FFFF, description=f"``{member1}``  💖  ``{member2}``"
                    )
                    embed.set_image(url="attachment://love.png")
                    embed.set_footer(text=f"┗Requested by {ctx.author}")
                    await ctx.send(embed=embed, file=file)

            if server_language == "English":
                if not Path("image/template.png").exists():
                    img = Image.new("RGB", (256, 128), color=(253, 254, 254))
                    img.save("image/template.png")

                else:
                    pass

                if not Path("arial.ttf").exists():
                    dirname = os.path.dirname(os.path.abspath(__file__))
                    fontfile = os.path.join(dirname, "arial.ttf")

                else:
                    fontfile = "arial.ttf"

                font = ImageFont.truetype(fontfile, 15)

                if member1 is None:
                    memberonly1 = [
                        member for member in ctx.guild.members if not member.bot
                    ]
                    member1 = choice(memberonly1)
                    memberonly2 = [
                        member
                        for member in ctx.guild.members
                        if not member.bot and member != member1
                    ]
                    member2 = choice(memberonly2)
                    template = Image.open("image/template.png")
                    heart = Image.open("image/heart.png")
                    member1asset = member1.avatar.with_size(128)
                    member1data = BytesIO(await member1asset.read())
                    member1pfp = Image.open(member1data)

                    n = random.randint(1, 100)
                    love = f"{n} %"
                    heart = heart.resize((42, 42))
                    draw = ImageDraw.Draw(heart)
                    draw.text((10, 10), love, font=font)

                    member2asset = member2.avatar.with_size(128)
                    member2data = BytesIO(await member2asset.read())
                    member2pfp = Image.open(member2data)

                    member1pfp = member1pfp.resize((128, 128))
                    member2pfp = member2pfp.resize((128, 128))

                    obj = BytesIO()
                    width = (template.width - heart.width) // 2
                    height = (template.height - heart.height) // 2
                    template.paste(member1pfp, (0, 0))
                    template.paste(member2pfp, (128, 0))
                    template.paste(heart, (width, height), heart)
                    template.save(obj, format="PNG")
                    obj.seek(0)
                    file = nextcord.File(obj, filename="love.png")
                    embed = nextcord.Embed(
                        colour=0x00FFFF, description=f"``{member1}``  💖  ``{member2}``"
                    )
                    embed.set_image(url="attachment://love.png")
                    embed.set_footer(text=f"┗Requested by {ctx.author}")
                    await ctx.send(embed=embed, file=file)

                elif member2 is None:
                    memberonly = [
                        member for member in ctx.guild.members if not member.bot
                    ]
                    member2 = choice(memberonly)
                    template = Image.open("image/template.png")
                    heart = Image.open("image/heart.png")
                    member2asset = member2.avatar.with_size(128)
                    member2data = BytesIO(await member2asset.read())
                    member2pfp = Image.open(member2data)

                    n = random.randint(1, 100)
                    love = f"{n} %"
                    heart = heart.resize((42, 42))
                    draw = ImageDraw.Draw(heart)
                    draw.text((10, 10), love, font=font)

                    member1asset = member1.avatar.with_size(128)
                    member1data = BytesIO(await member1asset.read())
                    member1pfp = Image.open(member1data)

                    member1pfp = member1pfp.resize((128, 128))
                    member2pfp = member2pfp.resize((128, 128))

                    obj = BytesIO()
                    width = (template.width - heart.width) // 2
                    height = (template.height - heart.height) // 2
                    template.paste(member1pfp, (0, 0))
                    template.paste(member2pfp, (128, 0))
                    template.paste(heart, (width, height), heart)
                    template.save(obj, format="PNG")
                    obj.seek(0)
                    file = nextcord.File(obj, filename="love.png")
                    embed = nextcord.Embed(
                        colour=0x00FFFF, description=f"``{member1}``  💖  ``{member2}``"
                    )
                    embed.set_image(url="attachment://love.png")
                    embed.set_footer(text=f"┗Requested by {ctx.author}")
                    await ctx.send(embed=embed, file=file)

                else:
                    template = Image.open("image/template.png")
                    heart = Image.open("image/heart.png")
                    member1asset = member1.avatar.with_size(128)
                    member1data = BytesIO(await member1asset.read())
                    member1pfp = Image.open(member1data)

                    n = random.randint(1, 100)
                    love = f"{n} %"
                    heart = heart.resize((42, 42))
                    draw = ImageDraw.Draw(heart)
                    draw.text((10, 10), love, font=font)

                    member2asset = member2.avatar.with_size(128)
                    member2data = BytesIO(await member2asset.read())
                    member2pfp = Image.open(member2data)

                    member1pfp = member1pfp.resize((128, 128))
                    member2pfp = member2pfp.resize((128, 128))

                    obj = BytesIO()
                    width = (template.width - heart.width) // 2
                    height = (template.height - heart.height) // 2
                    template.paste(member1pfp, (0, 0))
                    template.paste(member2pfp, (128, 0))
                    template.paste(heart, (width, height), heart)
                    template.save(obj, format="PNG")
                    obj.seek(0)
                    file = nextcord.File(obj, filename="love.png")
                    embed = nextcord.Embed(
                        colour=0x00FFFF, description=f"``{member1}``  💖  ``{member2}``"
                    )
                    embed.set_image(url="attachment://love.png")
                    embed.set_footer(text=f"┗Requested by {ctx.author}")
                    await ctx.send(embed=embed, file=file)

    @commands.command()
    async def captcha(self, ctx: commands.Context, *, text):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = languageserver["Language"]

            if server_language == "Thai":
                image = ImageCaptcha()
                image.write(text, "image/captcha.png")
                file = nextcord.File("image/captcha.png", filename="captcha.png")

                embed = nextcord.Embed(colour=0x00FFFF, title="Captcha")
                embed.set_image(url="attachment://captcha.png")
                embed.set_footer(text=f"┗Requested by {ctx.author}")

                await ctx.send(embed=embed, file=file)

            if server_language == "English":
                image = ImageCaptcha()
                image.write(text, "image/captcha.png")
                file = nextcord.File("image/captcha.png", filename="captcha.png")

                embed = nextcord.Embed(colour=0x00FFFF, title="Captcha")
                embed.set_image(url="attachment://captcha.png")
                embed.set_footer(text=f"┗Requested by {ctx.author}")

                await ctx.send(embed=embed, file=file)

    @captcha.error
    async def captcha_error(self, ctx: commands.Context, error):
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
                        description=f" ⚠️``{ctx.author}`` จะต้องพิมคําที่จะทําเป็น captcha ``{settings.COMMAND_PREFIX}captcha (word)``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` need to specify text to make into captcha ``{settings.COMMAND_PREFIX}captcha (word)``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")


def setup(bot: commands.Bot):
    bot.add_cog(MakeImage(bot))
