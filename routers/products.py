from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_db
from models.products import Product
from schemas.products import ProductCreate, ProductRead

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