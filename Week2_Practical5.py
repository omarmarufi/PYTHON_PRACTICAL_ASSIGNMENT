def pattern(n):
      for i in range(-1 , n):
           for j in range(0 , i + 1):
                print("* " , end ="")
           print("\r")
      for i in range(n , 0 , -1):
          for j in range(0 , i - 1):
               print("* ", end = "")
          print("\r")
pattern(4)