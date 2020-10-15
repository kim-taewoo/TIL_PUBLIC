[참고 블로그](https://victorydntmd.tistory.com/125?category=687930)

# DB 설계 단계
1. 실세계 - 요구사항 수집 분석
    먼저 실제 세계에서 어떤 시스템을 구축할 것인지에 대한 요구사항을 수집합니다.
요구사항에 대해 어떤 데이터들이 필요한지, 어떤 기능들이 필요한지 분석합니다. 
2. 개념적 설계
    ER 다이어그램을 통해 요구사항을 개념적으로 표현합니다.
3. 논리적 설계
    관계 모델(Relation model)을 통해 개념적 설계를 논리적으로 표현합니다.
4. 물리적 설계
    실제 디스크와 같은 물리 저장장치에 데이터를 저장할 수 있도록 표현합니다.

## 개념적 설계 

개념적 설계는 ER 다이어그램( Entity Relationship Diagram )을 통해 모델링하는 단계입니다.

ER 모델은 요구사항으로부터 얻어낸 정보들을 개체(Entity), 애트리뷰트(Attribute), 관계성(Relation)으로 기술하는 데이터 모델을 말합니다.

### 개체( Entity )
개체란 단독으로 존재하는 객체를 의미하며, 동일한 객체는 존재하지 않습니다.
예를 들어, 학생 정보가 학번, 이름, 학년이 있을 때, 3개의 정보가 모두 같은 학생이 오직 한 명이면 이를 개체라고 합니다.
즉, 학생 한명이 개체가 되는 것입니다.
이 **개체들의 집합을 Entity Type**이라고 합니다. 여기서는 Student, Course가 되겠네요.

ER 다이어그램에서 Entity Type은 네모로 표현합니다.

### 애트리뷰트, 속성( Attribute )

개체가 갖는 속성을 의미합니다.

예를 들어, Student에서 학번, 이름, 학년 같은 정보를 속성이라 합니다.

ER 다이어그램에서 Attribute는 원으로 표현합니다.

속성은 특성에 따라 많은 종류로 나뉘는데, 위 참조 블로그에 들어가서 읽어보면

DB 설계 때 어떻게 ER 을 그려야 할 지 감을 잡을 수 있을 것이다. 

### 관계 ( Relation )
Entity Type간의 관계를 의미합니다.
예를 들어, 수강을 뜻하는 Takes는 학생과 과목간의 "수강"이라는 관계를 갖습니다.
이 때 Takes를 Relation Type이라 하며, Relation Type 역시 속성을 가질 수 있습니다.
ER 다이어그램에서 Relation은 마름모로 표현합니다.

관계성은 2가지 제약조건을 명시함으로써 표현할 수 있습니다.
1. 카디널리티 비율 제약조건 ( Cardinality Ratio Constraint )
    - 흔히 1:1, 1:N, N:M 이라고 부르는 그것입니다.

2. 참여 제약조건 ( Participation Constraint )
    관계를 맺는 두 Entity Type에 대해 한 개체의 존재가 다른 개체의 존재에 의존하는지 여부를 나타내는 제약조건을 뜻합니다. 에를 들어, 학생은 과목을 꼭 수강 할 필요가 없지만 과목은 항상 수강생이 있어야 합니다. 수강생이 없는 과목은 폐강되기 때문이죠.

    1. 전체 참여 ( Total Participation ): 하나 또는 그 이상의 개체가 참여
    2. 부분 참여 ( Partial Participation ): 선택적인 참여

## 논리적 설계

논리적 설계는 개념적 설계에서 표현한 ER 다이어그램을 테이블로 표현하는 단계를 말합니다.

여기서 말하는 테이블은 행과 열이 있는 표를 의미합니다.

SQL을 작성하기 위한 테이블 정의라고 보면 됩니다.

## 물리적 설계

이제 테이블의 구조, 즉 스키마가 정리됐으니 사용하는 DBMS의 SQL로 테이블을 생성해야 합니다.



🙈[DB이론] ER 모델( Entity Relation Model ) - 개념적 설계🐵2018. 2. 5. 11:22


1. ER 모델( Entity Relation Model )

ER 모델은 요구사항으로부터 얻어낸 정보들을 개체(Entity), 애트리뷰트(Attribute), 관계성(Relation)으로 기술하는 데이터 모델을 말합니다.





개체( Entity )
개체란 단독으로 존재하는 객체를 의미하며, 동일한 객체는 존재하지 않습니다.
예를 들어, 학생 정보가 학번, 이름, 학년이 있을 때, 3개의 정보가 모두 같은 학생이 오직 한 명이면 이를 개체라고 합니다.
즉, 학생 한명이 개체가 되는 것입니다.
이 개체들의 집합을 Entity Type이라고 합니다. 여기서는 Student, Course가 되겠네요.

ER 다이어그램에서 Entity Type은 네모로 표현합니다.

애트리뷰트, 속성( Attribute )

개체가 갖는 속성을 의미합니다.

예를 들어, Student에서 학번, 이름, 학년 같은 정보를 속성이라 합니다.

ER 다이어그램에서 Attribute는 원으로 표현합니다.

관계 ( Relation )
Entity Type간의 관계를 의미합니다.
예를 들어, 수강을 뜻하는 Takes는 학생과 과목간의 "수강"이라는 관계를 갖습니다.
이 때 Takes를 Relation Type이라 하며, Relation Type 역시 속성을 가질 수 있습니다.
ER 다이어그램에서 Relation은 마름모로 표현합니다.


ER 다이어그램을 구성하는 요소는 위와 같습니다.

이제부터 ER 다이어그램을 그리기 위한 각 요소들을 표현하는 방법에 대해 알아보도록 하겠습니다.









2. 애트리뷰트 ( Attribute )

1) Attribute Domain

해당 Attribute가 가질수 있는 집합(도메인)을 말합니다.
예를 들어,
학생의 학년을 뜻하는 year 애트리뷰트는 1,2,3,4 와 같은 숫자만 허용하므로 year의 Attribute Domain은 정수형(integer)입니다.
학생의 이름을 뜻하는 name 애트리뷰트는 문자열이여야 하므로 name의 Attribute Domain은 문자열(String)입니다.




2) 키 애트리뷰트 ( Key Attribute )

다른 객체들과 중복되지 않는 고유한 값을 가진 Attribute로서, 주로 객체를 식별하는데 사용되는 Attribute입니다.
예를 들어, 학생의 학번을 의미하는 Student_no는 다른 학생들과 중복되지 않는 고유한 번호입니다.
따라서 Student_no는 Key Attribute 입니다.
Key Attribute를 ER 다이어그램에서는 원에 밑줄로 표시합니다.






3) 복합 애트리뷰트 ( Composite Attribute )

독립적인 Attribute들이 모여서 생성된 Attribute를 의미합니다.
예를 들어, 학생의 주소를 나타내는 Address 애트리뷰트가 있을 때, 우리나라에서 주소는 "경기도", "OO시", "OO동", "OO아파트"와 같이 표현합니다.

즉 Address는 위의 4개의 독립된 Attribute가 모여서 생성된 Attribute이므로 Address를 Composite Attribute라고 합니다.







4) 다중값 애트리뷰트 ( Multi-Valued Attribute )

하나의 Attribute가 여러 개의 값을 가지는 Attribute를 의미합니다.
예를 들어, 학생의 전공을 나타내는 Degree Attribute가 있다고 있을 때, 이 학생이 복수 전공을 할 경우 Degree Attribute 값이 2개가 되므로, 이 때 Degree Attribute를 Multi-Valued Attribute라고 합니다.
이와 달리, 오직 하나의 값을 갖는 애트리뷰트를 단일값 애트리뷰트(Single-Valued Attribute)라고 합니다.
Multi-Valued Attribute는 ER 다이어그램에서 두 개의 원으로 표현합니다.
            





5) 유도된 애트리뷰트 ( Derived Attribute )

다른 Attribute가 갖고 있는 값으로부터 계산되어져 나온 Attribute를 의미합니다.
예를 들어, 모든 상품의 총 가격을 나타내는 total, 상품의 가격을 나타내는 price, 상품의 개수를 나타내는 count Attribute가 있다고 가정하겠습니다. 
total은 price와 count의 곱으로 계산되어져 나오는 값이므로 total Attribute는 Derived Attribute입니다.
Derived Attribute는 ER 다이어그램에서 원을 점선으로 표현합니다.
              









3. 관계성 ( Relationship )

ER 다이어그램을 설계하는 가장 큰 목적은 Entity Type을 정의하고 Entity Type간의 관계를 표현하는 것입니다.

Attribute를 통해 Entity Type을 정의했다면, Relationship을 통해 Entity Type간의 관계를 표현 표현합니다.



관계성은 2가지 제약조건을 명시함으로써 표현할 수 있습니다.



1) 카디널리티 비율 제약조건 ( Cardinality Ratio Constraint )

관계를 맺는 두 Entity Type에 대해, 한 개체가 얼마나 많은 다른 개체와 관련될 수 있는지를 나타내는 제약조건을 뜻합니다.

일대일(1 : 1)

두 개 Entity Type의 개체들은 서로 일대일로 대응

일대다(1 : N)

하나의 개체가 다른 Entity Type의 많은 개체들과 관련되지만, 그 역은 성립하지 않음

다대다(N : M)

하나의 개체가 다른 Entity Type의 많은 개체들과 관련되며, 역이 성립

( 일대일, 일대다, 다대다에 대한 자세한 내용은 여기를 참고해주세요 ! )



예를 들어, "학사 관리 시스템"에서 한 학생은 많은 과목을 수강할 수 있고 한 과목에는 많은 학생이 수강하므로, Student Entity Type과 Course Entity Type은 N : M 관계입니다.

이러한 카디널리티 비율제약조건을 ER 모델에 표현하면 다음과 같이 N, M을 명시해줘서 표현합니다.





또 다른 예시로, 부모와 자식 Entity Type 관계에서 부모는 많은 자식을 가질 수 있지만 자식은 한 부모만 가질 수 있습니다.

즉, 부모와 자식은 1 : M 관계이며, 이를 ER 다이어그램으로 다음과 같이 표현할 수 있습니다.

간혹 1과 M을 어느 선에 명시해야 할지 헷갈리는 경우가 있는데, M에 해당하는 Entity Type에 M을 명시해주면 됩니다.









2) 참여 제약조건 ( Participation Constraint )

관계를 맺는 두 Entity Type에 대해 한 개체의 존재가 다른 개체의 존재에 의존하는지 여부를 나타내는 제약조건을 뜻합니다.

전체 참여 ( Total Participation )
하나 또는 그 이상의 개체가 참여
부분 참여 ( Partial Participation )
선택적인 참여


에를 들어, 학생은 과목을 꼭 수강 할 필요가 없지만 과목은 항상 수강생이 있어야 합니다.

수강생이 없는 과목은 폐강되기 때문이죠.



ER 모델에서 전체 참여는 두 개의 실선으로 부분 참여는 한 개의 실선으로 표현하고, 이를 표현하면 다음과 같습니다.









3) 구조적 제약조건 ( Structural Constraint )

앞서 살펴 본 두 개의 제약조건을 가리켜 구조적 제약조건이라 합니다.

구조적 제약조건은 관계를 맺는 두 Entity Type에 1 , N , M을 표시하거나 한 줄 또는 두 줄을 표시하지 말고 ( MIN, MAX ) 방식으로 두 제약조건을 한 번에 표현하는 방식입니다.



예를 들어, 학생은 최소 3개, 최대 6개의 강의를 수강할 수 있으며, 강의는 최소 10명 최대 100명의 학생들이 들을 수 있을 때, 이를 ER 다이어그램으로 표현하면 다음과 같습니다.









지금까지 여러 애트리뷰트와 관계성의 두 가지 제약조건의 개념, 그리고 이를 ER 다이어그램에서 어떻게 표현하는지에 대해 알아보았습니다.

이 내용들을 정리하면 아래 그림과 같습니다.













마지막으로 약한 개체 (Weak Entity)와 식별 관계성 타입(Identifying Relationship Type)에 대해 알아보도록 하겠습니다.

# 약한 개체( Weak Entity )와 식별 관계성 타입(Identifying Relationship Type)

약한 개체란 자신의 Key Attribute가 없는 Entity Type을 뜻합니다.

예를 들어 "학사 관리 시스템"에서 강의번호 10043는 10043-01 , 10043-02와 같이 여러 개의 분반이 있을 수 있습니다.

이 때 분반이라는 개체는 자신의 key Attribute가 없고, 강의 테이블에 의존하기 때문에 약한 개체라 합니다.

다시 말하면 분반이 존재하기 위해서는 꼭 Course Entity Type이 있어야 합니다. ER 다이어그램에서 부분 키는 점선으로 된 밑줄로 표현합니다.

또한 Entity type이 약한 개체와 관계를 맺을 때는 식별 관계성 타입으로 표현하고, ER 다이어그램에서 두 개의 마름모로 표현합니다.

약한 개체는 항상 의존적이기 때문에 참여 제약 조건은 전체 참여( total participation )입니다.



