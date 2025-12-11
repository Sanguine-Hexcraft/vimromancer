from textual.widget import Widget
from textual.reactive import reactive
import json
import os

class SpellList(Widget):
    spells = reactive([])

    def on_mount(self):
        # Load spells from JSON
        path = os.path.join("data", "spells.json")
        with open(path, "r") as f:
            self.spells = json.load(f)

    def render(self):
        if not self.spells:
            return "No spells loaded"

        lines = []
        for i, spell in enumerate(self.spells):
            line = f"[{i + 1}] {spell["name"]}"
            lines.append(line)

        return "\n".join(lines)
