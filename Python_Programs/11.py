price = float(input("Enter the product price: $"))
quantity = int(input("Enter the quantity: "))
is_new_customer = input("Are you a new customer? (yes/no): ").lower() == "yes"
is_employee = input("Are you an employee? (yes/no): ").lower() == "yes"
coupon_code = input("Enter coupon code, or press Enter to skip: ").strip().upper()

coupon_discounts = {
	"SAVE10": 10,
	"SAVE20": 20,
}

subtotal = price * quantity
discount = 0

if is_new_customer:
	discount += 20
if is_employee:
	discount += 15
if coupon_code in coupon_discounts:
	discount += coupon_discounts[coupon_code]
elif coupon_code:
	print("Coupon code not recognized.")

discount = min(discount, 50)
discount_amount = subtotal * discount / 100
discounted_subtotal = subtotal - discount_amount

shipping = 0 if discounted_subtotal >= 50 or is_employee else 5.99
tax = discounted_subtotal * 0.085
total = discounted_subtotal + shipping + tax

print("\n--- Order Summary ---")
print("Subtotal: $", round(subtotal, 2))
print("Discount:", discount, "%")
print("You save: $", round(discount_amount, 2))
print("Shipping: $", round(shipping, 2))
print("Tax: $", round(tax, 2))
print("Total: $", round(total, 2))
