# Importing the functions that scan for torrents
from torrents import *
import configparser
import argparse
import colorama
import os
from colorama import Fore, Back, Style
from config import *

try:
    config = configparser.ConfigParser()
    config.read('config.ini')
except Exception:
    pass


def checkConfig():
    # Check if config.ini exists
    if not os.path.isfile('config.ini'):
        return False
    else:
        return True


def createConfig(player: str = 'vlc', provider: str = '1337x'):
    if not config.sections():
        config['DEFAULT'] = {'player': player, 'provider': provider}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)


def buildConfig():
    isAdvanced = None
    while isAdvanced is None:
        buildmode = input(
            'Do you have experience with Torrents and piracy in general? If no, the program will be set to ask simpler questions. (Y/n) ')
        if buildmode == 'Y' or buildmode == 'y':
            isAdvanced = True
        elif buildmode == 'N' or buildmode == 'n':
            isAdvanced = False
        elif buildmode == "":
            isAdvanced = True
        else:
            print(Fore.RED + 'Invalid input. Please try again.' + Style.RESET_ALL)

    if isAdvanced:
        #search_mode = input('Do you want the program to create search queries for you? The program will ask you about '
        #                    'the name of the thing you want to watch, season, episode and stuff like that and create '
        #                    'a query for you. (y/n) ')
        #what_to_watch = input("Do you watch TV shows, anime or both? (TV/anime/both) ")
        trackers = []
        while not trackers:
            trackers_to_use = input('Enter the trackers you want to use (separated by commas, l for list. Default: 1337x): ')
            if trackers_to_use == 'l':
                print('Available trackers: 1337x, nyaa.si, thepiratebay')
                continue
            elif trackers_to_use == '':
                trackers = ['1337x']
            else:
                trackers = trackers_to_use.split(',')

            if set(trackers).issubset(set(available_trackers)):
                print(Fore.GREEN + 'Trackers accepted' + Style.RESET_ALL)
            else:
                print(Fore.RED + 'Invalid trackers. Please try again.' + Style.RESET_ALL)
                trackers = []

if __name__ == "__main__":
    print(Fore.MAGENTA + "Welcome to EmiStream, a basic torrent searcher that is " + Fore.GREEN + "Free as in Freedom!")
    print(Fore.RED + "Fuck netflix and DRM.")

    if not checkConfig():
        print(Fore.CYAN + "Looks like you don't have a config file. Let's create one that suits you the best!")
        print(Fore.RED + "REMEMBER: Piracy is a crime in many western countries. Before using this program, make sure "
                         "to do research about your country's laws and take cautions like a VPN if needed." + Fore.RESET)
        print("Please answer these questions so the program can create a config file for you.")
        buildConfig()
