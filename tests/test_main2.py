from src import main

def get_json_data_mock(id):
    return {'name' : 'test'}

def test_get_user_names(monkeypatch):
    monkeypatch.setattr(
        main, 'get_json_data', get_json_data_mock
    )
    result = main.get_user_names(['001', '009'])

    assert list(result.keys()) == ['001', '009']
    assert list(result.values()) == ['test', 'test']