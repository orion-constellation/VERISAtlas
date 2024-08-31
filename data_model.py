
from typing import List, Optional, Dict, Tuple
from dataclasses import dataclass
@dataclass
class AttackPatterns:
    attack_pattetn: object
    campaign: object #Broader scope on an attack
    intrusion_set: object
    malware_tool: object #Linked to a technique in Atlas
@dataclass
class Relationships:
    "USES": List[str]
    "INDICATES": List[str]
    "MITIGATES": List[str]
    "TARGETS": List[str]
    