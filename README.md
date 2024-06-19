# RollBar API Helper

This is a quick API helper for [Rollbar](https://rollbar.com).
It currently supports the following processes:

* [delete_item_occurances.py](delete_item_occurances.py) - [Delete all item occurrences](https://docs.rollbar.com/reference/delete_api-1-instance-instance-id)

## Setup
### Prerequisites

This project requires support for parsing environment variable files.

```bash
pip install python-dotenv
```

### Environment Variables

Store your project `read` and `write` tokens in an environment variable file.
Copy/paste the `.env.sample` file as `.env` and add in your own project tokens.

## Usages

* Run [delete_item_occurances.py](delete_item_occurances.py)

## TODO

* [delete_item_occurances.py](delete_item_occurances.py)
* * Support passing of parameters to control occurrences to be deleted