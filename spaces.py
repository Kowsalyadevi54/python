def spaces:
   number_of_spaces=0
   with open(TEXT,"r")as fh:
      for line in fh:
          space=line.split()
          for i  in space:
              for char in i:
                  if char.isspace():
                     number_of_spaces+=1
   return number_of_spaces
            
