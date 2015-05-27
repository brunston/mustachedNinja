def foo(bar):
	print(bar)
	text = baz(bar)
	print(text)

def baz(ara):
	bar = "newBAR"
	ara = "newARA"

foo("original")