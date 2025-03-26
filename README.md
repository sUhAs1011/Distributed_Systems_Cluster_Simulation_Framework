# Distributed_Systems_Cluster_Simulation_Framework

## Project Overview  
This project aims to develop a lightweight, simulation-based system that mimics core Kubernetes cluster management functionalities. It creates a simplified yet comprehensive platform for showcasing key distributed computing concepts such as resource allocation, fault tolerance, and system recovery.

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
