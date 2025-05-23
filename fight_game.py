import random
import math
#Define the options of characters in the game 

#Class of Speedster 
class Speedster:
    def __init__(self, name, power_level, morality):
        self.name = name
        self.power_level = power_level
        self.health = 200
        self.morality = morality
    
    def __repr__(self):
        return "{name} is a powerful {morality} that is connected to the Speed Force, making them a speedster. They are at a Speed Force level of {power_level}, making them a worthy opponent.".format(name = self.name, morality = self.morality, power_level = self.power_level)
    #Regular Actions of  Speedster 
    def throw_lightning(self, opponent):
        damage = 55

        if isinstance(opponent, Viltrumite):
            damage -= 20
        elif isinstance(opponent, Wizard):
            damage += 20

        if self.power_level > 170:
             damage += 15
        elif self.power_level > 200:
             damage += 30
        
        opponent.health -= damage
        print(f"{self.name} has thrown a bolt of lightning at {opponent.name}! {opponent.name} is now at {opponent.health}")
        return 
   
    def speed_rush(self, opponent):
        damage = 40
        if isinstance(opponent, Viltrumite):
            damage -= 10
        elif isinstance(self, Wizard):
            damage += 15

        opponent.health -= damage
        print(f"{self.name} has attacked {opponent.name} by throwing multiple punches at super speed, casuing {damage} damage! {opponent.name} is now at {opponent.health} health")
        return 
    
    def speed_heal(self):
        self.health += 25
        if self.power_level > 170:
             self.health += 30
        elif self.power_level >200:
             self.health += 35
        
        if self.health >= 200:
            print(f"{self.name} is at maximum health!")
            self.health = 200
            return 
        

        print(f"{self.name} has connected deeper to the speed force to heal, health is now at {self.health}")
        
        return 

         



    # Super action of a speedster 
    def super_sonic_punch(self, opponent, opponent_is_user=False):
        base_damage = 100
        extra_damage = 30


        if isinstance(opponent, Viltrumite):
            base_damage -= 10
        elif isinstance(opponent, Wizard):
            base_damage += 15
        
        print(f"{self.name} is charging up for a devastating super sonic punch!")
        if opponent_is_user == True:
            action = input("Do you want to 'attack' or 'defend'?").lower()
            if action == "attack":
                if isinstance(opponent, Speedster):
                    move = input("Which attack move do you want to use? Either 'throw lightning' or 'speed rush'.").lower()
                elif isinstance(opponent, Viltrumite):
                    move = input("Which attack move do you want to use? Either 'super punch' or 'sonic thunderclap'.").lower()
                elif isinstance(opponent, Wizard):
                    move = input("Which attack move do you want to use? Either 'elemental spell' or 'energy strike'.").lower()
                
                chance = random.random()
                if chance < 0.3:
                    counter_damage = 0
                    if move in ["throw lightning", "super punch", "elemental spell"]:
                        counter_damage = 75
                    elif move in ["speed rush", "sonic thunderclap", "energy strike"]:
                        counter_damage = 60

                    print(f"You managed to strike before the sonic punch with {move}! You even delt {counter_damage} damage in doing so!")
                    self.health -= counter_damage
                    print(f"{self.name} is now left with {self.health} health")
                    return 
                else:
                    print(f"Your attempt to counter with {move} failed. You suffer the sonic punch with full force!")
                    opponent.health -= int(base_damage + extra_damage)
                    print(f"{opponent.name} are now left with {opponent.health} health")
                    return 
                
            elif action == "defend":
                if isinstance(opponent, Speedster):
                    move = input("Which defense move do you want to use? either 'phase' or 'speed dodge'")
                elif isinstance(opponent, Viltrumite):
                    move = input("Which defence move do you want to use? Either 'invulnerable block' or 'aerial evasion' ")
                elif isinstance(opponent, Wizard):
                    move = input("Which defence move do you want to use? Either 'mystic shield' or 'mirror duplicate'.")

                #Calculate defence success
                reduction = 0 
                if move in ["phase", "invulnerable block", "mirror duplicate"]:
                    chance = random.random()
                    if chance < 0.45:
                        print(f"Your {move} was successful! You completely evaded the super sonic punch!")
                        reduction = 1
                        opponent.health -= int(base_damage * (1 - reduction))
                        print(f"{opponent.name} is now left with {opponent.health} health.")
                        return
                    else:
                        print(f"Your {move} was timed badly. You take the full force of the super sonic punch")
                        opponent.health -= int(base_damage * (1 - reduction))
                        print(f"{opponent.name} is now left with {opponent.health} health.")
                        return
                
                elif move in ["speed dodge", "aerial evasion", "mystic shield"]:
                    chance = random.random()
                    if chance < 0.65:
                        print(f"Your {move} was successful in avoiding the full contact of the super sonic punch! You still however suffered the after shock unfortunately.")
                        reduction = 0.5
                        opponent.health -= int(base_damage * (1 - reduction))
                        print(f"{opponent.name} is now left with {opponent.health} health.")
                    else:
                        print(f"Your {move} was unsuccessful, you are unable to avoid the full force of the super sonic punch.")
                        reduction = 0
                        opponent.health -= int(base_damage * (1 - reduction))
                        print(f"{opponent.name} is now left with {opponent.health} health.")
                return 
            else:
                print("Invalid choice! You hesitated and took the full force of the super sonic punch!")
                opponent.health -= base_damage
                print(f"{opponent.name} is now left with {opponent.health} health.")
                return 
            
            #CPU logic
        else:
            cpu_action = random.choice(["attack", "defend"])

            #CPU Attack logic
            if cpu_action == "attack":
                print(f"{opponent.name} attempts to counter-attack!")
                if isinstance(opponent, Speedster):
                    available_moves = ["throw lightning", "speed rush"]
                elif isinstance(opponent, Viltrumite):
                    available_moves = ["super punch", "sonic thunderclap"]
                elif isinstance(opponent, Wizard):
                    available_moves = ["energy strike", "elemental spell"]

                chosen_move = random.choice(available_moves)
                counter_chance = 0.3
                if random.random() < counter_chance:
                    counter_damage = 0
                    if chosen_move in ["throw lightning", "super punch", "elemental spell"]:
                        counter_damage = 75
                    elif chosen_move in ["speed rush", "sonic thunderclap", "energy strike"]:
                        counter_damage = 60
                    
                    self.health -= counter_damage
                    print(f"{opponent.name} succeeded in attempting their {chosen_move}! They have dealt {counter_damage} to {self.name} rather than suffering the force of the super sonic punch!")
                    print(f"{self.name} is now on {self.health} health")
                    return 
                else:
                    print(f"{opponent.name} failed the counter attack to the super sonic punch. Therefore suffering the full unlimited force of the punch!")
                    opponent.health -= int(base_damage + extra_damage)
                    print(f"{opponent.name} is now at {opponent.health} health.")
                    return 
            elif cpu_action == "defend":
                print(f"{opponent.name} attempts to evade the super sonic punch!")
                reduction = 0
                if isinstance(opponent, Speedster):
                    available_defences = ["phase", "speed dodge"]
                elif isinstance(opponent, Viltrumite):
                    available_defences = ["invulnerable block", "aerial evasion"]
                elif isinstance(opponent, Wizard):
                    available_defences = ["mystic shield", "mirror duplicate"]

                chosen_defence = random.choice(available_defences)
                if chosen_defence in ["phase", "invulnerable block", "mirror duplicate"]:
                    defence_chance = 0.45
                    if random.random() < defence_chance:
                        print(f"The {chosen_defence} was successful! {opponent.name} managed to completely evade the super sonic punch, suffering no damage at all!")
                        reduction = 1
                        opponent.health -= int(base_damage * (1 - reduction))
                        print(f"{opponent.name} is now left with {opponent.health} health!")
                    else:
                        print(f"The {chosen_defence} was unsuccessful.")
                        reduction = 0
                        opponent.health -= int(base_damage * (1 - reduction))
                        print(f"{opponent.name} is now left with {opponent.health} health!")
                elif chosen_defence in ["speed dodge", "aerial evasion", "mystic shield"]:
                    defence_chance = 0.65
                    if random.random() < defence_chance:
                        print(f"The {chosen_defence} was successful in avoiding the initial contact of the super sonic punch! {opponent.name} was not able to escape the after shock though.")
                        reduction = 0.5
                        opponent.health -= int(base_damage * (1 - reduction))
                        print(f"{opponent.name} is now left with {opponent.health} health!")
                    else:
                        print(f"The {chosen_defence} was unsuccessful.")
                        reduction = 0
                        opponent.health -= int(base_damage * (1 - reduction))
                        print(f"{opponent.name} is now left with {opponent.health} health!")
                return 



                      
                
            
        




#Class for a Viltrumite 


class Viltrumite:
    def __init__(self, name, power_level, morality):
        self.name = name
        self.power_level = power_level
        self.health = 200
        self.morality = morality

    def __repr__(self):
        return "{name} is a {morality} that is a descendant from the planet Viltrum, making them a Viltrumite! This makes them a very powerful being with the power level of {power_level}, making them a deadly opponent.".format(name = self.name, morality = self.morality, power_level = self.power_level)
    
    #Regular Actions of Viltrumite
    def super_punch(self, opponent):
        damage = 65

        if isinstance(opponent, Speedster):
             damage -= 10
        elif isinstance(opponent, Wizard):
             damage += 5

        if self.power_level > 170:
             damage += 20
        elif self.power_level > 200:
             damage += 30
        
        opponent.health -= damage
        print(f"{self.name} has caught {opponent.name} off guard with a Super Punch! {opponent.name} is now at {opponent.health}")
        return 
    
    def sonic_thunderclap(self, opponent):
        damage = 40

        if isinstance(opponent, Viltrumite):
             damage += 30
        elif isinstance(opponent, Speedster):
             damage -= 10
        elif isinstance(opponent, Wizard):
             damage += 15
        
        if self.power_level > 170:
             damage += 15
        elif self.power_level > 200:
             damage += 30

        opponent.health -= damage
        print(f"{self.name} has used their incredible strength to create a sonic soundwave with their hands! leaving {opponent.name} disoriented and at {opponent.health} health")

    
    #Super Action of Viltrumite 
    def orbital_strike(self, opponent, opponent_is_user=False):
            base_damage = 120
            extra_damage = 30


            if isinstance(opponent, Speedster):
                base_damage -= 10
            elif isinstance(opponent, Wizard):
                base_damage += 15
        
            print(f"{self.name} is charging up for a brutal orbital strike!")
            if opponent_is_user == True:
                action = input("Do you want to 'attack' or 'defend'?").lower()
                if action == "attack":
                    if isinstance(opponent, Speedster):
                        move = input("Which attack move do you want to use? Either 'throw lightning' or 'speed rush'.").lower()
                    elif isinstance(opponent, Viltrumite):
                        move = input("Which attack move do you want to use? Either 'super punch' or 'sonic thunderclap'.").lower()
                    elif isinstance(opponent, Wizard):
                        move = input("Which attack move do you want to use? Either 'elemental spell' or 'energy strike'.").lower()
                
                    chance = random.random()
                    if chance < 0.3:
                        counter_damage = 0
                        if move in ["throw lightning", "super punch", "elemental spell"]:
                            counter_damage = 75
                        elif move in ["speed rush", "sonic thunderclap", "energy strike"]:
                            counter_damage = 60

                        print(f"You managed to strike before the orbital strike with {move}! You even delt {counter_damage} in doing so!")
                        self.health -= counter_damage
                        print(f"{self.name} is now on {self.health} health")
                        return 
                    else:
                        print(f"Your attempt to counter with {move} failed. You suffer the orbital strike with full force!")
                        opponent.health -= int(base_damage + extra_damage)
                        print(f"{opponent.name} is now on {opponent.health} health")
                        return 
                
                elif action == "defend":
                    
                    if isinstance(opponent, Speedster):
                        move = input("Which defense move do you want to use? either 'phase' or 'speed dodge'")
                    elif isinstance(opponent, Viltrumite):
                        move = input("Which defence move do you want to use? Either 'invulnerable block' or 'aerial evasion' ")
                    elif isinstance(opponent, Wizard):
                        move = input("Which defence move do you want to use? Either 'mystic shield' or 'mirror duplicate'.")

                #Calculate defence success
                    reduction = 0 
                    if move in ["phase", "invulnerable block", "mirror duplicate"]:
                        chance = random.random()
                        if chance < 0.45:
                            print(f"Your {move} was successful! You completely evaded the orbital strike!")
                            reduction = 1
                            opponent.health -= int(base_damage * (1 - reduction))
                            print(f"{opponent.name} is now left with {opponent.health} health.")
                            return
                        else:
                            print(f"Your {move} was timed badly. You take the full force of the orbital strike")
                            opponent.health -= int(base_damage * (1 - reduction))
                            print(f"{opponent.name} is now left with {opponent.health} health.")
                            return
                
                    elif move in ["speed dodge", "aerial evasion", "mystic shield"]:
                        chance = random.random()
                        if chance < 0.65:
                            print(f"Your {move} was successful in avoiding the full contact of the orbital strike! You still however suffered the after shock unfortunately.")
                            reduction = 0.5
                            opponent.health -= int(base_damage * (1 - reduction))
                            print(f"{opponent.name} is now left with {opponent.health} health.")
                            return
                        else:
                            print(f"Your {move} was unsuccessful, you are unable to avoid the full contact of the orbital strike.")
                            reduction = 0
                            opponent.health -= int(base_damage * (1 - reduction))
                            print(f"{opponent.name} is now left with {opponent.health} health.")
                            return
                    else:
                        print("Invalid choice! You hesitated and took the force of the orbital strike!")
                        opponent.health -= base_damage
                        print(f"{opponent.name} is now at {opponent.health} health.")
                        return 
            
            #CPU logic
            else:
                cpu_action = random.choice(["attack", "defend"])

            #CPU Attack logic
                if cpu_action == "attack":
                    print(f"{opponent.name} attempts to counter-attack!")
                    if isinstance(opponent, Speedster):
                        available_moves = ["throw lightning", "speed rush"]
                    elif isinstance(opponent, Viltrumite):
                        available_moves = ["super punch", "sonic thunderclap"]
                    elif isinstance(opponent, Wizard):
                        available_moves = ["energy strike", "elemental spell"]

                    chosen_move = random.choice(available_moves)
                    counter_chance = 0.3
                    if random.random() < counter_chance:
                        counter_damage = 0
                        if chosen_move in ["throw lightning", "super punch", "elemental spell"]:
                            counter_damage = 75
                        elif chosen_move in ["speed rush", "sonic thunderclap", "energy strike"]:
                            counter_damage = 60
                    
                        self.health -= counter_damage
                        print(f"{opponent.name} succeeded in attempting their {chosen_move}! They have dealt {counter_damage} to {self.name} rather than suffering the force of the orbital strike!")
                        print(f"{self.name} is now left with {self.health} health")
                        return 0
                    else:
                        print(f"{opponent.name} failed the counter attack to the super sonic punch. Therefore suffering the full unlimited force of the strike!")
                        opponent.health -= int(base_damage + extra_damage)
                        print(f"{opponent.name} is now at {opponent.health} health")
                        return 
                elif cpu_action == "defend":
                    print(f"{opponent.name} attempts to evade the orbital strike!")
                    reduction = 0
                    if isinstance(opponent, Speedster):
                        available_defences = ["phase", "speed dodge"]
                    elif isinstance(opponent, Viltrumite):
                        available_defences = ["invulnerable block", "aerial evasion"]
                    elif isinstance(opponent, Wizard):
                        available_defences = ["mystic shield", "mirror duplicate"]

                    chosen_defence = random.choice(available_defences)
                    if chosen_defence in ["phase", "invulnerable block", "mirror duplicate"]:
                        defence_chance = 0.45
                        if random.random() < defence_chance:
                            print(f"The {chosen_defence} was successful! {opponent.name} managed to completely evade the orbital strike, suffering no damage at all!")
                            reduction = 1
                            opponent.health -= int(base_damage * (1 - reduction))
                            print(f"{opponent.name} is now left with {opponent.health} health.")
                            return
                        
                        else:
                            print(f"The {chosen_defence} was unsuccessful.")
                            reduction = 0
                            opponent.health -= int(base_damage * (1 - reduction))
                            print(f"{opponent.name} is now left with {opponent.health} health.")
                            return
                        
                    elif chosen_defence in ["speed dodge", "aerial evasion", "mystic shield"]:
                        defence_chance = 0.65
                        if random.random() < defence_chance:
                            print(f"The {chosen_defence} was successful in avoiding the initial contact of the orbital strike! {opponent.name} was not able to escape the after shock though.")
                            reduction = 0.5
                            opponent.health -= int(base_damage * (1 - reduction))
                            print(f"{opponent.name} is now left with {opponent.health} health.")
                            return
                        else:
                         print(f"The {chosen_defence} was unsuccessful.")
                         reduction = 0
                         opponent.health -= int(base_damage * (1 - reduction))
                         print(f"{opponent.name} is now left with {opponent.health} health.")
                         return
                            
                    






#Class of Wizard
class Wizard:
    def __init__(self, name, power_level, morality):
        self.name = name 
        self.power_level = power_level
        self.health = 200
        self.morality = morality

    def __repr__(self):
         return "{name} is a {morality} that also happens to be a master of the Mystic Arts. Their expertise in Wizardy makes them a very powerful wizard with the magic level of {power_level} ".format(name = self.name, morality = self.morality, power_level = self.power_level)
    
    #Regular Actions of Wizard
    def energy_strike(self, opponent):
        damage = 55 
        if isinstance(opponent, Viltrumite):
            damage += 5
        elif isinstance(opponent, Speedster):
             damage -= 5

        if self.power_level > 170:
            damage += 15
        elif self.power_level > 200:
            damage += 30
        
        opponent.health -= damage 
        print(f"{self.name} has used their magic power to strike {opponent.name} with an aenergy blast! {opponent.name} is now at {opponent.health} health")
        return 
    
    def elemental_spell(self, opponent):
        damage = 70

        if isinstance(opponent, Speedster):
            damage += 15

        if self.power_level > 170:
             damage += 15
        elif self.power_level > 200:
             damage += 30
        
        opponent.health -= damage 
        print(f"{self.name} has conjured an elemental spell, which launches all  of the base elements at {opponent.name} at a high velocity. Leaving them at {opponent.health} health")
        return 

    
    def healing_spell(self):
        heal = 35

        if self.power_level > 170:
             heal += 10
        elif self.power_level > 200:
             heal += 20

        
        self.health += heal
        if self.health >= 200:
            print(f"{self.name} is at full health!")
            self.health = 200
            return
        
        print(f"{self.name} has used a healing spell, boosting their health up to {self.health}!")
        return 

    def arcane_cataclysm(self, opponent, opponent_is_user=False):
            base_damage = 110
            extra_damage = 30


            if isinstance(opponent, Speedster):
                base_damage -= 10
            elif isinstance(opponent, Viltrumite):
                base_damage += 20
        
            print(f"{self.name} is charging up for a deadly arcane cataclysm!")
            if opponent_is_user == True:
                action = input("Do you want to 'attack' or 'defend'?").lower()
                if action == "attack":
                    if isinstance(opponent, Speedster):
                        move = input("Which attack move do you want to use? Either 'throw lightning' or 'speed rush'.").lower()
                    elif isinstance(opponent, Viltrumite):
                        move = input("Which attack move do you want to use? Either 'super punch' or 'sonic thunderclap'.").lower()
                    elif isinstance(opponent, Wizard):
                        move = input("Which attack move do you want to use? Either 'elemental spell' or 'energy strike'.").lower()
                
                    chance = random.random()
                    if chance < 0.3:
                        counter_damage = 0
                        if move in ["throw lightning", "super punch", "elemental spell"]:
                            counter_damage = 75
                        elif move in ["speed rush", "sonic thunderclap", "energy strike"]:
                            counter_damage = 60

                        print(f"You managed to strike before the arcane cataclysm with {move}! You even delt {counter_damage} in doing so!")
                        self.health -= counter_damage
                        print(f"{self.name} is now at {self.health} health.")
                        return 
                    else:
                        print(f"Your attempt to counter with {move} failed. You suffer the arcane cataclysm with full force!")
                        opponent.health -= int(base_damage + extra_damage)
                        print(f"{opponent.name} is now left with {opponent.health} health")
                        return 
                
                elif action == "defend":
                    
                    if isinstance(opponent, Speedster):
                        move = input("Which defense move do you want to use? either 'phase' or 'speed dodge'")
                    elif isinstance(opponent, Viltrumite):
                        move = input("Which defence move do you want to use? Either 'invulnerable block' or 'aerial evasion' ")
                    elif isinstance(opponent, Wizard):
                        move = input("Which defence move do you want to use? Either 'mystic shield' or 'mirror duplicate'.")

                #Calculate defence success
                    reduction = 0 
                    if move in ["phase", "invulnerable block", "mirror duplicate"]:
                        chance = random.random()
                        if chance < 0.45:
                            print(f"Your {move} was successful! You completely evaded the arcane cataclysm!")
                            reduction = 1
                            print(f"{opponent.name} is on {opponent.health} health")
                        else:
                            print(f"Your {move} was timed badly. You take the full force of the arcane cataclysm")
                            opponent.health -= base_damage
                            print(f"{opponent.name} is now on {opponent.health} health")
                
                    elif move in ["speed dodge", "aerial evasion", "mystic shield"]:
                        chance = random.random()
                        if chance < 0.65:
                            print(f"Your {move} was successful in avoiding the full contact of the arcane cataclysm! You still however suffered the after shock unfortunately.")
                            reduction = 0.5
                            opponent.health -= int(base_damage * (1 - reduction))
                            print(f"{opponent.name} is now on {opponent.health}")
                        else:
                            print(f"Your {move} was unsuccessful, you are unable to avoid the full force of the arcane cataclysm.")
                            reduction = 0
                            opponent.health -= int(base_damage * (1 - reduction))
                            print(f"{opponent.name} is now at {opponent.health} health")
                            return
                    
                    else:
                        print("Invalid choice! You hesitated and took the full force of the arcane cataclysm!")
                        opponent.health -= base_damage
                        return 
            
            #CPU logic
            else:
                cpu_action = random.choice(["attack", "defend"])

            #CPU Attack logic
                if cpu_action == "attack":
                    print(f"{opponent.name} attempts to counter-attack!")
                    if isinstance(opponent, Speedster):
                        available_moves = ["throw lightning", "speed rush"]
                    elif isinstance(opponent, Viltrumite):
                        available_moves = ["super punch", "sonic thunderclap"]
                    elif isinstance(opponent, Wizard):
                        available_moves = ["energy strike", "elemental spell"]

                    chosen_move = random.choice(available_moves)
                    counter_chance = 0.3
                    if random.random() < counter_chance:
                        counter_damage = 0
                        if chosen_move in ["throw lightning", "super punch", "elemental spell"]:
                            counter_damage = 75
                        elif chosen_move in ["speed rush", "sonic thunderclap", "energy strike"]:
                            counter_damage = 60
                    
                        self.health -= counter_damage
                        print(f"{opponent.name} succeeded in attempting their {chosen_move}! They have dealt {counter_damage} to {self.name} rather than suffering the force of the arcane cataclysm!")
                        print(f"{self.name} isn now at {self.health} health! ")
                        return 
                    else:
                        print(f"{opponent.name} failed the counter attack to the arcane cataclysm. Therefore suffering the full unlimited force of the cataclysm!")
                        opponent.health -= int(base_damage + extra_damage)
                        print(f"{opponent.name} is now at {opponent.health} health!")

                        return 
                elif cpu_action == "defend":
                    print(f"{opponent.name} attempts to evade the arcane cataclysm!")
                    reduction = 0
                    if isinstance(opponent, Speedster):
                        available_defences = ["phase", "speed dodge"]
                    elif isinstance(opponent, Viltrumite):
                        available_defences = ["invulnerable block", "aerial evasion"]
                    elif isinstance(opponent, Wizard):
                        available_defences = ["mystic shield", "mirror duplicate"]

                    chosen_defence = random.choice(available_defences)
                    if chosen_defence in ["phase", "invulnerable block", "mirror duplicate"]:
                        defence_chance = 0.45
                        if random.random() < defence_chance:
                            print(f"The {chosen_defence} was successful! {opponent.name} managed to completely evade the arcane cataclysm, suffering no damage at all!")
                            reduction = 1
                            opponent.health -= int(base_damage * (1 - reduction))
                            print(f"{opponent.name} is now at {opponent.health} health")
                        else:
                            print(f"The {chosen_defence} was unsuccessful.")
                            reduction = 0
                            opponent.health -= int(base_damage * (1 - reduction))
                    elif chosen_defence in ["speed dodge", "aerial evasion", "mystic shield"]:
                        defence_chance = 0.65
                        if random.random() < defence_chance:
                            print(f"The {chosen_defence} was successful in avoiding the initial contact of the arcane cataclysm! {opponent.name} was not able to escape the after shock though.")
                            reduction = 0.5
                            opponent.health -= int(base_damage * (1 - reduction))
                            print(f"{opponent.name} is now at {opponent.health} health!")
                            return
                        else:
                         print(f"The {chosen_defence} was unsuccessful.")
                         reduction = 0
                         opponent.health -= base_damage
                         print(f"{opponent.name} is now at {opponent.health} health!")
                         return
                        
                     
                



#Establish opponents for the user

#WIZARDS
#Low tier 
wiccan = Wizard("WICCAN", 150, "Hero")
clea = Wizard("CLEA", 150, "Hero")

kaecilius = Wizard("KAECILLIUS", 150, "Villain")
black_talon = Wizard("BLACK TALON", 150, "Villain")

#Mid tier
wong = Wizard("WONG", 180, "Hero")
mordo = Wizard("MORDO", 180, "Hero")

enchantress = Wizard("ENCHANTRESS", 180, "Villain")
belasco = Wizard("BELASCO", 180, "Villain")

#High tier
dr_strange = Wizard("DR STRANGE", 210, "Hero")
ancient_one = Wizard("ANCIENT ONE", 210, "Hero")

mephisto = Wizard("MEPHISTO", 210, "Villain")
dormammu = Wizard("DORMAMMU", 210, "Villain")


#VILTRUMITES 
#Low tier
kid_omni_man = Viltrumite("KID OMNI-MAN", 150, "Hero")
thadeus = Viltrumite("THADEUS", 150, "Hero")

lucan = Viltrumite("LUCAN", 150, "Villain")
thula = Viltrumite("THULA", 150, "Villain")

#Mid tier
terra = Viltrumite("TERRA", 180, "Hero")
ursaal = Viltrumite("URSAAL", 180, "Hero")

kregg = Viltrumite("GENERALL KREGG", 180, "Villain")
argaal = Viltrumite("ARGAAL", 180, "Villain")

#High tier
invincible = Viltrumite("INVINCIBLE", 210, "Hero")
omni_man = Viltrumite("OMNI-MAN", 210, "Hero")

thragg = Viltrumite("EMPEROR THRAGG", 210, "Villain")
conquest = Viltrumite("CONQUEST", 210, "Villain")
    
#SPEEDSTERS 

#Low tier 
impulse = Speedster("IMPULSE", 150, "Hero")
jesse_quick = Speedster("JESSE QUICK", 150, "Hero")

trajectory = Speedster("TRAJECTORY", 150, "Villain")
godspeed = Speedster("GODSPEED", 150, "Villain")

#Mid tier
kid_flash = Speedster("KID FLASH", 180, "Hero")
xs = Speedster("XS", 180, "Hero")

zoom = Speedster("ZOOM", 180, "Villain")
savitar = Speedster("SAVITAR", 180, "Villain")

#High tier
the_flash = Speedster("THE FLASH", 210, "Hero")
lightspeed = Speedster("Lightspeed", 210, "Hero")

reverse_flash = Speedster("REVERSE FLASH", 210, "Villain")
red_death = Speedster("RED DEATH", 210, "Villain")


#Group Opponents based on morality and level

low_tier_villains = [trajectory, godspeed, lucan, thula, kaecilius, black_talon]
low_tier_heroes = [wiccan, clea, impulse, jesse_quick, kid_omni_man, thadeus]

mid_tier_villains = [enchantress, belasco, zoom, savitar, kregg, argaal]
mid_tier_heroes = [kid_flash, xs, terra, ursaal, wong, mordo]

high_tier_villains = [red_death, reverse_flash, dormammu, mephisto, thragg, conquest]
high_tier_heroes = [the_flash, lightspeed, invincible, omni_man, dr_strange, ancient_one]


#Main game function to allow for restarts, and reboots
def main_game():
    
    #User's Character 
    user_name = input("Please enter the name you want for your charcater: ").upper()
    user_morality = input("Do you want be a villain or a hero? Type either 'hero' or 'villain' to confirm your choice.")
    user_class = input("What kind of super being do you want to be? Type either 'speedster', 'viltrumite' or 'wizard' to determine your abilities. ").lower()
    if user_class == 'speedster':
        user = Speedster(user_name, 150, user_morality)
    elif user_class == 'viltrumite':
        user = Viltrumite(user_name, 150, user_morality)
    elif user_class == 'wizard':
        user = Wizard(user_name, 150, user_morality)
    else:
        print("Input invalid, resume to default being of wizard.")
        user = Wizard(user_name, 150, user_morality)
    
    print(f"You are now {user.name}")
    print(user.__repr__())
    #Fight function
    def fight(user):
        if user.power_level == 150:
            if user.morality == 'hero':
                opponent = random.choice(low_tier_villains)
            elif user.morality == 'villain':
                opponent = random.choice(low_tier_heroes)
        elif user.power_level == 180:
            if user.morality == 'hero':
                opponent = random.choice(mid_tier_villains)
            elif user.morality == 'villain':
                opponent = random.choice(mid_tier_heroes)
        elif user.power_level == 210:
            if user.morality == 'hero':
                opponent = random.choice(high_tier_villains)
            elif user.morality == 'villain':
                opponent = random.choice(high_tier_heroes)
        elif user.power_level == 240:
            if user.morality == 'hero':
                opponent = random.choice(high_tier_villains)
            elif user.morality == 'villain':
                opponent = random.choice(high_tier_heroes)
        elif user.power_level == 270:
            print(f"Congratulations {user.name}! You have completed the game and become the most powerful being in the universe!")
            return 
            

        print(f"{user.name} is about to fight {opponent.name}")
        print(opponent.__repr__())
        user.health = 200
        while user.health > 0 and opponent.health > 0:
            print(f"Its your turn to act!")
            #Speedster Options when in a fight
            if isinstance(user, Speedster):
                valid_action = ["attack", "heal"]
                while True:
                    action = input("Do you want to attack or heal? ").lower()
                    if action in valid_action:
                        break
                    else:
                        print("Invalid choice. Please type 'attack' or 'heal'.")
            
                if action == 'heal':
                    user.speed_heal()
                elif action == 'attack':
                    valid_attacks = ['super sonic punch', 'speed rush', 'throw lightning']
                    while True:
                        attack = input("You have three attack options: 'super sonic punch', 'speed rush' and 'throw lightning'. Which attack do you want to use?").lower()
                        if attack in valid_attacks:
                            break
                        else:
                            print("Invalid attack please type either 'super sonic punch', 'speed rush' or 'throw lightning'.")
                
                    if attack == 'super sonic punch':
                        user.super_sonic_punch(opponent)
                    elif attack == 'speed rush':
                        user.speed_rush(opponent)
                    elif attack == 'throw lightning':
                        user.throw_lightning(opponent)

                #Viltrumite Options when in a fight
            elif isinstance(user, Viltrumite):
                valid_attacks = ['super punch', 'orbital strike', 'sonic thunderclap']
                while True:
                    attack = input("You have three attack options: 'super punch', 'sonic thunderclap' and 'orbital strike'. Which attack do you choose?").lower()
                    if attack in valid_attacks:
                        break
                    else:
                        print("Invalid attack. Please type either 'super punch', 'sonic thunderclap' or 'orbital strike'.")
            
                if attack == 'super punch':
                    user.super_punch(opponent)
                elif attack == 'sonic thunderclap':
                    user.sonic_thunderclap(opponent)
                elif attack == 'orbital strike':
                    user.orbital_strike(opponent)

                #Wizard options when in a fight
            elif isinstance(user, Wizard):
                valid_action = ["attack", "heal"]
                while True:
                    action = input("Do you want to attack or heal? ").lower()
                    if action in valid_action:
                        break
                    else:
                        print("Invalid choice. Please type 'attack' or 'heal'.")
            
                if action == 'heal':
                    user.healing_spell()
                elif action == 'attack':
                    valid_attacks = ['energy strike', 'elemental spell', 'arcane cataclysm']
                    while True:
                        attack = input("You have three attack options: 'energy strike', 'elemental spell' and 'arcane cataclysm'. Which attack do you choose? ")
                        if attack in valid_attacks:
                            break
                        else:
                            print("Invallid attack. Please type either 'energy strike' 'elemental spell' or 'arcane cataclysm'")
                
                    if attack == 'energy strike':
                        user.energy_strike(opponent)
                    elif attack == 'elemental spell':
                        user.elemental_spell(opponent)
                    elif attack == 'arcane cataclysm':
                        user.arcane_cataclysm(opponent)
            

            #CPU Logic within the fight
        
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated! Congratulations on your great victory!")
                user.power_level += 30
                user.health = 200
                print(f"You are now at power level {user.power_level}")
                return True
            elif user.health <= 0:
                print(f"{user.name} has unfortunately been defeated by {opponent.name}. Play again?")
                return False
            else:
                print(f"It is now {opponent.name}'s turn to fight back!")
                if isinstance(opponent, Speedster):
                    choices = ['attack', 'heal']
                    cpu_choice = random.choice(choices)
                    if cpu_choice == 'attack':
                        attacks = [opponent.super_sonic_punch, opponent.speed_rush, opponent.throw_lightning]
                        cpu_action = random.choice(attacks)
                        if cpu_action == opponent.super_sonic_punch:
                            cpu_action(user, opponent_is_user = True)
                        else:
                            cpu_action(user)
                    else:
                        opponent.speed_heal()
                
                elif isinstance(opponent, Viltrumite):
                    actions = [opponent.orbital_strike, opponent.sonic_thunderclap, opponent.super_punch]
                    cpu_action = random.choice(actions)
                    if cpu_action == opponent.orbital_strike:
                        cpu_action(user, opponent_is_user = True)
                    else:
                        cpu_action(user)
                
                elif isinstance(opponent, Wizard):
                    choices = ['attack', 'heal']
                    cpu_choice = random.choice(choices)
                    if cpu_choice == 'attack':
                        attacks = [opponent.elemental_spell, opponent.energy_strike, opponent.arcane_cataclysm]
                        cpu_action = random.choice(attacks)
                        if cpu_action == opponent.arcane_cataclysm:
                            cpu_action(user, opponent_is_user = True)
                        else:
                            cpu_action(user)
                    else:
                        opponent.healing_spell()

    #Loop to check who won the fight 
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated! Congratulations on your great victory!")
            user.power_level += 30
            user.health = 200
            return True
        elif user.health <= 0:
            print(f"{user.name} has unfortunately been defeated by {opponent.name}.")
            return False

    
    while True:
        result = fight(user)
        if result:  # user won
            cont = input("Press any key to fight another opponent, or just Enter to quit: ")
            if cont == "":
                break
        elif user.power_level == 270:
            print("Congratulations, you beat the game!!")
            break
        else:  # user lost
            print(f"{user.name} has perished in battle. You have unfortunately lost the game.")
            break


    
    
    
#Loop to check if user wishes to play again
while True:
    main_game()
    play = input("Game over! Press any key to play again, or just Enter to quit: ")
    if play == "":
        print("Thanks for playing!")
        break

        





