from random import randint
nuns = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(nuns, end=' ')
print(f"\nO maior número foi: {max(nuns)}")
print(f"O menor número foi: {min(nuns)}")