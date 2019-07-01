# Pseudocode, recipes, & KISS

There are a bunch of ways to simplify coding - and many more ways to complicate it. As a programmer, it can't be helped that some things are more involved to code than others. Coding a clock, for example, might seem simple. Why, you've probably seen and used clocks most of your life. Turns out though, coding a clock takes some time and thought, and doesn't lend itself well to being coded out on the fly by a new programmer.

I recommend you try writing the "recipe" or step-by-step process (also called algorithm) on paper for a 12 hour clock with AM and PM, that can "tick" forward by a fixed amount of time (1 hour, in this case). To make this easier for you, let's just show the hour and AM/PM. How many variables might you need? Do you need any functions, lists or loops? By looking at the possibilities on paper, you have a chance to make clear your solution without touching any "real" code. Your mission is to find out, programmatically, what is the time 1 hour after 11am?

Accomplish this first, and then, after that, I'd encourage you to try minutes, seconds, and variable time jumps (ie. What is the time 3 minutes after 11:59pm? Or, how about 12 hours, 2 minutes and 5 seconds after 12:01:55am?).

Here's another challenge: try writing out the pseudo-code for a high score board name setter. Old school arcade games would typically give the player 3 letters and a "cursor" which could be adjusted with the arrow keys alone, and a "confirmation" button (for computers we might use the Enter key). So, the starting display letters might be AAA, and for me to set my name into the high score board I would adjust the letters to be AVI, and then confirm. As an alternative to writing out a "finished recipe" or "perfect pseudocode" (perfection is in the eye of the beholder, remember), you can also make a simple walkthrough as the player/user, or as the program (if that makes it easier for you). For example:

Step 1. The player sees a screen with the letters "AAA" and a cursor underneath the first "A".
Step 2. The player hits the right arrow key, and the cursor moves to be under the 2nd A".
Step 3. The player hits the down arrow key, and the 2nd "A" turns into a "B"
... and so on.
