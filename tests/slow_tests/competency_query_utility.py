import requests
from tests.config import Config

FLATMAP_ENDPOINT = Config.FLATMAP_ENDPOINT

FLATMAPS = [
    'human-flatmap_male',
    'human-flatmap_female',
    'rat-flatmap',
    'mouse-flatmap',
    'pig-flatmap',
    'cat-flatmap'
]

TESTING_VARIABLES = {}

def get_variables(key):
    return TESTING_VARIABLES[key]

def set_variables(data):
    TESTING_VARIABLES["END_POINT"] = FLATMAP_ENDPOINT + 'competency/query'
    for key, value in data.items():
        if key == 'human-flatmap_male':
            TESTING_VARIABLES["MALE_UUID"] = value['uuid']
            TESTING_VARIABLES["SCKAN_VERSION"] = value['knowledge-source']
        elif key == 'human-flatmap_female':
            TESTING_VARIABLES["FEMALE_UUID"] = value['uuid']
        elif key == 'rat-flatmap':
            TESTING_VARIABLES["RAT_UUID"] = value['uuid']
        elif key == 'mouse-flatmap':
            TESTING_VARIABLES["MOUSE_UUID"] = value['uuid']
        elif key == 'pig-flatmap':
            TESTING_VARIABLES["PIG_UUID"] = value['uuid']
        elif key == 'cat-flatmap':
            TESTING_VARIABLES["CAT_UUID"] = value['uuid']

def get_latest_flatmap(data):
    latest_flatmap_dict = {}
    for key, value in data.items():
        if key not in latest_flatmap_dict and key in FLATMAPS:
            stored_maps = sorted(value, key=lambda x: x["created"], reverse=True)
            latest_flatmap_dict[key] = stored_maps[0]
    return latest_flatmap_dict

def get_flatmap_info():
    flatmap_dict = {}
    flatmap_response = requests.get(FLATMAP_ENDPOINT)
    flatmap_json = flatmap_response.json()
    for map in flatmap_json:
        map_id = map.get('id', 'N/A')
        if map_id not in flatmap_dict:
            flatmap_dict[map_id] = []
        info = {
            'uuid': map.get('uuid', 'N/A'),
            'created': map.get('created', 'N/A'),
            'knowledge-source': map.get('sckan', {}).get('knowledge-source', 'N/A')
        }
        flatmap_dict[map_id].append(info)
    return flatmap_dict