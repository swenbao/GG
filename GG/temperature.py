def f2c(f):
    c=(f-32)*5/9
    
    return c
f=float(input("輸入華氏溫度："))
print("攝氏:",f2c(f),"度")