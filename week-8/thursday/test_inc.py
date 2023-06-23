def inc(x):
    return x + 1

def mat(x, fn):
    return fn(x)


def test_correct_answer_inc():
    assert inc(4) == 5


def test_incorrect_answer_inc():
    assert inc(3) != 5

def test_correct_answer_mat():
    assert mat(4, inc) == 5


def test_incorrect_answer_mat():
    assert mat(3, inc) != 5
