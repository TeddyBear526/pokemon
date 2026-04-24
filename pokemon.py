import random
pokemons = [
    {
        "pokemon":"Pickachu",
        "typing": "electric",
        "hp": 42,
        "moves": [
            {
                "name": "Thunderbolt",
                "damage": 25,
                "type": "electric"
            }
            ,
            {
                "name": "Iron Tail",
                "damage": 20,
                "type": "steel"
            }
            ,
            {
                "name": "PLay Rough",
                "damage": 15,
                "type": "fairy"
            }
            ,
            {
                "name": "Volt Tackle",
                "damage": 25,
                "type": "electric"
            
            }
        ]

    },
    {
        "pokemon": "Blastois",
        "typing": "water",
        "hp": 110,
        "moves": [
            {
                "name":"Water Gun",
                "damage": 10,
                "type": "water"
            }
            ,
            {
                "name": "Aqua Jet",
                "damage": 10,
                "type": "water"
            }
            ,
            {
                "name":"Liquidation",
                "damage": 15,
                "type": "water"
            }
            ,
            {
                "name": "tackle",
                "damage": 5,
                "type": "normal"
            
            }
        ]
    },
    {
        "pokemon": "Sandygast",
        "typing": "ground/ghost",
        "hp": 55,
        "moves": [
            {
                "name": "Scorching Sands",
                "damage": 20,
                "type": "ground"
            }
            ,
            {
                "name": "Shadow Ball",
                "damage": 25,
                "type": "ghost"
            }
            ,
            {
                "name": "Rock Tomb",
                "damage": 15,
                "type": "rock"
                

            },
            {
                "name": "Earth Power",
                "damage": 20,
                "type": "ground"
            
            }
        ]
    },
    {
        "pokemon": "Swinub",
        "typing": "ground/ice",
        "hp": 38,
        "moves":[
            {
                "name":"Blizzard",
                "damage": 25,
                "type": "ice"
            }
            ,
            {
                "name": "Earthquake",
                "damage": 30,
                "type": "ground"
            }
            ,
            {
                "name":"Icicle Crash",
                "damage":30,
                "type": "ice"
            }
            ,
            {
                "name":"Take Down",
                "damage":20,
                "type": "normal"
            
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
print(type_resistance.get(enemy["typing"]))


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

            for i, move in enumerate(your_chosen["moves"], start=1):
                print(f"{i}. {move["name"]} {move["damage"]} dmg")
            choice = int(input("Choose move number: ")) -1
            if 0 <= choice < len(your_chosen["moves"]):
                    player_move = your_chosen["moves"][choice]
            else:
                print("Invalid move number, Turn skipped.")
                continue
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
            for i, move in enumerate(your_chosen["moves"], start=1):
                print(f"{i}. {move["name"]} {move["damage"]} dmg")
            choice = int(input("Choose move number: ")) -1
            if 0 <= choice < len(your_chosen["moves"]):
                    player_move = your_chosen["moves"][choice]
            else:
                print("Invalid move number, Turn skipped.")
                continue
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
            first = random(1, 2)

            if first == 1:
                for i, move in enumerate(your_chosen["moves"], start=1):
                    print(f"{i}. {move["name"]} {move["damage"]} dmg")
                choice = int(input("Choose move number: ")) -1
                if 0 <= choice < len(your_chosen["moves"]):
                        player_move = your_chosen["moves"][choice]
                else:
                    print("Invalid move number, Turn skipped.")
                    continue
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

                for i, move in enumerate(your_chosen["moves"], start=1):
                    print(f"{i}. {move["name"]} {move["damage"]} dmg")
                choice = int(input("Choose move number: ")) -1
                if 0 <= choice < len(your_chosen["moves"]):
                        player_move = your_chosen["moves"][choice]
                else:
                    print("Invalid move number, Turn skipped.")
                    continue
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