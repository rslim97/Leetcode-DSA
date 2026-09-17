
if __name__ == '__main__':
    s='abcabc'
    # for i in range(len(s)):
    #     # print("i",i)
    #     for j in range(i,len(s)):
    #         # print("j",j)
    #         print(s[i:j+1])

    # for i in range(1,len(s)):
    #     for j in range(len(s)):
    #         print(s[j:i+1])

    l=0
    for r in range(len(s)):
        print(s[l:r+1])
        # l+=1