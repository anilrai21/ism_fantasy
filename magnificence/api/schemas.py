from typing import Optional

from ninja import Schema


class ElementTypeSchema(Schema):
    singular_name: str
    singular_name_short: str


class TeamSchema(Schema):
    code: int
    name: str
    short_name: str


class ElementSchema(Schema):
    element_type: ElementTypeSchema
    first_name: str
    second_name: str
    team: TeamSchema
    goals_scored: int
    assists: int
    goals_conceded: int
    penalties_saved: int
    penalties_missed: int
    saves: int
    web_name: str
    total_points: int
    chance_of_playing_this_round: Optional[int]
    chance_of_playing_next_round: Optional[int]
