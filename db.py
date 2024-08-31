'''
DB Operations

'''

from pymongo import MongoClient
def store_in_database(data_model):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['integrated_threat_db']
    
    # Store VERIS incidents
    db.veris_incidents.insert_many([incident.dict() for incident in data_model.veris_incidents.values()])
    
    # Store MITRE techniques
    db.mitre_techniques.insert_many([technique.dict() for technique in data_model.mitre_techniques.values()])
    
    # Store mappings
    db.mappings.insert_one(data_model.mappings)

# Run the pipeline
extract_and_integrate_data()