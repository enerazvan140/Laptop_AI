import psutil
import socket


class NetworkMonitor:

    def get_interfaces(self):
        interfaces = []

        stats = psutil.net_if_stats()
        addresses = psutil.net_if_addrs()

        for name, info in stats.items():

            if not info.isup:
                continue

            ip = "N/A"

            for addr in addresses.get(name, []):

                if addr.family == socket.AF_INET:
                    ip = addr.address
                    break

            interfaces.append({
                "name": name,
                "ip": ip,
                "speed": info.speed
            })

        return interfaces

    def get_traffic(self):

        counters = psutil.net_io_counters()

        return {
            "download_mb": round(
                counters.bytes_recv / 1048576, 2
            ),
            "upload_mb": round(
                counters.bytes_sent / 1048576, 2
            ),
            "bytes_recv": counters.bytes_recv,
            "bytes_sent": counters.bytes_sent
        }

    def get_connection_status(self):

        return any(
            info.isup
            for info in psutil.net_if_stats().values()
        )

    def has_internet(self):

        try:
            socket.create_connection(
                ("8.8.8.8", 53),
                timeout=2
            )
            return True

        except OSError:
            return False