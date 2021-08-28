# Managing growing projects with Packages, Crates, and Modules

- A package can contain multiple binary crates and optionally one library crate.
- 패키지가 커지면 일부를 별도의 crates 로 추출해 외부 의존성으로 둘 수 있다.
- 엄청 큰 프로젝트의 경우 연관 패키지들을 Cargo workspaces 로 나눠 관리할 수 있다.
- 이런 프로젝트 관리, 스코프 관리 등을 모듈 시스템이라고도 한다.

# module system, include:

- Packages: A Cargo feature that lets you build, test, and share crates
- Crates: A tree of modules that produces a library or executable
- Modules and use: Let you control the organization, scope, and privacy of paths
- Paths: A way of naming an item, such as a struct, function, or module
