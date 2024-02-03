def main():
  user_input= input("Enter the numbers:")
  try:
      integers= [int(entry) for entry in user_input.split()]
  except:
      print("Numbers are incorrect.")
      return
  if len(integers) % 10 != 0:
      print("The length of the list is not a multiple of 10.")
      return

  print("You entered the list of integers:", integers)

if __name__ == "__main__":
  main()
