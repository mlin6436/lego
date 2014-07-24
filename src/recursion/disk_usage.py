import os


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for subdir in os.listdir(path):
            subpath = os.path.join(path, subdir)
            total += disk_usage(subpath)
    print('{0:<10}'.format(total), path)
    return total


if __name__ == '__main__':
    path = '/usr/local/'
    print('{0:<10}'.format(disk_usage(path)), path)