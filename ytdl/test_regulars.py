

def test_valid_input():
    assert regulars.isValidURL('https://www.ns.nl') is True


def test_invalid_input():
    assert regulars.isValidURL('Not an url') is False


pass
