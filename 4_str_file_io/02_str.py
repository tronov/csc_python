# str type
s = "я строка"
print(list(s))

# python hasn't char type - single char has str type
print(s[0], type(s[0]))

# since version 3.3 python use smart encoding selection
# UCS-1
print(list(map(ord, "hello")))
# UCS-2
print(list(map(ord, "привет")))
# UCS-4
print(ord("🀱"))
# remark: ord() return number of char, inverse of chr()

print(chr(0x68))

# unicode chars escaping
print("\u0068", "\U00000068")
print("\N{Domino tile horizontal-00-00}")

# be careful: unicode trap
char = "\N{latin small letter sharp s}"
print(char, char.upper(), char.upper().lower())
