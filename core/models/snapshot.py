from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Snapshot:
    cpu: float = 0.0
    ram: float = 0.0
    disk: float = 0.0

    battery: dict = field(default_factory=dict)
    network: dict = field(default_factory=dict)

    timestamp: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        return {
            "cpu": self.cpu,
            "ram": self.ram,
            "disk": self.disk,
            "battery": self.battery,
            "network": self.network,
            "timestamp": self.timestamp.isoformat()
        }