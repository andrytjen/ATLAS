from rich.progress import Progress

class AtlasProgress:
    def __enter__(self):
        self.progress = Progress()
        self.progress.start()
        return self.progress

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.progress.stop()
