# Interactive Sales Calculator

product = input("Product name: ")

price = float(input("Unit price: "))

quantity = int(input("Quantity: "))

total = price * quantity

print("------------------")
print("SALES SUMMARY")
print("Product:", product)
print("Quantity: ", quantity)
print("Total: R$", total)