from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional, List


@dataclass
class TeamInputSchema:
    code: int
    draw: int
    form: Optional[int]
    id: int
    loss: int
    name: str
    played: int
    points: int
    position: int
    short_name: str
    strength: int
    team_division: Optional[int]
    unavailable: bool
    win: int
    strength_overall_home: int
    strength_overall_away: int
    strength_attack_home: int
    strength_attack_away: int
    strength_defence_home: int
    strength_defence_away: int
    pulse_id: int


@dataclass
class ElementInputSchema:
    chance_of_playing_next_round: Decimal
    chance_of_playing_this_round: Decimal
    code: Decimal
    cost_change_event: Decimal
    cost_change_event_fall: Decimal
    cost_change_start: Decimal
    cost_change_start_fall: Decimal
    dreamteam_count: Decimal
    element_type: int
    ep_next: Decimal
    ep_this: Decimal
    event_points: Decimal
    first_name: str
    form: Decimal
    id: int
    in_dreamteam: bool
    news: str
    news_added: datetime
    now_cost: 54
    photo: str
    points_per_game: Decimal
    second_name: str
    selected_by_percent: Decimal
    special: bool
    squad_number: Optional[int]
    status: str
    team: int
    team_code: int
    total_points: int
    transfers_in: int
    transfers_in_event: int
    transfers_out: int
    transfers_out_event: int
    value_form: Decimal
    value_season: Decimal
    web_name: str
    region: Optional[int]
    minutes: int
    goals_scored: int
    assists: int
    clean_sheets: int
    goals_conceded: int
    own_goals: int
    penalties_saved: int
    penalties_missed: int
    yellow_cards: int
    red_cards: int
    saves: int
    bonus: int
    bps: int
    influence: Decimal
    creativity: Decimal
    threat: Decimal
    ict_index: Decimal
    starts: int
    expected_goals: Decimal
    expected_assists: Decimal
    expected_goal_involvements: Decimal
    expected_goals_conceded: Decimal
    influence_rank: int
    influence_rank_type: int
    creativity_rank: int
    creativity_rank_type: int
    threat_rank: int
    threat_rank_type: int
    ict_index_rank: int
    ict_index_rank_type: int
    corners_and_indirect_freekicks_order: Optional[None]
    corners_and_indirect_freekicks_text: str
    direct_freekicks_order: Optional[None]
    direct_freekicks_text: str
    penalties_order: Optional[None]
    penalties_text: str
    expected_goals_per_90: Decimal
    saves_per_90: Decimal
    expected_assists_per_90: Decimal
    expected_goal_involvements_per_90: Decimal
    expected_goals_conceded_per_90: Decimal
    goals_conceded_per_90: Decimal
    now_cost_rank: Decimal
    now_cost_rank_type: Decimal
    form_rank: Decimal
    form_rank_type: Decimal
    points_per_game_rank: Decimal
    points_per_game_rank_type: Decimal
    selected_rank: Decimal
    selected_rank_type: Decimal
    starts_per_90: Decimal
    clean_sheets_per_90: Decimal


@dataclass
class ElementTypeInputSchema:
    id: int
    plural_name: str
    plural_name_short: str
    singular_name: str
    singular_name_short: str
    squad_select: int
    squad_min_select: Optional[int]
    squad_max_select: Optional[int]
    squad_min_play: int
    squad_max_play: int
    ui_shirt_specific: bool
    sub_positions_locked: List[int]
    element_count: int
