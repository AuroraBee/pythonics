import json
import pyautogui
import time
from TwitchWebsocket import TwitchWebsocket
from handler import *


# https://github.com/CubieDev/TwitchWebsocket

def presshold(key):
    start = time.time()
    set_given(num=key)
    pyautogui.keyDown(key)
    while time.time() - start < 1:
        pyautogui.press(key)
    pyautogui.keyUp(key)


class Settings:
    def __init__(self, bot):
        try:
            # Try to load the file using json.
            # And pass the data to the MyBot class instance if this succeeds.
            with open("settings.txt", "r") as f:
                settings = f.read()
                data = json.loads(settings)
                bot.set_settings(data['Host'],
                                 data['Port'],
                                 data['Channel'],
                                 data['Nickname'],
                                 data['Authentication'])
        except ValueError:
            raise ValueError("Error in settings file.")
        except FileNotFoundError:
            # If the file is missing, create a standardised settings.txt file
            # With all parameters required.
            with open('settings.txt', 'w') as f:
                standard_dict = {
                    "Host": "irc.chat.twitch.tv",
                    "Port": 6667,
                    "Channel": "#<channel>",
                    "Nickname": "<name>",
                    "Authentication": "oauth:<auth>"
                }
                f.write(json.dumps(standard_dict, indent=4, separators=(',', ': ')))
                raise ValueError("Please fix your settings.txt file that was just generated.")


class MyBot:
    def __init__(self):
        self.host = None
        self.port = None
        self.chan = None
        self.nick = None
        self.auth = None

        # Fill previously initialised variables with data from the settings.txt file
        Settings(self)

        self.ws = TwitchWebsocket(host=self.host,
                                  port=self.port,
                                  chan=self.chan,
                                  nick=self.nick,
                                  auth=self.auth,
                                  callback=self.message_handler,
                                  capability=["membership", "tags", "commands"],
                                  live=False)
        self.ws.start_blocking()

    def set_settings(self, host, port, chan, nick, auth):
        self.host = host
        self.port = port
        self.chan = chan
        self.nick = nick
        self.auth = auth

    def message_handler(self, m):
        if m.type == "PRIVMSG":
            pass
        msg = m.message
        print(m.user, ":", msg)
        if msg == "1" or msg == "!place 1":
            presshold("1")
        if msg == "2" or msg == "!place 2":
            presshold("2")
        if msg == "3" or msg == "!place 3":
            presshold("3")
        if msg == "4" or msg == "!place 4":
            presshold("4")
        if msg == "5" or msg == "!place 5":
            presshold("5")
        if msg == "6" or msg == "!place 6":
            presshold("6")
        if msg == "7" or msg == "!place 7":
            presshold("7")
        if msg == "8" or msg == "!place 8":
            presshold("8")
        if msg == "9" or msg == "!place 9":
            presshold("9")


if __name__ == "__main__":
    MyBot()
