def main():
  user_input= input("Enter the numbers: ")

  try:
      user_input = [int(entry) for entry in user_input.split()]
  except:
      print("One or more input in the list was not a integer.")
      return

  print(" List of integers:", user_input)
if __name__ == "__main__":
  main()
