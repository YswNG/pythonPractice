import random

def main():
	num = list(range(48,58))
	lower = list(range(97,123))
	upper = list(range(65,91))

	l = num + lower + upper
	print(l)
	a = chr(random.choice(l))
	print(a)


if __name__ == '__main__':
	main()