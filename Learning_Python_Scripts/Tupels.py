def mystery(n):
    
    if n < 0:
        print(n)
        return 2 * n
    else:
        return mystery(n - 1) + n
    
    
def main():
    print(mystery(3))
main()
