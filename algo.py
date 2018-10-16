#!/usr/local/bin/python
#Factorial,Permute,Combine Recursive algorithms
import math
import sys
def factorial(n):
	if n>1:
		return n*factorial(n-1)
	else:
		return n
def permutations(s,n):
	if s==n:return 1
	return (factorial(s)/(factorial(n)*factorial(s-n)))
def combinations(s,n):
	if s==n:return 1
	return (factorial(s)/factorial(s-n))
def main(arg):
	print("The factorial of %i is %i"%(int(arg[1]),factorial(int(arg[1]))))
	print("The permutations of %iP%i is %i"%(int(arg[1]),int(arg[2]),permutations(int(arg[1]),int(arg[2]))))
	print("The combinations of %iC%i is %i"%(int(arg[1]),int(arg[2]),combinations(int(arg[1]),int(arg[2]))))
if __name__=="__main__":
	main(sys.argv[0:])
