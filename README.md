# Distributed_Systems_Cluster_Simulation_Framework

## Project Overview  
This project is a part of our 6th sem CC(cloud computing) course curriculum and this project aims to develop a lightweight, simulation-based system that mimics core Kubernetes cluster management functionalities. It creates a simplified yet comprehensive platform for showcasing key distributed computing concepts such as resource allocation, fault tolerance, and system recovery.

## Problem Statement  
Design and implement a distributed systems simulation framework featuring:  
- **API Server**: A centralized control unit for node management, pod scheduling, and health monitoring.  
- **Cluster Nodes**: Virtualized computing units that periodically send heartbeat signals to the API Server.  
- **Pods**: Deployable units simulated on nodes, which require specific CPU resources.

## Objectives  
1. Implement a **Node Manager** for tracking and managing nodes.  
2. Develop a **Pod Scheduler** to allocate resources efficiently.  
3. Create a **Health Monitor** for detecting node failures and initiating recovery actions.  
4. Provide a **CLI/Web Interface** for cluster operations.

## Key Deliverables  
1. Node addition process and cluster management.  
2. Efficient pod scheduling across nodes.  
3. Node health monitoring and recovery during failures.  
4. Node health status listing via CLI/Web Interface.

## Technology Stack  
- **Docker**: For simulating nodes.  
- **Flask or Node.js**: For implementing the API Server.  
- **Scheduling Algorithms**: First-Fit, Best-Fit, Worst-Fit for pod scheduling.

## Architecture Diagram

![WhatsApp Image 2025-04-16 at 16 20 15_75610a9e](https://github.com/user-attachments/assets/aff48c32-f048-44ee-a091-529e7479a9e3)


## Team Members:  
- Soumya Ranjan Mishra (PES2UG22CS571)  
- Suhas Karamalaputti (PES2UG22CS590)  
- Shuklav Reddy (PES2UG22CS557)  
- Soham Praveen Salunke (PES2UG22CS565)
- S K Hitha Sree (PES2UG22CS559)


## Individual Contribution

- Soham:- node_sim.py

- Suhas:- /heartbeat

- Soumya:- /add_node

- Shuklav:-/nodes, documentation

- Hitha:- /launch_pod


