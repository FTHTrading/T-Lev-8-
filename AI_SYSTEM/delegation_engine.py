#!/usr/bin/env python3
"""
TROPTIONS Delegation Engine — Sub-Agent Manager
Manages sub-agents, tasks, and execution queues
"""
import os, json, time, uuid
from datetime import datetime
from pathlib import Path

class DelegationEngine:
    def __init__(self):
        self.agents_dir = Path.home() / ".openclaw" / "agents"
        self.tasks_file = self.agents_dir / "tasks.json"
        self.agents_file = self.agents_dir / "agents.json"
        self.agents_dir.mkdir(parents=True, exist_ok=True)
        
        self.agents = self._load_agents()
        self.tasks = self._load_tasks()
    
    def _load_agents(self):
        if self.agents_file.exists():
            with open(self.agents_file) as f:
                return json.load(f)
        return {}
    
    def _load_tasks(self):
        if self.tasks_file.exists():
            with open(self.tasks_file) as f:
                return json.load(f)
        return {}
    
    def create_agent(self, name, role, capabilities):
        """Create a specialized sub-agent"""
        agent_id = str(uuid.uuid4())[:8]
        self.agents[agent_id] = {
            "id": agent_id,
            "name": name,
            "role": role,
            "capabilities": capabilities,
            "status": "idle",
            "created": datetime.now().isoformat(),
            "tasks_completed": 0
        }
        self._save()
        return agent_id
    
    def delegate_task(self, agent_id, task_type, params):
        """Delegate task to sub-agent"""
        task_id = str(uuid.uuid4())[:8]
        self.tasks[task_id] = {
            "id": task_id,
            "agent_id": agent_id,
            "type": task_type,
            "params": params,
            "status": "pending",
            "created": datetime.now().isoformat(),
            "completed": None,
            "result": None
        }
        self._save()
        return task_id
    
    def get_status(self):
        """Global status of all agents and tasks"""
        return {
            "agents": len(self.agents),
            "active_agents": sum(1 for a in self.agents.values() if a["status"] == "active"),
            "total_tasks": len(self.tasks),
            "pending": sum(1 for t in self.tasks.values() if t["status"] == "pending"),
            "completed": sum(1 for t in self.tasks.values() if t["status"] == "completed"),
            "failed": sum(1 for t in self.tasks.values() if t["status"] == "failed")
        }
    
    def _save(self):
        with open(self.agents_file, 'w') as f:
            json.dump(self.agents, f, indent=2)
        with open(self.tasks_file, 'w') as f:
            json.dump(self.tasks, f, indent=2)

if __name__ == "__main__":
    engine = DelegationEngine()
    print("Delegation Engine ready.")
