import random

def main():
	num = list(range(48,58))
	low = list(range(97,123))
	up = list(range(65,91))
	l = num + low + up
	a = str()
	for _ in range(6):
		a += chr(random.choice(l))
	print(a)

if __name__ == '__main__':
	main()