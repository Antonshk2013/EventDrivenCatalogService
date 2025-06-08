from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_db
from models.brands import Brand
from schemas.brands import BrandCreate, BrandsList, BrandRead

router = APIRouter(prefix="/brands", tags=["Бренды"])

@router.get(
    path="/",
    response_model=BrandsList,
    summary="Получить все брендов",
    description="Возвращает список всех брендов с указанием количества",
    response_description="Список брендов"
)
async def get_all_brands(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Brand))
    brands = result.scalars().all()
    return BrandsList(data=brands, count=len(brands))

@router.post(
    path="/",
    response_model=BrandRead,
    summary="Создать Бренд",
    description="Возвращает созданный бренд с присвоенным идентификатором",
    response_description="Созданный бренд"
)
async def create_brand(
    brand: BrandCreate,
    session: AsyncSession = Depends(get_db),
):
    new_brand = Brand(
        name=brand.name,
        logo=brand.logo,
        description=brand.description
    )
    session.add(new_brand)
    await session.commit()
    await session.refresh(new_brand)
    return new_brand


@router.get(
    path="/{id}",
    response_model=BrandRead,
    summary="Получить информцию о бренде по идентификатору",
    description="Возвращает объкет бренд со всеми аттрибутами",
    response_description="Бренд"
)
async def get_brand(
    id: int,
    session: AsyncSession = Depends(get_db),
):
    result = await session.execute(select(Brand).where(Brand.id == id))
    brand = result.scalars().first()

    if not brand:
        raise HTTPException(status_code=404, detail="Категория не найдена")

    return brand
