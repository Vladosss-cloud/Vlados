import random

def coin_toss():
  result = random.randint(0, 1)

  if result == 0:
    return "Орел"
  else:
    return "Решка"

toss_result = coin_toss()
print(f"Выпало: {toss_result}")