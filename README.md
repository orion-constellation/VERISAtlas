# VERISAtlas
## Unified Industry Threat Data Analysis  🤗 🦾⚔️ 🤗

![Version](https://img.shields.io/badge/version-v0.0.1-blue)![GitHub branch status](https://img.shields.io/github/checks-status/orion-constellation/VERISAtlas/main)
![Release](https://img.shields.io/badge/release-latest-green)![CodeCoverage](https://img.shields.io/codecov/c/gh/orion-constellation/VERISAtlas/main)![Tests](https://github.com/orion-constellation/VERISAtlas/actions/workflows/ci.yml/badge.svg?branch=develop)


## Objective

VERISAtlas aims to add to Orion by unifying the VERIS Incident Framework and the MITRE ATT&CK frameworks within a graph-based data structure. The project leverages these frameworks to integrate threat intelligence data, enabling the application of advanced machine learning models to identify hidden connections and predict potential cyber threats. 

************ ⚔️

VERIS Framework: The Vocabulary for Event Recording and Incident Sharing (VERIS) Framework provides a common language for describing security incidents in a structured, repeatable, and measurable manner. It is widely used for data-driven security reports and incident analysis.

MITRE Atlas: MITRE Atlas is a framework that integrates machine learning and artificial intelligence to automate and enhance threat detection, prediction, and response. It extends the MITRE ATT&CK framework by incorporating machine learning to provide more advanced and automated threat intelligence.

MITRE ATT&CK: MITRE ATT&CK is a globally recognized knowledge base of adversary tactics and techniques based on real-world observations. It provides a framework for threat modeling and helps organizations understand the behaviors and methods used by attackers.

Memgraph: Memgraph is an in-memory graph database designed for high-performance graph analytics. It enables real-time data processing and is optimized for analyzing the relationships between different data points, making it ideal for applications like threat intelligence where understanding these relationships is crucial.

************* ⚔️

With our focus on adversarial AI and the growing need for advanced threat intelligence, VERISAtlas integrates and expands upon MITRE Atlas to address these challenges.

************* ⚔️

Features:
**Data Ingestion:** Seamless ingestion of data from both the VERIS and MITRE ATT&CK frameworks, implemented in Python.
**Data Processing:** Parsing and processing of the data for integration with the Elastic Common Schema (ECS), ensuring compatibility with Elasticsearch.

**Graph Database Storage:** Storing processed data in a graph database, with Memgraph chosen for its performance and ability to handle complex relationship queries.

### 🔥🦀 Use of Mojo & Rust 🦀🔥 
As part of the roadmap, there is a planned migration from Python to higher-performance languages and frameworks, including Mojo and Rust.

### Potential Features:

**Metadata Association:** Enriching incidents with metadata to create a semantic knowledge graph, providing deeper insights into the relationships and patterns within the data.
Roadmap:

**Vector Storage:** Implementing vector-based storage to enable high-dimensional similarity searches.

**Real-Time Streaming:** Integrating close to real-time data streaming to track and analyze the multiple stages of an attack.
Language Optimization: Transitioning components to faster languages to ensure efficient data modeling within a knowledge graph that includes metadata.

**Incident Clustering:** Using traditional machine learning techniques to cluster similar incidents and metadata, facilitating pattern recognition and threat detection.

**LLM Analysis:** Incorporating large language model (LLM) analysis across aggregated data to identify correlations and anomalies.

**Correlation Analysis:** Identifying correlations between different events through incident association.

**Probability and Statistical Analysis:** Combining attack vector probabilities with statistical event analysis to provide a clearer understanding of ongoing threats.

**Self-Supervised Learning:** Developing self-supervised learning techniques and weak labeling of events to maintain up-to-date and robust data across both frameworks (TBD).
HMoE Model Integration: Applying the ClfGraph Gated system, which uses a classifier-gated Hierarchical Mixture of Experts (HMoE) model, to enhance the system's ability to identify and respond to emerging threats.

***Custom Attention Operations:*** Implementing specialized attention mechanisms to improve model efficiency and accuracy.

***SIMD Optimization:*** Utilizing SIMD (Single Instruction, Multiple Data) in Rust for optimized matrix multiplication, which is critical in various machine learning tasks.
Rust-Based Memgraph Client: Developing a Memgraph client in Rust to improve the performance and reliability of data operations.