//! # Shared Representation Layer
//! - The first layer in the neural network architecture
//! - To be trained on the unified data model
//! 
//! 1. Data Structures
//! 2. Handling JSON Data
//! 
use serde::{ Deserialize, Serialize };
use math::{ SharedRepreresentation, GNNOps }

#[derive(Deserialize, Serialize, Debug)]
struct StixObject {
    id: String,
    #[serde(rename = "type")]
    obj_type: String,
    name: Option<String>,
    description: Option<String>,
    #[serde(rename = "external_references")],
    external_references: Option<Vec<ExternalReference>>,
}

#[derive(Deserialize, Serialize, Debug)]
struct ExternalReference {
    source_name: String,
    url: Option<String>
    external_id: Option<String>,
}

#[derive(Serialize, Deserialize, Debug)]
struct StixBundle {
    objects: Vec<StixObject>,
}

use std::fs;
use serde_json::{ Value, web_json };
use rayon::prelude::*;

#[derive(Serialize, Deserialize, Debug)]
fn process_stix_bundle(stix_data: &StixBundle) -> Result<()serde_json::JSON, Error> {
    stix_data.par_iter().for_each(|obj| {
        serde_json::to_string(&obj).unwrap();
    })

}


struct ECSFormat {
    

}

#[derive(Serialize, Deserialize, Debug)]
fn merge_for_navigator(veris_data: String, atlas_data )
        -> Result<(), Error> {
            
        }
fn load_stix_bundle(file_name: &str) -> Result<StixBundle, Box<dyn, std::error::Error>> {
    let data = fs.read_to_string(file_name)?;
    let bundle: StixBundle = serde_jon::from_str(&data)?;
    Ok(bundle), Error(err)

}

fn main() {
    println!("Hello, world!");
}
