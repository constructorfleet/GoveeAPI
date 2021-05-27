import argparse

from constants import *
from controller import *

"""
    To parse device option passed to command line, enter in device names (bed, window, shelf, etc)
    followed by an list consisting of their address. If you have a 'scene' like a bedroom consisting
    of multiple devices, enter them all into the list.
    Include 'all' as a list of all of your device addresses as well.
"""

ps = argparse.ArgumentParser(description="Govee Home Control Script")

device_choices = device_names.append("all")
ps.add_argument('--device', default="all", type=str, choices=addr_dev_dict.values())
ps.add_argument('--brightness', type=int)
ps.add_argument('--color', nargs=3, type=int)
args = ps.parse_args()
chosen_devices = devices[args.device]

if args.brightness is not None:
    bright = args.brightness
    for device in chosen_devices:
        change_brightness(bright, device)
if args.color is not None:
    colort = tuple(args.color)
    for device in chosen_devices:
        change_color(colort, device)
