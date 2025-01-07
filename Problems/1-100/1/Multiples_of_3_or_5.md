# Multiples of 3 or 5
This file will contain my understanding and thought process behind solving this problem.
## The problem
If we list all the natural number below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.

Find the sum of all multiples of 3 or 5 below 1000.

## Thought process
This is a pretty simple problem and thus the solution is pretty easy to think about.

We just use a variable to store the sum and use a for loop to check every number from 1 to 1000 and check if divisible by either 3 or 5. And then if so add to our variable.

With this we get the correct total of 233,168

## Languages
### Python
For this solution I didn't need to use two functions to check if the number was divisible by 3 or 5 however its just good programming practice, and it makes my code look nicer.

Instead, I could have just used a conditional statement however since each function returns a boolean they work the same and especially in the future with more complex solutions it makes it easier to explain.
### Java