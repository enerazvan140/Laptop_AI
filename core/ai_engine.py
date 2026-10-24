from core.monitor.system_monitor import SystemMonitor


class AIEngine:
    def __init__(self):
        self.monitor = SystemMonitor()

    def get_snapshot(self):
        return self.monitor.get_snapshot()