''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
    n = int(input("Enter a number: "))

    test = []
    
    a = 0
    
    for i in range(1, n+1):
        if i <= n:
            test.insert(-i, i)
    
    for j in range(1, len(test)+1):
        if j <= n:
            #print('\t')
            print(*test)
            test.pop()
    return

main()