from PySide6.QtWidgets import QWidget


class ProcessPage(QWidget):
    def __init__(self, ai):
        super().__init__()
        self.ai = ai