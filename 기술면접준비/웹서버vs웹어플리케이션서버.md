# tldr
Web Server와 WAS 차이 정리

Web Server : 정적

WAS(Web Application Server) : 동적

# Web Server와 WAS를 따로 두는 이유 정리

1. 서버부하 방지 (정적 컨텐츠는 웹서버에서 바로 제공한다.)

2. 하나의 서버 혼용 Application (java, php.. 등)사용 가능
    - 더 앞단의 웹서버에서 정적 파일을 제공하면서 뒷단 연결하는 서버는 자유로우니까.

3. 로드밸런싱 (장애가 나거나 과부화된 WAS 로 연결하지 않는다.)

4. SSL 암호화, 복호화 처리에 웹서버를 사용하면 보안 강화도 가능하다.
    - SSL 인증서로 브라우저와 사이트의 웹서버 상의 암호화 통신을 지원. 해킹을 당해도 개인정보 복호화 불가능
    - SSL “핸드셰이크” 개념으로, 브라우저에 대한 암호화 통신 채널을 자동으로 생성
    - [SSL 자세히 설명하는 사이트](https://www.digicert.com/what-is-an-ssl-certificate)

즉, 자원 이용의 효율성 및 장애 극복, 배포 및 유지보수의 편의성을 위해 Web Server와 WAS를 분리한다.

### 용어 정리

1. 하나의 서버에 WEB, WAS, DB 설치 : single-Tier

2. WEB 서버 , WAS, DB 서버 : 2-Tier

3. WEB 서버 , WAS 서버 , DB 서버 : 3-Tier