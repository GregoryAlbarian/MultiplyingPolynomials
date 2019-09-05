"""
takes in a polynomial as a list where the indices are the exponent on the value
print out the  polynomials in a form that looks reasonable
"""
def print_polynomial (polynomial):
	for k in range(len(answer)-1,-1,-1):
		if k==0:
			print(answer[k]," + ",end="")
		elif answer[k]==0:
			continue
		else:
			print(answer[k],"x^",k,end="")

		if k!=0:
			print(" + ",end="")
	print("")


polynomial1 = [1,6,7]
polynomial2 = [3, 0, 2, 3]

SIZE = len(polynomial2)*len(polynomial2)

#used Google for the const.SIZE idea
answer = [0]*SIZE#got the idea from Quora

for i in range(0, len(polynomial1)):
	for j in range(0, len(polynomial2)):
		answer[i+j] += polynomial1[i]*polynomial2[j]
	#i + j because I add exponents
	#I need += because different exponents can still add up to the same number

print(answer)
print_polynomial(answer)
