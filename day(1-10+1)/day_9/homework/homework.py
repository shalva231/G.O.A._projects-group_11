'''
დაპრინტეთ 1 - იდან 100-ის ჩათვლით ყველა ლუწი და კენტი რიცხვი და გვერდით მიუწერეთ "ლუწია" "კენტია"
'''
for i in range(1,100+1):
    if i % 2 == 0:
        print(f"{i} - კენტია")
    else:
        print(f"{i} - ლუწია")