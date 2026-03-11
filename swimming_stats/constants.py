"""
This  module contains the constants  used  in this package.
"""

from enum import Enum

from openpyxl.styles import Font, Border, Side, Alignment


# Define font
BOLD = Font(bold=True)

# Define test alignment
CENTRE_ALIGNED = Alignment(horizontal="center", vertical="center")
LEFT_ALIGNED = Alignment(horizontal="left", vertical="center")
RIGHT_ALIGNED = Alignment(horizontal="right", vertical="center")

# Define the border
THIN_BORDER = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)

THICK_LEFT_BORDER = Border(
    left=Side(style="thick"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)
THICK_RIGHT_BORDER = Border(
    left=Side(style="thin"),
    right=Side(style="thick"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)
THICK_TOP_BORDER = Border(top=Side(style="thick"))

THICK_BOTTOM_BORDER = Border(bottom=Side(style="thick"))


class EventType(Enum):
    """
    An enum containing race names.
    """

    FC_RELAY = "4 X 50m FC Relay"
    MIXED_FC_RELAY = "Mixed 4 X 50m FC Relay"
    MEDLEY_RELAY = "4 X 50m Medley Relay"
    MIXED_MEDLEY_RELAY = "Mixed 4 X 50m Medley Relay"
    BACK_50 = "50m BK"
    BACK_100 = "100m BK"
    BACK_200 = "200m BK"
    BREAST_50 = "50m BR"
    BREAST_100 = "100m BR"
    BREAST_200 = "200m BR"
    FLY_50 = "50m Fly"
    FLY_100 = "100m Fly"
    FLY_200 = "200m Fly"
    FC_50 = "50m FC"
    FC_100 = "100m FC"
    FC_200 = "200m FC"
    FC_400 = "400m FC"
    FC_800 = "800m FC"
    FC_1500 = "1500m FC"
    IM_100 = "100m IM"
    IM_200 = "200m IM"
    IM_400 = "400m IM"
    SQUADRON = "Squadron"


class Gender(Enum):
    """
    An enum containing genders.
    """

    MALE = 0
    FEMALE = 1


EVENT_MAPPING = {
    "50m Freestyle": EventType.FC_50,
    "100m Freestyle": EventType.FC_100,
    "200m Freestyle": EventType.FC_200,
    "400m Freestyle": EventType.FC_400,
    "800m Freestyle": EventType.FC_800,
    "1500m Freestyle": EventType.FC_1500,
    "50m Backstroke": EventType.BACK_50,
    "100m Backstroke": EventType.BACK_100,
    "200m Backstroke": EventType.BACK_200,
    "50m Breaststroke": EventType.BREAST_50,
    "100m Breaststroke": EventType.BREAST_100,
    "200m Breaststroke": EventType.BREAST_200,
    "50m Butterfly": EventType.FLY_50,
    "100m Butterfly": EventType.FLY_100,
    "200m Butterfly": EventType.FLY_200,
    "100m Individual Medley": EventType.IM_100,
    "200m Individual Medley": EventType.IM_200,
    "400m Individual Medley": EventType.IM_400,
}


ARENA_LEAGUE_EVENTS = [
    EventType.FC_50,
    EventType.FC_100,
    EventType.BACK_50,
    EventType.BACK_100,
    EventType.BREAST_50,
    EventType.BREAST_100,
    EventType.FLY_50,
    EventType.FLY_100,
    EventType.IM_200,
]

COUNTY_EVENTS = [
    EventType.BACK_50,
    EventType.BREAST_50,
    EventType.FLY_50,
    EventType.FC_50,
]

JUNIOR_ARENA_LEAGUE_EVENTS = [
    EventType.FC_50,
    EventType.BACK_50,
    EventType.BREAST_50,
    EventType.FLY_50,
    EventType.IM_100,
]

MEDLEY_RELAY_50 = [
    EventType.BACK_50,
    EventType.BREAST_50,
    EventType.FLY_50,
    EventType.FC_50,
]

# The order determines the column order in the rankings sheet
RANKING_EVENTS = [
    EventType.FC_50,
    EventType.FC_200,
    EventType.BACK_50,
    EventType.BACK_200,
    EventType.BREAST_50,
    EventType.BREAST_200,
    EventType.FLY_50,
    EventType.FLY_200,
    EventType.IM_200,
    EventType.FC_400,
    EventType.IM_400,
    EventType.FC_100,
    EventType.FC_800,
    EventType.FC_1500,
    EventType.BACK_100,
    EventType.BREAST_100,
    EventType.FLY_100,
    EventType.IM_100,
]
