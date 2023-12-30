from components.ai import HostileEnemy
from components import consumable, equippable, ability
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from components.equippable import HandType
from entity import Actor, Item


# Player
player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=2, base_power=5),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

# Enemies
ashigaru = Actor(
    char="a",
    color=(63, 127, 63),
    name="Ashigaru",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)
ninja = Actor(
    char="n",
    color=(0, 127, 0),
    name="Ninja",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),
)
shinobi = Actor(
    char="s",
    color=(0, 127, 0),
    name="Shinobi",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),
)
onna_bugeisha = Actor(
    char="w",
    color=(0, 127, 0),
    name="Onna-bugeisha",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=25, base_defense=4, base_power=8),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=70),
)
samurai = Actor(
    char="s",
    color=(0, 127, 0),
    name="Samurai",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=25, base_defense=4, base_power=8),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=70),
)
ronin = Actor(
    char="R",
    color=(0, 127, 0),
    name="Ronin",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=3, base_power=10),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)
sohei = Actor(
    char="S",
    color=(0, 127, 0),
    name="Sohei",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=25, base_defense=2, base_power=10),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)
bushi = Actor(
    char="B",
    color=(0, 127, 0),
    name="Bushi",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=40, base_defense=4, base_power=15),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=150),
)


# Consumables
confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Smoke Screen",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)
fireball_scroll = Item(
    char="~",
    color=(255, 125, 0),
    name="Fire Bomb",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)
health_potion = Item(
    char="!",
    color=(0, 255, 175),
    name="Healing Cup",
    consumable=consumable.HealingConsumable(amount=4),
)
lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Shockwave",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

# Weapons
wrapped_fists = Item(
    char="/",
    color=(0, 191, 255),
    name="Wrapped Fists",
    equippable=equippable.Fists(
        hand_type=HandType.TWO_HANDED,
        power_bonus=1,
        defense_bonus=0,
    ),
)
tonfa = Item(
    char="/",
    color=(0, 191, 255),
    name="Tonfa",
    equippable=equippable.Fists(
        hand_type=HandType.TWO_HANDED,
        power_bonus=2,
        defense_bonus=2,
    ),
)
nunchucks = Item(
    char="/",
    color=(0, 191, 255),
    name="Nunchucks",
    equippable=equippable.Fists(
        hand_type=HandType.TWO_HANDED,
        power_bonus=3,
        defense_bonus=2,
    ),
)
shuko = Item(
    char="/",
    color=(0, 191, 255),
    name="Shuko",
    equippable=equippable.Fists(
        hand_type=HandType.TWO_HANDED,
        power_bonus=4,
        defense_bonus=0,
    ),
)
tekko = Item(
    char="/",
    color=(0, 191, 255),
    name="Tekko",
    equippable=equippable.Fists(
        hand_type=HandType.TWO_HANDED,
        power_bonus=5,
        defense_bonus=0,
    ),
)
dagger = Item(
    char="/",
    color=(0, 191, 255),
    name="Tanto",
    equippable=equippable.Dagger(
        hand_type=HandType.ONE_HANDED,
        power_bonus=2,
        defense_bonus=0,
    ),
)
wakizashi = Item(
    char="/",
    color=(0, 191, 255),
    name="Wakizashi",
    equippable=equippable.Dagger(
        hand_type=HandType.ONE_HANDED,
        power_bonus=3,
        defense_bonus=0,
    ),
)
katana = Item(
    char="/",
    color=(0, 191, 255),
    name="Katana",
    equippable=equippable.Sword(
        hand_type=HandType.TWO_HANDED,
        power_bonus=4,
        defense_bonus=1,
    ),
)
nagamaki = Item(
    char="/",
    color=(0, 191, 255),
    name="Nagamaki",
    equippable=equippable.Staff(
        hand_type=HandType.TWO_HANDED,
        power_bonus=5,
        defense_bonus=1,
    ),
)
naginata = Item(
    char="/",
    color=(0, 191, 255),
    name="Naginata",
    equippable=equippable.Staff(
        hand_type=HandType.TWO_HANDED,
        power_bonus=6,
        defense_bonus=2,
    ),
)
bo = Item(
    char="/",
    color=(0, 191, 255),
    name="Bo",
    equippable=equippable.Staff(
        hand_type=HandType.TWO_HANDED,
        power_bonus=4,
        defense_bonus=3,
    ),
)


# Shields
buckler = Item(
    char=")",
    color=(139, 69, 19),
    name="Buckler",
    equippable=equippable.Shield(
        hand_type=HandType.ONE_HANDED,
        defense_bonus=1,
    ),
)
targe = Item(
    char=")",
    color=(139, 69, 19),
    name="Targe",
    equippable=equippable.Shield(
        hand_type=HandType.ONE_HANDED,
        defense_bonus=2,
    ),
)
kite_shield = Item(
    char=")",
    color=(139, 69, 19),
    name="Kite Shield",
    equippable=equippable.Shield(
        hand_type=HandType.ONE_HANDED,
        defense_bonus=3,
    ),
)
heater_shield = Item(
    char=")",
    color=(139, 69, 19),
    name="Heater Shield",
    equippable=equippable.Shield(
        hand_type=HandType.ONE_HANDED,
        defense_bonus=4,
    ),
)
tower_shield = Item(
    char=")",
    color=(139, 69, 19),
    name="Tower Shield",
    equippable=equippable.Shield(
        hand_type=HandType.TWO_HANDED,
        defense_bonus=5,
    ),
)


# Armor
cloth_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Cloth Yoroi",
    equippable=equippable.Armor(defense_bonus=1),
)
leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Gusoku",
    equippable=equippable.Armor(defense_bonus=2),
)
chain_mail = Item(
    char="[",
    color=(139, 69, 19),
    name="Plated Gusoku",
    equippable=equippable.Armor(defense_bonus=3),
)
lamellar_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Lamellar Gusoku",
    equippable=equippable.Armor(defense_bonus=4),
)
tatami_do = Item(
    char="[",
    color=(139, 69, 19),
    name="Tatami Gusoku",
    equippable=equippable.Armor(defense_bonus=5),
)
o_yoroi = Item(
    char="[",
    color=(139, 69, 19),
    name="O-Yoroi",
    equippable=equippable.Armor(defense_bonus=6),
)
oni_mail = Item(
    char="[",
    color=(139, 69, 19),
    name="Oni Gusoku",
    equippable=equippable.Armor(defense_bonus=8),
)
star_forged_mail = Item(
    char="[",
    color=(139, 69, 19),
    name="Star-forged Gusoku",
    equippable=equippable.Armor(defense_bonus=10),
)


# Abilities
confusion_ability = Item(
    char="*",
    color=(54, 40, 113),
    name="Evoke Blindness",
    ability=ability.ConfusionAbility(number_of_turns=15, cooldown_turns=5),
)
fireball_ability = Item(
    char="*",
    color=(255, 0, 125),
    name="Supernova",
    ability=ability.FireballDamageAbility(damage=25, radius=5, cooldown_turns=5),
)
healing_ability = Item(
    char="*",
    color=(0, 255, 0),
    name="Gourd of Vitality",
    ability=ability.HealingAbility(amount=5, cooldown_turns=5),
)
lightning_ability = Item(
    char="*",
    color=(0, 100, 255),
    name="Comet Azure",
    ability=ability.LightningDamageAbility(damage=30, maximum_range=7, cooldown_turns=5),
)
shuriken = Item(
    char="*",
    color=(160, 160, 160),
    name="Shuriken",
    ability=ability.Shuriken(damage=7, maximum_range=4, cooldown_turns=0),
)
kunai = Item(
    char="*",
    color=(130, 160, 190),
    name="Kunai",
    ability=ability.Kunai(damage=10, maximum_range=4, cooldown_turns=0),
)
bow = Item(
    char="*",
    color=(130, 160, 190),
    name="Bow",
    ability=ability.Bow(damage=15, maximum_range=7, cooldown_turns=1),
)
black_hole = Item(
    char="*",
    color=(0, 0, 0),
    name="Black Hole",
    ability=ability.Blackhole(damage=100, radius=7, cooldown_turns=20),
)
solar_flare = Item(
    char="*",
    color=(255, 0, 0),
    name="Ruby Flare",
    ability=ability.SolarFlare(damage=30, maximum_range=7, cooldown_turns=5),
)
star_rage = Item(
    char="*",
    color=(125, 0, 255),
    name="Star Rage",
    ability=ability.StarRage(damage=20, radius=5, cooldown_turns=5),
)


# Accessories
# TODO: Add Accessories