from fastapi import FastAPI, HTTPException, BackgroundTasks  # Import BackgroundTasks
from pydantic import BaseModel
import subprocess
import uuid
import os
from .node_manager import NodeManager

app = FastAPI()
node_manager = NodeManager()

class NodeCreateRequest(BaseModel):
    cpu_cores: int

class HeartbeatRequest(BaseModel):
    node_id: str

class PodRequest(BaseModel):
    cpu_required: int

@app.post("/add_node")
def add_node(request: NodeCreateRequest):
    node_id = str(uuid.uuid4())
    success = node_manager.register_node(node_id, request.cpu_cores)
    if not success:
        raise HTTPException(status_code=400, detail="Node already exists")

    subprocess.Popen(["docker", "run", "--rm", "-d",
                      "--name", f"node_{node_id}",
                      "-e", f"NODE_ID={node_id}",
                      "-e", f"API_URL=http://host.docker.internal:8000",
                      "kube-node"])
    return {"message": "Node added", "node_id": node_id}

@app.post("/heartbeat")
def heartbeat(request: HeartbeatRequest):
    if node_manager.heartbeat(request.node_id):
        print(f"[Heartbeat] Node {request.node_id} is alive.")
        return {"message": "Heartbeat received"}
    raise HTTPException(status_code=404, detail="Node not found")

@app.get("/nodes")
def list_nodes(background_tasks: BackgroundTasks):  # Add BackgroundTasks parameter
    background_tasks.add_task(node_manager.check_health)  # Run health check in the background
    return node_manager.list_nodes()

@app.post("/launch_pod")
def launch_pod(request: PodRequest):
    result = node_manager.assign_pod(request.cpu_required)
    if result:
        return {"message": "Pod launched", **result}
    raise HTTPException(status_code=503, detail="No available node")
