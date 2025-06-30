#SwapCase -----------------------------------
def swap_case(words):
    return words.swapcase()
if __name__=='__main__':      #does not run when the file is imported {outside run but not inside.}        
    words=input("enter any words:")
    swap=swap_case(words)
    print(swap)

#Split & Join ------------------------------------------------
def split_join(words):
    s=words.split(" ")      # space is mandatory btw double quotes
    s="-".join(s)           #str.split(separator,maxsplit),,,,,str to split on/max no. of split
    return s                 # ex: text.split(":",4)
letter=input("enter any letter:")
result=split_join(letter)
print(result)
