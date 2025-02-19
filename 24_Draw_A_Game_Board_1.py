def ttt(n):
    x = (" ---")
    y = ("|   ")
    count = 0
    while count < n:
        print (n*x)
        print (n*y +"|")
        count += 1
        if count == n:
            print (n*x)
            break

if "__main__" == __name__:
    n = int(input("What size of the board do you want to generate? "))
    ttt(n)