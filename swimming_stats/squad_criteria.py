"""
This module provides the times required for each squad.

The order of the timings is:
    50m FC
    200m FC
    50m BK
    200m BK
    50m BR
    200m BR
    50m Fly
    200m Fly
    400m FC
    400m IM
"""

from swimming_stats.settings import (
    RANKING_SQUAD_1,
    RANKING_SQUAD_2,
    RANKING_SQUAD_3,
    RANKING_SQUAD_4,
    RANKING_SQUAD_5,
)

squad_criteria = {
    RANKING_SQUAD_1: [
        (0, 32),
        (2, 30),
        (0, 37),
        (2, 50),
        (0, 42),
        (3, 10),
        (0, 35),
        (3, 0),
        (2, 50),
        (5, 20),
        (6, 0),
    ],
    RANKING_SQUAD_2: [
        (0, 35),
        (2, 40),
        (0, 40),
        (3, 0),
        (0, 43),
        (3, 30),
        (0, 38),
        (3, 20),
        (3, 10),
    ],
    RANKING_SQUAD_3: [
        (0, 40),
        (3, 0),
        (0, 45),
        (3, 20),
        (0, 50),
        (3, 40),
        (0, 45),
        (3, 30),
        (3, 30),
    ],
    RANKING_SQUAD_4: [
        (0, 42),
        (3, 25),
        (0, 50),
        (3, 40),
        (0, 55),
        (4, 10),
        (0, 48),
        (4, 10),
        (4, 0),
    ],
    RANKING_SQUAD_5: [
        (0, 45),
        (4, 0),
        (0, 55),
        (4, 10),
        (1, 0),
        (5, 0),
        (1, 0),
        (4, 50),
        (4, 20),
    ],
}
