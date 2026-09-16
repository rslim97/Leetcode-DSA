def gcd(a,b):
    r=a%b
    while r:
        a=b
        b=r
        r=a%b
    return b


if __name__ == '__main__':
    a,b=24,16
    res=gcd(a,b)
    print(res)

    # lcm(a,b)=a*b/gcd(a,b)