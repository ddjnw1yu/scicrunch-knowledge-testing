import pytest
from tests.slow_tests.overrides.utility import cq_request, assert_valid_query_response, SCKAN_VERSION, MALE_UUID, FEMALE_UUID

# What are all neuron populations that run through the vagus nerve
# (without forward and backward connections)
base_query = {
    'query_id': '25',
    'parameters': [
        {
            'column': 'source_feature_id',
            'value': []
        },
        {
            'column': 'via_feature_id',
            'value': [
                'UBERON:0001759'
            ]
        },
        {
            'column': 'dest_feature_id',
            'value': []
        }
    ]
}

def test_sckan():
    query = {**base_query, 'parameters': base_query['parameters'] + [{'column': 'source_id', 'value': SCKAN_VERSION}]}
    response = cq_request(query)
    assert_valid_query_response(
        response,
        expected_num_keys=2,
        expected_num_values=24
    )

def test_human_male_map():
    query = {**base_query, 'parameters': base_query['parameters'] + [{'column': 'source_id', 'value': MALE_UUID}]}
    response = cq_request(query)
    assert_valid_query_response(
        response,
        expected_num_keys=2,
        expected_num_values=23
    )

def test_human_female_map():
    query = {**base_query, 'parameters': base_query['parameters'] + [{'column': 'source_id', 'value': FEMALE_UUID}]}
    response = cq_request(query)
    assert_valid_query_response(
        response,
        expected_num_keys=2,
        expected_num_values=28
    )
