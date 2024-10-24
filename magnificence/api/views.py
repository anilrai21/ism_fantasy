from typing import List

from django.http import HttpRequest
from ninja import Router

from magnificence.api.schemas import ElementSchema
from magnificence.services import get_magnificent_team

router = Router()


@router.get("/magnificent-team", response=List[ElementSchema])
def magnificence_team(request: HttpRequest):
    """
    Get the magnificent team

    :param request:
    :return:
    """
    return get_magnificent_team()
