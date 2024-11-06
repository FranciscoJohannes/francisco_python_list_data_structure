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

# List universities
university_id_list = [1, 2, 3, 4, 5]
university_name_list = ["University of the Philippines", "Ateneo de Manila University", "De La Salle University", "University of Santo Tomas", "Polytechnic University of the Philippines"]
university_location_list = ["Quezon City", "Quezon City", "Manila", "Manila", "Manila"]
university_established_year_list = [1908, 1859, 1911, 1611, 1904]
university_type_list = ["Public", "Private", "Private", "Private", "Public"]
university_website_list = ["www.up.edu.ph", "www.ateneo.edu", "www.dlsu.edu.ph", "www.ust.edu.ph", "www.pup.edu.ph"]

# Print universities
print("University List:")
for i in range(len(university_id_list)):
    print(f"ID: {university_id_list[i]}, "
          f"Name: {university_name_list[i]}, "
          f"Location: {university_location_list[i]}, "
          f"Established Year: {university_established_year_list[i]}, "
          f"Type: {university_type_list[i]}, "
          f"Website: {university_website_list[i]}")

# Restaurant Table list
restaurant_id_list = [1, 2, 3, 4, 5]
restaurant_name_list = ["Vikings Luxury Buffet", "Antonio's Restaurant", "Mesa Filipino Moderne", "Manam Comfort Filipino", "Ramen Nagi"]
restaurant_location_list = ["Pasay City", "Tagaytay", "Makati City", "Quezon City", "Various Locations"]
restaurant_Cuisine_type_list = [2011, 2002, 2009, 2013, 2013]
restaurant_established_year_list = ["Buffet", "Fine Dining", "Filipino", "Filipino", "Japanese"]
restaurant_website_or_contact_list = ["www.vikings.ph", "www.antoniosrestaurant.ph", "www.mesa.ph" , "www.manam.ph", "www.ramennagi.com.ph"]

# Print restaurants data
print("Restaurant List:")
for i in range(len(restaurant_id_list)):
    print(f"ID: {restaurant_id_list[i]}, "
          f"Name: {restaurant_name_list[i]}, "
          f"Location: {restaurant_location_list[i]}, "
          f"Cuisine type: {restaurant_Cuisine_type_list[i]}, "
          f"Established Year: {restaurant_established_year_list[i]}, "
          f"Website or Contact:{restaurant_website_or_contact_list[i]}")


if __name__ == '__main__':
    app.run(debug=True)