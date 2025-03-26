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

## Key Deliverables  
1. Node addition process and cluster management.  
2. Efficient pod scheduling across nodes.  
3. Node health monitoring and recovery during failures.  
4. Node health status listing via CLI/Web Interface.

## Technology Stack  
- **Docker**: For simulating nodes.  
- **Flask or Node.js**: For implementing the API Server.  
- **Scheduling Algorithms**: First-Fit, Best-Fit, Worst-Fit for pod scheduling.  
