def binary_search(data, target, low, high):
    '''
    A basic binary search.
    :param data: A list of sorted numbers
    :param target: The target number
    :param low: The lowest index
    :param high: The highest index
    :return:
    '''
    if low > high:
        print('No match found')
    else:
        mid = (high + low) // 2
        # print('low: ' + str(low))
        # print('mid: ' + str(mid))
        # print('high: ' + str(high))
        if data[mid] == target:
            print('The target number exists')
        elif data[mid] < target:
            '''
            For the case of misusing recursion, such as using: binary_search(data, target, mid, high)
            The Python interpreter is capable of raising an RuntimeError (maximum recursion depth exceeded)
            The default maximum recursion depth value is 1000, this is configurable via sys.setrecursionlimit(n)
            '''
            binary_search(data, target, mid + 1, high)
        else:
            binary_search(data, target, low, mid - 1)


if __name__ == '__main__':
    target = 17
    data = (2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37)
    binary_search(data, target, 0, len(data) - 1)