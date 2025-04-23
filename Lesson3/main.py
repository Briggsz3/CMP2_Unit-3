def divide(a: int, b: int):
  try:
    print(a/b)
  except TypeError or ZeroDivisionError:
    print("Parameter must be a number")
  except ZeroDivisionError:
    print("You can't divide by 0")
  else:
    return a/b

def main():
  results = []
  results.append(divide(5, 'a'))
  results.append(divide('5, 0))
  results.append(divide(5, 2))
  for result in results:
    if result is not None:
      print(result)
              
         
  
