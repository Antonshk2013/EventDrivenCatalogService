from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_db
from models.specifications import Specification
from schemas.specifications import SpecificationCreate, SpecificationRead, SpecificationsList


router = APIRouter(prefix='/specifications', tags=['Спецификации'])

@router.get(path='/',
            response_model=SpecificationsList,
            summary="Получить все спецификации",
            description="Возвращает список всех спецификаций с указанием количества",
            response_description="Список спецификаций"
            )
async def get_all_specifications(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Specification))
    specifications = result.scalars().all()
    return SpecificationsList(data=specifications, count=len(specifications))

@router.post(
    path="/",
    response_model=SpecificationCreate,
    summary="Создать Спецификацию",
    description="Возвращает созданную спецификацию с присвоенным идентификатором",
    response_description="Созданная спецификация"
            )
async def create_specifications(
    specification: SpecificationCreate,
    session: AsyncSession = Depends(get_db),
):
    new_specification = Specification(
        name=specification.name,
        specific_type=specification.specific_type,
    )
    session.add(new_specification)
    await session.commit()
    await session.refresh(new_specification)
    return new_specification

@router.get(path="/{id}",
    response_model=SpecificationRead,
    summary="Получить информцию о Спецификации по идентификатору",
    description="Возвращает объкет Спецификация со всеми аттрибутами",
    response_description="Спецификация")
async def get_specification(
    id: int,
    session: AsyncSession = Depends(get_db),
    ):
    result = await session.execute(select(Specification).where(Specification.id == id))
    specification = result.scalars().first()

    if not specification:
        raise HTTPException(status_code=404, detail="Спецификация не найдена")

    return specification
