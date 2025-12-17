from app.db.inventory import INVENTORY_DB

def lookup_inventory(item_name: str):
    item = item_name.lower()

    if item not in INVENTORY_DB:
        return {
            "item": item_name,
            "status": "Unknown Item",
            "quantity": 0,
            "recommended_action": "Manual verification required"
        }

    data = INVENTORY_DB[item]

    action = "No action required"
    if data["quantity"] <= data["reorder_level"]:
        action = "Reorder immediately"

    return {
        "item": item_name,
        "category": data["category"],
        "inventory_status": data["status"],
        "quantity": data["quantity"],
        "recommended_action": action
    }
