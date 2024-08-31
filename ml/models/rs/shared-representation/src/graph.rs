/// # Garph Representation of Stix 2.1 Bundle Data
/// Sources are both incident related, and TTP related
/// 

use petgraph::graph::{ DiGraph, NodeIndex };
use petgraph::dot::{ Dot, Config };
use serde::{ Deserialize, Serialize };
use serde_json::Value;
use std::prelude::*;

fn create_ttp_graph(stix_data: &StixBundle) -> DiGraph<String, String> {
    let mut graph = DiGraph::new();

    let mut node_map = std::collection::HashMap::new()
    //Add nodes (TTP's) to the graph
    for data in &stix_data.objects {
        if obj.obj_type == "attack-pattern" || obj.obj_type = "x-mitre-tactic" {
            let node = graph.add_node(obj.name.clonet().unwrap_or_default());
                    node_map.insert(&obj.id, node)


        }
    }
    //Add Relationships (Edges)
    for obj in &stix_data.objects {
        if obj.obj_type == "relationship" {
            let source_id = obj.external_references.as_ref().unwrap()
                    [0].external_id.as_ref.unwrap();
            let target_id = obj.external_references.as_ref().unwrap()
                    [1].external_id.as_ref().unwrap();

                    if let (Some(&source), Some(&target)) = 
                    (node.map.get(source_id), node_map.get(target_id)) {
                        graph.add_edge(source, target, obj.name.clone().unwrap_or("related to".into()));
                    }
                }   
            }
            graph
        }

// Visualize Graph with GraphViz        
fn visualize_graph(graph: &DiGraph<String, String>) {
    println!("{:?}", Dot::with_config(graph, &[Config::EdgeNoLabel]));
}



