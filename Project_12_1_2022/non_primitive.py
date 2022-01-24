a = [1, 3, 4, 5, 7]
b = ["hello", "hi", "bonjour"]
c = [20, "ca va bien?", False, 3.5, "bien", [1.2, [True, False]]]
e = [45, "ca va?", True, 3.5, "bien", c]
d = len(c)
print(d)
print(c[d-1]) #out of range
print(e[-1][-1][-1][-1]) #possible usage for API testing, UI testing

