def recursive_display(limit: int):
    if limit >= 0:
        print(limit)
        recursive_display(limit-1)


recursive_display(10)
