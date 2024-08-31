'''
Unified Data Model
- Combined MITRE and VERIS Data
- Planning for Database Integration

'''

from pydantic import BaseModel
from typing import List, Dict
from dataclasses import dataclass
from ..api import get_graph,

class VERISIncident(BaseModel):
    incident_id: str
    actor: Dict
    action: Dict
    asset: Dict
    attribute: Dict
    impact: Dict

class MITRETechnique(BaseModel):
    technique_id: str
    name: str
    description: str
    tactics: List[str]

class IntegratedDataModel:
    def __init__(self):
        self.veris_incidents: Dict[str, VERISIncident] = {}
        self.mitre_techniques: Dict[str, MITRETechnique] = {}
        self.mappings: Dict[str, List[str]] = {}  # VERIS action to MITRE technique IDs

    def add_veris_incident(self, incident: Dict):
        veris_incident = VERISIncident(**incident)
        self.veris_incidents[veris_incident.incident_id] = veris_incident

    def add_mitre_technique(self, technique: Dict):
        mitre_technique = MITRETechnique(**technique)
        self.mitre_techniques[mitre_technique.technique_id] = mitre_technique

    def map_veris_to_mitre(self, veris_action: str, mitre_technique_id: str):
        if veris_action not in self.mappings:
            self.mappings[veris_action] = []
        self.mappings[veris_action].append(mitre_technique_id)

# Usage
data_model = IntegratedDataModel()

# Load VERIS data
veris_incidents = load_veris_data('VERIS/data/json')
for incident in veris_incidents:
    data_model.add_veris_incident(incident)

# Load MITRE ATT&CK data
mitre_data = fetch_attack_data()
for item in mitre_data:
    if item['type'] == 'attack-pattern':
        data_model.add_mitre_technique(item)

# Perform mappings (this would be based on your mapping rules)
data_model.map_veris_to_mitre('action.hacking.variety.brute-force', 'T1110')