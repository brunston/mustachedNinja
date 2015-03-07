#invert_dict from 11.4
def invert_dict(d):
	invert = dict()
	for key in d:
		value = d[key]
		if value not in invert:
			invert[value] = [key]
		else:
			invert[value].append(key)
	return invert

#using setdefault, write a more concise version of invert_dict

def invert_dict_set(d):
	invert = dict()
	for key in d:
		inverter = invert.setdefault(d[key], []).append(key)
	return invert

def main():
	dict1 = {'one': 1, 'two': 2, 'notthree': 1}
	dict1_invert = invert_dict(dict1)
	dict1_invert_set = invert_dict_set(dict1)
	print("dict1: ", dict1)
	print("dict1_invert: ", dict1_invert)
	print("dict1_invert_set: ", dict1_invert_set)


if __name__ == '__main__':
	main()