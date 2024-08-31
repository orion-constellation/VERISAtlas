import rustworkx as rx
from rustworkx import PyDiGraph
import json
import os
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, field
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import re
from datetime import datetime
from uuid import uuid4


@dataclass
class SessionID:
    id: String() = f"{uuid4()}

@dataclass
class FrameworkElement:
    id: uuid4()
    name: str
    description: str
    type: str
    metadata: Optional[Dict] = field(default_factory=dict)
    links: Optional[Dict] = field(default_factory=dict)
    attributes: Dict[str, Union[str, int, float]] = field(default_factory=dict)

@dataclass
class ECSEvent:
    id: uuid4()
    event_id: str
    event_category: str
    event_type: str
    event_action: Optional[str] = None
    technique_id: Optional[str] = None
    action_id: Optional[str] = None

'''
FRAMEWORK MAPPER:
1. Does the heavy lifting to unify the two intelligence sources
2. Compatible with ECS for the use in ELK

'''

class FrameworkMapper:
    def __init__(self, rules_file):
        self.graph = rx.PyDiGraph()
        self.id_to_index = {}
        self.normalizer = TextNormalizer()
        
    def load_json_files(self, dir: str, framework: str) -> JSON:
        for file_name in os.listdir(dir):
            if file_name endswith('.json'):
                with open(os.path.join(dir, file_name)), 'r' as file:
                    data = json.load(file)
                    self.parse_data(data, framework, file_name)
    
    def parse_data(self, data: Union[Dict, List], framework:str, source:str):
        if isinstance(data, list):
            for item in data:
                self.parse_item(item, framework, source)
        elif isinstance(data, dict):
            for 'objects' in data: #Specifically the MITRE
                for items in data['objects']:
                    self.parse_item(item, framework, source)
        else: # VERIS FORMAT
            self.parse_item(data, framework, source)
    
    def parse_item(self, item: Dict, framework: str, source: str):
        if framework == "mitre" and item.get('type') == "attack-pattern":
            element = FrameworkElement(
                id=item['id'],
                name=item['name'],
                type='technique',
                description=item.get('description'),
                source=source,
                attributes={'tactic': [phase['phase_name'] for phase in item.get('kill_chain_phases', [])]}
            )
        elif framework == "veris":
            element = self.parse_item(item, source)
        else:
            raise ValueError(f" Invalid Data or Framework")
            

        
                
            )
        
    
                    
                    