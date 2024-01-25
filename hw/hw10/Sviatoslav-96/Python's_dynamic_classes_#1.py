def class_name_changer(cls, new_name):
    if new_name.isalnum() and new_name and not new_name[0].isdigit() and not new_name[0].islower():
        cls.__name__ = new_name
    else:
        raise ValueError