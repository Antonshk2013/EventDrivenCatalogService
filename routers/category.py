from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_db
from models.categories import Category
from schemas.category import CategoryList, CategoryCreate, CategoryRead

router = APIRouter(prefix="/categories", tags=["Категории"])

@router.get(
    path="/",
    response_model=CategoryList,
    summary="Получить все категории",
    description="Возвращает список всех категорий с указанием количества",
    response_description="Список категорий"
)
async def get_all_categories(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Category))
    categories = result.scalars().all()
    return CategoryList(data=categories, count=len(categories))

@router.post(
    path="/",
    response_model=CategoryRead,
    summary="Создать категорию",
    description="Возвращает созданную категорию с присвоенным идентификатором",
    response_description="Созданная категория"
)
async def create_category(
    category: CategoryCreate,
    session: AsyncSession = Depends(get_db),
):
    new_category = Category(
        name=category.name,
        description=category.description,
        parent_id=category.parent_id,
        image=category.image,
    )
    session.add(new_category)
    await session.commit()
    await session.refresh(new_category)
    return new_category


@router.get(
    path="/{id}",
    response_model=CategoryRead,
    summary="Получить информцию о категории по идентификатору",
    description="Возвращает объкет категория со всеми аттрибутами",
    response_description="Категория"
)
async def get_category(
    id: int,
    session: AsyncSession = Depends(get_db),
):
    result = await session.execute(select(Category).where(Category.id == id))
    category = result.scalars().first()

    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")

    return category