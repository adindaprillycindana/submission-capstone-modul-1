############################ Capstone Porject Modul  #################################
# Name  : Adinda Prilly Cindana
# Class : JCDS On Campus JKT
# Batch : 32

# Import modul
from tabulate import tabulate
from prettytable import PrettyTable
import time

# Initial dataset
listProduct = [
    ["101","Advertising Sign", "Miscellaneous", "Retail",5000000000,1.97,2.8,"Non Proportional","Active",120],
    ["201","Fire Insurance","Property","Retail",20000000000000,0.02,0.03,"Proportional","Inactive",110],
    ["401","Civil Engineering Completed Risk","Engineering","Corporate",1000000000,0.01,0.02,"Proportional","Freeze",90]
]

# Data in table format
product_headers = ["Product Code","Product Name","Class of Business","Customer Group","Sum Insured (IDR)","Net Rate (%)","Gross Rate (%)",
                   "Reinsurance Treaty","Status", "Number of Policies Issued"]

list_infoCode =[
    [1, "Miscellaneous"],
    [2, "Property"],
    [3, "Personal Accident"],
    [4, "Engineering"],
    [5, "Marine Cargo"],
    [6, "Marine Hull"],
    [7, "Property"],
    [8, "Energy Offshore/Onshore"],
    [9, "Liability"],
]

headers_code = ["First Digit", "Class of Business"]

dataInfo = [
    ["Product Name", str, ""],
    ["Class of Business", str, ""],
    ["Customer Group", str, ""],
    ["Sum Insured (IDR)", int, 0],
    ["Net Rate (%)", float, 0],
    ["Gross Rate (%)", float,0],
    ["Reinsurance Treaty", str,""],
    ["Status", str,""],
    ["Number of Policies Issued", int,-1]
]

main_menu = [
    [""],
    ["Welcome to INSYNC"],
    [""],
    ["Main Menu:"],
    ["1. Display Products"],
    ["2. Add New Product"],
    ["3. Update Product Details"],
    ["4. Delete Product"],
    ["5. Exit INSYNC"],
    [""]
]

sub_menu1 =  [
    ["Display Product Menu"],
    [""],
    ["Select a product option:"],
    ["1. Display all products"],
    ["2. Display specific product(s)"],
    ["3. Return to main menu"],
    [""]
]

sub_menu2 = [
    ["Create Data Menu"],
    [""],
    ["1. Add an insurance product"],
    ["2. Add new column"],
    ["3. Back to main menu"],
    [""]
]

sub_menu3 =[
    ["Update Data Menu"],
    [""],
    ["1. Update data"],
    ["2. Back to main menu"],
    [""]
]

sub_menu4 =[
    ["Delete Data Menu"],
    [""],
    ["1. Delete Data"],
    ["2. Back to main menu"]
]

# Define Functions 

def loading():
    print("Loading", end="")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print("\n")

def displayData():
    while True:
        print(tabulate(sub_menu1, tablefmt="rounded_outline"))
        input_submenu1 = input("Select an option from the Display Product Menu: ").strip()
        if input_submenu1 == "1": # Display all data
            if listProduct:
                print(tabulate(listProduct,headers=product_headers,tablefmt="simple_grid"))
                while True:
                    input_sortingOption = input("Do you want to sort the data? (Y/N)").strip().lower()
                    if input_sortingOption in ('y','n'):
                        break
                    else:
                        print("\n==================================================")
                        print("⚠️ Invalid input.Please type in the correct option.") # If input_sortingPtion is not equal to y or n
                        print("==================================================\n")
                if input_sortingOption == "y":
                    print("Please select a column for sorting: ")
                    for i, h in enumerate(product_headers): # Show all columns for sorting option
                        print(f"{i + 1}. {h}")
                    while True:
                        try:
                            input_column = int(input("Enter column number for sorting: ")) - 1 # Input column for sorting
                            if 0<= input_column < len(product_headers):
                                while True:
                                    input_sortingType = input("Ascending or Descending? (ASC/DESC): ").strip().lower()
                                    if input_sortingType == "asc":
                                        data_asc = listProduct.copy()
                                        data_asc.sort(key=lambda x:x[input_column]) # sorting listProduct based on input_column (ascending)
                                        print(tabulate(data_asc, headers=product_headers, tablefmt="simple_grid"))
                                        break
                                    elif input_sortingType == "desc":
                                        data_desc = listProduct.copy()
                                        data_desc.sort(key=lambda x:x[input_column], reverse=True) # sorting listProduct based on input_column (descending)
                                        print(tabulate(data_desc, headers=product_headers, tablefmt="simple_grid"))
                                        break
                                    else:
                                        print("\n===================================================")
                                        print("⚠️ Invalid input. Please type in the correct option.") # If inpur_sortinType is not equal to asc or desc
                                        print("===================================================\n")
                                break
                            else:
                                print("Invalid column input. Please try again.")
                        except ValueError:
                            print("Only numeric input is allowed. Please try again.")
                elif input_sortingOption == "n":
                    print(tabulate(listProduct, headers=product_headers, tablefmt="simple_grid"))
                    print("ℹ️ The data was not sorted")
            else:
                print("========================") 
                print("The data does not exist.") # When the data is empty
                print("========================")
        elif input_submenu1 == "2": # Display certain data
            if listProduct:
                print("Please select a column to apply the filter: ") 
                for i, h in enumerate(product_headers):
                    print(f"{i + 1}. {h}") # Show all columns for filtering option
                while True:
                    try:
                        input_column = int(input("Enter column number for filtering: ")) - 1 # Input column for filtering
                        if 0 <= input_column < len(product_headers):
                            input_filter= input("Enter the value to search: ") # Input value for filtering
                            try:
                                input_filter.strip().lower()
                                filtered_data=[]
                                for row in listProduct:
                                    if row[input_column].strip().lower() == input_filter:
                                        filtered_data.append(row)
                            except AttributeError:
                                filtered_data=[]
                                for row in listProduct:
                                    if str(row[input_column]) == input_filter:
                                        filtered_data.append(row)
                            if filtered_data:
                                print("\nData matching the filter:") 
                                print(tabulate(filtered_data, headers=product_headers, tablefmt="simple_grid")) # Show rows of data that match the filter
                                break
                            else:
                                print("\nNo matching data found.")
                                break
                        else:
                            print("Invalid column input. Please try again.")
                    except ValueError:
                        print("Only numeric input is allowed. Please try again.")
            else:
                print("========================") 
                print("The data does not exist.") # When the data is empty
                print("========================")
        elif input_submenu1 == "3": # Back to main menu
            print("Returning to the Main Menu")
            loading()
            break
        else:
            print("\n===============================================")
            print("⚠️ Invalid input. Please select another option.") # If input_submenu1 is not equal to 1, 2, or 3
            print("===============================================\n")

def createData():
    while True:
        print(tabulate(sub_menu2, tablefmt="rounded_outline"))
        input_submenu2 = input("Select an option from the Add New Product Menu: ").strip()
        if input_submenu2 == "1": # Add new product
            while True:
                print("Existing Data\n")
                print(tabulate(listProduct, headers=product_headers, tablefmt="simple_grid")) # Show all existing data
                print("Please enter the Product Code according to the following guidelines.") 
                print("- The Product Code must consists of exactly 3 digits.")
                print("- The first digit represents the Class of Business (COB)")
                print("- The remaining two digits represent the product number")
                print(tabulate(list_infoCode, headers=headers_code, tablefmt="simple_grid")) # Product Code guidelines
                input_productCode = input("Enter Product Code: ").strip()
                if not input_productCode:
                    print("Product Code cannot be empty. Please try again.")
                    continue
                already_exists = any(row[product_headers.index('Product Code')] == input_productCode for row in listProduct) # Check Product Code availability
                if not already_exists:
                    newProduct = [input_productCode]

                    for colName, datatype, minValue in dataInfo:
                        while True:
                            user_input = input(f"Enter {colName}: ").strip()
                            try:
                                if datatype == str:
                                    user_input = user_input.title()
                                    if user_input > minValue:
                                        newProduct.append(user_input)
                                    else:
                                        print(f"{colName} cannot be empty. Please try again.")
                                        continue
                                elif datatype == int:
                                    convertValue = datatype(user_input)
                                    if convertValue > minValue:
                                        newProduct.append(convertValue)
                                    else:
                                        print(f"{colName} cannot be negative or zero")
                                        continue
                                elif datatype == float:
                                    convertValue = datatype(user_input)
                                    if convertValue > minValue:
                                        newProduct.append(convertValue)
                                    else:
                                        print(f"{colName} cannot be negative or zero")
                                        continue
                                break
                            except ValueError:
                                if datatype == int:
                                    print("Invalid input. Please enter a whole number (integer).")
                                else:
                                    print("Only numeric input is allowed. Please try again.")
                    while True:
                        input_savingOption = input("Do you want to save the data? (Y/N)").strip().lower()
                        if input_savingOption in ('y','n'):
                            break
                        else:
                            print("\n==================================================")
                            print("⚠️ Invalid input.Please type in the correct option.") # If input_savingOption is not equal to y or n
                            print("==================================================\n")
                    if input_savingOption == "y":
                        listProduct.append(newProduct)
                        print(tabulate(listProduct, headers=product_headers, tablefmt="simple_grid"))
                        print("\n====================================")
                        print("✅ Data has been successfully saved.")
                        print("====================================\n")
                        break
                    elif input_savingOption == "n" :
                        print(tabulate(listProduct, headers=product_headers, tablefmt="simple_grid"))
                        print("\n======================")
                        print("🔴 Data was not saved.")
                        print("======================\n")
                        break
                else:
                    print("This product code already exists. Please try again")
                    break
        elif input_submenu2 == "2":
            print("Existing Data\n")
            print(tabulate(listProduct, headers=product_headers, tablefmt="simple_grid")) # Show all existing data
            while True:
                input_columnName = input("Enter column name: ").strip().title()
                if input_columnName in product_headers:
                    print("The column name already exists. Please enter a different name.")
                    continue
                while True:
                    print('''Please declare the type of data you want to insert in the new column.
                        For Example:
                        a. Text (letters only, e.g., names)
                        b. Whole number (e.g., 0,1,2,3)
                        c. Decimal (number with fraction, e.g., 0.2, 0.001, 0.50)''')
                    input_columnType = input("Please choose between a, b, or c: ")
                    if input_columnType =="a":
                        new_columnType = str
                        new_minValue = ""
                        break
                    elif input_columnType =="b":
                        new_columnType = int
                        while True:
                            input_ifnonnegative = input("Can the data entered be negative? (Y/N) ").strip().lower()
                            if input_ifnonnegative in ('y','n'):
                                break
                            else:
                                print("\n==================================================")
                                print("⚠️ Invalid input.Please type in the correct option.") # If input_ifnonnegative is not equal to y or n
                                print("==================================================\n")
                        while True:
                            input_ifnonzero = input("Can the data entered be zero (0))? (Y/N) ").strip().lower()
                            if input_ifnonzero in ('y','n'):
                                break
                            else:
                                print("\n==================================================")
                                print("⚠️ Invalid input.Please type in the correct option.") # If input_ifnonzero is not equal to y or n
                                print("==================================================\n")
                        if input_ifnonnegative == "n" and input_ifnonzero == "n":
                            new_minValue = 0
                        elif input_ifnonnegative == "n" and input_ifnonzero == "y":
                            new_minValue = -1
                        else:
                            new_minValue = float('-inf')
                        break
                    elif input_columnType =="c":
                        new_columnType = float
                        while True:
                            input_ifnonnegative = input("Can the data entered be negative? (Y/N) ").strip().lower()
                            if input_ifnonnegative in ('y','n'):
                                break
                            else:
                                print("\n==================================================")
                                print("⚠️ Invalid input.Please type in the correct option.") # If input_ifnonnegative is not equal to y or n
                                print("==================================================\n")
                        while True:
                            input_ifnonzero = input("Can the data entered be zero (0))? (Y/N) ").strip().lower()
                            if input_ifnonzero in ('y','n'):
                                break
                            else:
                                print("\n==================================================")
                                print("⚠️ Invalid input.Please type in the correct option.") # If input_ifnonzero is not equal to y or n
                                print("==================================================\n")
                        if input_ifnonnegative == "n" and input_ifnonzero == "n":
                            new_minValue = 0
                        elif input_ifnonnegative == "n" and input_ifnonzero == "y":
                            new_minValue = -1e30
                        else:
                            new_minValue = float('-inf')
                        break
                    else:
                        print("Invalid input. Please try again.")

                new_dataInfo = [input_columnName, new_columnType, new_minValue]
                while True:
                    if listProduct:
                        input_newColumn = input("Enter the value for each row, seperated by commas (e.g., Active, Inactive, Freeze)").strip().title().split(",")
                        try:
                            if new_columnType == int:
                                for i in range(len(input_newColumn)):
                                    input_newColumn[i] = int(input_newColumn[i])
                                    
                            elif new_columnType == float:
                                for i in range(len(input_newColumn)):
                                    input_newColumn[i] = float(input_newColumn[i])
                        except ValueError:
                            if new_columnType == int:
                                print("Invalid input. Please enter a whole number (integer).")
                                continue
                            else:
                                print("Only numeric input is allowed. Please try again.")
                                continue
                        invalid_value = False
                        for val in input_newColumn:
                            if val <= new_minValue:
                                print(f"Value {val} is below minimum allowed")
                                invalid_value = True
                                break
                        if invalid_value:
                            continue

                        if len(input_newColumn) < len(listProduct):
                            print(f"Your input was less than the number of rows ({len(listProduct)}). Please try again.")
                            continue
                        elif len(input_newColumn) > len(listProduct):
                            print(f"🔴 Your input was more than the number of rows ({len(listProduct)}). Extra data will be ignored")
                    else:
                        print("No data found. Skipping value entry for this column")

                    while True:
                        try:
                            input_index = int(input("In which column position do you want to place it? "))-1
                            if input_index ==0:
                                print("⚠️ Invalid position. 'Product Code' is the primary key and must remain the first column.")
                                continue
                            if not (0 < input_index <= len(product_headers)):
                                print(f"Column index must be an integer between 2 and {len(product_headers)+1}.")
                                continue
                            break
                        except ValueError:
                            print("\n=================================================")
                            print("⚠️ Please enter a valid number for column position.") # If input_submenu1 is not equal to 1 or 2
                            print("=================================================\n")
                            continue
                    while True:
                        input_savingOption = input("Do you want to save the data? (Y/N)").strip().lower()
                        if input_savingOption in ('y','n'):
                            break
                        else:
                            print("\n===============")
                            print("⚠️ Invalid input.") # If input_sortingPtion is not equal to y or n
                            print("===============\n")
                    if input_savingOption == "y":
                        for j in range(len(listProduct)):
                            listProduct[j].insert(input_index, input_newColumn[j])
                        product_headers.insert(input_index, input_columnName)
                        dataInfo.insert(input_index-1,new_dataInfo)
                        print(tabulate(listProduct, headers=product_headers, tablefmt="simple_grid"))
                        print(f"✅ All data for column {input_columnName} has already been added.\n")
                        break
                    elif input_savingOption == "n" :
                        new_dataInfo = []
                        print(tabulate(listProduct, headers=product_headers, tablefmt="simple_grid"))
                        print("\n======================")
                        print("🔴 Data was not saved.")
                        print("======================\n")
                        break 
                break
        elif input_submenu2 == "3":
            print("Returning to the Main Menu")
            loading()
            break
        else:
            print("\n===============================================")
            print("⚠️ Invalid input. Please select another option.") # If input_submenu1 is not equal to 1 or 2
            print("===============================================\n")

def updateData():
    while True:
        print(tabulate(sub_menu3, tablefmt="rounded_outline"))
        input_submenu3 = input("Enter an option from the Update Product Menu: ").strip()
        if input_submenu3 == "1":
            if listProduct:
                input_kodeProduk = input("Enter Product Code : ")
                found = False
                for index, produk in enumerate(listProduct):
                    if produk[product_headers.index('Product Code')] == input_kodeProduk:
                        found=True
                        print(tabulate([produk], headers=product_headers, tablefmt="simple_grid"))
                        while True:
                            input_updateSelection = input("Do you want to update this product? (Y/N): ").strip().lower()
                            if input_updateSelection in ('y','n'):
                                break
                            else:
                                print("\n==================================================")
                                print("⚠️ Invalid input.Please type in the correct option.") # If input_updateSelection is not equal to y or n
                                print("==================================================\n")
                        
                        if input_updateSelection =="y":
                            print("\nSelect the column you want to update: ")
                            for i, h in enumerate(product_headers):
                                print(f"{i+1}. {h}")
                            
                            while True:
                                try: 
                                    input_column = int(input("Enter the column number to update: ")) - 1
                                    if 0<=input_column < len(product_headers):
                                        colName, datatype, minValue = dataInfo[input_column-1]
                                        while True:
                                            input_newValue = input(f"Enter the new value for {product_headers[input_column]} : ").strip()
                                            try:
                                                if datatype == str:
                                                    if not input_newValue:
                                                        print(f"{colName} cannot be empty. Please try again.")
                                                        continue
                                                    input_newValue = input_newValue.title()
                                                elif datatype in (int, float):
                                                    convertValue = datatype(input_newValue)
                                                    if convertValue <= minValue:
                                                        print(f"{colName} must be greater than {minValue}")
                                                        continue
                                                    input_newValue = convertValue

                                                break
                                            except ValueError:
                                                if datatype == int:
                                                    print("Please enter a whole number (integer).")
                                                elif datatype == float:
                                                    print("Please enter a valid decimal number.")
                                                else:
                                                    print("Invalid input.")
                                        while True:
                                            confirm_save = input("Are you sure you want to update this data? (Y/N) ")
                                            if confirm_save in ("y","n"):
                                                break
                                            else:
                                                print("\n==================================================")
                                                print("⚠️ Invalid input.Please type in the correct option.") # If confirm_save is not equal to y or n
                                                print("==================================================\n")
                                        if confirm_save == "y":
                                            listProduct[index][input_column] = input_newValue
                                            print("✅ Data has been successfully updated.\n")
                                        else:
                                            print("ℹ️ Update canceled. No changes were made.")
                                        print(tabulate(listProduct,headers=product_headers,tablefmt="simple_grid"))    
                                        break
                                    else:
                                        print("Column not available. Please try again")
                                except ValueError:
                                    print("Only numeric input is allowed. Please try again.")
                        elif input_updateSelection == "n":
                            print("ℹ️ Data was not updated. Returning to the Update Product Menu.")
                            break
                if not found:
                    print("No product found with that code. Please try again.")
            else:
                print("========================") 
                print("The data does not exist.") # When the data is empty
                print("========================") 
        elif input_submenu3 == "2":
            print("Returning to the Main Menu")
            loading()
            break 
        else:
            print("\n===============================================")
            print("⚠️ Invalid input. Please select another option.") # If input_submenu1 is not equal to 1 or 2
            print("===============================================\n")

def deleteData():
    while True:
        print(tabulate(sub_menu4, tablefmt="rounded_outline"))
        input_submenu4 = input("Enter an option from the Delete Product Menu: ").strip()
        if input_submenu4 == "1":
            if listProduct:
                while True:
                    input_productCode = input("Enter Product Code to delete: ")
                    for index, product in enumerate(listProduct):
                        if product[product_headers.index('Product Code')] == input_productCode:
                            print(tabulate([product], headers=product_headers, tablefmt="simple_grid"))
                            while True:
                                input_dataDeletion = input("Are you sure you want to delete this product? (Y/N): ").strip().lower()
                                if input_dataDeletion in ('y','n'):
                                    break
                                else:
                                    print("\n==================================================")
                                    print("⚠️ Invalid input.Please type in the correct option.") # If input_dataDeletion is not equal to y or n
                                    print("==================================================\n")
                            
                            if input_dataDeletion =="y":
                                del listProduct[index]
                                print(tabulate(listProduct,headers=product_headers,tablefmt="simple_grid"))
                                print("\n================================")
                                print("🗑️ Product successfully deleted.")
                                print("================================\n")
                                break
                            elif input_dataDeletion =="n":
                                print("ℹ️ Data was not deleted. Returning to the Delete Product Menu.")
                                break
                    else:
                        print("No product found with that code. Please try again.")
                        break
                    break
            else:
                print("========================") 
                print("The data does not exist.") # When the data is empty
                print("========================")
        elif input_submenu4 == "2":
            print("Returning to the Main Menu")
            loading()
            break 
        else:
            print("\n===============================================")
            print("⚠️ Invalid input. Please select another option.") # If input_submenu1 is not equal to 1 or 2
            print("===============================================\n")


def INSYNC():
    while True:
        # Main menu
        print(tabulate(main_menu, tablefmt="double_outline"))
        input_menu = input("Select a menu option: ").strip()
        # Menu 1: Display data
        if input_menu == "1":
            displayData()
        # Menu 2: Create Data
        elif input_menu == "2":
            createData()
        # Menu 3: Update Data
        elif input_menu == "3":
            updateData()
        # Menu 4: Delete Data
        elif input_menu =="4":
            deleteData()
        # Menu 5: Exit Program
        elif input_menu =="5":
            loading()
            print("Program exited successfully.\n")
            break
        else:
            print("\n===============================================")
            print("⚠️ Invalid input. Please select another option.") # If input_submenu1 is not equal to 1, 2, 3, 4, or 5
            print("===============================================\n")

INSYNC()