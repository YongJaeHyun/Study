Website = input() # 웹사이트 입력
WebPassword = Website.replace("http://","") # http:// 제거
WebPassword = WebPassword[:WebPassword.index(".")] # 콤마(.) 이후로 제거

# 남은 문자열에서 처음 3개의 문자 + 패스워드 길이 + 문자 e 의 개수 + !
WebPasswordf = WebPassword[:3]+str(len(WebPassword))+str(WebPassword.count("e"))+"!" 

print(Website+"에서의 추천 비밀번호는"+WebPasswordf+"입니다")