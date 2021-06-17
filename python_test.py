x=[100,110,120,130,140,150]
for k in x:
    if k%2==0:
        print(k)

       
        multiplied =[f*5 for f in x]
        print(multiplied)

# question2
def divisible_by_tree(num, factor=3):
    if factor < num:
      num = divisible(num, factor * 2)
    if num >= factor:
        num -= factor
    if factor > 3:
       return num
    return num == 0


# question3
def flatten_list(_2d_list):
    flat_list = []
    
    for element in _2d_list:
        if type(element) is list:
            
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

nested_list  = [[1, 2], [3,4], [5,6]]
print('Original List', nested_list)
print('Transformed Flat List', flatten_list(nested_list))

# 6
def divisible_by_seven():
    p=[]
for x in range(100,200): 
    if x%7==0: 
       p.append(x)
    #  return p

    print(divisible_by_seven)()
        
            
# 5
# p=['e','r''k','w''f','e']
l=['f','k','r','l']
x = ['a','b','a','e','d','b','c','e','f','g','h']
p=(x+l)
print(p)

# question 4
def smallest():
    k=[2,4,6,7,9,10,20,8]
    k.smallest([2,4,6,7,9,10,20,8])
    print(smallest)


students1 ={"age": 19, "name": "Eunice"}, 
student2={"age": 21, "name": "Agnes"},
student3={"age": 18, "name": "Teresa"},
student4= {"age": 22, "name": "Asha"}, 
def pupil():
    name="Agnes",
    date_of_birth=2021-2000,
    name="Teresa",
    date_of_birth=2021-1999,
    name="Asha",
    date_of_birth=2021-2001,

    # print f"hello{student2}your name is{name} and you were born in{year}"
    
    





    






