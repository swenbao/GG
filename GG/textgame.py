import time


def print_slowly(text):
    line_list = text.split('\n') # 結果是一個 list 喔
 
    for line in line_list:
        print(line)
        time.sleep(0.5)
    
    # 沒有要 return 的東西，可以不寫 return
    # 執行到底 function 就會自己停了
    
print_slowly("""叮咚！歡迎光臨全聯福利中心！！
你跨過了自動門，冷風彿過你的四肢，突如其來的溫差使你忍不住發抖。
你環顧四周，發現全聯福利中心的燈光暗淡，顯得有些詭異""")


while True:
    print("""
    ------
    
    你要:
    1) 乾！太可怕惹！逃走！
    2) 進去啊！怕屁怕！
    
    """)
        
    selection = input()

    if selection == "1":
        print("怕屁阿")
        exit()

    elif selection == "2":
        break
    else:
        print("你在工三小")