def get_coordinates():
    global coordinates
    coordinates = input('Enter the coordinates: > ').split()
    if coordinates[0].isnumeric() and coordinates[1].isnumeric():
        if int(coordinates[0]) in [1, 2, 3] and int(coordinates[1]) in [1, 2, 3]:
            value = check_flag()
            fill_cells(value)
        else:
            print('Coordinates should be from 1 to 3!')
            return get_coordinates()
    else:
        print('You should enter numbers!')
        return get_coordinates()


def check_flag():
    global X_flag
    global O_flag
    if X_flag:
        return 'X'
    elif O_flag:
        return 'O'


def change_flag():
    global X_flag
    global O_flag
    if X_flag:
        X_flag = False
        O_flag = True
    elif O_flag:
        O_flag = False
        X_flag = True


def fill_cells(value):
    if ' '.join(coordinates) == '1 1':
        if input_data[6] not in [' ', '_']:
            print('This cell is occupied! Choose another one!')
            return get_coordinates()
        else:
            input_data[6] = value
            change_flag()
            print_cells()
    elif ' '.join(coordinates) == '2 1':
        if input_data[7] not in [' ', '_']:
            print('This cell is occupied! Choose another one!')
            return get_coordinates()
        else:
            input_data[7] = value
            change_flag()
            print_cells()
    elif ' '.join(coordinates) == '3 1':
        if input_data[8] not in [' ', '_']:
            print('This cell is occupied! Choose another one!')
            return get_coordinates()
        else:
            input_data[8] = value
            change_flag()
            print_cells()
    elif ' '.join(coordinates) == '1 2':
        if input_data[3] not in [' ', '_']:
            print('This cell is occupied! Choose another one!')
            return get_coordinates()
        else:
            input_data[3] = value
            change_flag()
            print_cells()
    elif ' '.join(coordinates) == '2 2':
        if input_data[4] not in [' ', '_']:
            print('This cell is occupied! Choose another one!')
            return get_coordinates()
        else:
            input_data[4] = value
            change_flag()
            print_cells()
    elif ' '.join(coordinates) == '3 2':
        if input_data[5] not in [' ', '_']:
            print('This cell is occupied! Choose another one!')
            return get_coordinates()
        else:
            input_data[5] = value
            change_flag()
            print_cells()
    elif ' '.join(coordinates) == '1 3':
        if input_data[0] not in [' ', '_']:
            print('This cell is occupied! Choose another one!')
            return get_coordinates()
        else:
            input_data[0] = value
            change_flag()
            print_cells()
    elif ' '.join(coordinates) == '2 3':
        if input_data[1] not in [' ', '_']:
            print('This cell is occupied! Choose another one!')
            return get_coordinates()
        else:
            input_data[1] = value
            change_flag()
            print_cells()
    elif ' '.join(coordinates) == '3 3':
        if input_data[2] not in [' ', '_']:
            print('This cell is occupied! Choose another one!')
            return get_coordinates()
        else:
            input_data[2] = value
            change_flag()
            print_cells()


def print_cells():
    print('---------')
    print('|', input_data[0], input_data[1], input_data[2], '|')
    print('|', input_data[3], input_data[4], input_data[5], '|')
    print('|', input_data[6], input_data[7], input_data[8], '|')
    print('---------')


def check_win(user, other_user):
    """Check if the 'user' holds a genuine WIN"""
    if ((input_data[0] == input_data[1] == input_data[2] == user or
        input_data[0] == input_data[3] == input_data[6] == user or
        input_data[0] == input_data[4] == input_data[8] == user or
        input_data[1] == input_data[4] == input_data[7] == user or
        input_data[2] == input_data[5] == input_data[8] == user or
        input_data[2] == input_data[4] == input_data[6] == user or
        input_data[3] == input_data[4] == input_data[5] == user or
        input_data[6] == input_data[7] == input_data[8] == user) and
        ((input_data[0] == input_data[1] == input_data[2] and input_data[0] != other_user) or
         (input_data[0] == input_data[3] == input_data[6] and input_data[0] != other_user) or
         (input_data[0] == input_data[4] == input_data[8] and input_data[0] != other_user) or
         (input_data[1] == input_data[4] == input_data[7] and input_data[1] != other_user) or
         (input_data[2] == input_data[5] == input_data[8] and input_data[2] != other_user) or
         (input_data[2] == input_data[4] == input_data[6] and input_data[2] != other_user) or
         (input_data[3] == input_data[4] == input_data[5] and input_data[3] != other_user) or
         (input_data[6] == input_data[7] == input_data[8] and input_data[6] != other_user)) and diff <= 1):
        return True
    else:
        return False


def check_impossible(user, other_user):
    """Check if this is an Impossible game"""
    if (input_data[0] == input_data[1] == input_data[2] == user or
        input_data[0] == input_data[3] == input_data[6] == user or
        input_data[0] == input_data[4] == input_data[8] == user or
        input_data[1] == input_data[4] == input_data[7] == user or
        input_data[2] == input_data[5] == input_data[8] == user or
        input_data[2] == input_data[4] == input_data[6] == user or
        input_data[3] == input_data[4] == input_data[5] == user or
        input_data[6] == input_data[7] == input_data[8] == user) and \
        (input_data[0] == input_data[1] == input_data[2] == other_user or
         input_data[0] == input_data[3] == input_data[6] == other_user or
         input_data[0] == input_data[4] == input_data[8] == other_user or
         input_data[1] == input_data[4] == input_data[7] == other_user or
         input_data[2] == input_data[5] == input_data[8] == other_user or
         input_data[2] == input_data[4] == input_data[6] == other_user or
         input_data[3] == input_data[4] == input_data[5] == other_user or
         input_data[6] == input_data[7] == input_data[8] == other_user) or diff >= 2:
        return True
    else:
        return False


def check_status():
    # Store the difference between Xs and Os in diff variable
    global diff
    global break_flag
    if input_data.count('X') > input_data.count('O'):
        diff = input_data.count('X') - input_data.count('O')
    else:
        diff = input_data.count('O') - input_data.count('X')

# Print the state
    if check_impossible('X', 'O'):
        print('Impossible')
        break_flag = True
    elif check_win('X', 'O'):
        print('X wins')
        break_flag = True
    elif check_win('O', 'X'):
        print('O wins')
        break_flag = True
    elif (' ' not in input_data and '_' not in input_data) and diff <= 1:
        print('Draw')
        break_flag = True
    elif (' ' in input_data or '_' in input_data) and diff <= 1:
        # print('Game not finished')
        pass


# Driver code
input_data, break_flag, diff, coordinates = [], False, 0, ''
X_flag, O_flag = False, False

# Game loop
while True:
    if not any(input_data):
        X_flag = True
        O_flag = False
        input_data = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        print_cells()
    get_coordinates()
    check_status()
    if break_flag:
        break
    else:
        get_coordinates()
