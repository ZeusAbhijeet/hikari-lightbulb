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
from __future__ import annotations

__all__ = [
    "LightbulbError",
    "CommandNotFound",
    "CommandInvocationError",
    "CommandIsOnCooldown",
    "ConverterFailure",
    "NotEnoughArguments",
    "CheckFailure",
    "NotOwner",
    "OnlyInGuild",
    "OnlyInDM",
    "BotOnly",
    "WebhookOnly",
    "HumanOnly",
    "NSFWChannelOnly",
]

import typing as t

if t.TYPE_CHECKING:
    from lightbulb_v2 import commands


class LightbulbError(Exception):
    """
    Base lightbulb exception class. All errors raised by lightbulb will be a subclass
    of this exception.
    """

    pass


class CommandAlreadyExists(LightbulbError):
    """
    Error raised when attempting to add a command to the bot but a name or alias
    for the command conflicts with a command that already exists.
    """

    pass


class CommandNotFound(LightbulbError):
    """
    Error raised when a command is attempted to be invoked but an implementation
    is not found. This will only be raised for prefix commands.
    """

    def __init__(self, *args: t.Any, invoked_with: str) -> None:
        super().__init__(*args)
        self.invoked_with: str = invoked_with
        """The name or alias of the command that was used."""


class CommandInvocationError(LightbulbError):
    """
    Error raised when an error is encountered during command invocation. This
    wraps the original exception that caused it, which is accessible through
    ``CommandInvocationError.__cause__`` or ``CommandInvocationError.original``.
    """

    def __init__(self, *args: t.Any, original: Exception) -> None:
        super().__init__(*args)
        self.original = original
        """The exception that caused this to be raised. Also accessible through ``CommandInvocationError.__cause__``"""
        self.__cause__ = original


class CommandIsOnCooldown(LightbulbError):
    """
    Error raised when a command was on cooldown when it was attempted to be invoked.
    """

    def __init__(self, *args: t.Any, retry_after: float) -> None:
        super().__init__(*args)
        self.retry_after: float = retry_after
        """The amount of time in seconds remaining until the cooldown expires."""


class ConverterFailure(LightbulbError):
    """
    Error raised when option type conversion fails while prefix command arguments are being parsed.
    """

    def __init__(self, *args: t.Any, opt: commands.base.OptionLike) -> None:
        super().__init__(*args)
        self.option: commands.base.OptionLike = opt
        """The option that could not be converted."""


class NotEnoughArguments(LightbulbError):
    """
    Error raised when a prefix command expects more options than could be parsed from the user's input.
    """

    def __init__(self, *args: t.Any, missing: t.Sequence[commands.base.OptionLike]) -> None:
        super().__init__(*args)
        self.missing_options: t.Sequence[commands.base.OptionLike] = missing
        """The missing options from the command invocation."""


class CheckFailure(LightbulbError):
    """
    Error raised when a check fails before command invocation. If another error caused this
    to be raised then you can access it using ``CheckFailure.__cause__``.
    """


class NotOwner(CheckFailure):
    """
    Error raised when a user who is not the owner of the bot attempts to use a command
    that is restricted to owners only.
    """


class OnlyInGuild(CheckFailure):
    """
    Error raised when a user attempts to use a command in DMs that has been restricted
    to being used only in guilds.
    """


class OnlyInDM(CheckFailure):
    """
    Error raised when a user attempts to use a command in a guild that has been restricted
    to being used only in DMs.
    """


class BotOnly(CheckFailure):
    """
    Error raised when any entity other than a bot attempts to use a command that has been
    restricted to being used only by bots.
    """


class WebhookOnly(CheckFailure):
    """
    Error raised when any entity other than a webhook attempts to use a command that has been
    restricted to being used only by webhooks.
    """


class HumanOnly(CheckFailure):
    """
    Error raised when any entity other than a human attempts to use a command that has been
    restricted to being used only by humans.
    """


class NSFWChannelOnly(CheckFailure):
    """
    Error raised when a user attempts to use a command in a non-NSFW channel that has
    been restricted to only being used in NSFW channels.
    """
