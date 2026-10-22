from tools import get_current_time, roll_dice, generate_password


def test_get_current_time():
    print(get_current_time())


def test_roll_dice():
    print(roll_dice())


def test_generate_password(length: int = 12):
    print(generate_password(length))


if __name__ == '__main__':
    test_get_current_time()
    test_roll_dice()
    test_generate_password(20)
    test_generate_password(50)
    test_generate_password()
