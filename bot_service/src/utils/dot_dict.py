from typing import Any

class DotDict(dict):
    def __getattr__(self, name):
        if name in self:
            value = self[name]
            if isinstance(value, dict):
                return DotDict(value)
            return value
        return None