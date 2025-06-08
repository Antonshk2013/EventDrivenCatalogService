
# 📦 EventDriven API

Проект на FastAPI с асинхронным SQLAlchemy и PostgreSQL. Управление миграциями осуществляется через Alembic. Все настройки считываются из `.env`.

---

## 📁 Структура проекта (упрощённо)

```


```

---

## 🚀 Быстрый старт

### 1. Клонировать проект и установить зависимости

```bash
git clone https://github.com/your-username/event-driven.git
cd event-driven
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Заполнить `.env`

```env
DATABASE_HOST=localhost
DATABASE_PORT=5433
DATABASE_NAME=event_driven
DATABASE_USERNAME=fast_api
DATABASE_PASSWORD=your_password
```

### 3. Запуск PostgreSQL через Docker

```bash
docker-compose up -d
```

---

## 🛠️ Alembic

### 📌 Создать новую миграцию

```bash
alembic revision --autogenerate -m "описание миграции"
```

### 🚀 Применить миграции

```bash
alembic upgrade head
```

### ⬅️ Откатить последнюю миграцию

```bash
alembic downgrade -1
```

---

## 🧪 Запуск проекта

```bash
uvicorn api.app.main:app --reload
```

---

## 🐳 Docker Compose (`docker-compose.yml`)

```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: ${DATABASE_USERNAME}
      POSTGRES_PASSWORD: ${DATABASE_PASSWORD}
      POSTGRES_DB: ${DATABASE_NAME}
    ports:
      - "${DATABASE_PORT}:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

---

## 📬 Контакты

Автор: Антон Шкарупа  
Email: [твой email]  
Telegram: [твой Telegram]
