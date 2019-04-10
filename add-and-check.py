import csv 

# Define a Stock Class
class stock:
  # Set default values to the variables 
  name = ""
  category = ""
  netPrice = 0.0
  quantity = 0

  # Function to calculate the gross price
  def getGrossPrice(self):
    return self.netPrice * 1.23

# Open the CSV file with the current store inventory 
fopen = open("storeInventory.csv", "r")

# Set a temporary list 
tmp = []
# Define a products list 
productsList = []

# Read the store inventory file lines
for line in fopen:
  # Split the file content by comma
  tmp = line.rstrip().split(",")

  # Define a class for each product
  newProduct = stock()

  # Assign a values to the class
  newProduct.name = tmp[0]
  newProduct.category = tmp[1]
  newProduct.netPrice = float(tmp[2])
  newProduct.quantity = int(tmp[3])

  # Add the products to the list
  productsList.append(newProduct)

# Choice menu 
print("Inventory Management Software")
print("- - - - - - - -")
print("1) Add New Product to the Stock - PRESS 1")
print("2) Check Store Inventory - PRESS 2 ")
print("3) Exit - PRESS 3 ")

# User menu choice
menuChoice = int(input("Your Choice: "))

# Load up the screen to add the products to the store inventory  
if (menuChoice == 1):
  # Ask the user for the product: 
  # .name
  newProductName = raw_input("Product Name: ").lower()
  # .category
  newProductCategory = raw_input("Product Category: ").lower()
  # .price
  newProductNetPrice = float(input("Product Net Price: "))
  # .quantity
  newProductQuantity = int(input("Product Quantity: "))

  # Define a new product class with the given values 
  newProduct =[newProductName, newProductCategory, newProductNetPrice, newProductQuantity]

  # Append the product to the store inventory 
  with open(r'storeInventory.csv', 'a') as f:
      writer = csv.writer(f)
      writer.writerow(newProduct)

# Display all the products available in the store 
elif (menuChoice == 2):
  # Show off the items by the For Loop
  for product in productsList:
    # Display the product: 
    # .name
    print ("Name:", product.name.title()) 
    # .category
    print ("Category:",product.category.title())
    # .net price
    print ("Net Price:",product.netPrice)
    # .gross price
    print ("Gross Price:",product.getGrossPrice())
    # .quantity
    print ("Quantity:",product.quantity)

    print("- -")
    print("")

# Close the programme
elif (menuChoice == 3):
  quit()
