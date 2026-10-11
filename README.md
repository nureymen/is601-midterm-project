# IS601 Midterm Project

This project processes restaurant order data from a JSON file. It creates two output files: `customers.json` and `items.json`.

## How to Run

Run the program from the terminal and pass the input JSON filename as the first argument:

```bash
python3 main.py example_orders.json
```
## Output Files

- `customers.json` contains customer phone numbers as keys and customer names as values.
- `items.json` contains each item name, its price, and the number of times it was ordered.

## Program Design

The program uses Python's json and sys modules.

It reads the input JSON file and processes each order using a loop.

Customer phone numbers and names are stored in a dictionary.
Item names, prices, and order counts are stored in another dictionary.

Finally, the program writes the results to two JSON files.