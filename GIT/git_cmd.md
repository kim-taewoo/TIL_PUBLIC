# git 명령어

bash 창에서 `git [명령어] -h`로 해당 명령의 도움말 확인 가능



| 명령                                      | 내용                                 | 비고 |
| ----------------------------------------- | ------------------------------------ | ---- |
| `git init`                                | 현재 폴더에 Git Repository 생성       |      |
| `git status`                              | git 현재 상태 확인                   |      |
| `git config -l`                           | config 설정 확인하기                 |      |
| `git add`                                 | 파일 또는 폴더를 staging             |      |
| `git add -u`                              | 수정사항을 모두 add                  |      |
| `git commit -m 'Commit message'`          | 커밋 메시지와 함께 저장              |      |
| `git log --oneline`                       | git log 한줄만 확인                  |      |
| `git checkout [branch]`                   | 해당 커밋으로 버전 변경              |      |
| `git remote`                              | 원격저장소와 통신(목록 표시)         |      |
| `git remote add [alias] [remote_URL]`     | 원격저장소 추가(기본: `origin`)      |      |
| `git push [remote] [branch]`              | 브랜치(`master`)를 원격저장소에 저장 |      |
| `git clone [remote_URL]`                  | 원격저장소를 복제(`git init` 필요 X) |      |
| `git clone [remote_URL] [alias]`          | 내가 정한 별명으로 clone             |      |
| `git pull [remote] [branch]`              | 원격저장소의 변경 내용을 끌어오기    |      |
| `git branch [alias]`                      | 브랜치 생성                        |      |
| `git branch -d [alias]` | 브랜치 삭제 | |
| `git switch [branch]`                     | 브랜치 이동                       |       |
| `git merge [branch]`                      | `master` 브랜치에서 merge하려면 `master`로 이동한 후 merge할 브랜치를 명령 뒤 매개변수로 입력                                 |       |
|           |           |       |




### git 초기화?

검색해볼 것...

```shell
$ git credential reject
protocol=https
host=lab.ssafy.com


```

