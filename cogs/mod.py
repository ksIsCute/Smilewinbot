import nextcord
import settings
import time
from utils.languageembed import languageEmbed
from nextcord.ext import commands


class Mod(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(
        self, ctx: commands.Context, member: nextcord.Member, *, reason=None
    ):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                await member.kick(reason=reason)
                if reason is None:
                    reason = "None"

                embed = nextcord.Embed(
                    color=0x983925,
                    title=f"😤 สมาชิก {member} ถูกเตะออกจากเซิร์ฟเวอร์",
                    description=f"""
                    ผู้เเตะ : ``{ctx.author}``
                    สาเหตุ : ``{reason}``""",
                )

                embed.set_thumbnail(url=f"{member.avatar.url}")
                embed.set_footer(text=f"┗Requested by {ctx.author}")

                message = await ctx.send(embed=embed)
                await message.add_reaction("😤")

            if server_language == "English":
                await member.kick(reason=reason)
                if reason is None:
                    reason = "None"

                embed = nextcord.Embed(
                    color=0x983925,
                    title=f"😤 {member} have been kicked from server",
                    description=f"""
                    Punisher : ``{ctx.author}``
                    Reason : ``{reason}``""",
                )

                embed.set_thumbnail(url=f"{member.avatar.url}")
                embed.set_footer(text=f"┗Requested by {ctx.author}")

                message = await ctx.send(embed=embed)
                await message.add_reaction("😤")

    @kick.error
    async def kick_error(self, ctx: commands.Context, error):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="ชื่อสมาชิกที่จะเเตะ",
                        description=f" ⚠️``{ctx.author}`` จะต้องใส่ชื่อของสมาชิกที่จะเเตะ ``{settings.COMMAND_PREFIX}kick [@user]``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="คุณไม่มีสิทธิ์เเตะ",
                        description=f"⚠️ ``{ctx.author}`` ไม่สามารถใช้งานคำสั่งนี้ได้ คุณจำเป็นต้องมีสิทธิ์ ``เเตะ`` ก่อนใช้งานคำสั่งนี้",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="Specify member",
                        description=f" ⚠️``{ctx.author}`` need to specify who to kick ``{settings.COMMAND_PREFIX}kick [@user]``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="You don't have permission",
                        description=f"⚠️ ``{ctx.author}`` You must have ``kick`` to be able to use this command",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, member: nextcord.Member, *, reason=None):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                await member.ban(reason=reason)
                if reason is None:
                    reason = "None"

                embed = nextcord.Embed(
                    color=0x983925,
                    title=f"😤 สมาชิก {member} ถูกเเบนออกจากเซิร์ฟเวอร์",
                    description=f"""
                    ผู้เเบน : ``{ctx.author}``
                    สาเหตุ : ``{reason}``""",
                )

                embed.set_thumbnail(url=f"{member.avatar.url}")
                embed.set_footer(text=f"┗Requested by {ctx.author}")

                message = await ctx.send(embed=embed)
                await message.add_reaction("😤")

            if server_language == "English":
                await member.ban(reason=reason)
                if reason is None:
                    reason = "None"

                embed = nextcord.Embed(
                    color=0x983925,
                    title=f"😤 {member} have been banned from server",
                    description=f"""
                    Punisher : ``{ctx.author}``
                    Reason : ``{reason}``""",
                )

                embed.set_thumbnail(url=f"{member.avatar.url}")
                embed.set_footer(text=f"┗Requested by {ctx.author}")

                message = await ctx.send(embed=embed)
                await message.add_reaction("😤")

    @ban.error
    async def ban_error(self, ctx: commands.Context, error):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="ชื่อสมาชิกที่จะเเบน",
                        description=f" ⚠️``{ctx.author}`` จะต้องใส่ชื่อของสมาชิกที่จะเเบน ``{settings.COMMAND_PREFIX}ban [@user]``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="คุณไม่มีสิทธิ์เเตะ",
                        description=f"⚠️ ``{ctx.author}`` ไม่สามารถใช้งานคำสั่งนี้ได้ คุณจำเป็นต้องมีสิทธิ์ ``เเบน`` ก่อนใช้งานคำสั่งนี้",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="Specify member",
                        description=f" ⚠️``{ctx.author}`` need to specify who to ban ``{settings.COMMAND_PREFIX}ban [@user]``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="You don't have permission",
                        description=f"⚠️ ``{ctx.author}`` You must have ``ban`` to be able to use this command",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx: commands.Context, *, member):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                banned_users = await ctx.guild.bans()
                member_name, member_discriminator = member.split("#")
                for ban_entry in banned_users:
                    user = ban_entry.user
                    if (user.name, user.discriminator) == (
                        member_name,
                        member_discriminator,
                    ):
                        await ctx.guild.unban(user)
                        embed = nextcord.Embed(
                            colour=0x00FFFF,
                            title=f"ปลดเเบน {member}",
                            description=f"{member} ได้ถูกปลนเเบน",
                        )
                        embed.set_footer(text=f"┗Requested by {ctx.author}")
                        await ctx.send(embed=embed)

                    else:
                        embed = nextcord.Embed(
                            colour=0x983925,
                            title=f"ไม่พบชื่อ {member}",
                            description="ไม่มีชื่อนี้ในรายชื่อคนที่ถูกเเบนโปรดเช็คชื่อเเละเลขข้างหลัง",
                        )
                        embed.set_footer(text=f"┗Requested by {ctx.author}")
                        await ctx.send(embed=embed)

            if server_language == "English":
                banned_users = await ctx.guild.bans()
                member_name, member_discriminator = member.split("#")
                for ban_entry in banned_users:
                    user = ban_entry.user
                    if (user.name, user.discriminator) == (
                        member_name,
                        member_discriminator,
                    ):
                        await ctx.guild.unban(user)
                        embed = nextcord.Embed(
                            colour=0x00FFFF,
                            title=f"unban {member}",
                            description=f"{member} have been unban",
                        )
                        embed.set_footer(text=f"┗Requested by {ctx.author}")
                        await ctx.send(embed=embed)

                    else:
                        embed = nextcord.Embed(
                            colour=0x983925,
                            title=f"No user named {member}",
                            description="Please check spelling and number behind the name",
                        )
                        embed.set_footer(text=f"┗Requested by {ctx.author}")
                        await ctx.send(embed=embed)

    @unban.error
    async def unban_error(self, ctx: commands.Context, error):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` จะต้องใส่ชื่อของคนที่ต้องการจะปลดเเบน ``{settings.COMMAND_PREFIX}unban (member#1111)``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="คุณไม่มีสิทธิ์ปลดเเบน",
                        description=f"⚠️ ``{ctx.author}`` ไม่สามารถใช้งานคำสั่งนี้ได้ คุณจำเป็นต้องมีสิทธิ์ ``เเอดมิน`` ก่อนใช้งานคำสั่งนี้",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="Specify member",
                        description=f" ⚠️``{ctx.author}`` need to specify who to unban ``{settings.COMMAND_PREFIX}unban (member#1111)``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="You don't have permission",
                        description=f"⚠️ ``{ctx.author}`` You must have ``Administrator`` to be able to use this command",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def giverole(
        self, ctx: commands.Context, user: nextcord.Member, role: nextcord.Role
    ):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                try:
                    await user.add_roles(role)
                    embed = nextcord.Embed(
                        colour=0x00FFFF,
                        description=f"ได้ทําการเพิ่มยศ {role} ให้กับ {user} ",
                    )

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("✅")

                except nextcord.Forbidden:
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f"ไม่สามารถให้ยศ{role} กับ {user.name} ได้",
                    )
                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":
                try:
                    await user.add_roles(role)
                    embed = nextcord.Embed(
                        colour=0x00FFFF, description=f"{role} have been given to {user}"
                    )

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("✅")

                except nextcord.Forbidden:
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f"unable to give role {role} to {user.name}",
                    )
                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

    @giverole.error
    async def giverole_error(self, ctx: commands.Context, error):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` จะต้องใส่ชื่อของคนที่ต้องการจะให้ยศเเละยศที่จะให้ ``{settings.COMMAND_PREFIX}giverole @user @role``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="คุณไม่มีสิทธิ์ให้ยศ",
                        description=f"⚠️ ``{ctx.author}`` ไม่สามารถใช้งานคำสั่งนี้ได้ คุณจำเป็นต้องมีสิทธิ์ ``เเอดมิน`` ก่อนใช้งานคำสั่งนี้",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` need to specify member and specify what role to give``{settings.COMMAND_PREFIX}giverole @user @role``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="You don't have permission",
                        description=f"⚠️ ``{ctx.author}`` You must have ``admin`` to be able to use this command",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removerole(
        self, ctx: commands.Context, user: nextcord.Member, role: nextcord.Role
    ):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                try:
                    await user.remove_roles(role)
                    embed = nextcord.Embed(
                        colour=0x00FFFF,
                        description=f"ได้ทําการเอายศ {role} ออกให้กับ {user}",
                    )

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("✅")

                except nextcord.Forbidden:
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f"ไม่สามารถเอายศ {role} ของ {user.name} ออกได้",
                    )
                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":
                try:
                    await user.remove_roles(role)
                    embed = nextcord.Embed(
                        colour=0x00FFFF,
                        description=f"{role} have been removed from {user}",
                    )

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("✅")

                except nextcord.Forbidden:
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f"unable to remove role {role} from {user.name}",
                    )
                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

    @removerole.error
    async def removerole_error(self, ctx: commands.Context, error):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` จะต้องใส่ชื่อของคนที่ต้องการจะให้ยศเเละยศที่เอาออก ``{settings.COMMAND_PREFIX}removerole @role``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="คุณไม่มีสิทธิ์เอายศออก",
                        description=f"⚠️ ``{ctx.author}`` ไม่สามารถใช้งานคำสั่งนี้ได้ คุณจำเป็นต้องมีสิทธิ์ ``เเอดมิน`` ก่อนใช้งานคำสั่งนี้",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` need to specify member and specify what role to remove ``{settings.COMMAND_PREFIX}giverole @user @role``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="You don't have permission",
                        description=f"⚠️ ``{ctx.author}`` You must have ``admin`` to be able to use this command",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def changenick(self, ctx: commands.Context, user: nextcord.Member, Change):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                embed = nextcord.Embed(
                    colour=0x00FFFF,
                    description=f"ได้ทําการเปลี่ยนชื่อ {user.name} เป็น {Change}",
                )

                message = await ctx.send(embed=embed)
                await message.add_reaction("✅")
                await user.edit(nick=Change)

            if server_language == "English":
                embed = nextcord.Embed(
                    colour=0x00FFFF,
                    description=f"{user.name} Name have been change to {Change}",
                )

                message = await ctx.send(embed=embed)
                await message.add_reaction("✅")
                await user.edit(nick=Change)

    @changenick.error
    async def changenick_error(self, ctx: commands.Context, error):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` จะต้องใส่ชื่อของคนที่ต้องที่จะเปลี่ยนชื่อเเละชื่อใหม่ ``{settings.COMMAND_PREFIX}changenick @member newnick``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="คุณไม่มีสิทธิ์เปลี่ยนชื่อ",
                        description=f"⚠️ ``{ctx.author}`` ไม่สามารถใช้งานคำสั่งนี้ได้ คุณจำเป็นต้องมีสิทธิ์ ``เเอดมิน`` ก่อนใช้งานคำสั่งนี้",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` need to specify member and new nickname ``{settings.COMMAND_PREFIX}changenick @member newnick``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="You don't have permission",
                        description=f"⚠️ ``{ctx.author}`` You must have ``kick`` to be able to use this command",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx: commands.Context, amount: int):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":

                if amount < 2000:
                    await ctx.channel.purge(limit=amount + 1)

                else:
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title=f"คําสั่งลบข้อความ {amount}",
                        description=f"⚠️ ``{ctx.author}`` การลบข้อความที่จํานวนมากกว่า 2000 นั้นมากเกินไป",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":

                if amount < 2000:
                    await ctx.channel.purge(limit=amount + 1)

                else:
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title=f"Clear message {amount}",
                        description=f"⚠️ ``{ctx.author}`` Cannot clear more than 2000 messages",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

    @clear.error
    async def clear_error(self, ctx: commands.Context, error):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="จํานวนข้อความที่ต้องการที่จะลบ",
                        description=f" ⚠️``{ctx.author}`` จะต้องใส่จํานวนของข้อความที่จะลบหลังจากคําสั่ง ``{settings.COMMAND_PREFIX}clear [จํานวน]``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="คุณไม่มีสิทธิ์ลบข้อความ",
                        description=f"⚠️ ``{ctx.author}`` ไม่สามารถใช้งานคำสั่งนี้ได้ คุณจำเป็นต้องมีสิทธิ์ ``ลบข้อความ`` ก่อนใช้งานคำสั่งนี้",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="Amount of messages",
                        description=f" ⚠️``{ctx.author}`` need to specify amount of messages to delete ``{settings.COMMAND_PREFIX}clear [จํานวน]``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="You don't have permission",
                        description=f"⚠️ ``{ctx.author}`` You must have ``manage messages`` to be able to use this command",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def roleall(self, ctx: commands.Context, role: nextcord.Role):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                i = 0
                embed = nextcord.Embed(
                    title="ให้ยศสมาชิกทุกคน",
                    colour=0x00FFFF,
                    description=f"กําลังดําเนินการให้ยศ {role} กับสมาชิกทั้งหมด {ctx.guild.member_count}คน",
                )
                message = await ctx.send(embed=embed)

                for user in ctx.guild.members:

                    try:
                        await user.add_roles(role)
                        time.sleep(0.5)
                        i += 1

                    except nextcord.Forbidden:
                        pass

                embed = nextcord.Embed(
                    title="ให้ยศสมาชิกทุกคน",
                    colour=0x00FFFF,
                    description=f"ให้ยศ {role} สมาชิกทั้งหมด {i}คนสําเร็จ",
                )
                await message.edit(embed=embed)

            if server_language == "English":
                i = 0
                embed = nextcord.Embed(
                    title="give role to all members",
                    colour=0x00FFFF,
                    description=f"Progressing to give role {role} to {ctx.guild.member_count} members",
                )
                message = await ctx.send(embed=embed)

                for user in ctx.guild.members:

                    try:
                        await user.add_roles(role)
                        time.sleep(0.5)
                        i += 1

                    except nextcord.Forbidden:
                        pass
                embed = nextcord.Embed(
                    title="give role to all members",
                    colour=0x00FFFF,
                    description=f"successfully give role {role} to {i} members",
                )
                await message.edit(embed=embed)

    @roleall.error
    async def roleall_error(self, ctx: commands.Context, error):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` จะต้องใส่ยศที่จะให้ ``{settings.COMMAND_PREFIX}roleall @role``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="คุณไม่มีสิทธิ์เเอดมิน",
                        description=f"⚠️ ``{ctx.author}`` ไม่สามารถใช้งานคำสั่งนี้ได้ คุณจำเป็นต้องมีสิทธิ์ ``เเอดมิน`` ก่อนใช้งานคำสั่งนี้",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` need to specify what role to give ``{settings.COMMAND_PREFIX}roleall @role``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="You don't have permission",
                        description=f"⚠️ ``{ctx.author}`` You must have ``admin`` to be able to use this command",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removeroleall(self, ctx: commands.Context, role: nextcord.Role):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                i = 0
                embed = nextcord.Embed(
                    title="ลบยศสมาชิกทุกคน",
                    colour=0x00FFFF,
                    description=f"กําลังดําเนินการลบยศ {role} กับสมาชิกทั้งหมด {ctx.guild.member_count}คน",
                )
                message = await ctx.send(embed=embed)

                for user in ctx.guild.members:

                    try:
                        await user.remove_roles(role)
                        time.sleep(0.5)
                        i += 1

                    except nextcord.Forbidden:
                        pass

                embed = nextcord.Embed(
                    title="ลบยศสมาชิกทุกคน",
                    colour=0x00FFFF,
                    description=f"ลบยศ {role} สมาชิกทั้งหมด {i}คนสําเร็จ",
                )
                await message.edit(embed=embed)

            if server_language == "English":
                i = 0
                embed = nextcord.Embed(
                    title="remove role from all members",
                    colour=0x00FFFF,
                    description=f"Progressing to remove role {role} from {ctx.guild.member_count} members",
                )
                message = await ctx.send(embed=embed)

                for user in ctx.guild.members:

                    try:
                        await user.remove_roles(role)
                        time.sleep(0.5)
                        i += 1

                    except nextcord.Forbidden:
                        pass
                embed = nextcord.Embed(
                    title="remove role from all members",
                    colour=0x00FFFF,
                    description=f"successfully remove role {role} from {i} members",
                )
                await message.edit(embed=embed)

    @roleall.error
    async def removeroleall_error(self, ctx: commands.Context, error):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` จะต้องใส่ยศที่จะให้ ``{settings.COMMAND_PREFIX}removeroleall @role``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="คุณไม่มีสิทธิ์เเอดมิน",
                        description=f"⚠️ ``{ctx.author}`` ไม่สามารถใช้งานคำสั่งนี้ได้ คุณจำเป็นต้องมีสิทธิ์ ``เเอดมิน`` ก่อนใช้งานคำสั่งนี้",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` need to specify what role to remove ``{settings.COMMAND_PREFIX}removeroleall @role``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="You don't have permission",
                        description=f"⚠️ ``{ctx.author}`` You must have ``admin`` to be able to use this command",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def movetome(self, ctx: commands.Context, member: nextcord.Member):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                if ctx.author.voice and ctx.author.voice.channel:
                    await member.move_to(channel=ctx.author.voice.channel)

                    embed = nextcord.Embed(
                        colour=0x00FFFF,
                        title=f"{member}ได้ถูกย้ายไปที่ห้องของ {ctx.author}",
                    )
                    message = await ctx.send(embed=embed)
                    await message.add_reaction("✅")

                else:
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` คุณไม่ได้อยู่ในห้องคุย",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":
                if ctx.author.voice and ctx.author.voice.channel:
                    await member.move_to(channel=ctx.author.voice.channel)

                    embed = nextcord.Embed(
                        colour=0x00FFFF,
                        title=f"{member}have been move to {ctx.author} voice chat",
                    )
                    message = await ctx.send(embed=embed)
                    await message.add_reaction("✅")

                else:
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` You are not connected to voice chat",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

    @movetome.error
    async def movetome_error(self, ctx: commands.Context, error):
        language = await settings.collectionlanguage.find_one(
            {"guild_id": ctx.guild.id}
        )
        if language is None:
            message = await ctx.send(embed=languageEmbed.languageembed(self, ctx))
            await message.add_reaction("👍")

        else:
            server_language = language["Language"]

            if server_language == "Thai":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` จะต้องพิมสิ่งที่จะส่ง ``{settings.COMMAND_PREFIX}movetome @member``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="คุณไม่มีสิทธิ์เเอดมิน",
                        description=f"⚠️ ``{ctx.author}`` ไม่สามารถใช้งานคำสั่งนี้ได้ คุณจำเป็นต้องมีสิทธิ์ ``เเอดมิน`` ก่อนใช้งานคำสั่งนี้",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

            if server_language == "English":
                if isinstance(error, commands.MissingRequiredArgument):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        description=f" ⚠️``{ctx.author}`` need to specify a member to move ``{settings.COMMAND_PREFIX}movetome @member``",
                    )
                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")

                if isinstance(error, commands.MissingPermissions):
                    embed = nextcord.Embed(
                        colour=0x983925,
                        title="You don't have permission",
                        description=f"⚠️ ``{ctx.author}`` You must have ``Administrator`` to be able to use this command",
                    )

                    embed.set_footer(text=f"┗Requested by {ctx.author}")

                    message = await ctx.send(embed=embed)
                    await message.add_reaction("⚠️")


def setup(bot: commands.Bot):
    bot.add_cog(Mod(bot))
