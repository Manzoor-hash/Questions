import json

def calculate_cart_total(cart, products):
    total = 0
    for item in cart:
        product_name = item["product"]
        quantity = item["quantity"]
        
        if product_name in products:
            price = products[product_name]
            total += price * quantity
        else:
            print(f"Product '{product_name}' not found in the product list.")
    return total

def main():
    with open("json.json", "r") as products_file:
        products_data = json.load(products_file)
    
    products = {product["product"]: product["price"] for product in products_data}
    
    cart = []
    while True:
        product_name = input("Enter product name (or 'done' to finish): ")
        if product_name == 'done':
            break
        
        quantity = int(input("Enter quantity: "))
        cart.append({"product": product_name, "quantity": quantity})
    
    total_price = calculate_cart_total(cart, products)
    print(f"Total price of the shopping cart: ${total_price:.2f}")

if __name__ == "__main__":
    main()