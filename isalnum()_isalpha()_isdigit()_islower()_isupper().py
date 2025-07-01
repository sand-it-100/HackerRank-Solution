if __name__=="__main__":
    s=input("Enter :")
    print(any(c.isalnum() for c in s))   # Any --> This checks each character, and prints True if at least one satisfies the condition. 
    print(any(c.isalpha() for c in s))   # isalnum --> a-z ,A-Z & 0-9
    print(any(c.isdigit() for c in s))    # isalpha --> a-z, A-Z 
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))