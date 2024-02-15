# Treasure-Island-Game

This Python code represents a text-based adventure game called "Bhim's Treasure Island." Here's a breakdown of how the code works:

The print function is used to display introductory messages to the player.

The input function prompts the player to make a choice at the beginning of the game, asking them whether they want to go left or right at a crossroad. The input is converted to lowercase using the lower() method for easier comparison.

The first if statement checks the player's choice. If the player chooses "left", the game continues to the next stage; otherwise, it prints "Game Over" and ends the game.

Inside the "left" branch, another input function asks the player whether they want to wait for a boat or swim across the lake to reach an island. Again, the input is converted to lowercase.

The second if statement checks the player's choice after reaching the island. If the player chooses to "wait," they can proceed to the next stage; otherwise, the game ends with a "Game Over" message.

If the player waits, they are prompted to choose a door among three options: red, yellow, or blue. Their choice is converted to lowercase for comparison.

The third if statement evaluates the player's choice of door. Depending on their choice, different outcomes occur:

If the player chooses the red door, they encounter a room full of fire and lose the game.
If the player chooses the blue door, they enter a room filled with beasts and lose the game.
If the player chooses the yellow door, they find the treasure and win the game.
If the player chooses any other color, they are informed that the chosen door doesn't exist, and the game ends.
If the player chose to swim instead of waiting for a boat, they encounter angry trout and lose the game.

If the player initially chose "right" at the crossroad, they fall into a hole, resulting in a "Game Over" message.

This code presents a simple text-based adventure game where the player makes choices to navigate through different scenarios until they either find the treasure and win or encounter a situation leading to their defeat.
