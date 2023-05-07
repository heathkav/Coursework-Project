def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i][3] < right_arr[j][3]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


def read_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        database = []
        for i in range(0, len(lines), 9):
            customer_id = lines[i].strip()
            first_name = lines[i+1].strip()
            last_name = lines[i+].strip()
            dob = lines[i+3].strip()
            user_name = lines[i+4].strip()
            email = lines[i+5].strip()
            phone_number = lines[i+6].strip()
            address = lines[i+7].strip()
            postcode = lines[i+8].strip()
            password = lines[i+9].strip()
            database.append([customer_id, first_name, last_name, dob, user_name, email, phone_number, address, postcode, password])
        return database


def write_file(file_name, database):
    with open(file_name, 'w') as f:
        for user in database:
            f.write('\n'.join(user) + '\n')


def sort_database(file_name):
    database = read_file(file_name)
    merge_sort(database)
    write_file(file_name, database)


if __name__ == '__main__':
    sort_database('database.txt')
