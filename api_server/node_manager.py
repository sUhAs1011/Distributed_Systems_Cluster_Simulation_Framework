from datetime import datetime, timedelta

class NodeManager:
    def __init__(self):
        self.nodes = {}  # node_id: {cpu_cores, available_cores, status, last_heartbeat, pod_ids}

    def register_node(self, node_id, cpu_cores):
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = {
            "cpu_cores": cpu_cores,
            "available_cores": cpu_cores,
            "status": "healthy",  # initial status is healthy
            "last_heartbeat": datetime.utcnow(),
            "pod_ids": []
        }
        return True

    def heartbeat(self, node_id):
        if node_id in self.nodes:
            self.nodes[node_id]["last_heartbeat"] = datetime.utcnow()
            self.nodes[node_id]["status"] = "healthy"
            return True
        return False

    def check_health(self):
        """
        Check health of all nodes based on their last heartbeat.
        If the node has not sent a heartbeat in the last 90 seconds, mark it as unreachable.
        """
        now = datetime.utcnow()
        for node_id, data in self.nodes.items():
            if now - data["last_heartbeat"] > timedelta(seconds=90):
                data["status"] = "unreachable"  # mark node as unreachable if heartbeat timeout
                print(f"[Health Monitor] Node {node_id} marked as unreachable.")

    def assign_pod(self, cpu_required):
        for node_id, data in self.nodes.items():
            if data["status"] == "healthy" and data["available_cores"] >= cpu_required:
                data["available_cores"] -= cpu_required
                pod_id = f"pod-{len(data['pod_ids']) + 1}"
                data["pod_ids"].append(pod_id)
                return {"node_id": node_id, "pod_id": pod_id}
        return None


    def list_nodes(self):
        return self.nodes
