from contextlib import redirect_stdout
import io


handle = io.StringIO()
with redirect_stdout(handle):
    print('Hello, World!')

print('-' * 70)
print(handle.getvalue())
