import random
from tkinter import *
import time
from colorama import Fore
import keyboard
rollcount = 0

weather = ['Windy', 'Snowy', 'Rainy', 'Starfall', 'Null', 'Glitched']
random.choices(weather, weights=(0.2, 0.133, 0.133, 0.0166, 0.0075, 0.00333), k=1)

stat_list = ['Common (1 in 2)', 'Bleeding (1 in 4,444) ', 'Uncommon (1 in 4)', 'Good (1 in 5)', 'Natural (1 in 8)', 'Rare (1 in 16)', 'Divinus (1 in 32)', 'Diaboli (1 in 1,004)' , 'Crystallized (1 in 64)', 'Rage (1 in 128',
    'Rage: Heated (1 in 12,800)', 'Glacier (1 in 256)', 'Permafrost (1 in 24,500)', 'Wind (1 in 300)', 'Ruby (1 in 350)', 'Gilded (1 in 512)', 'Jackpot (1 in 777)', 'Precious (1 in 1,024)', 'Magnetic (1 in 2,048)', 'Sidereum (1 in 4,096)',
    ':Flushed: (1 in 6,900)', ':Flushed: Lobotomy (1 in 69,000)', 'Undead (1 in 10,000)', 'Stormal (1 in 30,000)', 'Aquatic (1 in 40,000)', 'Nautilus (1 in 70,000)', 'Exotic (1 in 99,999)', 'Comet (1 in 12,000)', 'Lunar (1 in 5,000)', 'Solar (1 in 5,000)', 'Undefined (1 in 1,111)',
    'Undead: Devil (1 in 100,000)', 'Diaboli: Void (1 in 100,400)', 'Bounded (1 in 200,000)', 'Celestial (1 in 350,000)', 'Galaxy (1 in 500,000)', 'Lunar: Full Moon (1 in 500,00)', 'Twilight (1 in 600,000)', 'Arcane (1 in 1,000,000)', 'Starscourge (1 in 1,000,000)',
    'Gravitational (1 in 2,000,000)', 'Virtual (1 in 2,500,000)', 'Sailor (1 in 3,000,000)', 'Poseidon (1 in 3,800,000)', 'Aquatic: Flame (1 in 4,000,000)', 'Hades (1 in 6,666,666)', 'Hyper-volt (1 in 7,500,000)', 'Glitch (1 in 12,210,110)', 'Arcane: Legacy (1 in 15,000,000)', 'Chromatic (1 in 20,000,000)',
    'Arcane: Dark (1 in 30,000,000)', 'Exotic: APEX (1 in 49,999,500)', 'Matrix (1 in 50,000,000)', 'Chromatic: Exotic (1 in 99,999,999)', 'Abyssal Hunter (1 in 100,000,000)', 'Impeached (1 in 200,000,000)', 'Archangel (1 in 250,000,000)']

weight = [50, 0.02250225, 25, 20, 12.5, 6.25, 3.125, 0.0996016, 1.5625, 0.78125,
        0.0078125, 0.390625, 0.00408163, 0.333333, 0.285714, 0.1953125, 0.1287, 0.0976563, 0.0488281, 0.02441406, 0.01449275,
        0.001449275, 0.01, 0.00333333, 0.0025, 0.001428571, 0.00100001, 0.00833333, 0.02, 0.02, 0.090009, 0.001, 0.00996016,
        0.0005, 0.000285714, 0.0002, 0.0002, 0.0001666667, 0.0001, 0.0001, 0.00005, 0.00004, 0.0000333333, 0.0000263158,
        0.000025, 0.000015, 0.00001333333, 0.00000818993, 0.00000666667, 0.000005, 0.00000333333, 0.00000200002, 0.000002,
        0.000001, 0.0000001, 0.0000005, 0.0000004]

while True:
    if keyboard.read_key() == "r":
        stat_chances = random.choices(stat_list, weights=weight, k=1)[0]
        stat_chance_float = weight[stat_list.index(stat_chances)]
        rollcount = rollcount + 1
        if 0.01 < stat_chance_float < 0.1:
            print(Fore.GREEN + stat_chances)
            print("You just got " + stat_chances + " " + 'Rolls: ' + str(rollcount))
        elif 0.00143 < stat_chance_float < 0.009 and stat_chance_float <= 0.009:
            print(Fore.YELLOW + stat_chances + " " + 'Rolls: ' + str(rollcount))
            print("You just got " + stat_chances + " " + 'Rolls: ' + str(rollcount))
        elif 0.0001 < stat_chance_float < 0.00143 and stat_chance_float <= 0.00143:
            print(Fore.LIGHTRED_EX + stat_chances + " " + 'Rolls: ' + str(rollcount))
            print("You just got " + stat_chances + " " + 'Rolls: ' + str(rollcount))
        elif 0.000001 < stat_chance_float < 0.0099 and stat_chance_float <= 0.0001:
            print(Fore.BLUE + stat_chances)
            print("You just got " + stat_chances + " " + 'Rolls: ' + str(rollcount))
        elif stat_chance_float <= 0.0000999:
            print(Fore.MAGENTA + stat_chances)
            print("You just got " + stat_chances + " " + 'Rolls: ' + str(rollcount))
        else:
            print(Fore.RESET + stat_chances + " " + 'Rolls: ' + str(rollcount))