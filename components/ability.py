from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import actions
from actions import Action
import color
import components.ai
import components.inventory
from components.base_component import BaseComponent
from entity import Actor
from exceptions import Impossible
from input_handlers import (
    ActionOrHandler,
    AreaRangedAttackHandler,
    SingleRangedAttackHandler
)

if TYPE_CHECKING:
    from entity import Actor, Item


class Ability(BaseComponent):
    parent: Item

    def __init__(self, cooldown_turns: int):
        self.cooldown_turns = cooldown_turns
        self.current_cooldown = 0

    def get_action(self, consumer: Actor) -> Optional[ActionOrHandler]:
        return actions.ItemAction(consumer, self.parent)
    
    def activate(self, action: actions.ItemAction) -> None:
        raise NotImplementedError()
    
    def cooldown(self) -> None:
        """Reduce cooldown by 1 turn."""
        if self.current_cooldown > 0:
            self.current_cooldown -= 1


class ConfusionAbility(Ability):
    def __init__(self, number_of_turns: int, cooldown_turns: int):
        super().__init__(cooldown_turns)
        self.number_of_turns = number_of_turns

    def get_action(self, consumer: Actor) -> SingleRangedAttackHandler:
        self.engine.message_log.add_message(
            "Select a target location.", color.needs_target
        )
        return SingleRangedAttackHandler(
            self.engine,
            callback=lambda xy: actions.ItemAction(consumer, self.parent, xy)
        )
    
    def activate(self, action: actions.ItemAction) -> None:
        if self.current_cooldown > 0:
            raise Impossible(f"{self.parent.name} is still cooling down. ({self.current_cooldown})")
        
        consumer = action.entity
        target = action.target_actor

        if not self.engine.game_map.visible[action.target_xy]:
            raise Impossible("You cannot target an area that you cannot see.")
        if not target:
            raise Impossible("You must select an enemy to target.")
        if target is consumer:
            raise Impossible("You cannot confuse yourself!")
        
        self.engine.message_log.add_message(
            f"The eyes of the {consumer.name} look vacant, as it starts to stumble around!",
            color.status_effect_applied,
        )
        target.ai = components.ai.ConfusedEnemy(
            entity=target, previous_ai=target.ai, turns_remaining=self.number_of_turns
        )
        self.current_cooldown = self.cooldown_turns
    
    def cooldown(self) -> None:
        if self.current_cooldown > 0:
            self.current_cooldown -= 1
            if self.current_cooldown == 0:
                self.engine.message_log.add_message(
                    f"{self.parent.name} is ready to use again.",
                    color.status_effect_applied
                )


class HealingAbility(Ability):
    def __init__(self, amount: int, cooldown_turns: int):
        super().__init__(cooldown_turns)
        self.amount = amount
    
    def activate(self, action: actions.ItemAction) -> None:
        if self.current_cooldown > 0:
            raise Impossible(f"{self.parent.name} is still cooling down.")
        
        consumer = action.entity
        amount_recovered = consumer.fighter.heal(self.amount)
        
        if amount_recovered > 0:
            self.engine.message_log.add_message(
                f"You consume the {self.parent.name}, and recover {amount_recovered} HP!",
                color.health_recovered,
            )
            self.current_cooldown = self.cooldown_turns
        else:
            raise Impossible("Your health is already full.")
    
    def cooldown(self) -> None:
        if self.current_cooldown > 0:
            self.current_cooldown -= 1
            if self.current_cooldown == 0:
                self.engine.message_log.add_message(
                    f"{self.parent.name} is ready to use again.",
                    color.status_effect_applied
                )


class FireballDamageAbility(Ability):
    def __init__(self, damage: int, radius: int, cooldown_turns: int):
        super().__init__(cooldown_turns)
        self.damage = damage
        self.radius = radius
    
    def get_action(self, consumer: Actor) -> AreaRangedAttackHandler:
        self.engine.message_log.add_message(
            "Select a target location.", color.needs_target
        )
        return AreaRangedAttackHandler(
            self.engine,
            radius=self.radius,
            callback=lambda xy: actions.ItemAction(consumer, self.parent, xy)
        )
    
    def activate(self, action: actions.ItemAction) -> None:
        if self.current_cooldown > 0:
            raise Impossible(f"{self.parent.name} is still cooling down.")
        
        target_xy = action.target_xy

        if not self.engine.game_map.visible[target_xy]:
            raise Impossible("You cannot target an area that you cannot see.")
        
        target_hit = False
        for actor in self.engine.game_map.actors:
            if actor.distance(*target_xy) <= self.radius:
                self.engine.message_log.add_message(
                    f"The {actor.name} is engulfed in a fiery explosion, taking {self.damage} damage!",
                    color.player_atk
                )
                actor.fighter.take_damage(self.damage)
                target_hit = True
        
        if not target_hit:
            raise Impossible("There are no targets in the radius.")
        self.current_cooldown = self.cooldown_turns
    
    def cooldown(self) -> None:
        if self.current_cooldown > 0:
            self.current_cooldown -= 1
            if self.current_cooldown == 0:
                self.engine.message_log.add_message(
                    f"{self.parent.name} is ready to use again.",
                    color.status_effect_applied
                )


class LightningDamageAbility(Ability):
    def __init__(self, damage: int, maximum_range: int, cooldown_turns: int):
        super().__init__(cooldown_turns)
        self.damage = damage
        self.maximum_range = maximum_range

    def activate(self, action: actions.ItemAction) -> None:
        if self.current_cooldown > 0:
            raise Impossible(f"{self.parent.name} is still cooling down.")
        
        consumer = action.entity
        target = None
        closest_distance = self.maximum_range + 1.0

        for actor in self.engine.game_map.actors:
            if actor is not consumer and self.parent.gamemap.visible[actor.x, actor.y]:
                distance = consumer.distance(actor.x, actor.y)

                if distance < closest_distance:
                    target = actor
                    closest_distance = distance
        if target:
            self.engine.message_log.add_message(
                f"A lighting bolt strikes the {target.name} with a loud thunder, for {self.damage} damage!",
                color.player_atk
            )
            target.fighter.take_damage(self.damage)
            self.current_cooldown = self.cooldown_turns
    
    def cooldown(self) -> None:
        if self.current_cooldown > 0:
            self.current_cooldown -= 1
            if self.current_cooldown == 0:
                self.engine.message_log.add_message(
                    f"{self.parent.name} is ready to use again.",
                    color.status_effect_applied
                )