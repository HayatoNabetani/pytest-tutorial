import pytest
from src import main

def test_get_user_names():
    with pytest.raises(ValueError) as e:
        main.user_name_validation(None)
    assert str(e.value) == '名前が設定されていません。'