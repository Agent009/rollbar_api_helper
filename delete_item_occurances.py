# _______________________________________________________________
# Delete all occurrences in specified items
# _______________________________________________________________
import lib.rollbar_utils as rollbar_utils


if __name__ == "__main__":
    items = rollbar_utils.get_items()

    if items["total_count"] > 0:
        for item in items["items"]:
            rollbar_utils.delete_occurrences(item["id"])
    else:
        print("No items found")
