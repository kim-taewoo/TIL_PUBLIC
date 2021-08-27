[공식 러스트 가이드북 내용 정리](https://doc.rust-lang.org/book/title-page.html)

# 폴더명

- 하나 이상의 단어일 경우 언더스코어를 이용한다.

# main 함수

- main 은 어떤 인자도 받지 않고 아무것도 반환하지 않는다.

# 설치

- `rustup` 이란 놈으로 러스트를 설치하고 업데이트 할 수 있다.

# rustc (러스트 컴파일러)

- `rustfmt` 이란 포맷터가 포함되어 있다.
- `C`, `C++` 의 `gcc`, `clang` 과 유사하다.
- binary 실행파일을 반환한다.
- 윈도우에서는 윈도우 실행파일(`.exe`) 외에도 `.pdb` 라는 디버깅 정보를 가진 파일을 반환한다.
- `ahead-of-time compiled language` 로, 자바스크립트, 파이썬, 루비와 같은 implementation 이 필요한 언어와 달리 실행파일만을 반환한다.

# Cargo

- Cargo 는 러스트의 빌드 시스템이자 패키지 매니저다.
- 코드를 구조화하고, 라이브러리(dependencies)를 다운로드하고, 그 라이브러리를 구조화하는 등의 역할을 한다.
- 공식 인스톨러에 포함되어 있다.
- `cargo --version` 으로 버전 확인
- `cargo new --help` 로 도움말 찾기
- `cargo new 프로젝트명` 으로 프로젝트 생성. `Cargo.toml` 파일과 , `main.rs` 파일을 가진 `src` 폴더를 생성한다.
- `.gitignore` 와 함께 Git 레포를 생성하는 게 기본 설정이지만 이미 존재하는 Git 레포가 있다면 생성되지 않는다. `cargo new --vcs=git` 으로 설정을 바꿀 수 있다.
- `.toml` 은 TOML(Tom's Obvious, Minimal Language) 포맷이며, 카고의 설정 포맷파일이다.
- `[package]`, `[dependencies]` 와 같은 대괄호 라인으로 섹션이 나누어져 있다.
- `cargo build` 로 `taget/debug/프로젝트명` 의 실행파일과 `Cargo.lock` 파일을 만들어낸다.
- `cargo run`으로 빌드 & 실행을 할 수 있다. 코드에 변경된 부분이 없으면 새로 빌드하지 않는다.
- `cargo check` 은 빌드가 가능한지 빠르게 체크하며, 실제로 빌드 결과물을 반환하진 않는다. 개발 도중 컴파일 가능한지 체크하기 위해 종종 쓸 것이다.
- `cargo build --release` 로 최적화를 갖춘 배포용 빌드를 할 수 있다. `target/release` 경로에 생성된다.
- Cargo 는 운영체제와 상관없이 같은 명령어를 사용할 수 있다는 장점도 있다.

# 코드 스타일

- 탭이 아닌 4개의 스페이스로 indent 한다.
- `println` 은 평범한 함수가 아니라 매크로다. 매크로는 `!` 를 이용해서 호출한다.
- 세미콜론으로 라인을 끝낸다.
