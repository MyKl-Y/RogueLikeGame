from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import color
from components.base_component import BaseComponent
from equipment_types import EquipmentType
from components.equippable import HandType

if TYPE_CHECKING:
    from entity import Actor, Item


class Equipment(BaseComponent):
    parent: Actor

    def __init__(
        self,
        weapon: Optional[Item] = None,
        armor: Optional[Item] = None,
        shield: Optional[Item] = None,
        accessory: Optional[Item] = None,
    ):
        self.weapon = weapon
        self.armor = armor
        self.shield = shield
        self.accessory = accessory

    @property
    def defense_bonus(self) -> int:
        bonus = 0

        if self.weapon is not None and self.weapon.equippable is not None:
            bonus += self.weapon.equippable.defense_bonus

        if self.armor is not None and self.armor.equippable is not None:
            bonus += self.armor.equippable.defense_bonus

        if self.shield is not None and self.shield.equippable is not None:
            bonus += self.shield.equippable.defense_bonus

        return bonus

    @property
    def power_bonus(self) -> int:
        bonus = 0

        if self.weapon is not None and self.weapon.equippable is not None:
            bonus += self.weapon.equippable.power_bonus

        if self.armor is not None and self.armor.equippable is not None:
            bonus += self.armor.equippable.power_bonus

        if self.shield is not None and self.shield.equippable is not None:
            bonus += self.shield.equippable.power_bonus

        return bonus

    def item_is_equipped(self, item: Item) -> bool:
        return self.weapon == item or self.armor == item or self.shield == item
    
    def unequip_message(self, item_name: str) -> None:
        self.parent.gamemap.engine.message_log.add_message(
            f"You remove the {item_name}."
        )

    def equip_message(self, item_name: str) -> None:
        self.parent.gamemap.engine.message_log.add_message(
            f"You equip the {item_name}."
        )

    def equip_to_slot(self, slot: str, item: Item, add_message: bool) -> None:
        current_item = getattr(self, slot)

        if current_item is not None:
            self.unequip_from_slot(slot, add_message)

        setattr(self, slot, item)

        if add_message:
            self.equip_message(item.name)

    def unequip_from_slot(self, slot: str, add_message: bool) -> None:
        current_item = getattr(self, slot)

        if add_message:
            self.unequip_message(current_item.name)

        setattr(self, slot, None)

    def toggle_equip(self, equippable_item: Item, add_message: bool = True) -> None:
        """ OLD LOGIC (Without Shields and Accessories)
        if (
            equippable_item.equippable
            and equippable_item.equippable.equipment_type == EquipmentType.WEAPON
        ):
            slot = "weapon"
        else:
            slot = "armor"
        """
        if equippable_item.equippable:
            if equippable_item.equippable.equipment_type == EquipmentType.WEAPON:
                slot = "weapon"
                if self.shield and self.shield.equippable.hand_type == HandType.TWO_HANDED:
                    if add_message:
                        self.parent.gamemap.engine.message_log.add_message(
                            f"You cannot equip a weapon while wielding a two-handed shield.",
                            color.error
                        )
                    return
                elif self.shield and equippable_item.equippable.hand_type == HandType.TWO_HANDED:
                    if add_message:
                        self.parent.gamemap.engine.message_log.add_message(
                            f"You cannot equip a two-handed weapon while wielding a shield.",
                            color.error
                        )
                    return
            elif equippable_item.equippable.equipment_type == EquipmentType.ARMOR:
                slot = "armor"
            elif equippable_item.equippable.equipment_type == EquipmentType.SHIELD:
                slot = "shield"
                if self.weapon and self.weapon.equippable.hand_type == HandType.TWO_HANDED:
                    if add_message:
                        self.parent.gamemap.engine.message_log.add_message(
                            f"You cannot equip a shield while wielding a two-handed weapon.",
                            color.error
                        )
                    return
                elif self.weapon and equippable_item.equippable.hand_type == HandType.TWO_HANDED:
                    if add_message:
                        self.parent.gamemap.engine.message_log.add_message(
                            f"You cannot equip a two-handed shield while wielding a weapon.",
                            color.error
                        )
                    return
            else:
                slot = "accessory"

        if getattr(self, slot) == equippable_item:
            self.unequip_from_slot(slot, add_message)
        else:
            self.equip_to_slot(slot, equippable_item, add_message)