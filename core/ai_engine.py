from core.monitor.system_monitor import SystemMonitor
from core.diagnostics.diagnostic_engine import DiagnosticEngine


class AIEngine:

    def __init__(self):
        self.monitor = SystemMonitor()
        self.diagnostics = DiagnosticEngine()

    def get_snapshot(self):
        return self.monitor.get_snapshot()

    def get_issues(self):
        snapshot = self.get_snapshot()

        return self.diagnostics.analyze(snapshot)