![Image](https://user-images.githubusercontent.com/108267207/206887668-a3ba847a-ef73-43a3-9718-9f23b2f91427.png)
## 디스코드 종합 봇
---
~24시간 사용가능~
서버컴이 켜져 있을때만 사용가능

> 평소 가장 자주 하는 고민이 무엇인가요? 혹시 "오늘 뭐 먹지?", "내일 뭐 입지?" 라면 이 BOT이 좋은 역할을 해줄 것입니다!  
>> 매일 저녁메뉴를 고르는 것도 참 어렵고, 내일 입고 나갈 옷을 고르는 일은 더 어렵습니다.  
>> 패션에는 관심이 없지만, 적어도 계절에 맞는 옷을 입는 것은 건강과 안전을 위해 중요합니다.  
>> 하지만 날씨 앱을 켜면 기온과 날씨만 표시될 뿐 해당 기온에는 어떤 옷차림으로 나가야 하는지 알 수 없습니다.  
>> 가령 17도라면 반팔을 입어야 할지, -3도라면 목도리까지 해야할지, 10도라면...?  
>> 체감이 되질 않아서 더더욱 옷을 입기가 어렵습니다.
그래서 간단한 명령어 하나만으로 내일의 날씨와 기온, 그리고 그에 맞는 옷차림을 자동으로 알려주는 봇을 구현해보았습니다.  
>> + 날씨•옷차림 알림 기능
>> + 메뉴 고민까지 해결하기 위해 랜덤으로 식사 메뉴를 추천해주는 기능
>> + 무료함을 달래줄 음악까지 재생되는 기능

> 게이머들에게 친숙한 디스코드에서 사용해봅시다!


## 명령어


| 명령어 | 설명 |
| ------ | ----------- |
| Hello   | 인사를 합니다. |
| Cody | 온도와 날씨, 그리고 거기에 맞는 옷을 추천합니다. |
| Menu    | 메뉴를 추천해줍니다.|
| Play title | 보이스 채널에서 title을 재생합니다. ( youtube에서 title을 검색후 가장 첫 영상 재생 ) |
| Leave | 음악을 종료합니다. |

## [시연](https://github.com/arypte/discord_bot/tree/master/%EC%8B%9C%EC%97%B0%EB%AA%A8%EC%8A%B5)

> 디스코드 서버에 초대하여 이용하는 경우
> + 봇은 서버 주인만 초대할 수 있습니다
> + 디스코드에서 서버를 신규 생성한 후,
   [링크](https://discord.com/api/oauth2/authorize?client_id=1048451699204948098&permissions=0&scope=bot)를 사용하여 봇을 초대해주세요.
> + 봇이 들어온 후 명령어를 사용합니다.

> 직접 코드를 사용하여 실행하는 경우
> + [디스코드 개발자 웹](https://discord.com/developers/applications/)에 접속합니다.
> + 새로운 봇을 만들고 토큰 키를 받아와 코드에 첨부합니다.
> + 명령어를 사용합니다.

<details>
<summary>시연 스크린샷</summary>
<div markdown="1">

![Hello](https://user-images.githubusercontent.com/108267207/206887888-b00c4932-c6c8-4c5b-b376-cd4a1d666984.png)
![Help](https://user-images.githubusercontent.com/108267207/206887889-71fb3b56-82f6-4e3d-822a-35162cf9a5b0.png)
![Menu](https://user-images.githubusercontent.com/108267207/206887891-e814917d-2bb4-49cb-be72-cdd2f5a69394.png)
![Play](https://user-images.githubusercontent.com/108267207/206887892-652d573d-e6b1-4fe5-a463-44c235b36204.png)
![Leave](https://user-images.githubusercontent.com/108267207/206887890-84fa4031-793e-425f-aeaf-8435f2ac92d5.png)

</div>
</details>

## 그 외


> 이 프로젝트는 API discord.py 를 기반으로 개발되었습니다. 개발에 사용한 패키지 목록은 다음과 같습니다.

    - discord
    - discord.ext
    - youtube_dl
    - requests
    - bs4 (BeautifulSoup)
    - urllib
    - ffmpeg


> 아래는 프로젝트를 개발하면서 코드 일부 인용 및 참고한 사이트 입니다.

+  [돔돔이블로그](https://domdom.tistory.com/entry/%ED%81%AC%EB%A1%A4%EB%A7%81-BeautifulSoup-%EC%82%AC%EC%9A%A9%ED%95%98%EB%A9%B4%EC%84%9C-%EC%8A%A4%ED%81%AC%EB%9E%98%ED%95%91%ED%95%B4%EC%98%A4%EA%B8%B0-%EC%96%B4%EB%A0%A4%EC%9B%A0%EB%8D%98-%EA%B2%83-%EC%A0%95%EB%A6%AC)

    파이썬 크롤링에 어려움을 느끼는 부분이 있어
    이 블로그를 참고하였습니다.

+ [꿀벌봇](https://github.com/NyaNyak/discord-beebot)

    아이디어와 readme 파일 제작에 참고하였습니다.

+ [디스코드 봇](https://koreanbots.dev/)

    개발자 페이지에서 Discord.py 기본 코드를 인용하였습니다.
    
+ [Markdown-it](https://markdown-it.github.io/)

    ReadMe파일 작성에 필요한 마크다운 문법을 참고.

## 문제점 및 개선점
<details>
<summary>더보기</summary>
<div markdown="1">

   

+ 문제점 / 개발하면서 어려웠던 점.
      
      1. Discord.py , youtube_dl , ffmpeg의 작동. 참고 할 수 있는 라이브러리나 코드가 대부분 구버전이어서 구현에 어려움이 있었다. Discord.py 의 경우 작년 11월에 지원, 개발을 중지하였다가 올 4월 부근 다시 재개하면서 많은 점이 달라졌다. 더구나 메인 서버컴에서는 작동하지만 노트북에서는 작동하지 않음. 문제점이 뭔지 확인하지 못함.

      2. ANACONDA의 호환성. 도저히 해결되지 않던 에러가 vscode로 ide를 바꾸니 해결되었다.
      
      3. 무료 배포를 해주던 웹사이트가 올 6월부터 유료로 전환되어 봇이 상시 작동하지 않음. 직접 서버컴에서 컴파일을 해주어야 함.

      4. 기존 계획은 옷의 추천에 실사용 코디를 넣을 예정이었지만, 개발자도 옷을 못입는 관계로 온도에 맞는 옷으로 변경.



+ 개선할 수 있는 부분
      
      1. 아마존 aws나 구글을 사용해서 배포
 
      2. 최신버전의 라이브러리를 사용해서 모든 곳에서 동일하게 사용하도록 업데이트.

      3. 온도에 맞는 옷에서 실제 활용 가능한 코디로 변경, 데이터베이스를 사용할 것.
 
      4. 음악 재생 - 리스트, 다음곡, 중지등 편의기능 추가


</div>
</details>
