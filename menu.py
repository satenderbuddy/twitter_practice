import helper

me = 'Hadd_hai_bhai'

continue_app = True
while(continue_app):
    print(helper.menu)
    option = int(input('Choose from above:'))
    func = helper.choose(option-1)
    if isinstance(func, str):
        print(func)
    else:
        func(me)
    flag = input("Do you want to continue?: ")
    if flag.lower() == 'n':
        continue_app = False
        
    
