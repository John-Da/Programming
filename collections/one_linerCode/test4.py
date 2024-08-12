
lst = lambda *x, **j: print(f"Products: {', '.join(map(str, x))}\n" + "\n".join(f"{key}: {value}" for key, value in j.items()))

lst('Apple', 'Banana', apple={"price": 40}, banana={"price": 54})

