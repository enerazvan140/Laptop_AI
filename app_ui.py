from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTabWidget
)

from core.ai_engine import AIEngine

# Pagini UI
from ui.dashboard import DashboardPage
from ui.assistant_page import AssistantPage
from ui.monitor_page import MonitorPage
from ui.process_page import ProcessPage
from ui.optimizer_page import OptimizerPage
from ui.settings_page import SettingsPage


class LaptopAI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Laptop AI")
        self.resize(1200, 800)

        # Creierul aplicației
        self.ai = AIEngine()

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        title = QLabel("Laptop AI")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            padding: 10px;
        """)

        layout.addWidget(title)

        self.tabs = QTabWidget()

        # Pagini
        self.dashboard_page = DashboardPage(self.ai)
        self.assistant_page = AssistantPage(self.ai)
        self.monitor_page = MonitorPage(self.ai)
        self.process_page = ProcessPage(self.ai)
        self.optimizer_page = OptimizerPage(self.ai)
        self.settings_page = SettingsPage(self.ai)

        self.tabs.addTab(self.dashboard_page, "Dashboard")
        self.tabs.addTab(self.assistant_page, "Assistant")
        self.tabs.addTab(self.monitor_page, "Monitor")
        self.tabs.addTab(self.process_page, "Processes")
        self.tabs.addTab(self.optimizer_page, "Optimizer")
        self.tabs.addTab(self.settings_page, "Settings")

        layout.addWidget(self.tabs)