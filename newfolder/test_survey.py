import pytest
from survey import AnonymousSurvey
@pytest.fixture
def language_survey():
    print()    
def test_store_single_response():
    '''Test that a single response if stored properly'''
    question = 'What language did you learn first'
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('english')
    assert 'english' in language_survey.responses

def test_store_responses():
    '''Test that more than one response can be stored properly'''
    question = "What langugage did you learn first? "
    language_survey = AnonymousSurvey(question)
    responses = ['english', 'spanish', 'dutch']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses