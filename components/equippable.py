from __future__ import annotations

from typing import TYPE_CHECKING
from enum import Enum, auto

from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
    from entity import Item


class HandType(Enum):
    ONE_HANDED = auto()
    TWO_HANDED = auto()


class Equippable(BaseComponent):
    parent: Item

    def __init__(
        self,
        equipment_type: EquipmentType,
        hand_type: HandType = HandType.ONE_HANDED,
        power_bonus: int = 0,
        defense_bonus: int = 0,
    ):
        self.equipment_type = equipment_type
        self.hand_type = hand_type
        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus


# Weapons
class Fists(Equippable):
    def __init__(
            self,
            hand_type: HandType = HandType.TWO_HANDED,
            power_bonus: int = 1,
            defense_bonus: int = 0,
        ):
        super().__init__(
            equipment_type=EquipmentType.WEAPON,
            hand_type=hand_type,
            power_bonus=power_bonus,
            defense_bonus=defense_bonus,
        )

class Dagger(Equippable):
    def __init__(
            self,
            hand_type: HandType = HandType.ONE_HANDED,
            power_bonus: int = 2,
            defense_bonus: int = 0,
        ):
        super().__init__(
            equipment_type=EquipmentType.WEAPON,
            hand_type=hand_type,
            power_bonus=power_bonus,
            defense_bonus=defense_bonus,
        )

class Sword(Equippable):
    def __init__(
            self,
            hand_type: HandType = HandType.ONE_HANDED,
            power_bonus: int = 3,
            defense_bonus: int = 0,
        ):
        super().__init__(
            equipment_type=EquipmentType.WEAPON,
            hand_type=hand_type,
            power_bonus=power_bonus,
            defense_bonus=defense_bonus,
        )

class Staff(Equippable):
    def __init__(
            self,
            hand_type: HandType = HandType.TWO_HANDED,
            power_bonus: int = 3,
            defense_bonus: int = 1,
        ):
        super().__init__(
            equipment_type=EquipmentType.WEAPON,
            hand_type=hand_type,
            power_bonus=power_bonus,
            defense_bonus=defense_bonus,
        )


# Shields
class Shield(Equippable):
    def __init__(
            self,
            hand_type: HandType = HandType.ONE_HANDED,
            defense_bonus: int = 1,
        ):
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            hand_type=hand_type,
            defense_bonus=defense_bonus,
        )


# Armor
class Armor(Equippable):
    def __init__(self, defense_bonus: int = 1):
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=defense_bonus)


# Accessories
# TODO: Do accessories as well as more attributes so that accessories can change more