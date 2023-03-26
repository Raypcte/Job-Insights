from src.pre_built.counter import count_ocurrences


def test_counter():
    pass
    assert count_ocurrences("data/jobs.csv", "Xablau") == 0
    assert count_ocurrences("data/jobs.csv", "Javascript") == 122
