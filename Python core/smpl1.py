def outFunc(func):
    def inFunc():
        print('unFunc exceuted')
        return func()
    return inFunc


@outFunc
def disp():
    print('Disp executed')


disp()
# fun = outFunc(disp)
# fun()


'''
def outFunc(msg):
    # msg = 'Hello'

    def inFunc():
        print(msg)
    return inFunc


print(outFunc('jdfbhaf'))
func1 = outFunc('heol')
func2 = outFunc('hayl')
func1()
func2()
print(func2.__name__)
'''
