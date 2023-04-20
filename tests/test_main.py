from src import main

def test_sum_numbers():
    result1, result2 = main.sum_numbers(1,2)
    assert result1 == 3 # 想定通りの結果を書くところ
    assert result2 == 1 # 想定通りの結果を書くところ