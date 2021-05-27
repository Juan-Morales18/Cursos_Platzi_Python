def run():
    iter1 = [1, 2, 2, 3, 3]
    iter2 = 'AaBBCCCcccAD'
    unique_in_order(iter1)
    unique_in_order(iter2)


def unique_in_order(iterable):
    output = []
    previous_item = None

    # for item in iterable:
    #    if previous_item == item:
    #        continue
    #    output.append(item)
    #    previous_item = item

    # print(output)

    # Use of "continue" with while bucle

    index = 0
    while index < len(iterable):
        if previous_item == iterable[index]:
            index += 1
            continue
        output.append(iterable[index])
        previous_item = iterable[index]
        index += 1
    print(output)


if __name__ == '__main__':
    run()
