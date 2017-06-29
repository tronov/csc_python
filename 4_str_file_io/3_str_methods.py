# the most frequently used methods of str
string = "foo bar"
print(string.capitalize())
print(string.title())
print(string.upper())
print(string.lower())
print(string.title().swapcase())

# str justifying
print(string.ljust(16, '~'))
print(string.rjust(16, '~'))
# space is the default fillchar
print(string.center(16))

# str stripping
print("]>>foo bar<<[".lstrip("]>"))
print("]>>foo bar<<[".lstrip("[<"))
# removing whitespaces by default
print("\t foo bar \r\n ".strip())

# str splitting
print("foo,bar".split(","))
print("foo,,,bar".split(","))
print("foo, ,, bar".split(", "))
# by default - greedy whitespace
print("\t foo bar \r\n ".split())
# second argument - maximum chunks
print("foo.bar.baz.tar.gz".rsplit(".", 1))

print("foo,bar,baz".partition(","))
print("foo,bar,baz".rpartition(","))

print(", ".join(["foo", "bar", "baz"]))
print(", ".join(filter(None, ["", "foo", "", "baz"])))
print(", ".join("bar"))

print("foo" in "foobar")
print("spam" not in "foobar")

print("foobar".startswith("foo"))
print("foobar".endswith(("boo", "bar")))

word = "abracadabra"

print(word.find("ra"))
print(word.find("ra", 0, 3))  # as [:3].find("ra")
print(word.rfind("ra"))

print(word.index("ra", 0, 4))
print(word.rindex("ra"))

print(word.replace("ra", "**"))
print(word.replace("ra", "**", 1))

translation_map = {ord("a"): "*", ord("b"): "?"}
print(word.translate(translation_map))

print("100500".isdigit())
print("foo100500".isalnum())
print("foobar".isalpha())

print("foobar".islower())
print("FOOBAR".isupper())
print("Foo Bar".istitle())
print("\r  \n\t \r\n".isspace())
# etc...
