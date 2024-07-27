import requests
from bs4 import BeautifulSoup
import csv

# URL of the e-commerce website's product listing page
url = 'https://example-ecommerce-website.com/products'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all product listings (Assuming each product is in a <div> with class 'product-item')
products = soup.find_all('div', class_='product-item')

# Open a CSV file to write the product information
with open('products.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Name', 'Price', 'Rating'])

    # Extract and write the product information
    for product in products:
        # Extract product name (Assuming it's in a <h2> with class 'product-name')
        name = product.find('h2', class_='product-name').text.strip()
        
        # Extract product price (Assuming it's in a <span> with class 'product-price')
        price = product.find('span', class_='product-price').text.strip()
        
        # Extract product rating (Assuming it's in a <div> with class 'product-rating' and ratings are in data-rating attribute)
        rating = product.find('div', class_='product-rating')['data-rating']
        
        # Write the product information to the CSV file
        writer.writerow([name, price, rating])

print("Product information has been successfully written to products.csv")
