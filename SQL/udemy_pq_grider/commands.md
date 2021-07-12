#### 대상의 메모리 차지 크기 구하기

`SELECT pg_size_pretty(pg_relation_size('[name of target]'))`

#### 데이터베이스가 가진 모든 인덱스 표시

```sql
SELECT relname, relkind
FROM pg_class
WHERE relkind = 'i';
```
