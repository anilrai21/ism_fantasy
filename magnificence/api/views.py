from django.http import HttpRequest
from ninja import Router

router = Router()


@router.get(
    "/magnificence",
)
def hello_world(request: HttpRequest):
    return {"hello": "world"}
