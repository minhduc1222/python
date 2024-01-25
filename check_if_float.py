def check_if_float(number):
    try:
        float(number)
    except ValueError:
        return False
    else:
        return True