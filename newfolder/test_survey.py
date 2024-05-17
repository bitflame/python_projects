import pytest
from survey import AnonymousSurvey
@pytest.fixture
def language_survey():
     question = 'What language did you learn first'
     language_survey = AnonymousSurvey(question)
     return language_survey
 
def test_store_single_response(language_survey):
    '''Test that a single response if stored properly'''
    language_survey.store_response('english')
    assert 'english' in language_survey.responses

def test_store_responses(language_survey):
    '''Test that more than one response can be stored properly'''
    responses = ['english', 'spanish', 'dutch']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses