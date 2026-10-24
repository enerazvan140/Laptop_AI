from core.models.issue import Issue


class DiskDiagnostic:

    def analyze(self, snapshot):
        issues = []

        if snapshot.disk >= 95:
            issues.append(
                Issue(
                    code="CRITICAL_DISK",
                    title="Spațiu pe disc critic",
                    description="Discul este aproape plin.",
                    severity="critical"
                )
            )

        elif snapshot.disk >= 85:
            issues.append(
                Issue(
                    code="LOW_DISK_SPACE",
                    title="Spațiu redus pe disc",
                    description="Spațiul disponibil pe disc începe să fie limitat.",
                    severity="medium"
                )
            )

        return issues