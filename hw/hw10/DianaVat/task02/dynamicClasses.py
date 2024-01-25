def class_name_changer(cls, new_name):
    if str.isupper(new_name[:1]):
        if new_name.isalnum():
            cls.name = new_name
        else:
            raise "Error"     
    else:
        raise "Error"