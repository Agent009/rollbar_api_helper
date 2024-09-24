# _______________________________________________________________
# Delete all occurrences in specified items
# _______________________________________________________________
import lib.rollbar_utils as rollbar_utils


if __name__ == "__main__":
    # Optional: You can specify the counters you want to delete occurrences for.
    counters = []
    ids = []
    for counter in counters:
        ids.append(rollbar_utils.get_item_id_by_counter(counter))

    items = rollbar_utils.get_items(environments=["development"])

    if items["total_count"] > 0:
        # Filter items based on the provided counters/ids.
        if ids:
            items = [item for item in items["items"] if item["id"] in ids]
        else:
            items = items["items"]

        for item in items:
            # print("Item ID:", item["id"], item["id"] in ids)
            # if item["id"] in ids:
            rollbar_utils.delete_occurrences(item["id"])
    else:
        print("No items found")
