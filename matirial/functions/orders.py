def total_price(product, count):
    if product == "coffee":
        return count * 1.5
    elif product == "coke":
        return count * 1.4
    elif product == "water":
        return count * 1
    elif product == "snacks":
        return count * 2


current_product = input()
current_count = int(input())

final_price = total_price(current_product, current_count)
print(f"{final_price:.2f}")
