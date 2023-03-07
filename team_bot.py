import os
from webex_bot.commands.echo import EchoCommand
from webex_bot.commands.help import HelpCommand
from webex_bot.webex_bot import WebexBot
import logging
from webex_bot.models.command import Command
from challenge1.command import hello


log = logging.getLogger(__name__)


class JamCommand(Command):

    def __init__(self, keyword, help_msg, exec_fn):
        super().__init__(
            command_keyword=keyword,
            help_message=help_msg
        )
        self.keyword = keyword
        self.help_msg = help_msg
        self.exec_fn = exec_fn

    def execute(self, message, attachment_actions, activity):
        """
        :param message: message with command already stripped
        :param attachment_actions: attachment_actions object
        :param activity: activity object

        :return: a string or Response object (or a list of either). Use Response if you want to return another card.
        """

        # If the message came in a space (rather than 1:1), we need to strip out the command.
        cmd_str = f'Jam {self.keyword}'
        if message.startswith(cmd_str):
            message = message[len(cmd_str):]
        # trim whitespace
        message = message.strip()

        return self.exec_fn(message)


my_bot_botName="PingChillingBot"

# Create a Bot Object
bot = WebexBot(teams_bot_token=os.getenv("WEBEX_TEAMS_ACCESS_TOKEN"),
               approved_rooms=[],
               bot_name=my_bot_botName,
               include_demo_commands=False,
               approved_users=[])

# Add new commands for the bot to listen out for.
# Round 1
bot.add_command(JamCommand('hello', 'Hello, Cisco!', hello))


bot.run()
