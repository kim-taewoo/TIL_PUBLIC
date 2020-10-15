[출처](https://victorydntmd.tistory.com/124?category=687930)

# DBMS ( Database Management System )

애플리케이션과 시스템에 저장되어 있는 데이터의 중재자로서의 소프트웨어 시스템을 말합니다.

흔히 알고 있는 MySQL, Oracle, MS-SQL 등이 DBMS입니다.

# 데이터베이스 시스템

collect(데이터 수집), processing(원하는 정보를 얻기 위해 데이터 처리), organize(데이터를 조직화해서 저장) 등의 작업을 잘할 수 있도록 도와주는 시스템을 말합니다.

데이터베이스는 다음과 같은 특징이 있습니다.

1. 여러 사용자들의 공동 접근이 가능해야 한다.
2. 계속적인 변화를 통해 실시간으로 처리할 수 있는 운영 시스템이어야 한다.
3. 메모리 주소가 아닌 내용을 통해 데이터를 참조한다.
    => 실시간 접근성 / 계속적인 변화 / 동시 공유성 / 운영 가능 / 내용 참조

# DBMS의 기능

DBMS는 데이터를 정의, 조작, 제어할 수 있어야 하며, 관계형 데이터베이스 관리 시스템( RDBMS )에서는 데이터를 SQL 언어를 통해 다룰 수 있습니다.

SQL에는 다음과 같은 종류로 나눌 수 있습니다.

- DDL ( Data Definition Language )
    - 데이터를 정의하는 언어
- DML ( Data Manipulation Language )
    - 데이터를 조작하는 언어
- TCL  ( Transaction Control Language )
    - 데이터의 안정성, 정확성을 유지하는 언어
    - Mutual exclusion( 상호배제 )를 통한 transaction이 서로 방해를 받지 않도록 병행 제어
        - **transaction** : 하나의 실행 묶음 단위

