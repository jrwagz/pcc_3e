"""Test cases for the name function module"""
from name_function import get_formatted_name


def test_first_last_name():
    """Test only providing first and last name"""
    formatted_name = get_formatted_name("janis", "joplin")
    assert formatted_name == "Janis Joplin"
    formatted_name = get_formatted_name("bob", "ross")
    assert formatted_name == "Bob Ross"


def test_first_middle_last_name():
    """Test providing first, middle, and last name"""
    formatted_name = get_formatted_name(first="Janis", last="joplin", middle="jane")
    assert formatted_name == "Janis Jane Joplin"
    formatted_name = get_formatted_name(first="bob", last="Ross", middle="joe")
    assert formatted_name == "Bob Joe Ross"
    formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
    assert formatted_name == "Wolfgang Amadeus Mozart"
