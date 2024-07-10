name = "dachi"
age = 19

match name:
    case "dachi"|"shalva" if age >= 18:
        print("go to hell")
    case other if age < 18:
        print("you a good")
    case other:
        print("hi")