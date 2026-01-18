import pytest
from tests.slow_tests.overrides.utility import cq_request, assert_valid_query_response, SCKAN_VERSION, MALE_UUID, FEMALE_UUID

# Neuron populations associated with location/[locations]
# Liver & Tongue
base_query = {
    'query_id': '1',
    'parameters': [
        {
            'column': 'feature_id',
            'value': ["UBERON:0002107", "UBERON:0001723"]
        }
    ]
}

def test_sckan():
    query = {**base_query, 'parameters': base_query['parameters'] + [{'column': 'source_id', 'value': SCKAN_VERSION}]}
    response = cq_request(query)
    assert_valid_query_response(
        response,
        expected_num_keys=2,
        expected_num_values=2
    )

def test_human_male_map():
    query = {**base_query, 'parameters': base_query['parameters'] + [{'column': 'source_id', 'value': MALE_UUID}]}
    response = cq_request(query)
    assert_valid_query_response(
        response,
        expected_num_keys=2,
        expected_num_values=16
    )

def test_human_female_map():
    query = {**base_query, 'parameters': base_query['parameters'] + [{'column': 'source_id', 'value': FEMALE_UUID}]}
    response = cq_request(query)
    assert_valid_query_response(
        response,
        expected_num_keys=2,
        expected_num_values=16
    )
