"""You are given a string s and width w.
Your task is to wrap the string into a paragraph of width w.

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to"""

import textwrap
if __name__=="__main__":
    def text_wrap(paragraph,width):        #width --> "maximum number of line allowed in a line."
        return textwrap.fill(paragraph,width)    #newline after each words.
    string,max_width=input("Enter str:"),int(input("Enter maximun width:"))
    result=text_wrap(string,max_width)
    print(result)



import textwrap
if __name__=="__main__":
    def text_wrap(paragraph,width):
        return textwrap.wrap(paragraph,width)    #collection of string of defined width in a LIST.
    string,max_width=input("Enter str:"),int(input("Enter maximun width:"))
    result=text_wrap(string,max_width)
    print(result)