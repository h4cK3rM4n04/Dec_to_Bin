#Simple conversion de décimal en binaire!
def dectobin_1(c):
	if c == 0:
		return "00000000"
	res = ""
	if c < 2:
		return str(c)
	while c > 0:
		res = res + str(c % 2)
		c = c // 2
	return str(res[::-1])
	variable = c
print(dectobin_1(5))