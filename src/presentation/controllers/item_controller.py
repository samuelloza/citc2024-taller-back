from fastapi import APIRouter, Depends, HTTPException

from src.core.abstractions.services.item_service_abstract import IItemService
from src.core.dependency_inyection.dependency_inyection import (
    build_item_service
)
item_controller = APIRouter(prefix="/api/v1", tags=["item"])


@item_controller.get("/item/{item_id}")
async def get_item_by_id(
    item_id: int,
    item_service: IItemService = Depends(build_item_service)
):
    item = await item_service.get_item_by_id(item_id)
    if item is not None:
        return item
    raise HTTPException(status_code=404, detail="item no encontrado.")
