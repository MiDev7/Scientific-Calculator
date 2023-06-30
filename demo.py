import math

demo = []
trigo = ["sin", "cos", "tan"]
trigo_bool = False

count_trigo = 0
# task = str(input(""))

while True:
    num = input("")
    # Input in this format
    # sin
    # (
    # 8
    # )
    # +
    # 7
    # =

    if num == "=":
        break

    if num in trigo:
        trigo_bool = True

    demo.append(num)
    if trigo_bool:
        if num == ")":
            demo.append(")")
    else:
        pass


demo = [
    "math.sin(math.radians"
    if item == "sin"
    else "math.cos(math.radians"
    if item == "cos"
    else item
    for item in demo
]

print(demo)

result = "".join(demo)
print(eval(f"{result}"))
