'''
Parsing JSON and other Data Shenanigan

'''
import json
import os

'''
Load attack data from JSON files in a specified directory.

Parameters:
- directory (str): The directory path where JSON files are located.

Returns:
- list: A list containing the parsed data from the JSON files.

Example:
    load_attack_data('/path/to/directory')
'''

def load_veris_data(directory):
    '''
    Load all JSON files in a given directory and return them as a list of dicts.

    :param directory: The path to the directory containing the JSON files
    :returns: A list of dictionaries, where each dictionary represents a VERIS incident
    '''
    veris_data = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r') as f:
                incident = json.load(f)
                veris_data.append(incident)
    return veris_data

# Usage
veris_incidents = load_veris_data('VERIS/data/json')

'''
MITRE ATLAS Framework
'''

import json
import os

mitre_data = load_attack_data('cti/enterprise-attack')