left_Coffee_Num = 200  # 현재 팔 수 있는 커피의 개수
coffee_Price = 200    # 커피의 가격
while 1:
      # 판매기에 음의 값을 넣을 수는 없으므로 고려하지 않음
      get_Money = int(input("""
      커피의 가격은 {coffee_Price}원 입니다.
      현금을 넣어주세요 : """))
      print("")
      
      # 받은 현금이 커피 한 잔 가격이상이어야 수량을 선택 가능
      if get_Money >= coffee_Price:
            get_Coffee_Num = int(input("수량을 선택해주세요 : "))
            get_Extra_Money = 0
            print("")
            
            # 커피의 총 가격보다 판매기에 들어온 돈이 적다면, 들어온 돈이 더 많을 때까지 입력을 받음.
            if get_Money < get_Coffee_Num*coffee_Price: 
                  
      # 여분의 돈 입력에서 return 값을 받으면 while문을 탈출하여 else문을 통해 다시 처음으로 돌아감.
                  while get_Money < get_Coffee_Num*coffee_Price and get_Extra_Money != 'return':
                        
                        print(f"""      
잔액이 {abs(get_Money - get_Coffee_Num*coffee_Price)}원 부족합니다. 
현재 총 {get_Money}원 받았습니다... 
""")                      
                        # 입력값에 따라 if, elif, else 중 하나의 명령을 실행함.
                        get_Extra_Money = input(f"""
돈을 {abs(get_Money - get_Coffee_Num*coffee_Price)}원 이상 더 넣어주세요.
개수를 다시 정하시고 싶으시면 엔터를 입력해주세요
처음부터 다시 정하시고 싶으시면 'return'을 입력해주세요 : """)

                        # 입력값에 따른 명령들  
                        if get_Extra_Money == '':
                              get_Coffee_Num = int(input("커피 개수를 다시 정해주세요 : "))
                        
                        elif get_Extra_Money == 'return': pass
                        
                        elif get_Extra_Money == '%d':
                              get_Money += int(get_Extra_Money)
                        else:
                              print("숫자, 엔터키 혹은 return 중에서 입력해주세요.")
                              continue
            # 입력한 커피의 개수가 남아 있는 커피 개수보다 많다면 다시 처음으로 돌아감.               
            if get_Coffee_Num > left_Coffee_Num:
                  
                  print(f"""
커피의 수량이 부족합니다... 더 적은 수량으로 다시 선택해주세요!
{get_Money}원을 다시 돌려주고 커피를 주지 않습니다...
현재 판매 가능한 커피의 개수는 {left_Coffee_Num}개 입니다.
                        """)                  
                  continue
            
            # 커피의 총 가격보다 입력한 돈이 크다면, 정상적으로 커피를 줌. 
            if get_Money >= get_Coffee_Num*coffee_Price:
                  left_Coffee_Num -= get_Coffee_Num
                  
                  print(f"""
거스름돈 {get_Money - get_Coffee_Num*coffee_Price}원을 주고 커피 {get_Coffee_Num}개가 나옵니다...
앞으로 팔 수 있는 커피의 개수는 {left_Coffee_Num}개 입니다.
                        """)
                  
            # 2번째 While 문에서 Pass를 통해 빠져나온 값 예외 처리
            else:
                  print(f"""
{get_Money}원을 다시 돌려주고 커피를 주지 않습니다...
앞으로 팔 수 있는 커피의 개수는 {left_Coffee_Num}개 입니다.
                  """)
                  
      # 받은 돈이 커피 한 잔의 가격보다 적을 때
      else:
            print(f"""
{get_Money}원을 다시 돌려주고 커피를 주지 않습니다...
앞으로 팔 수 있는 커피의 개수는 {left_Coffee_Num}개 입니다.
                  """)
      
      # 커피를 준 후, 더이상 팔 수 있는 커피가 없을 때
      if left_Coffee_Num == 0:
            print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
            break