try:
    totalValue = int(input("Enter total value: "))
    value = int(input("Enter value: "))
    percentage = float(value/totalValue)*100

    print(f"Total value: {percentage}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be zero.")

