from name_func import get_formatted

def test_first_and_last_name():
    formatted = get_formatted('janis', 'joplin')
    assert formatted == 'Janis Joplin'

def test_first_middle_last():
    formatted = get_formatted('Burt', 'bojangles', 'bubba')
    assert formatted == 'Burt Bubba Bojangles'