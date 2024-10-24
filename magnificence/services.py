import json
from typing import Optional

from django.db.models import F, Case, When, QuerySet
from django.db import transaction

from .models import Team, ElementType, Element, ElementTypeName
from .schemas import (
    TeamInputSchema,
    ElementTypeInputSchema,
    ElementInputSchema,
)

NO_OF_GOALKEEPER = 1
NO_OF_DEFENDERS = 2
NO_OF_MIDFIELDERS = 3
NO_OF_FORWARD = 1


@transaction.atomic
def populate_data(delete_prev_data=True) -> None:
    print("Data Population Started")

    if delete_prev_data:
        delete_populated_data()

    with open("magnificence/tests/artifacts/test_data.json", "r") as json_file:
        json_data = json.load(json_file)

        teams_data = (
            TeamInputSchema(**teams_datum) for teams_datum in json_data["teams"]
        )
        element_types_data = (
            ElementTypeInputSchema(**element_types_datum)
            for element_types_datum in json_data["element_types"]
        )
        elements_data = (
            ElementInputSchema(**element_datum)
            for element_datum in json_data["elements"]
        )

    team_model_data = [
        Team(
            id=team.id,
            code=team.code,
            name=team.name,
            short_name=team.short_name,
        )
        for team in teams_data
    ]

    Team.objects.bulk_create(team_model_data)

    element_type_model_data = [
        ElementType(
            id=element_type.id,
            singular_name=element_type.singular_name,
            singular_name_short=element_type.singular_name_short,
        )
        for element_type in element_types_data
    ]

    ElementType.objects.bulk_create(element_type_model_data)

    element_model_data = [
        Element(
            id=element.id,
            element_type_id=element.element_type,
            first_name=element.first_name,
            second_name=element.second_name,
            goals_scored=element.goals_scored,
            assists=element.assists,
            goals_conceded=element.goals_conceded,
            penalties_saved=element.penalties_saved,
            penalties_missed=element.penalties_missed,
            saves=element.saves,
            team_id=element.team,
            chance_of_playing_next_round=element.chance_of_playing_next_round,
            chance_of_playing_this_round=element.chance_of_playing_this_round,
            web_name=element.web_name,
            total_points=element.total_points,
        )
        for element in elements_data
    ]

    Element.objects.bulk_create(element_model_data)

    print("Data Population Completed")


def delete_populated_data() -> None:
    print("Deletion Started")
    Team.objects.all().delete()
    ElementType.objects.all().delete()
    Element.objects.all().delete()
    print("Deletion Completed")


def get_magnificent_team(
    team_short_name: Optional[str] = None,
) -> QuerySet[Element]:
    elements = (
        Element.objects.select_related("element_type", "team")
        .annotate(
            magnificence=Case(
                When(
                    element_type__singular_name_short=ElementTypeName.GOALKEEPER,
                    then=F("saves") + F("assists"),
                ),
                default=F("goals_scored") + F("assists"),
            )
        )
        .order_by("-magnificence", "id")
    )

    if team_short_name:
        elements = elements.filter(team__short_name__iexact=team_short_name)

    goalkeepers = elements.filter(
        element_type__singular_name_short=ElementTypeName.GOALKEEPER
    )[:NO_OF_GOALKEEPER]

    defenders = elements.filter(
        element_type__singular_name_short=ElementTypeName.DEFENDER
    )[:NO_OF_DEFENDERS]

    midfielders = elements.filter(
        element_type__singular_name_short=ElementTypeName.MIDFIELDER
    )[:NO_OF_MIDFIELDERS]

    forwards = elements.filter(
        element_type__singular_name_short=ElementTypeName.FORWARD
    )[:NO_OF_FORWARD]

    queryset = goalkeepers | defenders | midfielders | forwards

    return queryset
