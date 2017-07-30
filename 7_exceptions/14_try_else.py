try:
    1 + 2
except Exception as e:
    print(' '.join(e.args))
else:
    print('Definitely nothing bad happens.')
finally:
    print('And life goes on.')
