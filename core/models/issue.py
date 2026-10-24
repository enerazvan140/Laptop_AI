from dataclasses import dataclass


@dataclass
class Issue:
    code: str
    title: str
    description: str
    severity: str = "low"

    def to_dict(self) -> dict:
        return {
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "severity": self.severity
        }
