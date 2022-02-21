from ast import alias
from aiohttp.helpers import ProxyInfo
import nextcord
from nextcord.ext import commands
import aiohttp
import asyncio
import re
import requests
import settings
from utils.languageembed import languageEmbed
import bson
import json
import idna
from urllib.parse import urlparse


async def get_domain_name_from_url(url):
    return url.split("//")[-1].split("/")[0]


async def bitlybypass(url):
    print(requests.Session().head(url, allow_redirects=True).url)
    return requests.Session().head(url, allow_redirects=True).url


async def get_mode(guild_id):
    # if server setting have scam in it, then check is scam mode is warn or delete
    data = await settings.collection.find_one({"guild_id": guild_id})
    if data is None:
        return "warn"
    else:
        return data["scam"]


async def check_scam_link(message):
    if not message.content.startswith(f"{settings.COMMAND_PREFIX}"):
        link = re.search("(?P<url>https?://[^\s]+)", message.content)
        mode = await get_mode(message.guild.id)

        if link != None:
            link = link.group("url")
            if "bit.ly" in link:
                link = await bitlybypass(link)
            link = idna.decode(urlparse(link).netloc)

            if link in settings.phishing:
                if mode == "warn":
                    await message.channel.send(
                        f"{message.author.mention} โปรดอย่าส่งลิ้งค์ที่ไม่น่าเชื่อถือ | Please do not send a scam link here."
                    )
                elif mode == "delete":
                    await message.delete()
                    await message.channel.send(
                        f"{message.author.mention} โปรดอย่าส่งลิ้งค์ที่ไม่น่าเชื่อถือ | Please do not send a scam link here."
                    )

        else:

            for content in message.content.split():
                if content in settings.phishing:
                    if mode == "warn":
                        await message.channel.send(
                            f"{message.author.mention} โปรดอย่าส่งลิ้งค์ที่ไม่น่าเชื่อถือ | Please do not send a scam link here."
                        )
                    elif mode == "delete":
                        await message.delete()
                        await message.channel.send(
                            f"{message.author.mention} โปรดอย่าส่งลิ้งค์ที่ไม่น่าเชื่อถือ | Please do not send a scam link here."
                        )


class Scam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, aliases=["helpscam"])
    async def scam(self, ctx):
        languageserver = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if languageserver is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            languageserver = languageserver["Language"]
            if languageserver == "Thai":
                embed = nextcord.Embed(
                    title="ข้อมูลเกี่ยวคำสั่ง scam",
                    colour=0xFED000,
                )
                embed.add_field(
                    name="Add",
                    value="ส่งคำขอเพิ่มลิ้งที่ไม่ปลอดภัยไปให้ผู้พัฒนา | `scam add [link]`",
                )
                embed.add_field(
                    name="Remove",
                    value="ส่งคำขอลบลิ้งที่ไม่ปลอดภัยไปให้ผู้พัฒนา | `scam remove [link]`",
                )
                embed.add_field(
                    name="Mode",
                    value="ตั้งค่า ลบหรือเตือนเฉยๆหากมีคนส่งลิงค์ Virus | `scam mode [warn/delete]`",
                )
                embed.add_field(
                    name="📢หมายเหตุ",
                    value="""```
[] คือ ค่าที่จำเป็นต้องใส่
/ คือ หรือ
<> คือ ค่าที่จะใส่หรือไม่ใส่ก็ได้``````
• เพื่อให้บอทสามารถใช้งานได้ทุกฟังชั่นควรให้บอทมีบทบาท Administrator (ผู้ดูเเล)
• ฟังชั่นไม่สามารถทํางานในเเชทส่วนตัวได้
```
""",
                    inline=False,
                )
            elif languageserver == "English":
                embed = nextcord.Embed(
                    title="Scam command information",
                    colour=0xFED000,
                )
                embed.add_field(
                    name="Add",
                    value="Request to add scam link to developer | `scam add [link]`",
                )
                embed.add_field(
                    name="Remove",
                    value="Request to remove scam link to developer | `scam remove [link]`",
                )
                embed.add_field(
                    name="Mode",
                    value="Set wheter to warn or delete virus link | `scam mode [warn/delete]`",
                )
                embed.add_field(
                    name="📢Note",
                    value="""```
[] = required
/ = or
<> = optional``````
• In order for bots to use all functions, bots should have Administrator permission.
• The function cannot work in private chat.
```
""",
                    inline=False,
                )
            await ctx.send(embed=embed)

    @scam.command()
    async def mode(self, ctx, mode1):
        languageserver = await get_server_lang(ctx)
        if languageserver == "Thai":
            if mode1 == "warn":
                await settings.collection.update_one(
                    {"guild_id": ctx.guild.id}, {"$set": {"scam": "warn"}}
                )
                await ctx.send(f"{ctx.author.mention} ตั้งโหมดเป็นตักเตือนแล้ว")
            elif mode1 == "delete":
                await settings.collection.update_one(
                    {"guild_id": ctx.guild.id}, {"$set": {"scam": "delete"}}
                )
                await ctx.send(f"{ctx.author.mention} ตั้งโหมดเป็นลบทันทีแล้ว")

            else:
                await ctx.send(
                    f"{ctx.author.mention} กรุณาใช้ `{settings.COMMAND_PREFIX} scam mode [warn/delete]`"
                )

        if languageserver == "English":
            if mode1 == "warn":
                await settings.collection.update_one(
                    {"guild_id": ctx.guild.id}, {"$set": {"scam": "warn"}}
                )
                await ctx.send(f"{ctx.author.mention} Set mode to warn")
            elif mode1 == "delete":
                await settings.collection.update_one(
                    {"guild_id": ctx.guild.id}, {"$set": {"scam": "delete"}}
                )
                await ctx.send(f"{ctx.author.mention} Set mode to delete")

            else:
                await ctx.send(
                    f"{ctx.author.mention} Please use `{settings.COMMAND_PREFIX} scam mode [warn/delete]`"
                )

    @scam.command()
    async def add(self, ctx: commands.Context, link=None):
        server_lang = await get_server_lang(ctx)
        link = await get_domain_name_from_url(link)
        if server_lang == "Thai":
            if link != None:
                if link in settings.phishing:
                    await ctx.send(f"{ctx.author.mention} มีลิ้งค์นี้ในระบบแล้ว")
                    return

                with open("data/request_approve.json", "r") as f:
                    data = json.load(f)

                newdata = {
                    "category": "add",
                    "link": link,
                    "author": str(ctx.author),
                    "author_id": ctx.author.id,
                    "id": str(bson.objectid.ObjectId()),
                }
                data.append(newdata)

                with open("data/request_approve.json", "w") as f:
                    json.dump(data, f, indent=2)

                for dev in settings.developers:
                    user = await self.bot.fetch_user(dev)
                    text = await text_beautifier(
                        f"New add scam link request from {str(ctx.author)}\nData : {json.dumps(newdata, indent=2)}"
                    )
                    await user.send(text)

                await ctx.send(f"{ctx.author.mention} ส่งคำขอเพิ่มลิ้งสำเร็จ")
            else:
                await ctx.send(
                    f"{ctx.author.mention} กรุณาใช้ `{settings.COMMAND_PREFIX} scam add [link]`"
                )

        elif server_lang == "English":
            if link != None:
                if link in settings.phishing:
                    await ctx.send(
                        f"{ctx.author.mention} The link is already in the database"
                    )
                    return

                with open("data/request_approve.json", "r") as f:
                    data = json.load(f)

                id = str(bson.objectid.ObjectId())
                newdata = {
                    "category": "add",
                    "link": link,
                    "author": str(ctx.author),
                    "author_id": ctx.author.id,
                    "id": id,
                }
                data.append(newdata)

                with open("data/request_approve.json", "w") as f:
                    json.dump(data, f, indent=2)

                for dev in settings.developers:
                    user = await self.bot.fetch_user(dev)
                    text = await text_beautifier(
                        f"New add scam link request from {str(ctx.author)}\nData : {json.dumps(newdata, indent=2)}"
                    )
                    await user.send(text)

                await ctx.send(f"{ctx.author.mention} Request add link success")
                await ctx.author.send(
                    f"Your request add link has been sent to developer\nTo cancel your request, use `{settings.COMMAND_PREFIX} scam cancel {id}`"
                )
            else:
                await ctx.send(
                    f"{ctx.author.mention} Please use `{settings.COMMAND_PREFIX} scam add [link]`"
                )

    @scam.command()
    async def remove(self, ctx: commands.Context, link=None):
        server_lang = await get_server_lang(ctx)
        link = await get_domain_name_from_url(link)
        if server_lang == "Thai":
            if link != None:
                if link not in settings.phishing:
                    await ctx.send(f"{ctx.author.mention} ไม่มีลิ้งค์นี้ในระบบ")
                    return

                with open("data/request_approve.json", "r") as f:
                    data = json.load(f)

                newdata = {
                    "category": "remove",
                    "link": link,
                    "author": str(ctx.author),
                    "author_id": ctx.author.id,
                    "id": str(bson.objectid.ObjectId()),
                }
                data.append(newdata)

                with open("data/request_approve.json", "w") as f:
                    json.dump(data, f, indent=2)

                for dev in settings.developers:
                    user = await self.bot.fetch_user(dev)
                    text = await text_beautifier(
                        f"New remove scam link request from {str(ctx.author)}\nData : {json.dumps(newdata, indent=2)}"
                    )
                    await user.send(text)

                await ctx.send(f"{ctx.author.mention} ส่งคำขอลบลิ้งสำเร็จ")
            else:
                await ctx.send(
                    f"{ctx.author.mention} กรุณาใช้ `{settings.COMMAND_PREFIX} scam remove [link]`"
                )

        elif server_lang == "English":
            if link != None:
                if link not in settings.phishing:
                    await ctx.send(
                        f"{ctx.author.mention} The link is not in the database"
                    )
                    return

                with open("data/request_approve.json", "r") as f:
                    data = json.load(f)

                id = str(bson.objectid.ObjectId())
                newdata = {
                    "category": "remove",
                    "link": link,
                    "author": str(ctx.author),
                    "author_id": ctx.author.id,
                    "id": id,
                }
                data.append(newdata)

                with open("data/request_approve.json", "w") as f:
                    json.dump(data, f, indent=2)

                for dev in settings.developers:
                    user = await self.bot.fetch_user(dev)
                    text = await text_beautifier(
                        f"New remove scam link request from {str(ctx.author)}\nData : {json.dumps(newdata, indent=2)}"
                    )
                    await user.send(text)

                await ctx.send(f"{ctx.author.mention} Request remove link success")
                await ctx.author.send(
                    f"Your request remove link has been sent to developer\nTo cancel your request, use `{settings.COMMAND_PREFIX} scam cancel {id}`"
                )
            else:
                await ctx.send(
                    f"{ctx.author.mention} Please use `{settings.COMMAND_PREFIX} scam remove [link]`"
                )

    @scam.command(aliases=["request_list"])
    async def list(self, ctx: commands.Context):
        server_lang = await get_server_lang(ctx)
        if server_lang == "Thai":
            if ctx.author.id in settings.developers:
                await ctx.send(f"{ctx.author.mention} ส่งไปที่แชทส่วนตัวแล้ว!!!.")
                with open("data/request_approve.json", "r") as f:
                    data = json.load(f)

                text = await text_beautifier(
                    f"The list of all requests\n{json.dumps(data, indent=2)}"
                )
                await ctx.author.send(text)
            else:
                await ctx.send("คุณไม่มีสิทธิ์ใช้คำสั่งนี้")

        elif server_lang == "English":
            if ctx.author.id in settings.developers:
                await ctx.send(f"{ctx.author.mention} I have sent it to you DM!!!.")
                with open("data/request_approve.json", "r") as f:
                    data = json.load(f)

                text = await text_beautifier(
                    f"The list of all requests\n{json.dumps(data, indent=2)}"
                )
                await ctx.author.send(text)
            else:
                await ctx.send("You don't have permission to use this command")

    @scam.command()
    async def approve(self, ctx: commands.Context, id):
        server_lang = await get_server_lang(ctx)
        if server_lang == "Thai":
            if ctx.author.id in settings.developers:
                with open("data/request_approve.json", "r") as f:
                    data = json.load(f)

                for i in data:
                    if i["id"] == id:
                        if i["category"] == "add":

                            settings.phishing.append(i["link"])
                            settings.phishing.sort()

                            with open("data/phishing.txt", "w") as f:
                                f.write("\n".join(settings.phishing))

                            await ctx.send(
                                f"{ctx.author.mention} อนุมัติคำขอเพิ่มลิ้งสำเร็จ"
                            )

                            data.remove(i)
                            with open("data/request_approve.json", "w") as f:
                                json.dump(data, f, indent=2)
                            break
                        elif i["category"] == "remove":
                            for j in settings.phishing:
                                if j == i["link"]:
                                    settings.phishing.remove(j)
                                    settings.phishing.sort()
                                    with open("data/phishing.txt", "w") as f:
                                        f.write("\n".join(settings.phishing))
                                    break
                            await ctx.send(
                                f"{ctx.author.mention} อนุมัติคำขอลบลิ้งสำเร็จ"
                            )
                            data.remove(i)
                            with open("data/request_approve.json", "w") as f:
                                json.dump(data, f, indent=2)
                            break
                for dev_user_id in settings.developers:
                    user = await self.bot.fetch_user(dev_user_id)
                    text = await text_beautifier(
                        f"{str(ctx.author)} has approved the request from {i['author']}\nid : {i['id']}\ncategory : {i['category']}\nlink : {i['link']}"
                    )
                    await user.send(text)
            else:
                await ctx.send("คุณไม่มีสิทธิ์ในการใช้คำสั่งนี้")
        elif server_lang == "English":
            if ctx.author.id in settings.developers:
                with open("data/request_approve.json", "r") as f:
                    data = json.load(f)

                for i in data:
                    if i["id"] == id:
                        if i["category"] == "add":
                            settings.phishing.append(i["link"])
                            settings.phishing.sort()
                            with open("data/phishing.txt", "w") as f:
                                f.write("\n".join(settings.phishing))

                            await ctx.send(
                                f"{ctx.author.mention} Approve add link success"
                            )
                            data.remove(i)
                            with open("data/request_approve.json", "w") as f:
                                json.dump(data, f, indent=2)
                            break
                        elif i["category"] == "remove":
                            for j in settings.phishing:
                                if j == i["link"]:
                                    settings.phishing.remove(j)
                                    settings.phishing.sort()
                                    with open("data/phishing.txt", "w") as f:
                                        f.write("\n".join(settings.phishing))
                                    break
                            await ctx.send(
                                f"{ctx.author.mention} Approve remove link success"
                            )

                            data.remove(i)
                            with open("data/request_approve.json", "w") as f:
                                json.dump(data, f, indent=2)
                            break

                for dev_user_id in settings.developers:
                    user = await self.bot.fetch_user(dev_user_id)
                    text = await text_beautifier(
                        f"{str(ctx.author)} has approved the request from {i['author']}\nid : {i['id']}\ncategory : {i['category']}\nlink : {i['link']}"
                    )
                    await user.send(text)

            else:
                await ctx.send("You don't have permission to use this command")

    @scam.command()
    async def disapprove(self, ctx: commands.Context, id):
        server_lang = await get_server_lang(ctx)
        if server_lang == "Thai":
            if ctx.author.id in settings.developers:
                with open("data/request_approve.json", "r") as f:
                    data = json.load(f)

                for i in data:
                    if i["id"] == id:
                        await ctx.send(f"{ctx.author.mention} ปฏิเสธคำขอแล้ว")
                        data.remove(i)
                        with open("data/request_approve.json", "w") as f:
                            json.dump(data, f, indent=2)
                        break
                for dev_user_id in settings.developers:
                    user = await self.bot.fetch_user(dev_user_id)
                    text = await text_beautifier(
                        f"{str(ctx.author)} has disapproved the request from {i['author']}\nid : {i['id']}\ncategory : {i['category']}\nlink : {i['link']}"
                    )
                    await user.send(text)
            else:
                await ctx.send("คุณไม่มีสิทธิ์ในการใช้คำสั่งนี้")
        elif server_lang == "English":
            if ctx.author.id in settings.developers:
                with open("data/request_approve.json", "r") as f:
                    data = json.load(f)

                for i in data:
                    if i["id"] == id:
                        await ctx.send(f"{ctx.author.mention} Approve add link success")
                        data.remove(i)
                        with open("data/request_approve.json", "w") as f:
                            json.dump(data, f, indent=2)
                        break

                for dev_user_id in settings.developers:
                    user = await self.bot.fetch_user(dev_user_id)
                    text = await text_beautifier(
                        f"{str(ctx.author)} has approved the request from {i['author']}\nid : {i['id']}\ncategory : {i['category']}\nlink : {i['link']}"
                    )
                    await user.send(text)
            else:
                await ctx.send("You don't have permission to use this command")

    @scam.command()
    async def cancel(self, ctx: commands.Context, id):
        server_lang = await get_server_lang(ctx)
        if server_lang == "Thai":
            with open("data/request_approve.json", "r") as f:
                data = json.load(f)

            for i in data:
                if i["id"] == id:
                    await ctx.send(f"{ctx.author.mention} ยกเลิกคำขอแล้ว")
                    data.remove(i)
                    with open("data/request_approve.json", "w") as f:
                        json.dump(data, f, indent=2)
                    break

            for dev_user_id in settings.developers:
                user = await self.bot.fetch_user(dev_user_id)
                text = await text_beautifier(
                    f"{str(ctx.author)} has canceled his request.\nid : {i['id']}\ncategory : {i['category']}\nlink : {i['link']}"
                )
                await user.send(text)

        elif server_lang == "English":
            with open("data/request_approve.json", "r") as f:
                data = json.load(f)

            for i in data:
                if i["id"] == id:
                    await ctx.send("Cancel request success")
                    data.remove(i)
                    with open("data/request_approve.json", "w") as f:
                        json.dump(data, f, indent=2)
                    break

            for dev_user_id in settings.developers:
                user = await self.bot.fetch_user(dev_user_id)
                text = await text_beautifier(
                    f"{str(ctx.author)} has canceled his request.\nid : {i['id']}\ncategory : {i['category']}\nlink : {i['link']}"
                )
                await user.send(text)


async def get_server_lang(ctx: commands.Context):
    server_lang = await settings.collectionlanguage.find_one({"guild_id": ctx.guild.id})
    if server_lang is None:
        message = await ctx.send(embed=languageEmbed.languageembed(ctx))
        await message.add_reaction("👍")
        return None

    return server_lang["Language"]


async def text_beautifier(text):
    start_end = "-" * 50
    result = start_end + "\n" + text + "\n" + start_end
    return result


def setup(bot):
    bot.add_cog(Scam(bot))
