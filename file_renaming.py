def solution():
    # write your code in Python 3.6
    # photo.jpg, Warsaw, 2013-09-05 14:08:15
    files = open('files.txt', 'r')
    photos = [line.strip() for line in files]
    city = {}
    city_len = {}
    for photo in photos:
        items = photo.split(',')
        if items[1] in city:
            city[items[1]] += 1
        else:
            city[items[1]] = 1

        city_len[items[1]] = len(str(city[items[1]]))

    file_names = []
    for photo in photos:
        items = photo.split(',')
        number = city[items[1]]
        if city_len[items[1]] > 1 and len(str(number)) < city_len[items[1]]:
            leading_zeros = (int(city_len[items[1]]) - 1) * '0'
            number = f'{leading_zeros}{number}'

        file_name = f"{items[1]}{number}.{items[0].split('.')[1]}"
        print(file_name)
        file_names.append(file_name)

        city[items[1]] -=1

    return file_names

solution()


