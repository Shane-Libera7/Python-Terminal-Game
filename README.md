# Python-Terminal-Game
*A Python terminal based game in which the user is given choices for their own character which affects the opponents they face along with the "moves" they have at their disposal.*


The user has a choice between 3 different types of characters: Wizard, Viltrumite and Speedster.

Their opponents in the game is determined by two things, their power level (which increases after winning a fight) and whether they are either a hero or a villain. Heroes go up against villains and villains go up against heroes.

Both opponent and user start with 200 health and aim to get the other's health down to 0.

## Classes of Beings
### Speedster
- A speedster has both healing and attack properties.
- The attack moves include "throw lightning", "speed rush" and "supersonic punch"
- Speedster are less sensitive to viltrumite attacks than Wizards but they are especially vulerable to the "elemental spell" attack from wizards
  - Inspired by DC Comics' The Flash

### Viltrumite
- Viltrumite oinly has attacking properties but they take less damage in general from regular attacks compared to both speedsters and wizards
- A viltrumites regular attack moves also deal more damage in general than speedsters and wizards
- the attack properties include "super punch", "sonic thunderclap" and "orbital strike"
- a viltrumite is alot more sensitive to their own "sonic thunderclap" compared to other regular attacks from any other class
  - Inspired by the Invincible Comics

### Wizard
- Wizards are in general more vulnerable to hits compared to both Speedsters and Viltrumites but they also have higher healing properties
- Attack moves include "energy strike", "elemental spell" and "arcane cataclysm"
  - Inspired by Marvel's Dr Strange


## Super Attack Moves
- Each types of character have three attack options, 2 normal attacks and one super attack.
- The super attack for speedster is "super sonic punch", for viltrumites its "orbital strike" and for wizards its "arcane cataclysm"
- The super attacks offer the opponent a window to act, they can either defend or counter attack and it is through random probability which decides whether or not the chosen move will work or not. If the opponent choses to attack, there is a chance that they will end up doing damage instead of suffering damage, but the liklihood of that chosem move working out is only 30%. Should that attack fail, they will suffer even extra damage on top of the base damage of the super attack move.
- The choice of defending has a higher chance of succeeding, there are two choices to defend, one move that will attempt completely evade the attack, and one which will half the damage of the base attack.
- The probability of completely evading all damage has a success probabilty of 45%, those said moves from each class are "phase" for speedsters, "invulnerable block" for viltrumites, and "mirror duplicate" for wizards.
- The chances of only suffering half the base damage is 65%, and those moves are "speed dodge" for speedsters, "aerial evasion" for viltrumnites and "mystic shield" for wizards  


## Power Level
- All users start at 150 power level and with every victory, their power levels increase by 30, making them come up against more formiddable opponents in the next fight
- The opponents power level go up to 210, and if the user reaches a power level of 270, they have completed the game
- As the power level increases, the higher damage is dealt on regular moves, along with higher healing properties from both speedsters and wizards 
- The opponents are chosen randomly within the power level class, but they can come against any class in each fight no matter the level. 


## Summary
The user has freedom to choose their name, whether they are a hero or villain and their abilities.Once that has been decided they then fight up to 4 opponents in hopes they can beat them and complete the game, if they are defeated its game over and the program must be restarted.
