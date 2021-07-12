SQL 문은 `중간 -> 뒤 -> 앞` 의 순서로 읽는 게 해석하기 좋다.
`SELECT * FROM users WHERE users.id > 5` 같은 경우 users 테이블에서, users.id > 5 조건에 맞는 것들 중에, `SELECT *` 해라. 라고 해석하는 게 자연스럽다. sql 문 작성할 때도 일단 SELECT 까지 치고 엔터로 다음줄 넘어가서 테이블 선택, 필터링 다 한 뒤에 마지막으로 SELECT 를 완성하는 게 편하다.

sql 에서는 변수할당의 개념이 없기 때문에 `==` 대신 `=` 으로 `같다` 연산자를 가진다.

one-to-many, many-to-one 의 개념에서 보통 many 쪽이 one 을 가리키는 Foreign Key 를 가진다. 즉 화살표 방향이 many -> one 이다. 애초에 아래 코드처럼, `REFERENCES` 한다는 말이 대상을 가리킨다는 뜻이기도 하다.

```sql
CREATE TABLE photos (
  id SERIAL PRIMARY KEY,
  url VARCHAR(200),
  user_id INTEGER REFERENCES users(id)
);
```

FK 부분에 아무것도 넣기 싫다면 'NULL' 값을 넣으면 된다.

FK 가 가리키는 대상이 삭제되었을 때 어떻게 할지는 약 5가지가 있다.

1. 자신을 가리키는 many 쪽 레코드가 있다면 에러
2. 무조건 에러
3. CASCADE `ON DELETE CASCADE`
4. SET NULL `ON DELETE SET NULL`
5. default 값

위 삭제 설정은 당연히 FK 컬럼을 만들 때 설정한다.

```sql
CREATE TABLE photos (
  id SERIAL PRIMARY KEY,
  url VARCHAR(200),
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
```

## Join 과 Aggergation

Join 은 다양한 리소스로 부터 테이블 row 들을 모아서 데이터 값들을 만들 때 사용한다고 생각하면 되고, Aggregation 은 다양한 row 들을 사용해서 **계산** 해서 목표하는 값을 만들어내는 것이 목적이다.

### Join

1. INNER JOIN <- DEFAULT in pg
1. LEFT JOIN
1. RIGHT JOIN
1. FULL JOIN

INNER JOIN 외의 JOIN 에서 매칭되지 않는 모든 값들은 NULL 이 된다.

### GROUP BY 와 Aggregation

```sql
SELECT manufacturer
FROM phones
GROUP BY manufacturer;
```

위와 같이 GROUP 화 한 뒤에는, `SELECT` 구문에 그 **그룹화된 컬럼만 직접적으로 선택 가능**하다. 즉, phones 테이블에 name 과 같은 컬럼이 있었어도 GROUP 뒤에는 선택하려고 하면 에러가 발생한다.

GROUP BY 는 Aggregates 와 함께 많이 쓰인다. GROUP BY 로 묶인 그룹들을 대상으로 AVG(), COUNT(그룹화된 컬럼) 등등을 많이 쓰기 때문. **Aggregate 는 각 그룹마다 연산된다.**

물론 그룹화 없이 `COUNT(*)` 같은 것도 많이 쓰이는 Aggregate

HAVING 은 WHERE 처럼 필터링 하는 키워드긴 한데, WHERE 은 ROWS 를 필터링 한다면 HAVING 은 반드시 GROUP BY 와 함께 쓰이면서 GROUP 들을 대상으로 필터링 한다.

```sql
SELECT user_id, COUNT(*)
FROM comments
WHERE photo_id < 50
GROUP BY user_id
HAVING COUNT(*) > 20;
```

## UNION

두 개의 sql 문을 합쳐서 반환해준다.
물론 조건이 있다.

1. 컬럼명과, 해당 컬럼의 자료형이 같아야 한다.

UNION 은 중복 row 가 있으면 한 번만 표시하지만, `UNION ALL` 하면 중복 내용까지 중복해서 표현해준다.

`INTERSECT` `INTERSECT ALL` `EXCEPT` `EXCEPT ALL` 등도 있음.
다른 것과 달리 `EXCEPT` 의 경우에는 앞 뒤 순서가 바뀌면 당연히 결과도 달라진다. 뒤에 것에 없는 것을 남기는 것이니까.

## SubQueries

어떤 기준을 찾기 위한 쿼리를 먼저 실행한 뒤에 그 결과값을 가지고 목표한 쿼리문을 실행한다. 보통 그 보조 쿼리를 괄호 안에 넣어서 실행한다.

```sql
SELECT name, price
FROM products
WHERE price > (
  SELECT MAX(price) from products WHERE department = 'Toy'
);
```

복잡한 쿼리일수록 서브쿼리가 너무 많아져서 혼란스러워진다. 위치하는 곳에 따라서 서브쿼리가 하는 역할이 또 달라지기 때문에...
앞, 중간, 뒤 각각에서 서브쿼리가 갖는 의미

1. A source of a value (subqueries in a SELECT)
1. A source of rows
1. A source of a column

근데 그 위치에 따라서 다음과 같은 특징(강제되는 조건)이 있다.

1. 하나의 값만(a single value) 나와야 한다. (SELECT MAX(price) FROM products) (스칼라 쿼리라고도 함)

### Subqueries with WHERE

서브쿼리 중에서도 나름 유용한 것은 SELECT, FROM 의 위치에 있는 것보다 WHERE 과 같이 쓰이는 서브쿼리다.

```sql
SELECT id
FROM orders
WHERE product_id IN (
  SELECT id FROM products WHERE price / weight > 50
);
```

L `IN` 은 리스트를 대상으로 하는데, **하나의 컬럼** 을 대상으로 하면 그걸 리스트로 인식한다. 즉 WHERE 과 관련된 연산자에 따라서, 하나의 '값' 이나 하나의 '컬럼' 이 서브쿼리의 결과값이 요구된다.

WHERE 서브쿼리는 사실 JOIN 으로도 할 수 있는 경우가 많다. 즉, 상황에 따라서 WHERE+서브쿼리를 쓰든 JOIN 을 사용하든 상관 없다. 아예 pg 내부적으로, 두 쿼리를 같은 방식으로 전환해서 사용하기 때문에 성능 차이도 없는 경우가 많다.

WHERE 절에는 일반 비교 연산자 외에도, `ALL`, `SOME(ANY)` 을 붙여서도 많이 사용한다.

## 인덱스

디폴트 설정으로는 **B-Tree** 를 이용해서 구현된다. 

프라이머리 키나, 유니크 제약이 있는 컬럼은 자동으로 인덱스가 생긴다. pgadmin 에서 직접적으로 index 라고 표시되지는 않지만, 별도의 sql 문을 사용해서 모든 인덱스를 출력해보면 존재한다는 것을 알 수 있다.(`commands.md` 파일 참고)
