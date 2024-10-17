# Prime Game

## Task 0 - Prime Game

### Mandatory

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

### Prototype:
```python
def isWinner(x, nums)

EXAMPLE

x = 3
nums = [4, 5, 1]

# First round: n = 4
# Maria picks 2 and removes 2, 4, leaving 1, 3
# Ben picks 3 and removes 3, leaving 1
# Ben wins because there are no prime numbers left for Maria to choose

# Second round: n = 5
# Maria picks 2 and removes 2, 4, leaving 1, 3, 5
# Ben picks 3 and removes 3, leaving 1, 5
# Maria picks 5 and removes 5, leaving 1
# Maria wins because there are no prime numbers left for Ben to choose

# Third round: n = 1
# Ben wins because there are no prime numbers for Maria to choose

# Result: Ben has the most wins

EXAMPLE OF USAGE

carrie@ubuntu:~/0x0A-primegame$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

carrie@ubuntu:~/0x0A-primegame$ ./main_0.py
Winner: Ben

