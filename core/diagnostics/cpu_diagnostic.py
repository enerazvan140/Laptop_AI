from core.models.issue import Issue


class CpuDiagnostic:

    def analyze(self, snapshot):
        issues = []

        if snapshot.cpu >= 95:
            issues.append(
                Issue(
                    code="CRITICAL_CPU",
                    title="CPU critic",
                    description="Utilizarea procesorului depășește 95%.",
                    severity="critical"
                )
            )

        elif snapshot.cpu >= 85:
            issues.append(
                Issue(
                    code="HIGH_CPU",
                    title="CPU ridicat",
                    description="Utilizarea procesorului este foarte mare.",
                    severity="high"
                )
            )

        return issues