SQL 문은 `중간 -> 뒤 -> 앞` 의 순서로 읽는 게 해석하기 좋다.
`SELECT * FROM users WHERE users.id > 5` 같은 경우 users 테이블에서, users.id > 5 조건에 맞는 것들 중에, SELECT \* 해라. 라고 해석하는 게 자연스럽다.

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

위와 같이 GROUP 화 한 뒤에는, `SELECT` 구문에 그 그룹화된 컬럼만 직접적으로 선택 가능하다. 즉, phones 테이블에 name 과 같은 컬럼이 있었어도 GROUP 뒤에는 선택하려고 하면 에러가 발생한다.

GROUP BY 는 Aggregates 와 함께 많이 쓰인다. GROUP BY 로 묶인 그룹들을 대상으로 AVG(), COUNT(그룹화된 컬럼) 등등을 많이 쓰기 때문. **Aggregate 는 각 그룹마다 연산된다.**

물론 그룹화 없이 `COUNT(*)` 같은 것도 많이 쓰이는 Aggregate
