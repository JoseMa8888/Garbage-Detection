from fastapi import APIRouter
from service.api.endpoints.mn_detection import mn_router
from service.api.endpoints.vit_detection import vit_router

main_router = APIRouter()

main_router.include_router(mn_router)
main_router.include_router(vit_router)