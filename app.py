from textual.app import App
from textual.widgets import Header, Footer
from textual.containers import Horizontal
from widgets.spell_list import SpellList
from widgets.spell_detail import SpellDetail

class SpellbookApp(App):
    CSS_PATH = "styles/green_spellbook.css"

    def compose(self):
        yield Header()
        yield Horizontal(
            SpellList(),
            SpellDetail()
        )
        yield Footer()

if __name__ == "__main__":
    SpellbookApp().run()

