from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from database import get_db
from models.products import Product
from schemas.products import ProductCreate, ProductRead, ProductsList, ProductFilter

router = APIRouter(prefix="/products", tags=["Продукты"])

@router.post(
    path="/",
    response_model=ProductRead,
    summary="Создать Продукт",
    description="Возвращает созданный продукт с присвоенным идентификатором",
    response_description="Созданный продукт"
)
async def create_product(
    product: ProductCreate,
    session: AsyncSession = Depends(get_db),
):
    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        sku=product.sku,
        category_id=product.category_id,
        brand_id=product.brand_id,
        rate=product.rate,
        is_active=product.is_active
    )
    session.add(new_product)
    await session.commit()
    await session.refresh(new_product)
    return new_product

@router.get(
    path="/",
    response_model=ProductsList,
    summary="Получить все продукты",
    description="Поиск/фильтрация (по названию, категории, бренду, цене, характеристикам), сортировка (цена, рейтинг, "
                "новизна), пагинация. Не возвращает неактивные или отсутствующие товары",
    response_description="Список продуктов"
)
async def get_all_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).options(selectinload(Product.category)).options(selectinload(Product.brand)))
    products = result.scalars().all()
    return ProductsList(data=products, count=len(products))



@router.get(
    path="/fillter",
    response_model=ProductsList,
    summary="Получить все продукты ",
    description="Поиск/фильтрация (по названию, категории, бренду, цене, характеристикам), сортировка (цена, рейтинг, "
                "новизна), пагинация. Не возвращает неактивные или отсутствующие товары",
    response_description="Список продуктов"
)
async def get_all_products_by_fillter(
        db: AsyncSession = Depends(get_db),

        name: str | None = Query(default=None),
        category_id: int | None = Query(default=None),
        min_price: Optional[float] = Query(None, ge=0),
        max_price: Optional[float] = Query(None, ge=0),
        skip: int = Query(0, ge=0),
        limit: int = Query(10, ge=1),
):
    db_query = select(Product).options(selectinload(Product.category)).options(selectinload(Product.brand))
    if name:
        db_query = db_query.where(Product.name.ilike(f"%{name}%"))
    if category_id:
        db_query = db_query.where(Product.category_id==category_id)
    if min_price is not None:
        stmt = db_query.where(Product.price >= min_price)
    if max_price is not None:
        stmt = db_query.where(Product.price <= max_price)
    db_query = db_query.offset(skip).limit(limit)
    result = await db.execute(db_query)
    products = result.scalars().all()
    return ProductsList(data=products, count=len(products))


@router.get(
    path="/{id}",
    response_model=ProductRead,
    summary="Получить информцию о продукте по идентификатору",
    description="Возвращает объкет продукт со всеми аттрибутами",
    response_description="Продукт"
)
async def get_product(
    id: int,
    session: AsyncSession = Depends(get_db)
    ):
    result = await session.execute(select(Product)
                                   .options(selectinload(Product.category))
                                   .options(selectinload(Product.brand))
                                   .where(Product.id==id)
                                   .where(Product.is_active==True))
    product = result.scalars().first()

    if not product:
        raise HTTPException(status_code=404, detail="Продукт не найдена")

    return product


