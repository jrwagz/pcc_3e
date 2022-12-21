"""pytest for survey module"""
import pytest
from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions"""
    question = "What language did you first learn to speak?"
    survey = AnonymousSurvey(question)
    return survey


def test_store_single_response(
    language_survey: AnonymousSurvey,  # pylint: disable=redefined-outer-name
) -> None:
    """Test that a single response is stored properly"""
    language_survey.store_response("Blue")
    assert "Blue" in language_survey.responses


def test_store_three_responses(
    language_survey: AnonymousSurvey,  # pylint: disable=redefined-outer-name
) -> None:
    """Test that we can handle 3 responses"""
    responses = ["USA", "Brazil", "Japan"]
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
