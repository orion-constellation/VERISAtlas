'''
Rule Based Mapping Approach


'''
import json
from typing import Dict, List
from dataclasses import dataclass
from pydantic import BaseModel
from typing import List, Dict

@dataclass
class MappingRule:
    id: str
    veris_pattern: Dict
    mitre_mapping: Dict

class RuleBasedMapper:
    def __init__(self, rules_file):
        with open(rules_file, 'r') as f:
            data = json.load(f)
            self.rules = [MappingRule(**rule) for rule in data['mapping_rules']]

    def apply_rules(self, veris_incident: Dict) -> List[Dict]:
        results = []
        for rule in self.rules:
            if all(veris_incident.get(k) == v for k, v in rule.veris_pattern.items()):
                results.append(rule.mitre_mapping)
        return results

# Usage
mapper = RuleBasedMapper('rules.json')
mitre_mappings = mapper.apply_rules({
    'actor.external.variety': 'nation-state',
    'action.hacking.variety': 'brute-force'
})
