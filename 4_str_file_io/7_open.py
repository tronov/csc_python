file = open("./7_open.py")
# modes: (r)ead only - default,
#        (w)rite only with erasing,
#        (r+) - read and write,
#         x - create strictly new file for writing,
#        (a)ppend
# file types: b (binary), t (text)

print(list(file))
file.close()

file = open("./7_open.py", "rt", encoding="utf-8", errors="ignore")
# file descriptor number
print(file.fileno())
print(file.read(20))
# get cursor position
print(file.tell())
# set cursor position
file.seek(0)
print(file.tell())
print(file.readline())
print(file.readlines())
file.close()

# writen = file.write("abracadabra")
# file.writelines(["foo\n", "bar\n"])
# file.flush() - apply changes to disk (close() calls flush())
