

import random

symbols = ["🍒","🍇","🍉","7️⃣"]

results = random.choices(symbols, k=3)
jackpot = ["7️⃣","7️⃣","7️⃣"]

for i in range(len(results)):
  if i != len(results) - 1:
    print(results[i]+"  | ", end="")
  else:
    print(results[i])

if results == jackpot:
  print("Jackpot! 💰")
else:
  print("Thanks for playing!")