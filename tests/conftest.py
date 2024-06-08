import sys
import os
import pytest

# Adiciona o diretório pai ao sys.path para encontrar o módulo 'app'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client