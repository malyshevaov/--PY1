def delete(list_, index=None):
    if index is not None:
        del list_[index]
    else:
        del list_[-1]
    return list_
print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))
