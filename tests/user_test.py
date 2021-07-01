# Third party modules
import pytest
import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(
        os.path.join(
            os.getcwd(),
            os.path.expanduser(__file__)
        )
    )
)
sys.path.append(
    os.path.normpath(
        os.path.join(
            SCRIPT_DIR,
            PACKAGE_PARENT
        )
    )
)

from app import create_app
@pytest.fixture
def client():
    app = create_app("config_test.py")
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_square(client):
    rv = client.get("/test/hello")
    print("tgao")
    print(rv)
    print(rv.data)