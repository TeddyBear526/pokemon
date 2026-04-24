import random
pokemons = [
    {
        "pokemon":"Raichu", "typing": "electric", "hp": 60, "speed": 100,
        "moves": [
            {
                "name": "Thunderbolt", "damage": 30, "type": "electric"
            },
            {
                "name": "Brick Break", "damage": 30, "type": "fighting"
            },
            {
                "name": "Shadow Ball", "damage": 25, "type": "ghost"
            },
            {
                "name": "Nasty Plot", "damage": 0, "type": "dark"
            }
        ]
    },
    {
        "pokemon":"Ninetales", "typing": "fire", "hp": 73, "speed": 100,
        "moves": [
            {
                "name": "Fire Blast", "damage": 35, "type": "fire"
            },
            {
                "name": "Nasty Plot", "damage": 0, "type": "dark"
            },
            {
                "name": "Dazzling Gleam", "damage": 30, "type": "fairy"
            },
            {
                "name": "Dark Pulse", "damage": 30, "type": "dark"
            }
        ]
    },
    {
        "pokemon":"Arcanine", "typing": "fire", "hp": 90, "speed": 95,
        "moves": [
            {
                "name": "Flare Blitz", "damage": 40, "type": "fire"
            },
            {
                "name": "Wild Charge", "damage": 30, "type": "electric"
            },
            {
                "name": "Extreme Speed", "damage": 20, "type": "normal"
            },
            {
                "name": "Close Combat", "damage": 40, "type": "fighting"
            }
        ]
    },
    {
        "pokemon":"Lapras", "typing": "water", "hp": 130, "speed": 60,
        "moves": [
            {
                "name": "Surf", "damage": 30, "type": "water"
            },
            {
                "name": "Ice Beam", "damage": 30, "type": "ice"
            },
            {
                "name": "Dragon Dance", "damage": 0, "type": "dragon"
            },
            {
                "name": "Earthquake", "damage": 30, "type": "ground"
            }
        ]
    },
    {
        "pokemon":"Dragonite", "typing": "dragon", "hp": 91, "speed": 80,
        "moves": [
            {
                "name": "Outrage", "damage": 40, "type": "dragon"
            },
            {
                "name": "Earthquake", "damage": 30, "type": "ground"
            },
            {
                "name": "Hurricane", "damage": 35, "type": "flying"
            },
            {
                "name": "Superpower", "damage": 35, "type": "fighting"
            }
        ]
    },
    {
        "pokemon":"Gyarados", "typing": "water", "hp": 95, "speed": 81,
        "moves": [
            {
                "name": "Waterfall", "damage": 30, "type": "water"
            },
            {
                "name": "Earthquake", "damage": 30, "type": "ground"
            },
            {
                "name": "Stone Edge", "damage": 35, "type": "rock"
            },
            {
                "name": "Crunch", "damage": 30, "type": "dark"
            }
        ]
    },
    {
        "pokemon":"Gengar", "typing": "ghost", "hp": 65, "speed": 130,
        "moves": [
            {
                "name": "Shadow Ball", "damage": 30, "type": "ghost"
            },
            {
                "name": "Focus Blast", "damage": 35, "type": "fighting"
            },
            {
                "name": "Sludge Bomb", "damage": 30, "type": "poison"
            },
            {
                "name": "Thunderbolt", "damage": 30, "type": "electric"
            }
        ]
    },
    {
        "pokemon":"Machamp", "typing": "fighting", "hp": 90, "speed": 55,
        "moves": [
            {
                "name": "Close Combat", "damage": 40, "type": "fighting"
            },
            {
                "name": "Stone Edge", "damage": 35, "type": "rock"
            },
            {
                "name": "Earthquake", "damage": 30, "type": "ground"
            },
            {
                "name": "Bullet Punch", "damage": 20, "type": "steel"
            }
        ]
    },
    {
        "pokemon":"Golem", "typing": "rock", "hp": 80, "speed": 45,
        "moves": [
            {
                "name": "Stone Edge", "damage": 35, "type": "rock"
            },
            {
                "name": "Earthquake", "damage": 30, "type": "ground"
            },
            {
                "name": "Explosion", "damage": 50, "type": "normal"
            },
            {
                "name": "Iron Head", "damage": 30, "type": "steel"
            }
        ]
    },
    {
        "pokemon":"Alakazam", "typing": "psychic", "hp": 55, "speed": 120,
        "moves": [
            {
                "name": "Psychic", "damage": 35, "type": "psychic"
            },
            {
                "name": "Focus Blast", "damage": 35, "type": "fighting"
            },
            {
                "name": "Shadow Ball", "damage": 25, "type": "ghost"
            },
            {
                "name": "Dazzling Gleam", "damage": 30, "type": "fairy"
            }
        ]
    },
    {
        "pokemon":"Tentacruel", "typing": "water", "hp": 80, "speed": 55,
        "moves": [
            {
                "name": "Hydro Pump", "damage": 35, "type": "water"
            },
            {
                "name": "Sludge Wave", "damage": 30, "type": "poison"
            },
            {
                "name": "Ice Beam", "damage": 30, "type": "ice"
            },
            {
                "name": "Psychic", "damage": 35, "type": "psychic"
            }
        ]
    },
    {
        "pokemon":"Vileplume", "typing": "grass", "hp": 75, "speed": 50,
        "moves": [
            {
                "name": "Solar Beam", "damage": 40, "type": "grass"
            },
            {
                "name": "Sludge Bomb", "damage": 30, "type": "poison"
            },
            {
                "name": "Dazzling Gleam", "damage": 30, "type": "fairy"
            },
            {
                "name": "Moonblast", "damage": 35, "type": "fairy"
            }
        ]
    },
    {
        "pokemon":"Rapidash", "typing": "fire", "hp": 65, "speed": 100,
        "moves": [
            {
                "name": "Fire Blast", "damage": 35, "type": "fire"
            },
            {
                "name": "Wild Charge", "damage": 30, "type": "electric"
            },
            {
                "name": "Bounce", "damage": 25, "type": "flying"
            },
            {
                "name": "Fury Attack", "damage": 20, "type": "normal"
            }
        ]
    },
    {
        "pokemon":"Slowbro", "typing": "water", "hp": 95, "speed": 30,
        "moves": [
            {
                "name": "Surf", "damage": 30, "type": "water"
            },
            {
                "name": "Psychic", "damage": 35, "type": "psychic"
            },
            {
                "name": "Ice Beam", "damage": 30, "type": "ice"
            },
            {
                "name": "Earthquake", "damage": 30, "type": "ground"
            }
        ]
    },
    {
        "pokemon":"Snorlax", "typing": "normal", "hp": 150, "speed": 35,
        "moves": [
            {
                "name": "Body Slam", "damage": 30, "type": "normal"
            },
            {
                "name": "Crunch", "damage": 30, "type": "dark"
            },
            {
                "name": "Earthquake", "damage": 30, "type": "ground"
            },
            {
                "name": "Stone Edge", "damage": 35, "type": "rock"
            }
        ]
    },
    {
        "pokemon":"Exeggutor", "typing": "grass", "hp": 95, "speed": 55,
        "moves": [
            {
                "name": "Solar Beam", "damage": 40, "type": "grass"
            },
            {
                "name": "Psychic", "damage": 35, "type": "psychic"
            },
            {
                "name": "Earthquake", "damage": 30, "type": "ground"
            },
            {
                "name": "Dragon Hammer", "damage": 30, "type": "dragon"
            }
        ]
    },
]

type_weaknesses = {
     "normal": ["fighting"],
     "fighting": ["fairy", "flying", "psychic"],
     "flying": ["electric", "ice", "rock"],
     "poison": ["ground", "psychic"],
     "ground":["grass", "ice", "water"],
     "rock": ["fighting", "grass","ground","steel","water"],
     "electric": ["ground"],
     "water": ["electric", "grass"],
     "ghost": ["ghost", "dark"],
     "ice": ["fire", "fighting", "rock", "steel"],
     "steel": ["fire", "fighting", "ground"],
     "fairy": ["poison", "steel"],
     "dragon": ["dragon", "ice", "fairy"],
     "bug": ["fire", "flying", "rock"],
     "fire": ["water", "ground", "rock"],
     "dark": ["fighting", "bug", "fairy"]
}

type_resistance = {
     "normal": [],
     "fighting": ["rock", "bug", "dark"],
     "flying": ["fighting", "bug", "grass"],
     "poison": ["fighting", "poison", "bug", "fairy"],
     "ground": ["poison", "rock", "electric"],
     "rock": ["normal", "flying", "poison", "fire"],
     "electric": ["flying", "steel", "electric"],
     "water": ["fire", "water", "ice", "steel"],
     "ghost": ["poison", "bug"],
     "ice": ["ice"],
     "steel": ["normal", "flying", "rock", "bug", "steel", "grass", "psychic", "ice", "dragon", "fairy"],
     "fairy": ["fighting", "bug", "dark"],
     "dragon": ["fire", "water", "grass", "electric"],
     "bug": ["fighting", "ground", "grass"],
     "fire": ["bug", "steel", "grass", "ice", "fairy", "fire"],
     "dark": ["ghost", "dark"]
}
enemy = random.choice(pokemons)

print(f"You encounter a wild {enemy["pokemon"]}")
print(f"The {enemy["typing"]} pokemon")
print(f"It has {enemy["hp"]} health")


battle = input("Do you wish to fight it [y/n]? ")
if battle .lower() == "n":
    print(f"You panic and flee from the wild {enemy["pokemon"]}")
else:
    print("You stand your ground to fight the wild pokemon")

    your_chosen = random.choice(pokemons)
    print(f"You choose {your_chosen["pokemon"]}")
    print(f"The {your_chosen["typing"]} pokemon")
    print(f"It has {your_chosen["hp"]} health")

    current_hp = your_chosen["hp"]
    enemy_hp = enemy["hp"]

    while current_hp > 0 and enemy_hp > 0:
        if enemy["speed"] > your_chosen["speed"]:
            enemy_move = random.choice(enemy["moves"])
            print(f"{enemy['pokemon']} uses {enemy_move['name']}")
            types = your_chosen["typing"].split("/")
            weak = any(enemy_move["type"] in type_weaknesses.get(t, []) for t in types)
            resist = any(enemy_move["type"] in type_resistance.get(t, []) for t in types) and not weak

            if weak:
                current_hp -= enemy_move["damage"] *2
                print(f"Your {your_chosen['pokemon']} takes {enemy_move["damage"]*2} damage! HP left: {current_hp}")
            elif resist:
                current_hp -= enemy_move["damage"] *0.5
                print(f"Your {your_chosen['pokemon']} takes {enemy_move["damage"]*0.5} damage! HP left: {current_hp}")
            elif weak and resist:
                current_hp-=enemy_move["damage"]
                print(f"Your {your_chosen['pokemon']} takes {enemy_move["daamge"]} damage! HP left: {current_hp}")
            else:
                current_hp -= enemy_move["damage"]
                print(f"Your {your_chosen['pokemon']} takes {enemy_move["damage"]} damage! HP left: {current_hp}")
            
            if current_hp <= 0:
                print(f"Your {your_chosen['pokemon']} fainted!")
                break

            while True:
                for i, move in enumerate(your_chosen["moves"], start=1):
                    print(f"{i}. {move["name"]} {move["damage"]} dmg")
                try:
                    choice = int(input("Choose move number: ")) -1
                except ValueError:
                    print("Please enter a number")
                if 0 <= choice < len(your_chosen["moves"]):
                    player_move = your_chosen["moves"][choice]
                    break
                print("Invalid move number, try again.")

            print(f"Your {your_chosen["pokemon"]} uses {player_move["name"]}")
            types = enemy["typing"].split("/")
            weak = any(player_move["type"] in type_weaknesses.get(t, []) for t in types)
            resist = any(player_move["type"] in type_resistance.get(t, []) for t in types)
            if weak:
                enemy_hp -= player_move["damage"] *2
                print(f"The wild {enemy['pokemon']} takes {player_move["damage"]*2} damage, HP left: {enemy_hp}")
            elif resist:
                enemy_hp -= player_move["damage"]* 0.5
                print(f"The wild {enemy['pokemon']} takes {player_move["damage"]*0.5} damage, HP left: {enemy_hp}")
            elif resist and weak:
                enemy_hp -= player_move["damage"]
                print(f"The wild {enemy['pokemon']} takes {player_move["damage"]} damage, HP left: {enemy_hp}")
            else:
                enemy_hp -= player_move["damage"]
                print(f"The wild {enemy['pokemon']} takes {player_move["damage"]} damage, HP left: {enemy_hp}")

            if enemy_hp <= 0:
                print(f"Wild {enemy['pokemon']} fainted!")
                break

        elif enemy["speed"] < your_chosen["speed"]:

            while True:
                for i, move in enumerate(your_chosen["moves"], start=1):
                    print(f"{i}. {move["name"]} {move["damage"]} dmg")
                try:
                    choice = int(input("Choose move number: ")) -1
                except ValueError:
                    print("Please enter a number")
                if 0 <= choice < len(your_chosen["moves"]):
                    player_move = your_chosen["moves"][choice]
                    break
                print("Invalid move number, try again.")
            
            print(f"Your {your_chosen["pokemon"]} uses {player_move["name"]}")
            types = enemy["typing"].split("/")
            weak = any(player_move["type"] in type_weaknesses.get(t, []) for t in types)
            resist = any(player_move["type"] in type_resistance.get(t, []) for t in types)
            if weak:
                enemy_hp -= player_move["damage"] *2
                print(f"The wild {enemy['pokemon']} takes {player_move["damage"]*2} damage, HP left: {enemy_hp}")
            elif resist:
                enemy_hp -= player_move["damage"]* 0.5
                print(f"The wild {enemy['pokemon']} takes {player_move["damage"]*0.5} damage, HP left: {enemy_hp}")
            elif resist and weak:
                enemy_hp -= player_move["damage"]
                print(f"The wild {enemy['pokemon']} takes {player_move["damage"]} damage, HP left: {enemy_hp}")
            else:
                enemy_hp -= player_move["damage"]
                print(f"The wild {enemy['pokemon']} takes {player_move["damage"]} damage, HP left: {enemy_hp}")

            if enemy_hp <= 0:
                print(f"Wild {enemy['pokemon']} fainted!")
                break

            enemy_move = random.choice(enemy["moves"])
            print(f"{enemy['pokemon']} uses {enemy_move['name']}")
            types = your_chosen["typing"].split("/")
            weak = any(enemy_move["type"] in type_weaknesses.get(t, []) for t in types)
            resist = any(enemy_move["type"] in type_resistance.get(t, []) for t in types) and not weak

            if weak:
                current_hp -= enemy_move["damage"] *2
                print(f"Your {your_chosen['pokemon']} takes {enemy_move["damage"]*2} damage! HP left: {current_hp}")
            elif resist:
                current_hp -= enemy_move["damage"] *0.5
                print(f"Your {your_chosen['pokemon']} takes {enemy_move["damage"]*0.5} damage! HP left: {current_hp}")
            elif weak and resist:
                current_hp-=enemy_move["damage"]
                print(f"Your {your_chosen['pokemon']} takes {enemy_move["daamge"]} damage! HP left: {current_hp}")
            else:
                current_hp -= enemy_move["damage"]
            print(f"Your {your_chosen['pokemon']} takes {enemy_move["damage"]} damage! HP left: {current_hp}")
            
            if current_hp <= 0:
                print(f"Your {your_chosen['pokemon']} fainted!")
                break
        else:
            first = random.randint(1,2)

            if first == 1:

                while True:
                    for i, move in enumerate(your_chosen["moves"], start=1):
                        print(f"{i}. {move["name"]} {move["damage"]} dmg")
                    try:
                        choice = int(input("Choose move number: ")) -1
                    except ValueError:
                        print("Please enter a number")
                    if 0 <= choice < len(your_chosen["moves"]):
                        player_move = your_chosen["moves"][choice]
                        break
                    print("Invalid move number, try again.")

                print(f"Your {your_chosen["pokemon"]} uses {player_move["name"]}")
                types = enemy["typing"].split("/")
                weak = any(player_move["type"] in type_weaknesses.get(t, []) for t in types)
                resist = any(player_move["type"] in type_resistance.get(t, []) for t in types)
                if weak:
                    enemy_hp -= player_move["damage"] *2
                    print(f"The wild {enemy['pokemon']} takes {player_move["damage"]*2} damage, HP left: {enemy_hp}")
                elif resist:
                    enemy_hp -= player_move["damage"]* 0.5
                    print(f"The wild {enemy['pokemon']} takes {player_move["damage"]*0.5} damage, HP left: {enemy_hp}")
                elif resist and weak:
                    enemy_hp -= player_move["damage"]
                    print(f"The wild {enemy['pokemon']} takes {player_move["damage"]} damage, HP left: {enemy_hp}")
                else:
                    enemy_hp -= player_move["damage"]
                    print(f"The wild {enemy['pokemon']} takes {player_move["damage"]} damage, HP left: {enemy_hp}")

                if enemy_hp <= 0:
                    print(f"Wild {enemy['pokemon']} fainted!")
                    break

                enemy_move = random.choice(enemy["moves"])
                print(f"{enemy['pokemon']} uses {enemy_move['name']}")
                types = your_chosen["typing"].split("/")
                weak = any(enemy_move["type"] in type_weaknesses.get(t, []) for t in types)
                resist = any(enemy_move["type"] in type_resistance.get(t, []) for t in types) and not weak

                if weak:
                    current_hp -= enemy_move["damage"] *2
                    print(f"Your {your_chosen['pokemon']} takes {enemy_move["damage"]*2} damage! HP left: {current_hp}")
                elif resist:
                    current_hp -= enemy_move["damage"] *0.5
                    print(f"Your {your_chosen['pokemon']} takes {enemy_move["damage"]*0.5} damage! HP left: {current_hp}")
                elif weak and resist:
                    current_hp-=enemy_move["damage"]
                    print(f"Your {your_chosen['pokemon']} takes {enemy_move["daamge"]} damage! HP left: {current_hp}")
                else:
                    current_hp -= enemy_move["damage"]
                print(f"Your {your_chosen['pokemon']} takes {enemy_move["damage"]} damage! HP left: {current_hp}")
                
                if current_hp <= 0:
                    print(f"Your {your_chosen['pokemon']} fainted!")
                    break

            elif first == 2:
                enemy_move = random.choice(enemy["moves"])
                print(f"{enemy['pokemon']} uses {enemy_move['name']}")
                types = your_chosen["typing"].split("/")
                weak = any(enemy_move["type"] in type_weaknesses.get(t, []) for t in types)
                resist = any(enemy_move["type"] in type_resistance.get(t, []) for t in types) and not weak

                if weak:
                    current_hp -= enemy_move["damage"] *2
                    print(f"Your {your_chosen['pokemon']} takes {enemy_move["damage"]*2} damage! HP left: {current_hp}")
                elif resist:
                    current_hp -= enemy_move["damage"] *0.5
                    print(f"Your {your_chosen['pokemon']} takes {enemy_move["damage"]*0.5} damage! HP left: {current_hp}")
                elif weak and resist:
                    current_hp-=enemy_move["damage"]
                    print(f"Your {your_chosen['pokemon']} takes {enemy_move["daamge"]} damage! HP left: {current_hp}")
                else:
                    current_hp -= enemy_move["damage"]
                    print(f"Your {your_chosen['pokemon']} takes {enemy_move["damage"]} damage! HP left: {current_hp}")
                
                if current_hp <= 0:
                    print(f"Your {your_chosen['pokemon']} fainted!")
                    break

                while True:
                    for i, move in enumerate(your_chosen["moves"], start=1):
                        print(f"{i}. {move["name"]} {move["damage"]} dmg")
                    try:
                        choice = int(input("Choose move number: ")) -1
                    except ValueError:
                        print("Please enter a number")
                    if 0 <= choice < len(your_chosen["moves"]):
                        player_move = your_chosen["moves"][choice]
                        break
                    print("Invalid move number, try again.")
                
                print(f"Your {your_chosen["pokemon"]} uses {player_move["name"]}")
                types = enemy["typing"].split("/")
                weak = any(player_move["type"] in type_weaknesses.get(t, []) for t in types)
                resist = any(player_move["type"] in type_resistance.get(t, []) for t in types)
                if weak:
                    enemy_hp -= player_move["damage"] *2
                    print(f"The wild {enemy['pokemon']} takes {player_move["damage"]*2} damage, HP left: {enemy_hp}")
                elif resist:
                    enemy_hp -= player_move["damage"]* 0.5
                    print(f"The wild {enemy['pokemon']} takes {player_move["damage"]*0.5} damage, HP left: {enemy_hp}")
                elif resist and weak:
                    enemy_hp -= player_move["damage"]
                    print(f"The wild {enemy['pokemon']} takes {player_move["damage"]} damage, HP left: {enemy_hp}")
                else:
                    enemy_hp -= player_move["damage"]
                    print(f"The wild {enemy['pokemon']} takes {player_move["damage"]} damage, HP left: {enemy_hp}")

                if enemy_hp <= 0:
                    print(f"Wild {enemy['pokemon']} fainted!")
                    break