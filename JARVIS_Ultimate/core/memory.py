import json
from config import MEMORY_FILE

class Memory:
    def __init__(self):
        self.data = {}
        self.load()

    def load(self):
        try:
            if MEMORY_FILE.exists():
                self.data = json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
        except Exception:
            self.data = {}

    def save(self):
        MEMORY_FILE.write_text(json.dumps(self.data, indent=2, ensure_ascii=False), encoding="utf-8")

    def set(self, key, value):
        self.data[key] = value
        self.save()

    def get(self, key, default=None):
        return self.data.get(key, default)

    def forget(self, key):
        self.data.pop(key, None)
        self.save()

    def summary(self):
        return dict(self.data)
