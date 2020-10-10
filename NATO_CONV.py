Program = int(input("To Code a message enter 1 / To decode a message enter 2 \n >>>"))


def Convert():
    My_text = input("what's your text: "  )

    My_text = My_text.lower()
    for letter in My_text:
    
        if letter == "a":
            print("ALPHA", end= " ")
            
        elif letter == "b":
            print("BRAVO", end=" ")
            
        elif letter == "c":
            print("CHARLIE", end=" ")
        
        elif letter == "d":
            print("DELTA" , end=" ") 
            
        elif letter == "e":
            print("ECHO" , end=" ")
            
        elif letter == "f":
            print("FOXTROT" , end=" ")
            
        elif letter == "g":
            print("GOLF" , end=" ")
        
        elif letter == "h":
              print("HOTEL" , end=" ")
            
        elif letter == "i":
            print("INDIA" , end=" ")
            
        elif letter == "j":
            print("JULIETT" , end=" ")
        
        elif letter == "k":
            print("KILO" , end=" ")
        
        elif letter == "l":
            print("LEMON" , end=" ")
        
        elif letter == "m":
            print("MIKE" , end=" ")
            
        elif letter == "n":
            print("NOVEMBER" , end=" ")
            
        elif letter == "o":
            print("OSCAR" , end=" ")
            
        elif letter == "p":
            print("PAPA" , end=" ")
            
        elif letter == "q":
            print("QUEBEC" , end=" ")
        
        elif letter == "r":
            print("ROMEO" , end=" ")
            
        elif letter == "s":
            print("SIERRA" , end=" ")
        
        elif letter == "t":
            print("TANGO" , end=" ")
            
        elif letter == "u":
            print("UNIFORM" , end=" ")
        
        elif letter == "v":
            print("VICTOR" , end=" ")
            
        elif letter == "x":
            print("X-RAY" , end=" ")
                
        elif letter == "y":
            print("WHISKEY" , end=" ")
                
        elif letter == "z":
            print("ZULU" , end=" ")
            
        elif letter == " ":
            print("/", end=" ")
 
def decode():
      My_code = input("what's your code: ")     
      My_code = My_code.lower()
      My_code = My_code.strip()
      for code in My_code: 
          if code == "alpha":
              print("a" , end = " ")
          elif code == "bravo":
              print("b")
          elif code == "charlie":
               print("c")
          elif code == "delta":
               print("d")
          elif code == "echo":
               print("h")
          elif code == "foxtrot":
               print("f")
          elif code == "golf":
               print("g")
          elif code == "hotel":
               print("h")
          elif code == "india":
               print("i")
          elif code == "":
              print()            
          elif code == "/":
               print(" ")
     
   

    
if Program == 1:
    Convert()
elif Program == 2:
    decode()
else: 
    print("Please inseart 1 or 2")
