# Smart Inventory Filter


def filter_inventory(items: list[dict]) -> tuple[list[str], set[str], dict[str, int], list[int]]:
    items = [
        {"name": "Notebook", "price": 250, "category": "Stationery"},
        {"name": "Pen", "price": 100, "category": "Stationery"},
        {"name": "Bag", "price": 1200, "category": "Accessories"},
        {"name": "Bottle", "price": 400, "category": "Utensils"},
    ]
    
    affordable_products = [items["name"] for items in items if items["price"]< 500]
    
    unique_one = {items["category"] for items in items}
    
    price_map = {items["name"]: items["price"] for items in items}
    
    discount = list(items["price"]* 0.9 for items in items)
    
    return(affordable_products, unique_one, price_map, discount)
    
