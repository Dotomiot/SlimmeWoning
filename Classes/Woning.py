from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Smarthub import Smarthub
    from .Kamer import Kamer

class Woning():
    def __init__(self,naam="Huis"):
        self.naam = naam

        self.kamers: list[Kamer] = []
        self.smarthub: Smarthub

    def voeg_kamer_toe(self, kamer: Kamer):
        self.kamers.append(kamer)

    def voeg_smarthub_toe(self, hub: Smarthub):
        self.smarthub = hub
