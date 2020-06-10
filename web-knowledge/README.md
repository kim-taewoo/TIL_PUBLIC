# Git

## What is Git?
- Super popular Version Control System.  
- Git helps us manage our projects files.  

### Three main jobs Git helps us with
1. History
    - Git tracks changes (Git's `history`)

2. Collaboration
    - Helps collaboration with others with `merge`. 

3. Feature branches
    - 기능단위로 `branch` 를 나눠서 작업하고, 작업이 완료된 기능만을 실사용 서비스에 `merge` 할 수 있다. 즉, 여러 작업이 진행중이더라도 다른 작업들을 신경 쓸 필요 없이 눈앞의 `branch` 만 잘 관리하고 통합하면 된다.

## Vocab
- Project: Repository (repo)
- Working directory: Current git initialized folder
- Staging: Contorl what gets commited
    - 수정된 파일을 모두 `commit` 하지 않고, `commit` 할 파일만을 따로 `Staging Area` 로 뺀 후 `commit` 한다.
- Commit: Git's way of 'saving'
- Push && Pull

## Commands
- `git add -A`: `git add .` 와 동일
- `git checkout -- .`: 이전 `commit` 시점으로 복귀
- `git remote set-url origin https://...`: 기존에 `origin` 으로 저장되어있는 원격저장소 주소를 새로운 url 로 변경