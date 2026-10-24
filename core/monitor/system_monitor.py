import psutil
import os

from core.models.snapshot import Snapshot
from core.monitor.battery import BatteryMonitor
from core.monitor.network import NetworkMonitor


class SystemMonitor:
    def __init__(self):
        self.battery_monitor = BatteryMonitor()
        self.network_monitor = NetworkMonitor()

    def get_snapshot(self) -> Snapshot:
        return Snapshot(
            cpu=psutil.cpu_percent(interval=0.1),
            ram=psutil.virtual_memory().percent,
            disk=psutil.disk_usage(
                    os.path.abspath(os.sep)
                ).percent,
            battery=self.battery_monitor.get_battery(),
            network=(getattr(self.network_monitor, "get_network", lambda: {})() or {}),
        )