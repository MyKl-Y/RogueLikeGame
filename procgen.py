from __future__ import annotations

import random
from typing import Dict, Iterator, List, Tuple, TYPE_CHECKING

import tcod

import entity_factories
from game_map import GameMap
import tile_types


if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

# (floor_number, maximum_number_of_items)
max_items_by_floor = [
    (1, 2),
    (4, 3),
    (6, 4),
    (8, 5),
    (10, 6),
    (12, 7),
    (14, 8),
]

# (floor_number, maximum_number_of_monsters)
max_monsters_by_floor = [
    (1, 2),
    (4, 4),
    (6, 6),
    (8, 8),
    (10, 10),
    (12, 12),
    (14, 14),
]

# TODO: Add more items
# floor_number: [(item, weighted_chances), ...]
item_chances: Dict[int, List[Tuple[Entity, int]]] = {
    # Early Floors (1-3): Basic items and low-tier weapons/abilities
    1: [
        (entity_factories.health_potion, 35),
        (entity_factories.confusion_scroll, 10),
        (entity_factories.lightning_scroll, 10),
        (entity_factories.fireball_scroll, 5),
        (entity_factories.tonfa, 10),
        (entity_factories.dagger, 10),
        (entity_factories.nunchucks, 5),
        (entity_factories.wakizashi, 5),
    ],
    2: [
        (entity_factories.health_potion, 35),
        (entity_factories.confusion_scroll, 10),
        (entity_factories.lightning_scroll, 10),
        (entity_factories.fireball_scroll, 5),
        (entity_factories.tonfa, 10),
        (entity_factories.dagger, 10),
        (entity_factories.nunchucks, 5),
        (entity_factories.wakizashi, 5),
        (entity_factories.shuriken, 10),
    ],
    3: [
        (entity_factories.health_potion, 35),
        (entity_factories.confusion_scroll, 10),
        (entity_factories.lightning_scroll, 10),
        (entity_factories.fireball_scroll, 5),
        (entity_factories.tonfa, 10),
        (entity_factories.dagger, 10),
        (entity_factories.nunchucks, 5),
        (entity_factories.wakizashi, 5),
        (entity_factories.shuriken, 10),
        (entity_factories.kunai, 5),
        (entity_factories.buckler, 5),
        (entity_factories.leather_armor, 5)
    ],

    # Mid Floors (4-8): Transition to more powerful items and introduction of abilities
    4: [
        (entity_factories.health_potion, 20),
        (entity_factories.confusion_scroll, 5),
        (entity_factories.confusion_ability, 2),
        (entity_factories.lightning_scroll, 10),
        (entity_factories.fireball_scroll, 5),
        (entity_factories.tonfa, 0),
        (entity_factories.dagger, 0),
        (entity_factories.shuko, 5),
        (entity_factories.katana, 5),
        (entity_factories.bo, 5),
        (entity_factories.nunchucks, 10),
        (entity_factories.wakizashi, 10),
        (entity_factories.shuriken, 0),
        (entity_factories.kunai, 10),
        (entity_factories.buckler, 10),
        (entity_factories.targe, 5),
        (entity_factories.leather_armor, 10),
        (entity_factories.chain_mail, 2),
    ],
    5: [
        (entity_factories.health_potion, 20),
        (entity_factories.confusion_scroll, 0),
        (entity_factories.confusion_ability, 5),
        (entity_factories.lightning_scroll, 5),
        (entity_factories.lightning_ability, 2),
        (entity_factories.fireball_scroll, 5),
        (entity_factories.shuko, 10),
        (entity_factories.katana, 10),
        (entity_factories.bo, 10),
        (entity_factories.nunchucks, 5),
        (entity_factories.wakizashi, 5),
        (entity_factories.kunai, 5),
        (entity_factories.buckler, 5),
        (entity_factories.targe, 10),
        (entity_factories.leather_armor, 0),
        (entity_factories.chain_mail, 10),
        (entity_factories.lamellar_armor, 5),
    ],
    6: [
        (entity_factories.health_potion, 10),
        (entity_factories.confusion_ability, 10),
        (entity_factories.lightning_scroll, 0),
        (entity_factories.lightning_ability, 5),
        (entity_factories.fireball_scroll, 2),
        (entity_factories.fireball_ability, 5),
        (entity_factories.shuko, 10),
        (entity_factories.katana, 10),
        (entity_factories.bo, 10),
        (entity_factories.nunchucks, 0),
        (entity_factories.wakizashi, 0),
        (entity_factories.kunai, 0),
        (entity_factories.buckler, 0),
        (entity_factories.targe, 10),
        (entity_factories.chain_mail, 5),
        (entity_factories.lamellar_armor, 10),
        (entity_factories.tatami_do, 2),
    ],
    7: [
        (entity_factories.health_potion, 5),
        (entity_factories.healing_ability, 2),
        (entity_factories.confusion_ability, 5),
        (entity_factories.lightning_ability, 10),
        (entity_factories.fireball_ability, 5),
        (entity_factories.shuko, 5),
        (entity_factories.katana, 5),
        (entity_factories.bo, 5),
        (entity_factories.targe, 5),
        (entity_factories.nagamaki, 2),
        (entity_factories.tekko, 2),
        (entity_factories.heater_shield, 2),
        (entity_factories.chain_mail, 0),
        (entity_factories.lamellar_armor, 5),
        (entity_factories.tatami_do, 10),
        (entity_factories.o_yoroi, 2),
    ],
    8: [
        (entity_factories.health_potion, 0),
        (entity_factories.healing_ability, 10),
        (entity_factories.confusion_ability, 0),
        (entity_factories.lightning_ability, 5),
        (entity_factories.fireball_ability, 10),
        (entity_factories.shuko, 0),
        (entity_factories.katana, 0),
        (entity_factories.bo, 0),
        (entity_factories.targe, 0),
        (entity_factories.naginata, 1),
        (entity_factories.nagamaki, 5),
        (entity_factories.tekko, 5),
        (entity_factories.heater_shield, 5),
        (entity_factories.lamellar_armor, 0),
        (entity_factories.tatami_do, 5),
        (entity_factories.o_yoroi, 10),
        (entity_factories.oni_mail, 2),
        (entity_factories.star_rage, 5),
    ],

    # Later Floors (9+): High-tier items and abilities
    9: [
        (entity_factories.healing_ability, 15),
        (entity_factories.lightning_ability, 0),
        (entity_factories.fireball_ability, 5),
        (entity_factories.naginata, 5),
        (entity_factories.nagamaki, 0),
        (entity_factories.tekko, 0),
        (entity_factories.heater_shield, 0),
        (entity_factories.tower_shield, 2),
        (entity_factories.tatami_do, 0),
        (entity_factories.o_yoroi, 5),
        (entity_factories.oni_mail, 10),
        (entity_factories.star_rage, 10),
        (entity_factories.solar_flare, 5),
    ],
    10: [
        (entity_factories.healing_ability, 5),
        (entity_factories.fireball_ability, 0),
        (entity_factories.naginata, 10),
        (entity_factories.tower_shield, 5),
        (entity_factories.o_yoroi, 0),
        (entity_factories.oni_mail, 5),
        (entity_factories.star_rage, 5),
        (entity_factories.solar_flare, 10),
        (entity_factories.star_forged_mail, 2),
        (entity_factories.black_hole, 1),
    ],
    11: [
        (entity_factories.healing_ability, 0),
        (entity_factories.naginata, 5),
        (entity_factories.tower_shield, 10),
        (entity_factories.oni_mail, 0),
        (entity_factories.star_rage, 0),
        (entity_factories.solar_flare, 5),
        (entity_factories.star_forged_mail, 5),
        (entity_factories.black_hole, 5),
    ],
    12: [
        (entity_factories.naginata, 0),
        (entity_factories.tower_shield, 5),
        (entity_factories.solar_flare, 0),
        (entity_factories.star_forged_mail, 10),
        (entity_factories.black_hole, 10),
    ],
    13: [
        (entity_factories.tower_shield, 0),
        (entity_factories.star_forged_mail, 5),
        (entity_factories.black_hole, 5),
    ],
    14: [
        (entity_factories.star_forged_mail, 0),
        (entity_factories.black_hole, 0),
    ],
}

# floor_number: [(item, weighted_chances), ...]
enemy_chances: Dict[int, List[Tuple[Entity, int]]] = {
    1: [
        (entity_factories.ashigaru, 80),
        (entity_factories.ninja, 20),
    ],
    2: [
        (entity_factories.ashigaru, 70),
        (entity_factories.ninja, 30),
    ],
    3: [
        (entity_factories.ashigaru, 60),
        (entity_factories.ninja, 40),
        (entity_factories.shinobi, 10),
    ],
    4: [
        (entity_factories.ninja, 50),
        (entity_factories.shinobi, 30),
        (entity_factories.onna_bugeisha, 20),
    ],
    5: [
        (entity_factories.ninja, 40),
        (entity_factories.shinobi, 40),
        (entity_factories.onna_bugeisha, 30),
    ],
    6: [
        (entity_factories.shinobi, 40),
        (entity_factories.onna_bugeisha, 40),
        (entity_factories.samurai, 20),
    ],
    7: [
        (entity_factories.shinobi, 30),
        (entity_factories.onna_bugeisha, 30),
        (entity_factories.samurai, 30),
    ],
    8: [
        (entity_factories.onna_bugeisha, 30),
        (entity_factories.samurai, 30),
        (entity_factories.ronin, 5),
    ],
    9: [
        (entity_factories.onna_bugeisha, 20),
        (entity_factories.samurai, 20),
        (entity_factories.ronin, 10),
    ],
    10: [
        (entity_factories.samurai, 10),
        (entity_factories.ronin, 20),
        (entity_factories.sohei, 5),
    ],
    11: [
        (entity_factories.samurai, 5),
        (entity_factories.ronin, 15),
        (entity_factories.sohei, 10),
    ],
    12: [
        (entity_factories.ronin, 10),
        (entity_factories.sohei, 15),
        (entity_factories.bushi, 5),
    ],
    13: [
        (entity_factories.ronin, 5),
        (entity_factories.sohei, 10),
        (entity_factories.bushi, 10),
    ],
    14: [
        (entity_factories.sohei, 5),
        (entity_factories.bushi, 15),
    ],
}


def get_max_value_for_floor(
    weighted_chances_by_floor: List[Tuple[int, int]], floor: int
) -> int:
    current_value = 0

    for floor_minimum, value in weighted_chances_by_floor:
        if floor_minimum > floor:
            break
        else:
            current_value = value
    
    return current_value


def get_entities_at_random(
    weighted_chances_by_floor: Dict[int, List[Tuple[Entity, int]]],
    number_of_entities: int,
    floor: int,
) -> List[Entity]:
    entity_weighted_chances = {}

    for key, values in weighted_chances_by_floor.items():
        if key > floor:
            break
        else:
            for value in values:
                entity = value[0]
                weighted_chance = value[1]

                entity_weighted_chances[entity] = weighted_chance

    entities = list(entity_weighted_chances.keys())
    entity_weighted_chances_values = list(entity_weighted_chances.values())

    chosen_entities = random.choices(
        entities, weights=entity_weighted_chances_values, k=number_of_entities
    )

    return chosen_entities


class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height
    
    @property
    def center(self) -> Tuple[int, int]:
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y
    
    @property
    def inner(self) -> Tuple[slice, slice]:
        """Return the inner area of this room as a 2D array index."""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)
    
    def intersects(self, other: RectangularRoom) -> bool:
        """Return True if this room overlaps with another RectangularRoom."""
        return (
            self.x1 <= other.x2
            and self.x2 >= other.x1
            and self.y1 <= other.y2
            and self.y2 >= other.y1
        )


def place_entities(
    room: RectangularRoom, dungeon: GameMap, floor_number: int,
) -> None:
    number_of_monsters = random.randint(
        0, get_max_value_for_floor(max_monsters_by_floor, floor_number)
    )
    number_of_items = random.randint(
        0, get_max_value_for_floor(max_items_by_floor, floor_number)
    )

    monsters: List[Entity] = get_entities_at_random(
        enemy_chances, number_of_monsters, floor_number
    )
    items: List[Entity] = get_entities_at_random(
        item_chances, number_of_items, floor_number
    )

    for entity in monsters + items:
        x = random.randint(room.x1 + 1, room.x2 - 1)
        y = random.randint(room.y1 + 1, room.y2 - 1)
        
        if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
            entity.spawn(dungeon, x, y)


def tunnel_between(
    start: Tuple[int, int], end: Tuple[int, int]
) -> Iterator[Tuple[int, int]]:
    """Return an L-shaped tunnel between these two points."""
    x1, y1 = start
    x2, y2 = end
    if random.random() < 0.5: # 50% chance
        # Move horizontally, then vertically
        corner_x, corner_y = x2, y1
    else:
        # Move vertically, then horizontally
        corner_x, corner_y = x1, y2
    
    # Generate the coordinates for this tunnel
    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        yield x, y
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        yield x, y

def generate_dungeon(
    max_rooms: int,
    room_min_size: int,
    room_max_size: int,
    map_width: int,
    map_height: int,
    engine: Engine,
) -> GameMap:
    """Generate a new dungeon map."""
    player = engine.player
    dungeon = GameMap(engine, map_width, map_height, entities=[player])

    rooms: List[RectangularRoom] = []

    center_of_last_room = (0, 0)

    for r in range(max_rooms):
        # Random width and height
        room_width = random.randint(room_min_size, room_max_size)
        room_height = random.randint(room_min_size, room_max_size)

        # Random position without going out of the boundaries of the map
        x = random.randint(0, dungeon.width - room_width - 1)
        y = random.randint(0, dungeon.height - room_height - 1)
        
        # "RectangularRoom" class makes rectangles easier to work with
        new_room = RectangularRoom(x, y, room_width, room_height)

        # Run through the other rooms and see if they intersect with this one
        if any(new_room.intersects(other_room) for other_room in rooms):
            continue
        # If there are no intersections then the room is valid

        # Dig out this room's inner area
        dungeon.tiles[new_room.inner] = tile_types.floor

        if len(rooms) == 0:
            # The first room, where the player starts
            player.place(*new_room.center, dungeon)
        else: # All rooms after the first
            # Dig out a tunnel between this room and the previous one
            for x, y in tunnel_between(rooms[-1].center, new_room.center):
                dungeon.tiles[x, y] = tile_types.floor

            center_of_last_room = new_room.center

        place_entities(new_room, dungeon, engine.game_world.current_floor)

        dungeon.tiles[center_of_last_room] = tile_types.down_stairs
        dungeon.downstairs_location = center_of_last_room

        # Finally, append the new room to the list
        rooms.append(new_room)

    return dungeon