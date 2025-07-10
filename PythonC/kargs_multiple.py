def full_name(first,last,title):
    name=f'full name is :{first} {last} {title}' #f string bole etare
    return name
name=full_name('alu','kodu','alubhotta')
print(name)
def famous_name(first,last,title,addition):
    name=f'{title}{first} {last} {addition}'
    return name
name=famous_name(first='taheri',last='ali',title='hujur',addition='sayok')
print(name)






#simple bhabe return

def a_lot(num1,num2):
    sum=num1 + num2
    mult=num1*num2
    remain=num1-num2
    return sum,mult,remain

everything =a_lot(55,21)
print(everything)