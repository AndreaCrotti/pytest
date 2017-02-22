import pytest


@pytest.fixture #(scope='session')
def use_me():
    import pdb; pdb.set_trace()
    # heavily generated data
    return {'k1': 'val'}


def test_dic_check(use_me):
    assert len(use_me) == 1


def test_dic_check_second(use_me):
    assert list(use_me.keys()) == ['k1']
