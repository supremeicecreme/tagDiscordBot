import discord
from discord.ext import commands
import dataAccess
import constants

bot = commands.Bot(command_prefix=">")


@bot.event
async def on_connect():
    print("Connected as {0.user}".format(bot))


@bot.command(name="admin")
async def admin(ctx, *, args=None):
    if not args:
        embed = discord.Embed()
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.title = "Error"
        embed.description = "You didn't supply a further command.\n" \
                            "If you're an admin, you can use `>admin add <id/@user>` or `>admin remove <id/@user>`"
        embed.colour = discord.Colour.red()
        await ctx.send(embed=embed)
    else:
        args = args.split(" ")
        if args[0] == "add":
            admins = dataAccess.get_admins_by_guild(ctx.guild.id)
            if ctx.author.id in admins:
                add_id = args[1].replace("<", "").replace(">", "").replace("@", "").replace("!", "")
                dataAccess.add_admin(add_id, ctx.guild.id)
                embed = discord.Embed()
                embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.title = "Success"
                embed.description = "Admin <@{0}> added!".format(add_id)
                embed.colour = discord.Colour.green()
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed()
                embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.title = "Error"
                embed.description = "You are not an admin in this server"
                embed.colour = discord.Colour.red()
                await ctx.send(embed=embed)
        elif args[0] == "remove":
            admins = dataAccess.get_admins_by_guild(ctx.guild.id)
            if ctx.author.id in admins:
                rem_id = args[1].replace("<", "").replace(">", "").replace("@", "").replace("!", "")
                dataAccess.remove_admin_by_guild_and_id(ctx.guild.id, rem_id)
                embed = discord.Embed()
                embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.title = "Success"
                embed.description = "Admin <@{0}> removed.".format(rem_id)
                embed.colour = discord.Colour.dark_teal()
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed()
                embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.title = "Error"
                embed.description = "You are not an admin in this server"
                embed.colour = discord.Colour.red()
                await ctx.send(embed=embed)


@bot.command(name="tag")
async def tag(ctx, *, args=None):
    if not args:
        embed = discord.Embed()
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.title = "Error"
        embed.description = "You didn't supply a further command.\n" \
                            "You can try `>tag list` to see the tags you can view."
        embed.colour = discord.Colour.red()
        await ctx.send(embed=embed)
    else:
        args = args.split(" ")
        if args[0].lower() == "list":
            embed = discord.Embed()
            embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.title = "Tags in this server"
            embed.description = ""
            embed.set_footer(text="Access these by typing >tag <tag name>")
            tags = dataAccess.get_tags_by_guild(ctx.guild.id)
            for tag_name in tags:
                embed.description += "{0}\n".format(tag_name)
            await ctx.send("You found the list function", embed=embed)
        elif args[0].lower() == "add":
            name = args[1]
            response_text = " ".join(args[2:])
            admins = dataAccess.get_admins_by_guild(ctx.guild.id)
            if ctx.author.id in admins:
                dataAccess.add_tag(name, ctx.guild.id, response_text)
                embed = discord.Embed()
                embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.title = "Success"
                embed.description = "Tag **{0}** added!".format(name)
                embed.colour = discord.Colour.green()
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed()
                embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.title = "Error"
                embed.description = "You are not an admin in this server"
                embed.colour = discord.Colour.red()
                await ctx.send(embed=embed)
        elif args[0] == "remove":
            admins = dataAccess.get_admins_by_guild(ctx.guild.id)
            if ctx.author.id in admins:
                name = args[1]
                dataAccess.remove_tag_by_name_and_guild(name, ctx.guild.id)
                embed = discord.Embed()
                embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.title = "Success"
                embed.description = "Tag **{0}** removed.".format(name)
                embed.colour = discord.Colour.dark_teal()
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed()
                embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.title = "Error"
                embed.description = "You are not an admin in this server"
                embed.colour = discord.Colour.red()
                await ctx.send(embed=embed)
        elif args[0] == "edit":
            name = args[1]
            response_text = " ".join(args[2:])
            admins = dataAccess.get_admins_by_guild(ctx.guild.id)
            if ctx.author.id in admins:
                dataAccess.edit_tag_by_name_and_guild(name, ctx.guild.id, response_text)
                embed = discord.Embed()
                embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.title = "Success"
                embed.description = "Tag **{0}** edited!".format(name)
                embed.colour = discord.Colour.green()
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed()
                embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.title = "Error"
                embed.description = "You are not an admin in this server"
                embed.colour = discord.Colour.red()
                await ctx.send(embed=embed)
        else:
            name = args[0]
            response_text = dataAccess.get_tag_by_name_and_guild(name, str(ctx.guild.id))
            embed = discord.Embed()
            embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.title = "Tag: {0}".format(name)
            embed.description = response_text
            embed.set_footer(text=ctx.author.nick, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)


@bot.command(name="quickresponse", aliases=["qr"])
async def quickresponse(ctx, *, args=None):
    if not args:
        embed = discord.Embed()
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.title = "Error"
        embed.description = "You didn't supply a further command.\n" \
                            "You can try `>qr list`."
        embed.colour = discord.Colour.red()
        await ctx.send(embed=embed)
    else:
        args = args.split(" ")
        if args[0].lower() == "add":
            print()
        elif args[0] == "list":
            guild_triggers = dataAccess.get_triggers_and_ids_by_guild(ctx.guild.id)
            embed = discord.Embed()
            embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.title = "Triggers and IDs in this server"
            embed.description = ""
            embed.set_footer(text="Add/remove a trigger to the trigger list with the ID specified")
            for trigger_group in guild_triggers:
                embed.description += "`{0}`:\t{1}\n".format(trigger_group[0], trigger_group[1])
            await ctx.send(embed=embed)


@bot.event
async def on_message(ctx):
    if not ctx.author.bot:
        guild_triggers = dataAccess.get_triggers_by_guild(ctx.guild.id)
        for triggers in guild_triggers:
            for trigger in triggers:
                if trigger in ctx.content:
                    triggers_list = ", ".join(triggers)
                    response_text = dataAccess.get_response_by_guild_and_triggers(ctx.guild.id, triggers_list)
                    embed = discord.Embed()
                    embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
                    embed.title = "QuickResponse: {0}".format(trigger)
                    embed.description = response_text
                    embed.set_footer(text=ctx.author.nick, icon_url=ctx.author.avatar_url)
                    await ctx.reply(embed=embed)
    await bot.process_commands(ctx)


def kickstart():
    bot.run(constants.BOT_TOKEN)
