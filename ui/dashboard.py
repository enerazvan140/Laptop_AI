from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer


class DashboardPage(QWidget):
    def __init__(self, ai):
        super().__init__()

        self.ai = ai

        layout = QVBoxLayout(self)

        self.cpu_label = QLabel("CPU: --%")
        self.ram_label = QLabel("RAM: --%")
        self.disk_label = QLabel("DISK: --%")
        self.battery_label = QLabel("BATTERY: --%")

        for label in (
            self.cpu_label,
            self.ram_label,
            self.disk_label,
            self.battery_label,
        ):
            label.setStyleSheet(
                """
                font-size:18px;
                padding:8px;
                """
            )
            layout.addWidget(label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

        self.update_stats()

    def update_stats(self):
        snapshot = self.ai.get_snapshot()

        self.cpu_label.setText(f"CPU: {snapshot.cpu:.1f}%")
        self.ram_label.setText(f"RAM: {snapshot.ram:.1f}%")
        self.disk_label.setText(f"DISK: {snapshot.disk:.1f}%")

        battery_percent = snapshot.battery.get("percent", "N/A")

        self.battery_label.setText(
            f"BATTERY: {battery_percent}%"
        )