from core.models.issue import Issue


class BatteryDiagnostic:

    def analyze(self, snapshot):
        issues = []

        battery = snapshot.battery

        if not battery.get("available", False):
            return issues

        percent = battery.get("percent", 0)
        plugged = battery.get("plugged", False)

        if percent <= 10 and not plugged:
            issues.append(
                Issue(
                    code="LOW_BATTERY",
                    title="Baterie scăzută",
                    description="Nivelul bateriei este sub 10%.",
                    severity="critical"
                )
            )

        return issues