"""Optional LiDAR integration (disabled by default)."""
class Lidar:
    def __init__(self, port="/dev/ttyUSB0", enabled=False):
        self.enabled = enabled
        self.port = port
        if enabled:
            # TODO: integrate rplidar-roboticia / ydlidar SDK
            raise NotImplementedError("LiDAR support stub - add SDK here.")

    def distance_ahead(self):
        return None
