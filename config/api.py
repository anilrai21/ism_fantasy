from ninja import NinjaAPI

from magnificence.api.views import router as app_router

api = NinjaAPI()


api.add_router("/data/", app_router)
