from starlette.responses import Response
from ..service.main import app
from httpx import AsyncClient
from fastapi.testclient import TestClient
import pytest


@pytest.mark.asyncio
async def test_get_main():
    async with AsyncClient(app=app, base_url="https://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"johnnie": "fujita"}

@pytest.mark.asyncio
async def test_get_items():
    async with AsyncClient(app=app, base_url="https://test") as ac:
        data = {"title": "Johnnie", "description": "a pair of old sock"}
        response = await ac.get("/api/items")
        assert response.status_code ==200
        assert data in response.json()

@pytest.mark.asyncio
async def test_get_item():
    async with AsyncClient(app=app, base_url="https://test") as ac:
        data = {"title": "Johnnie", "description": "a pair of old sock"}
        response = await ac.get("/api/items/0")
        assert response.status_code ==200
        assert data == response.json()
    
@pytest.mark.asyncio
async def test_create_item():
    async with AsyncClient(app=app, base_url="https://test") as ac:
        data = {"title": "Johnnie", "description": "a pair of old sock"}
        response = await ac.post("/api/items", json=data)
        assert response.status_code ==200
        assert data == response.json()