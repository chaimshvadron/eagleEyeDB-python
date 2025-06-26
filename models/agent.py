from dataclasses import dataclass
@dataclass
class Agent:
    code_name: str
    real_name: str
    location: str
    status: str
    missions_completed: int
    id: int = None
    
    def __str__(self):
        return f"Agent {self.code_name} ({self.real_name}) - Location: {self.location}, Status: {self.status}, Missions Completed: {self.missions_completed}"