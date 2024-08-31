# VERISAtlas
## Unified Industry Threat Data Analysis  🤗 🦾⚔️ 🤗

![Version](https://img.shields.io/badge/version-v0.0.1-blue)![Release](https://img.shields.io/badge/release-latest-green)![CodeCoverage](https://img.shields.io/codecov/c/gh/orion-constellation/VERISAtlas/main)![Tests](https://github.com/orion-constellation/veris-atlas/actions/workflows/ci.yml/badge.svg?branch=develop)[Tests](https://github.com/orion-constellation/veris-atlas/actions/workflows/ci.yml/badge.svg?branch=main)


## Objective 

A complete mapping between the VERIS Incident Framework and the MITRE ATT&CK frameworks. Stored in graph data structures and within graph databases. A project to unify the data
and then leverage the novel LLM's to find hidden connections and hypothesize new attacks or recognize them on the fly as a component of the Orion Threat Intelligence application.

************ ⚔️

**VERIS Framework:** {description two sentences}

**MITRE Atlas:** {description, 2 sentences}

not implemented but compatible with the original MITRE ATT&CK framework

**MITRE ATT&CK:** {description, two sentences}

**Memgraph:** In memory graph storage which emphasises the relationship between key data rather than the data in isolation.

************* ⚔️

 ***With our interest in adversarial AI and the growing need for threat intelligence focusing on MITRE Atlas***

************* ⚔️

## Features:

1. Ingestion of data from both frameworks (Implemented in Python)
2. Parsing and processing the data for the ECS framework (ElasticSearch is again Open Source Software)
3. Storage in a Graph Database (Chose Memgraph for its performance but it is up to the developer and business)
4. Association of metadata with attacks to create a rich semantic knowledge graph.

## Roadmap:

0. Storage in Vector format for higher dimensionally encoded similarity.
1. Implement close to real time streaming data in order to track events and optimize for finding the multiple stages of an attack.
   1. Requires moving componenets to faster languages but solving how to model the data in a Knowledge Graph including metadata is critical first step
2. Cluster similar incidents and the metadata using traditional machine learning techniques.
3. Incorporate LLM Analysis across the aggregation.
4. Find the correlations between different events through the incident association.
   1. Knowing the probability that one attack vector is presen, and then combining that with the statistical analysis of events will offer a clearer picture of an unfolding event
5. Self Supervized Learning and weak labelling of events as they enter in order to create robust, up to date data for both frameworks (TBD)
6. Apply the in research ClfGraph Gated system using a classifier gated, Hiearachal Mixture of Experts model.

## Use of Mojo & Rust 🦀🔥

On the roadmap is a migration from Python to a more high performance language and framework.

**Some Potential Features:**
1. Custom Attention Op
2. Matrix Multiplication SIMD
3. Memgraph Client and operations in Rust



### Research Goal

- Create a shared representation layer for applied and specific training of classifiers and other neural networks of traditional Machine Learning Models.
- Link to the HMoE structure of ClfGraph
  - A classifier gated mixture of GNN's
  - No dtermination on the effectiveness as yet

### Hiearachal Mixture of Experts (HMoE) Model

Research and Development of Composite Architecture enhanced by custom SIMD
and Operations for expanding knowledge of structuring MITRE Attack as Graphs
as well as subsampling using GNNs.

This is purely a fun exploration and learning activity both in the space of GNN's

**It can also serve as a WandB logging sklearn template on it's own by extracting the sklearn_baseline**


ClfGraph is a research project focused on developing a model architecture that leverages MITRE data to create a shared representation layer, coupled with a classifier to gate a Hierarchical Mixture of Experts (HMoE) GCN and GAT models. The aim is to periodically build fingerprints of the information using graphs. The project integrates various components and uses Weights and Biases for experiment tracking.



## How to Contribute

We welcome contributions to ClfGraph! Whether you're interested in refining the model architecture, enhancing the front-end, or improving database interactions, your input is valuable.

### Steps to Contribute:

1. Fork the repository.
2. Clone your fork locally.
3. Create a new branch for your feature or bugfix.
4. Submit a pull request with a clear description of your changes.

Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for detailed guidelines.

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for more details.

Happy coding! 😊