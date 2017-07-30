try:
    1 + 2
except Exception as e:
    print(' '.join(e.args))
finally:
    print('Life goes on.')


try:
    raise RuntimeWarning('Something happened.')
except Exception as e:
    print(' '.join(e.args))
finally:
    print('But life still goes on.')
