def generator():
    # this will be a generator function
    yield "foo"
    yield "bar"


wierd_obj = generator()
print(next(wierd_obj))
