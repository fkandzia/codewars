"""
You are given a (small) check book as a - sometimes - cluttered (by non-alphanumeric characters) string:

"1000.00
125 Market 125.45
126 Hardware 34.95
127 Video 7.45
128 Book 14.32
129 Gasoline 16.10"

The first line shows the original balance. Each other line (when not blank) gives information: check number, category, check amount. (Input form may change depending on the language).

First you have to clean the lines keeping only letters, digits, dots and spaces.

Then return a report as a string (underscores show spaces -- don't put them in your solution. They are there so you can see them and how many of them you need to have):

"Original_Balance:_1000.00
125_Market_125.45_Balance_874.55
126_Hardware_34.95_Balance_839.60
127_Video_7.45_Balance_832.15
128_Book_14.32_Balance_817.83
129_Gasoline_16.10_Balance_801.73
Total_expense__198.27
Average_expense__39.65"

On each line of the report you have to add the new balance and then in the last two lines the total expense and the average expense. So as not to have a too long result string we don't ask for a properly formatted result.
Notes

    See input examples in Sample Tests.
    It may happen that one (or more) line(s) is (are) blank.
    Round to 2 decimals your calculated results (Elm: without traling 0)
    The line separator of results may depend on the language \n or \r\n. See examples in the "Sample tests".
    R language: Don't use R's base function "mean()" that could give results slightly different from expected ones.

"""

import re

# Line separator is \r\n in Python
def balance(book: str) -> str:
    line_sep = "\r\n"
    lines = book.split("\n")

    balance_out = "Original Balance: {:.2f}".format
    original_balance = _extract_original_balance(lines[0])
    expense_out = "{id} {category} {amount:.2f} Balance {current:.2f}".format

    balance = original_balance
    result = [balance_out(balance)]

    expense_pattern = r'^(?P<id>\d+).*?(?P<category>\w+).*?(?P<amount>\d+\.?\d?\d?).*$'
    num_transactions = 0
    for line in lines[1:]:
        if line:
            expense_match = re.match(expense_pattern, line)
            if expense_match:
                amount = float(expense_match.group("amount"))
                balance -= amount
                category = expense_match.group("category")
                check_id = expense_match.group("id")
                result.append(expense_out(id=check_id,
                                          category=category,
                                          amount=amount,
                                          current=balance
                                          ))
                num_transactions += 1

    total_expense = original_balance - balance
    result.append(f"Total expense  {total_expense:.2f}")
    result.append(f"Average expense  {total_expense/max(1.0, num_transactions):.2f}")
    return line_sep.join(result)


def _extract_original_balance(balance_line: str) -> float:
    balance_pattern = "\d+\.?\d?\d?"
    balance_match = re.match(balance_pattern, balance_line)

    if balance_match:
        return float(balance_match.group(0))
