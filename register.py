
registory = []

def register(func):
    print("Running deco..!")
    registory.append(func)
    return func


@register
def f1():
    print("running f1")


from dis import dis

dis(f1)
