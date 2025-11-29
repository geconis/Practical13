from infra.api_client import GenshinAPIClient

def test_get_characters_returns_data():
    client = GenshinAPIClient()
    data = client.get_characters()
    assert isinstance(data, dict)
    assert "albedo" in data 

def test_get_weapons_returns_data():
    client = GenshinAPIClient()
    data = client.get_weapons()
    assert isinstance(data, dict)
