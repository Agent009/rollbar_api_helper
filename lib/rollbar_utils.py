import requests
import lib.constants as constants
import lib.http_utils as http_utils


# Get the list of items.
# https://docs.rollbar.com/reference/list-all-items
# _______________________________________________________________
def get_items():
    url = 'items'
    all_records = []
    page = 1

    while True:
        params = {'page': page}
        response_data = http_utils.send_http_request('GET', url, params=params)

        try:
            total_count = response_data['result']['total_count']
            records = response_data['result']['items']
            print('get_items -> Page: ' + str(page) + ', Total: ' + str(total_count))
            all_records.extend(records)
            # return {'page': page, 'total_count': total_count, 'items': records}

            # Break if we have fewer items than the limit per page
            if total_count < constants.default_limit_per_page:
                break

            page += 1
        except KeyError as e:
            print('get_items -> The items data was not found with error:', e)
            exit()
        except ValueError as e:
            print('get_items -> Error parsing the items data response JSON:', e)
            exit()
        except Exception as e:
            print('get_items -> An unexpected error occurred while fetching the items data:', e)
            exit()

    return {'total_count': total_count, 'items': all_records}


# Get the item ID based on the counter value from a project
# https://docs.rollbar.com/reference/get-an-item-by-project-counter
# _______________________________________________________________
def get_item_id_by_counter(rollbar_item_counter):
    url = 'item_by_counter/' + str(rollbar_item_counter)
    response_data = http_utils.send_http_request('GET', url)
    # print(response_data)

    try:
        item_id = response_data['result']['id']
        print('get_item_id_by_counter -> Item ID: ' + str(item_id))
        return item_id
    except KeyError as e:
        print('get_item_id_by_counter -> The item data was not found with error:', e)
        exit()
    except ValueError as e:
        print('get_item_id_by_counter -> Error parsing the item data response JSON:', e)
        exit()
    except Exception as e:
        print('get_item_id_by_counter -> An unexpected error occurred while fetching the item data:', e)
        exit()


# Delete all occurrences for the given item
# https://docs.rollbar.com/reference/get_api-1-item-item-id-instances
# _______________________________________________________________
def delete_occurrences(item_id):
    url = f'item/{item_id}/instances'
    page = 1

    while True:
        params = {'page': page}
        response_data = http_utils.send_http_request('GET', url, params=params)

        try:
            occurrences = response_data['result']['instances']
            print('delete_occurrences -> ItemID: ',
                  str(item_id) + ', Page: ' + str(page) + ', Occurrences: ' + str(len(occurrences)))
        except KeyError as e:
            print('delete_occurrences -> The occurrence data for item (' + str(item_id) + ') was not found with error:',
                  e)
            exit()
        except ValueError as e:
            print('delete_occurrences -> Error parsing the occurrence data response JSON for item  (' + str(
                item_id) + '):', e)
            exit()
        except Exception as e:
            print(
                'delete_occurrences -> An unexpected error occurred while fetching the occurrence data for item (' + str(
                    item_id) + '):', e)
            exit()

        for occurrence in occurrences:
            occurrence_id = occurrence['id']

            # Delete the occurrence
            url2 = f'instance/{occurrence_id}'
            response2 = http_utils.send_http_request('DELETE', url2)
            print('delete_occurrences -> Item ID: ' + str(item_id) + ' -> deleted occurrence ID: ' + str(
                occurrence_id) + f', response: {response2}')

        # Break if we have fewer occurrences than the limit per page
        if len(occurrences) < constants.default_limit_per_page:
            break

        page += 1
