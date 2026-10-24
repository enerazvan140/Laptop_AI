from core.models.issue import Issue


class RamDiagnostic:

    def analyze(self, snapshot):
        issues = []

        if snapshot.ram >= 95:
            issues.append(
                Issue(
                    code="CRITICAL_RAM",
                    title="RAM critic",
                    description="Memoria RAM este aproape complet folosită.",
                    severity="critical"
                )
            )

        elif snapshot.ram >= 85:
            issues.append(
                Issue(
                    code="HIGH_RAM",
                    title="Consum RAM ridicat",
                    description="Utilizarea RAM este ridicată.",
                    severity="high"
                )
            )

        return issues