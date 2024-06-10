def maskify(cc):
    new_cc = (len(cc)-4) * "#"
    for i in cc[-4:]:
        new_cc += i
    return new_cc


def maskify(cc):
    new_cc = (len(cc)-4) * "#"
    return new_cc + cc[-4:]