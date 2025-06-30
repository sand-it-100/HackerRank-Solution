#Mutable the string using the LIST and SLICING...........
def mutate_str(string,position,character):
    l=list(string)
    l[position]=character
    str=''.join(l)     # it's join the each char in list in order to form string.
    return str
string=input("Enter sring:")
pos,char=input().split()          #there must be space during taking input eg: 3 k --------------------
result=mutate_str(string,int(pos),char)        # 3 was in str SO, it is mandatory to convert this into integer
print(result)


#number of times substring occurs---------------
def occurence(string,sub_string):
    count=0
    for i in range(len(string)-len(sub_string) +1):      # "kmklokmkmk" & kmk...(10-3 +1)=8,,,,search upto 7 letter.
        if string[i:i+len(sub_string)]==sub_string:      # 2:2+3 means 2 to 5,,,,means searching the substring of letter 3 place
            count+=1
    return count
str=input("Enter string:")
sub=input("Enter substing:")
result=occurence(str,sub)
print(result)