import random
dice_sum = 0
dice_rolls = 2
for i in range(0,dice_rolls):
  roll = random.randint(1, 6)
  print(f'You rolled a {roll}')
  dice_sum += roll

print(f'You have rolled a total of {dice_sum}')

def main():
  print('You rolled a die')

if __name__== "__main__":
  main()