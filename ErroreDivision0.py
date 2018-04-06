def divide(x, y):
  try:
        result = x // y
        return(result)
  except ZeroDivisionError:
        print("divison por 0")
  finally:
      print("error division")
      return(1)



print(divide(7,3))

print(divide(4,0))

print(divide(4,"hola"))
