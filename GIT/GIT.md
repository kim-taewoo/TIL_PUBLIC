# GIT

## 상식

1. 리누스 토발즈가 개발
2. SCM(Sorce Code Management) 또는  VCS(Version Control System) 이라고 한다.
3. Version(버전)을 Snapshot(스냅샷) 이라고도 한다.



[GIT 괜찮은 참고자료](https://backlog.com/git-tutorial/kr/intro/intro1_1.html)



## 만들기 & 지우기

1. git init
2. ls -a  로 숨겨진 `.git` 파일 확인 가능.
3. `cat config` 명령어로 config 폴더 내용 출력 가능.
4. `rm -r .git/` 으로 git 폴더를 지울 수 있다. (`-r` 이 폴더를 지우기 위해 필요하다.)



## 기본 사용법

흔히 사진 찍는 과정에 비유한다. `add` 로 피사체를 찍는 판에 올리고, `commit` 으로 사진을 찍는다.

1. git status` 로 폴더 버전 상태 확인
2. `git add 파일||폴더명`  (ex: git add 00_markdown_basic.md) `git add .` 로 폴더 내 모든 파일 추가 가능.
3. `commit` 하기 전 git 의 전역 설정을 해야한다.
   1. `git config --global user.email "you@example.com"`  // github 가입 이메일과 같이 할 것!
   2. `git config --global user.name "Your name"`
   3. `git config --global --list` 로 현재 git 전역 설정 확인
4. `git commit -m "Your commit message"` 로 기록할 메시지와 함께 현재 버전을 기록한다. 메시지 내용은 어떤 작업을 했는지 명확히 표현하도록 한다.
5. `git log` 로 지금껏 commit 기록을 볼 수 있다. 이 때 좀 더 간략히 한 줄로 출력하도록 `git log --oneline` 을 많이 쓴다.
6. `git checkout 커밋로그식별주소` 명령어로 과거 commit 시점을 슬쩍 볼 수 있다. 이 때 sha-1 해시 값으로 된 식별값을 이용한다. (`git log` 쳤을 때 나오는 맨 앞 16진수 수)  이 때 과거 시점으로 돌아간 뒤 함부로 내용을 바꾸면 큰일난다...
7. `git checkout master` 으로 과거 시점에서 현시점으로 돌아올 수 있다. 
8. `git remote add 원격저장소의이름(별명) 저장소의주소` 로 원격 저장소 주소를 추가할 수 있다.
9. 원격 저장소를 추가한 뒤 `git remote -v` 로 원격저장소 연결 상태를 확인할 수 있다. 
10. `git push 원격저장소이름 브랜치이름` 으로 원격저장소에 로컬 commit 내역과 코드를 저장할 수 있다.



