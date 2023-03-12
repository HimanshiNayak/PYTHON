# 1 . write a program to display a user enters a name followed by good afternoon ;-



name = input("Enter your name ,")
greeting = " Good Afternoon"
print(name + greeting)
# 2. write a program to fill ina letter tempelate given below with name and date :- 
# letter = '''dear <|Name|>,
                  #  you are selected !
                  # <|Date|>


letter = ''' Dear <|Name|> 
        Greetings from ABC coding house . I am happy to tell you about your selection .
        you are selected !
        have a graet day ahead !
        Date : <|date|>
        '''
name = input(" Enter your name")
date = input("Enter todays date")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("|Date|>" , date)
print(letter)

## find double spaces in the line . , will tell the no. on which   falls
st = "this is a string with double spaces   ."

doubleSpaces = st.find(" ")
print(doubleSpaces)
#replace doublespaces by sifle space
st =st.replace("  ", " ")
print(st)
## write a program to format the following letter by using escape sequence charace ers
letter = "Dear X , \n the wheather today is nice .\n That`s the beauty of mother earth !"
print(letter)
