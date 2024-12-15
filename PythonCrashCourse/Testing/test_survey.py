# import pytest
'''import error'''
from survey import Survey

# @pytest.fixture
# def wood_survey():
#     question = 'How much would could a wood chuck chuck?'
#     wood_survey = Survey(question)
#     return wood_survey

def test_store_single_response():
    wood_survey = Survey('How much would could a wood chuck chuck?')
    wood_survey.store_response('none')
    assert 'none' in wood_survey.responses
    
def test_store_multiple_responses():
    wood_survey = Survey('How much would could a wood chuck chuck?')
    responses = [39, 'wow, so many', 'at least 5 pounds']
    for response in responses:
        wood_survey.store_response(response)
    for response in responses:
        assert response in wood_survey.responses