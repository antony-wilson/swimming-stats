"""
This package provides a number of data classes.

Classes:
    AgeGroup: A group of Swimmers that fall within the age group.
    Event: An Event has a description along with a Swimmer or Team of Swimmers taken from an
        AgeGroup.
    Gala: A gala is a container for Event objects.
    PBs: A dict of PBs.
    Rankings: A dict of Rankings
    Squad: The Squad object contains information about the Squad and swimmers in it.
    SquadronEvent: A specialisation of the Event class
    Swimmer: The Swimmer object contains information about a swimmer.
    Squad: The Squad object contains information about the Squad and swimmers in it.
"""

import datetime

from swimming_stats.constants import EventType, Gender, EVENT_MAPPING
from swimming_stats.team_selection import (
    get_fastest_swimmer,
    get_fc_relay_team,
    get_mixed_fc_relay_team,
    get_medley_relay_team,
    get_mixed_medley_relay_team,
    Squadron,
    Team,
)


class AgeGroup:
    """
    A group of Swimmers that fall within the age group.

    Methods:
        get_swimmers get the list of age group Swimmers, optionally filtering on Gender

    Properties:
        age_group (str) a representation of the age group
        female_swimmers (list(Swimmer) a list of female swimmers in the age group
        male_swimmers (list(Swimmer) a list of open/male swimmers in the age group
        swimmers (list(Swimmer) a list of swimmers in the age group
    """

    def __init__(self, age_min, age_max, swimmers):
        """
        Create an AgeGroup object.

        @param age_min (int)
        @param age_max(int)
        @param swimmers (list(Swimmer))
        """
        self._age_min = age_min
        self._age_max = age_max
        self._swimmers = self._get_swimmers(age_min, age_max, swimmers)

    def __str__(self):
        return f"AgeGroup: {self.age_group}, containing {len(self._swimmers)} swimmers"

    def get_swimmers(self, gender=None):
        """
        Get the list of age group Swimmers, optionally filtering on Gender.

        @param gender(Gender) the Gender to filter on

        @return a list of Swimmers
        """
        if gender is None:
            # return all swimmers in  the age group
            return self._swimmers

        if gender is Gender.MALE:
            return self.male_swimmers

        return self.female_swimmers

    @property
    def age_group(self):
        """
        Get a str representation of the age group.
        """
        if self._age_min == self._age_max:
            return self._age_max
        return f"{self._age_min}-{self._age_max}"

    @property
    def female_swimmers(self):
        """A list of female swimmers in the age group."""
        swimmers = []
        for swimmer in self._swimmers:
            if swimmer.gender == Gender.FEMALE:
                swimmers.append(swimmer)
        return swimmers

    @property
    def male_swimmers(self):
        """A list of open/male swimmers in the age group."""
        swimmers = []
        for swimmer in self._swimmers:
            if swimmer.gender == Gender.MALE:
                swimmers.append(swimmer)
        return swimmers

    @property
    def swimmers(self):
        """A list of swimmers in the age group."""
        return self.swimmers

    def _get_swimmers(self, age_min, age_max, swimmers):
        """
        Get the swimmers whose age is between the given min and max.
        """
        age_group_swimmers = []
        for swimmer in swimmers:
            if swimmer.age < age_min or swimmer.age > age_max:
                continue
            age_group_swimmers.append(swimmer)
        return age_group_swimmers


class Event:
    """
    An Event has a description along with a Swimmer or Team of Swimmers.

    Properties:
        description (str) a description of the event
        relay (boolean) True if the event is a relay
        swimmer (Swimmer) only set if it is not a relay
        team (Team) the swimmers in a relay
    """

    def __init__(self, description, group, event_type, gender=None):
        self._description = description
        swimmers = group.get_swimmers(gender)
        self._team = self._get_team(event_type, swimmers, gender)

    def __str__(self):
        if self.relay:
            return f"Event: {self.description}\n{self.team}"

        return f"Event: {self.description}\n{self.swimmer.full_name}"

    def _get_team(self, event_type, swimmers, gender):

        if event_type == EventType.FC_RELAY:
            return get_fc_relay_team(swimmers, gender)

        if event_type == EventType.MIXED_FC_RELAY:
            return get_mixed_fc_relay_team(swimmers)

        if event_type == EventType.MEDLEY_RELAY:
            return get_medley_relay_team(swimmers, gender)

        if event_type == EventType.MIXED_MEDLEY_RELAY:
            return get_mixed_medley_relay_team(swimmers)

        # must be an individual event
        return get_fastest_swimmer(swimmers, event_type)

    @property
    def description(self):
        """The description of the Event."""
        return self._description

    @property
    def relay(self):
        """The relay flag, True if the Event is a relay."""
        if "RELAY" in self._description.upper():
            return True
        return False

    @property
    def swimmer(self):
        """
        The Swimmer for this Event.

        The swimmer is only available if the Event is an individual event.
        """
        if isinstance(self._team, Team):
            raise Exception
        return self._team

    @property
    def team(self):
        """The Team of Swimmers for this Event."""
        return self._team


class Gala:
    """
    The Gala has a number of Events.

    Properties:
        age_groups(list(AgeGroup)) a list of age groups
        events (dict) key=event number, value=event
    """

    def __init__(self, event_list, swimmers):
        self._events = {}
        swimmers_age_groups = {}
        squadron = False

        for (
            event_no,
            description,
            age_min,
            age_max,
            event_type,
            gender,
        ) in event_list:
            if event_type == EventType.SQUADRON:
                squadron = (event_no, gender)
                continue
            if swimmers_age_groups.get(f"{age_min}_{age_max}") is not None:
                swimmers_age_group = swimmers_age_groups.get(f"{age_min}_{age_max}")
            else:
                swimmers_age_group = AgeGroup(age_min, age_max, swimmers)
                swimmers_age_groups[f"{age_min}_{age_max}"] = swimmers_age_group

            self._events[event_no] = Event(
                description, swimmers_age_group, event_type, gender
            )

        if squadron is not False:
            self._events[squadron[0]] = self._get_squadron_event(squadron[1])

        self._age_groups = swimmers_age_groups.values()

    def __str__(self):
        output = "Gala:\n"
        for event_no, event in self._events.items():
            output = f"{output}{event_no} {event}\n\n"

        return output

    def _get_squadron_event(self, event_nums):
        squadron = Squadron()
        for num in event_nums:
            squadron.add(self._events[num].swimmer)

        return SquadronEvent(EventType.SQUADRON.value, squadron)

    @property
    def age_groups(self):
        """A list of age groups."""
        return self._age_groups

    @property
    def events(self):
        """
        A  dict of events.

        key=event number, value=event
        """
        return self._events


class PBs(dict):
    """
    A dict of PBs.

    key = event
    value = PB
    """

    def __str__(self):
        output = ""
        for key, value in self.items():
            if value is None:
                continue
            output = f"{output}{key}: {get_delta(value)}\n"
        return output


class Rankings(dict):
    """
    A dict of Rankings.

    key = event
    value = ranking
    """

    def __str__(self):
        output = ""
        for key, value in self.items():
            if value is None:
                continue
            output = f"{output}{key}: {value}\n"
        return output


class SquadronEvent(Event):
    """
    A specialisation of the Event class.

    Properties:
        relay (boolean) the relay flag, True if the Event is a relay
    """

    def __init__(self, description, team):
        self._description = description
        self._team = team

    @property
    def relay(self):
        """The relay flag, True if the Event is a relay."""
        return True


class Swimmer:
    """
    The Swimmer object contains information about a swimmer.

    Methods:
        add_pb if the time is faster than the recorded time then add it to the PBs
        add_ranking add a ranking for the swimmer

    Properties:
        first_name (str) the first name of the swimmer
        last_name (str) the last name of the swimmer
        full_name (str) the full name of the swimmer
        age () the age of the swimmer
        dob (datetime) the dob of the swimmer
        gender (Gender) the gender of the swimmer
        memb_no (str) the membership number of the swimmer
        squad (str) the squad the swimmer is in
        pbs (PBs) a PBs object containing event names and times
        rankings (Rankings) a ranking object  containing event names and rankings
    """

    def __init__(self, first_name, last_name, age, dob, gender, memb_no, squad):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._dob = dob
        self._gender = gender
        self._memb_no = memb_no
        self._squad = squad
        self._pbs = PBs()
        self._rankings = Rankings()

    def __str__(self):
        output = f"""Swimmer: {self._first_name} {self._last_name}
        age at date: {self._age}
        dob: {self._dob}
        gender: {self._gender}
        membership number: {self._memb_no}
        squad:{self._squad}
        pbs:\n"""
        for event, pb in self._pbs.items():
            output = f"{output}                {event}: {pb}\n"

        if len(self._rankings) > 0:
            output = f"{output}        rankings:\n" ""
            for event, ranking in self._rankings.items():
                output = f"{output}                {event}: {ranking}\n"

        return output

    def add_pb(self, event, event_time):
        """
        If the time is faster than the recorded time then add it to the PBs.

        @param event (str): the name of the event
        @param event_time (datetime.time): the time taken to do the event
        """
        if event_time is None:
            return
        event = EVENT_MAPPING[event]
        _event_time = self._pbs.get(event)
        if _event_time is None:
            self._pbs[event] = event_time
            return
        if _event_time > event_time:
            self._pbs[event] = event_time

    def add_ranking(self, event, ranking):
        """
        Add a ranking for the swimmer.

        @param event
        @paran ranking
        """
        self._rankings[event] = ranking

    @property
    def first_name(self):
        """The first name of the swimmer."""
        return self._first_name

    @property
    def last_name(self):
        """The last name of the swimmer."""
        return self._last_name

    @property
    def full_name(self):
        """The full name of the swimmer."""
        return f"{self.first_name} {self._last_name}"

    @property
    def age(self):
        """The age of the swimmer."""
        return self._age

    @property
    def dob(self):
        """The dob of the swimmer."""
        return self._dob

    @property
    def gender(self):
        """The gender of the swimmer."""
        return self._gender

    @property
    def memb_no(self):
        """The membership number of the swimmer."""
        return self._memb_no

    @property
    def squad(self):
        """The squad the swimmer is in."""
        return self._squad

    @property
    def pbs(self):
        """
        A PBs object containing event names and times.
        """
        return self._pbs

    @property
    def rankings(self):
        """A Rankings object containing event names and rankings."""
        return self._rankings


class Squad:
    """
    The Squad object contains information about the Squad and swimmers in it.

    Methods:
        add_swimmer (Swimmer) Add a swimmer to the squad.

    Properties:
        name (str) the name of the Squad
        swimmers (Swimmer) a list of swimmers in the Squad
    """

    def __init__(self, name):
        self._name = name
        self._swimmers = []

    def __str__(self):
        output = f"Squad:{self._name}\n"
        for swimmer in self._swimmers:
            output = f"{output}{swimmer}\n"

        return output

    def add_swimmer(self, swimmer):
        """
        Add a swimmer to the squad.

        @param swimmer (Swimmer): a swimmer to add to the squad
        """
        self._swimmers.append(swimmer)

    @property
    def name(self):
        """The name of the squad."""
        return self._name

    @property
    def swimmers(self):
        """A list of swimmers in the squad."""
        return self._swimmers


def get_delta(swim_time):
    """Get the time as 00:00.0000."""
    return datetime.timedelta(
        minutes=swim_time.minute,
        seconds=swim_time.second,
        microseconds=swim_time.microsecond,
    )
