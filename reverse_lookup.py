#reverse_lookup
#brupoon

def histogram(str):
    d = dict()
    for char in str:
        d[char] = 1 + d.get(char, 0)
    print(d)

def reverse_lookup(d, v):
	for k in d:
		if d[k] == v:
			return i
	raise ValueError

def reverse_lookup2(d, v):
	reverse = list()
	for k in d:
		if d[k] == v:
			reverse.append(k)
	return reverse


if __name__ == "__main__":
	h = histogram("parrot")
	print(h)
	r = reverse_lookup(h, 2)
	print(r)