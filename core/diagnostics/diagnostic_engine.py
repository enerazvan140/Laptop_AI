from core.diagnostics.cpu_diagnostic import CpuDiagnostic
from core.diagnostics.ram_diagnostic import RamDiagnostic
from core.diagnostics.disk_diagnostic import DiskDiagnostic
from core.diagnostics.battery_diagnostic import BatteryDiagnostic


class DiagnosticEngine:

    def __init__(self):
        self.cpu = CpuDiagnostic()
        self.ram = RamDiagnostic()
        self.disk = DiskDiagnostic()
        self.battery = BatteryDiagnostic()

    def analyze(self, snapshot):
        issues = []

        issues.extend(self.cpu.analyze(snapshot))
        issues.extend(self.ram.analyze(snapshot))
        issues.extend(self.disk.analyze(snapshot))
        issues.extend(self.battery.analyze(snapshot))

        return issues