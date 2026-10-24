import psutil


class ProcessManager:
    def get_processes(self) -> list[dict]:
        processes = []

        for proc in psutil.process_iter(
            ["pid", "name", "memory_info", "cpu_percent"]
        ):
            try:
                processes.append(
                    {
                        "pid": proc.info["pid"],
                        "name": proc.info["name"],
                        "cpu": proc.info["cpu_percent"],
                        "ram": round(
                            proc.info["memory_info"].rss / 1024 / 1024,
                            2
                        ),
                    }
                )

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess,
            ):
                continue

        return sorted(
            processes,
            key=lambda p: p["cpu"],
            reverse=True
        )

    def kill_process(self, pid: int) -> bool:
        try:
            process = psutil.Process(pid)
            process.terminate()
            return True

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess,
        ):
            return False