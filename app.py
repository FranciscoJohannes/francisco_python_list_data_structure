from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', message="Hello, World!")

# List product data
product_id_list = [1, 2, 3, 4, 5]
product_name_list = ["Laptop", "Desk Chair", "Smartwatch", "Notebook", "Running Shoes"]
product_category_list = ["Electronics", "Furniture", "Electronics", "Stationery", "Apparel"]
product_price_list = [750, 100, 200, 5, 80]
product_stock_list = [50, 200, 150, 500, 100]
product_supplier_email_list = ["supplier1@gmail.com", "supplier2@gmail.com", "supplier3@gmail.com", "supplier4@gmail.com", "supplier5@gmail.com"]

# Print product data
print("Product List:")
for i in range(len(product_id_list)):
    print(f"ID: {product_id_list[i]}, "
          f"Name: {product_name_list[i]}, "
          f"Category: {product_category_list[i]}, "
          f"Price: ${product_price_list[i]}, "
          f"Stock: {product_stock_list[i]}, "
          f"Supplier Email: {product_supplier_email_list[i]}")

# Print product data
print("Product List:")
for i in range(len(product_id_list)):
    print(f"ID: {product_id_list[i]}, "
          f"Name: {product_name_list[i]}, "
          f"Category: {product_category_list[i]}, "
          f"Price: ${product_price_list[i]}, "
          f"Stock: {product_stock_list[i]}, "
          f"Supplier Email: {product_supplier_email_list[i]}")

# List employee data
employee_id_list = [1, 2, 3, 4, 5]
employee_name_list = ["John Doe", "Jane Smith", "Mark Johnson", "Lisa Wong", "Paul McDonald"]
employee_department_list = ["Sales", "Human Resources", "IT", "Marketing", "Finance"]
employee_age_list = [30, 25, 40, 28, 35]
employee_email_list = ["john.doe@company.com", "jane.smith@company.com", "mark.johnson@company.com", "lisa.wong@company.com", "paul.mcdonald@company.com"]

# Print employee data
print("Employee List:")
for i in range(len(employee_id_list)):
    print(f"ID: {employee_id_list[i]}, "
          f"Name: {employee_name_list[i]}, "
          f"Department: {employee_department_list[i]}, "
          f"Age: {employee_age_list[i]}, "
          f"Email: {employee_email_list[i]}")



if __name__ == '__main__':
    app.run(debug=True)