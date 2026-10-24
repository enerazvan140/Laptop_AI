import psutil


class BatteryMonitor:

    @staticmethod
    def get_battery():
        battery = psutil.sensors_battery()

        if battery is None:
            return {
                "available": False,
                "percent": 0,
                "plugged": False,
                "seconds_left": None,
            }

        return {
            "available": True,
            "percent": int(battery.percent),
            "plugged": battery.power_plugged,
            "seconds_left": battery.secsleft,
        }

    @classmethod
    def get_status(cls):
        battery = cls.get_battery()

        if not battery["available"]:
            return "Baterie nedetectată"

        if battery["plugged"]:
            return "La încărcat"

        if battery["percent"] <= 15:
            return "Nivel critic"

        if battery["percent"] <= 30:
            return "Nivel scăzut"

        return "Normal"
