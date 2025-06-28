## The-Shooter_Game
## Project-Goal
## ✅ What Result Did the Customer Want to Get?

The customer aimed to create a complete and playable 2D shooting game with the following key features:

- 🎯 **Game Goal:** Control a rocket to destroy falling UFOs before they reach the bottom of the screen.
- 🎮 **Controls:** Use the **Left Arrow (←)** and **Right Arrow (→)** keys to move the rocket, and press the **Spacebar** to shoot bullets.
- ✅ **Win Condition:** Shoot down **10 UFOs** to win the game; a **“YOU WIN!”** message is displayed.
- ❌ **Lose Condition 1:** If **10 UFOs** pass the rocket and reach the bottom, the player loses.
- ❌ **Lose Condition 2:** If the rocket **collides with any UFO**, the game ends immediately with a **“YOU LOSE!”** message.
- 📊 **Score & UI:** The top-left corner of the screen displays the current **score** (UFOs destroyed) and **missed count** (UFOs that got past).
- 💥 **Bullet System:** Bullets are fired straight upward and destroy UFOs upon collision. Both the bullet and the UFO are removed from the game.
- 🔁 **Game Reset:** After a win or a loss, the game automatically resets the rocket, enemies, and score to start a new round.
- 🚀 **Objective:** Survive, aim carefully, and shoot down UFOs to win before letting too many escape.
## The developed project includes the following components:
- main.py
- spriteclass.py
- GameSprite
- Player
- Bullet
- Enemy
- Rocket.png
- Ufo.png
- Bullet.png
- Galaxy.png
## (The program interface is simple and functional ...)
- The player controls a rocket that can move left and right using arrow keys.
- Pressing the spacebar fires bullets upward from the rocket to hit enemies.
- If a bullet hits a UFO, both disappear and the player's score increases.
- If a UFO reaches the bottom without being hit, it is counted as “missed.”
- If a UFO touches the rocket, the game ends instantly with a “YOU LOSE” message.
- Win: Destroy 10 UFOs.
- Lose: Miss 10 UFOs or collide with one.
- After a win or loss, the game will reset and start back.
## (There are three types of characters in the game ...)
- Rocket
 - Controlled by the player using arrow keys.
- Enemy
 - If hit by the bullet, it disappears and increase the player’s score.
- Bullet.
 - Fired by the rocket when the player pressed the spacebar
## (Extras: auto-restart of the game, increased difficulty ...)
Auto restart:
- After win or loss, the game automatically  resets:
- The score and missed counters return to 0.
New enemies are spawned.
- The player can play again without restarting the program.
- Increased Difficulty:
- Each enemy UFO is given a random speed when it respawns.
- This makes the game more challenging.
## Project Prospects
## (Will the game make profit? Any possible improvements?)
The project prospects is :
- Add levels with increase difficulty(more enemies, faster speed).
- Make the enemies can shoot back to player.
- Allow two players to play together.

