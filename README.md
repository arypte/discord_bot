# discord_bot
## 디스코드 종합 봇
---
~24시간 서버~

> '디스코드'는 게임을 좋아하는 사람들은 대부분 써
>> AA
> > > ...or with spaces between arrows.


## 명령어


| 명령어 | 설명 |
| ------ | ----------- |
| Hello   | 인사를 합니다. |
| Cody | 온도와 날씨, 그리고 거기에 맞는 옷을 추천합니다. |
| Menu    | 메뉴를 추천해줍니다.|
| play title | 보이스 채널에서 title을 재생합니다 |

## [시연](https://github.com/arypte/discord_bot/tree/master/%EC%8B%9C%EC%97%B0%EB%AA%A8%EC%8A%B5)

> 디스코드 서버에 초대하여 이용하는 경우
>> + 봇은 서버 주인만 초대할 수 있습니다
>> + 디스코드에서 서버를 신규 생성한 후,
   [링크](https://discord.com/api/oauth2/authorize?client_id=1048451699204948098&permissions=0&scope=bot)를 사용하여 봇을 초대해주세요.
>> + 봇이 들어온 후 명령어를 사용합니다.

> 직접 코드를 사용하여 실행하는 경우
>> + [디스코드 개발자 웹](https://discord.com/developers/applications/)에 접속합니다.
>> + 새로운 봇을 만들고 토큰 키를 받아와 코드에 첨부합니다.
>> + 명령어를 사용합니다.


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


</div>
</details>
