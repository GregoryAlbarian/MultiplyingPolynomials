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
for k in range(len(answer)-1,-1,-1):
	if k==0:
		print(answer[k],end="")
	elif answer[k]==0:
		continue
	else:
		print(answer[k],"x^",k,end="")

	if k!=0:
		print(" + ",end="")
print("")
#put on Github
#put the bottom part in as a method for a second commit
#make a third commit for user input
#make a shell script for like a go to Desktop or go to hard drive
#download Grammarly Premium it's free for college students