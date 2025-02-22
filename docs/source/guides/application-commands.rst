====================
Application Commands
====================

**What are application commands?**

In the words of discord:

"Application commands are commands that an application (bot) can register to Discord. They provide users a
first-class way of interacting directly with your application that feels deeply integrated into Discord."

Examples of application commands include:

- `Slash commands <https://discord.com/developers/docs/interactions/application-commands#slash-commands>`_

- `Message context menu commands (message commands) <https://discord.com/developers/docs/interactions/application-commands#message-commands>`_

- `User context menu commands (user commands) <https://discord.com/developers/docs/interactions/application-commands#user-commands>`_

**Important Information:**

As Discord has decided to ban bots from reading messages without the intent enabled, you should be using application commands wherever possible.

You should at least have a basic understanding of:

- interaction

- `global <https://discord.com/developers/docs/interactions/application-commands#making-a-global-command>`_ and
  `guild <https://discord.com/developers/docs/interactions/application-commands#making-a-guild-command>`_ commands

- the ``application.commands`` `OAuth scope <https://discord.com/developers/docs/interactions/application-commands#authorizing-your-application>`_

For an example slash command, see the `examples directory <https://github.com/tandemdude/hikari-lightbulb/tree/v2/examples>`_

.. warning::
    Note that by default, application commands will be **global** unless you specify a set of guilds that they should
    be created in using ``BotApp.default_enabled_guilds`` or by passing a set of guilds into the ``@lightbulb.command``
    decorator. Global commands **will** take up to one hour to sync to discord, so it is reccommended that you use
    guild-specific commands during development and testing.

----

Creating a Basic Slash Command
==============================

Slash commands (and other application command types) are implemented exactly the same way as prefix commands. You just
replace the ``commands.PrefixCommand`` with ``commands.SlashCommand`` in the ``@lightbulb.implements`` decorator.

See Below
::

    import lightbulb
    from lightbulb import commands

    bot = lightbulb.BotApp(...)

    @bot.command
    @lightbulb.command("ping", "checks that the bot is alive")
    @lightbulb.implements(commands.SlashCommand)
    async def ping(ctx):
        await ctx.reply("Pong!")

    bot.run()


Adding options to slash commands is also identical to how you add options to prefix commands
::

    import lightbulb
    from lightbulb import commands

    bot = lightbulb.BotApp(...)

    @bot.command
    @lightbulb.option("text", "text to repeat")
    @lightbulb.command("echo", "repeats the given text")
    @lightbulb.implements(commands.SlashCommand)
    async def echo(ctx):
        await ctx.reply(ctx.options.text)

    bot.run()


To create message or user commands you need to add ``commands.MessageCommand`` and ``commands.UserCommand`` respectively
to the ``@lightbulb.implements`` decorator. You should note that message and user commands cannot take any options.

.. error::
    Message and user commands are not currently supported by hikari so will **always** raise an error if you
    try to create either currently.
