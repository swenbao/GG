hw = input("請輸入所有作業成績，成績間隔用空白鍵：")

hw_list=hw.split() 
print(hw_list)


hw= [float(grade) for grade in hw_list]
print(hw)


mid = float(input("請輸入期末考成績："))
final = float(input("請輸入期末考成績："))
 
avg_hw = sum(hw)/ len(hw) # 這裡也有改動
grade = (mid * 0.3) + (final * 0.3) + (avg_hw * 0.4)
grade **= 0.5 # 縮寫
grade *= 10 # 縮寫
 
print(grade)
