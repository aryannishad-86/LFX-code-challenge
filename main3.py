def removingitems(integers):
  final= [num for index, num in enumerate(integers) if (index + 1) % 2 != 0]

  return final

def main():
  user= input("Enter numbers: ")
  try:
      user1 = [int(entry) for entry in user.split()]
  except:
      print("Numbers are incorrect")
      return

  modified = removingitems(user1)
  print("Original Numbers:", user1)
  print("Numbers after modification", modified)

if __name__ == "__main__":
  main()
