try:
    1 + '42'
except Exception as e:
    caught = e

print(caught.args)
print(caught.__traceback__)

print('-' * 70)

import traceback

traceback.print_tb(caught.__traceback__)
