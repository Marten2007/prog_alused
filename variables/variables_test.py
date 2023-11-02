import pytest
import variables


# 1

@pytest.mark.dependency(name="word_exists")
@pytest.mark.timeout(1.0)
def test_variable_word_exists():
    assert hasattr(variables, "word"), "Do you have a variable 'word' in your code?"


@pytest.mark.timeout(1.0)
@pytest.mark.dependency(depends=['word_exists'])
def test_variable_word_type():
    from variables import word
    assert isinstance(word, str)


@pytest.mark.dependency(depends=['word_exists'])
@pytest.mark.timeout(1.0)
def test_variable_word_value():
    from variables import word
    assert word == "spider"

# 2
@pytest.mark.dependency(name="thousand_exists")
@pytest.mark.timeout(1.0)
def test_variable_thousand_exists():
    assert hasattr(variables, "thousand"), "Do you have a variable 'thousand' in your code?"

@pytest.mark.dependency(depends=["thousand_exists"])
@pytest.mark.timeout(1.0)
def test_variable_thousand_type():
    from variables import thousand
    assert isinstance(thousand, str)


@pytest.mark.dependency(depends=["thousand_exists"])
@pytest.mark.timeout(1.0)
def test_variable_thousand_value():
    from variables import thousand
    assert thousand == "1000"

# 3

@pytest.mark.dependency()
@pytest.mark.timeout(1.0)
def test_variable_number_exists():
    assert hasattr(variables, "ten"), "Do you have a variable 'ten' in your code?"


@pytest.mark.dependency(depends=["test_variable_number_exists"])
@pytest.mark.timeout(1.0)
def test_variable_number_type():
    from variables import ten
    assert isinstance(ten, int)


@pytest.mark.dependency(depends=["test_variable_number_exists"])
@pytest.mark.timeout(1.0)
def test_variable_number_value():
    from variables import ten
    assert ten == 10


# 4

@pytest.mark.dependency()
@pytest.mark.timeout(1.0)
def test_variable_first_exists():
    assert hasattr(variables, "first_half"), "Do you have a variable 'first_half' in your code?"


@pytest.mark.dependency(depends=["test_variable_first_exists"])
@pytest.mark.timeout(1.0)
def test_variable_first_type():
    from variables import first_half
    assert isinstance(first_half, str)


@pytest.mark.dependency(depends=["test_variable_first_exists"])
@pytest.mark.timeout(1.0)
def test_variable_first_value():
    from variables import first_half
    assert first_half == "full"


# 5

@pytest.mark.dependency()
@pytest.mark.timeout(1.0)
def test_variable_second_exists():
    assert hasattr(variables, "second_half"), "Do you have a variable 'second_half' in your code?"


@pytest.mark.dependency(depends=["test_variable_second_exists"])
@pytest.mark.timeout(1.0)
def test_variable_second_type():
    from variables import second_half
    assert isinstance(second_half, str)


@pytest.mark.dependency(depends=["test_variable_second_exists"])
@pytest.mark.timeout(1.0)
def test_variable_second_value():
    from variables import second_half
    assert second_half == "moon"

# 6

@pytest.mark.dependency()
@pytest.mark.timeout(1.0)
def test_variable_complete_exists():
    assert hasattr(variables, "complete"), "Do you have a variable 'complete' in your code?"


@pytest.mark.dependency(depends=["test_variable_complete_exists"])
@pytest.mark.timeout(1.0)
def test_variable_complete_type():
    from variables import complete
    assert isinstance(complete, str)


@pytest.mark.dependency(depends=["test_variable_complete_exists"])
@pytest.mark.timeout(1.0)
def test_variable_complete_value():
    from variables import complete
    assert complete == "full moon"