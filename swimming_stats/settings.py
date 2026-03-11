"""
This module provides default settings, if necessary they should be overwritten in local_settings.py
"""

from os import path

from swimming_stats.fills import (
    FILL_1,
    FILL_2,
    FILL_3,
    FILL_4,
    FILL_5,
    FILL_6,
    FILL_7,
    FILL_8,
    FILL_9,
    FILL_10,
    FILL_11,
    FILL_12,
    FILL_13,
    FILL_EMPTY,
)


try:
    from swimming_stats.local_settings import BASE_DIRECTORY
except ImportError:
    BASE_DIRECTORY = "/"

MEMBERS_FILE = path.join(BASE_DIRECTORY, "members.xlsx")
MEMBERS_TIMES_FILE = path.join(BASE_DIRECTORY, "member_times.xlsx")
TT_FILE = path.join(BASE_DIRECTORY, "time_trial.xlsx")
FILE_OUT = path.join(BASE_DIRECTORY, "pbs.xlsx")
ARENA_FILE = path.join(BASE_DIRECTORY, "arena.xlsx")
ARENA_JUNIOR_FILE = path.join(BASE_DIRECTORY, "arena_junior.xlsx")
COUNTY_FILE = path.join(BASE_DIRECTORY, "counties.xlsx")

SWIM_MEMBERSHIPS = ["Club Compete", "Club Train"]


DATE_TITLE_COLUMN = "X"
DATE_COLUMNS = "YZ"

# Set these values in local_settings.py

RANKING_SQUAD_1 = "S1"
RANKING_SQUAD_2 = "S2"
RANKING_SQUAD_3 = "S3"
RANKING_SQUAD_4 = "S4"
RANKING_SQUAD_5 = "S5"

# The names must match those in swim manager
# The abbreviations can be anything
SQUAD_NAMES = {
    "SQUAD 1": RANKING_SQUAD_1,
    "SQUAD 2": RANKING_SQUAD_2,
    "SQUAD 3": RANKING_SQUAD_3,
    "SQUAD 4": RANKING_SQUAD_4,
    "SQUAD 5": RANKING_SQUAD_5,
    "SQUAD 6": "S6",
    "SQUAD 7": "S7",
    "SQUAD 8": "S8",
    "SQUAD 9": "S9",
    "SQUAD 10": "S10",
    "SQUAD 11": "S11",
    "SQUAD 12": "S12",
    "SQUAD 13": "S13",
    "SQUAD 14": "S14",
}

# Arena League
ARENA_LEAGUE_AGE_AT_DATE = None
ARENA_IGNORE_MEMBERS = []
ARENA_IGNORE_SQUADS = []

RANKING_IGNORE_MEMBERS = []
RANKING_IGNORE_SQUADS = []

# date for counties ages
COUNTY_AGE_AT_DATE = None
COUNTY_IGNORE_MEMBERS = []
COUNTY_IGNORE_SQUADS = []

ALWAYS_INCLUDE = []

try:
    from swimming_stats.local_settings import *
except ImportError:
    pass


FILLS = [
    FILL_1,
    FILL_2,
    FILL_3,
    FILL_4,
    FILL_5,
    FILL_6,
    FILL_7,
    FILL_8,
    FILL_9,
    FILL_10,
    FILL_11,
    FILL_12,
    FILL_13,
    FILL_EMPTY,
]

# Squad names, the order is important
# The names must match those used in `SQUAD_NAMES`
SQUAD_FILLS = {}

for i, name in enumerate(SQUAD_NAMES.keys()):
    try:
        SQUAD_FILLS[name] = FILLS[i]
    except IndexError:
        break
