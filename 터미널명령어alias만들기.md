## jupyter notebook alias 만들기



1. `vi .bashrc` 로 `.bashrc` 파일 만들기 및 접근 (`~` 위치에서 접근해야 함.)
2. `i` , 즉 insert mode 의 약자를 쳐서 편집 모드 진입
3. `alias jn="jupyter notebook"`
4. `esc` 3번 정도 연타해 편집 모드를 벗어난 후 `:wq` 를 쳐서 저장하고 vi 탈출.
5. 설정이 바뀌었음을 터미널에 알려주는 명령어인 `source ~/.bashrc` 를 쳐서 업데이트.
6. 나와서 `ls -a` 쳐보면 `.bashrc` 파일이 생겨 있는 걸 알 수 있음. 
7. `cat .bash_history` 를 치면 내가 이전에 어떤 명령어를 쳤었는지 리스트를 볼 수 있음. 사실 그냥 `history` 라고만 쳐도 비슷한 결과를 받아볼 수 있음.



## 동시에 두 개의 원격저장소에 `git push` 하는 방법

1. `vi .bashrc`
2. `alias doublepush="git push origin master && git push hub master"` 작성 및 저장
3. `source ~/.bashrc` 로 업데이트



## vi 단축키 몇개

### 입력 모드가 아닐 때.

1. 이동하기
   1. `l` 오른쪽
   2. `h` 왼쪽
   3. `k` 위쪽
   4. `j` 아래쪽
2. `o` 현재 커서 다음 줄로 넘어가며 입력모드로 변경
3. `i` 로 현재 커서 위치에서 입력모드로 변경