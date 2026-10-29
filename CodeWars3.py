def abbrev_name(name):
    name1 = name.split(" ")[0]
    name2 = name.split(" ")[1]
    first_name = name1[:1].upper()
    last_name = name2[:1].upper()
    return first_name + "." + last_name