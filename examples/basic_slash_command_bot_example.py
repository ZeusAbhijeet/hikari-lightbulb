# -*- coding: utf-8 -*-
# Copyright © tandemdude 2020-present
#
# This file is part of Lightbulb.
#
# Lightbulb is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Lightbulb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Lightbulb. If not, see <https://www.gnu.org/licenses/>.
import lightbulb
from lightbulb import commands

bot = lightbulb.BotApp(prefix="!", token="YOUR_TOKEN")


@bot.command()
@lightbulb.command("ping", "Checks that the bot is alive")
@lightbulb.implements(commands.SlashCommand)
async def ping(ctx):
    """Checks that the bot is alive"""
    await ctx.respond("Pong!")


@bot.command()
@lightbulb.option("text", "Text to repeat")
@lightbulb.command("echo", "Repeats the user's input")
@lightbulb.implements(commands.SlashCommand)
async def echo(ctx):
    await ctx.respond(ctx.options.text)


bot.run()
