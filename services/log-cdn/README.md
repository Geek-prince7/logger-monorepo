# Log CDN Service

A production-ready FastAPI service for storing and retrieving logs with PostgreSQL and Redis caching.

## Features

- 🚀 **FastAPI** - Modern, fast web framework
- 🗄️ **PostgreSQL** - Reliable database with SQLAlchemy ORM
- ⚡ **Redis** - High-performance caching layer
- 🔒 **Production Ready** - Middleware, error handling, logging
- 🐳 **Docker** - Multi-stage build for optimized images
- 📝 **OpenAPI** - Auto-generated API documentation

## Project Structure

```
log-cdn/
├── app/
│   ├── api/                 # API routes
│   │   ├── v1/              # Version 1 endpoints
│   │   │   ├── health.py    # Health check endpoints
│   │   │   └── logs.py      # Log CRUD endpoints
│   │   ├── deps.py          # Common dependencies
│   │   └── router.py        # Main API router
│   ├── cache/               # Redis cache layer
│   │   └── redis.py         # Redis client wrapper
│   ├── core/                # Core configuration
│   │   ├── config.py        # Settings management
│   │   └── exceptions.py    # Custom exceptions
│   ├── db/                  # Database layer
│   │   ├── models/          # SQLAlchemy models
│   │   ├── base.py          # Base model class
│   │   └── session.py       # Database session
│   ├── middleware/          # Custom middleware
│   │   ├── cors.py          # CORS configuration
│   │   ├── error_handler.py # Global error handling
│   │   └── logging.py       # Request/response logging
│   ├── schemas/             # Pydantic schemas
│   │   ├── common.py        # Common response schemas
│   │   ├── health.py        # Health check schemas
│   │   └── logs.py          # Log schemas
│   ├── services/            # Business logic
│   │   └── logs.py          # Log service
│   ├── utils/               # Utility functions
│   │   └── logging.py       # Logging setup
│   └── main.py              # Application entry point
├── tests/                   # Test files
├── .env.example             # Environment template
├── .gitignore
├── docker-compose.yml       # Local development setup
├── Dockerfile               # Production container
├── pyproject.toml           # Project configuration
├── README.md
└── requirements.txt         # Python dependencies
```

## Quick Start

### Local Development

1. **Clone and setup environment:**
   ```bash
   cd services/log-cdn
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your database and Redis settings
   ```

3. **Run with Docker Compose (recommended):**
   ```bash
   docker-compose up -d
   ```

4. **Or run locally:**
   ```bash
   # Start PostgreSQL and Redis separately, then:
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Access the API:**
   - API: http://localhost:8000
   - Docs: http://localhost:8000/docs (development only)
   - Health: http://localhost:8000/api/v1/health

### Docker Production Build

```bash
docker build -t log-cdn:latest .
docker run -p 8000:8000 --env-file .env log-cdn:latest
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Service info |
| GET | `/api/v1/health` | Full health check |
| GET | `/api/v1/ready` | Readiness probe (K8s) |
| GET | `/api/v1/live` | Liveness probe (K8s) |
| POST | `/api/v1/logs` | Create log entry |
| GET | `/api/v1/logs` | List logs (paginated) |
| GET | `/api/v1/logs/{id}` | Get log by ID |
| DELETE | `/api/v1/logs/{id}` | Delete log |

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `APP_NAME` | Application name | Log CDN Service |
| `APP_VERSION` | Application version | 1.0.0 |
| `DEBUG` | Enable debug mode | false |
| `DATABASE_URL` | PostgreSQL connection URL | - |
| `REDIS_HOST` | Redis host | localhost |
| `REDIS_PORT` | Redis port | 6379 |
| `REDIS_PASSWORD` | Redis password | - |
| `CORS_ORIGINS` | Allowed CORS origins | ["*"] |

## Development

### Run Tests
```bash
pytest --cov=app tests/
```

### Linting
```bash
ruff check app/
black app/
mypy app/
```

### Database Migrations
```bash
# Initialize Alembic (first time only)
alembic init alembic

# Create migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head
```

## License

MIT
