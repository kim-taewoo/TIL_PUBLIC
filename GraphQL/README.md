# TODO
- [] GraphQL Server Basics: GraphQL Schemas, TypeDefs & Resolvers Explained [링크](https://www.prisma.io/blog/graphql-server-basics-the-schema-ac5e2950214e)
- [] Apollo 의 graphQL 캐싱을 위한 Normalize 정책 알아보기 [링크](https://www.apollographql.com/blog/the-concepts-of-graphql-bc68bd819be3/)
- [] Core concepts 의 맨 밑 **Learn More** 파트 링크 3개 공부 [링크](https://www.howtographql.com/basics/2-core-concepts/)
- [] GraphQL 이 어떤 순서로 resolvers 들을 실행해서 합치는지 작동원리 [링크](https://www.apollographql.com/blog/graphql-explained-5844742f195e/)
- [] GraphQL 은 어떻게 서버사이드 캐싱을 하려고 하는가 [링크](https://graphql.org/learn/caching/)

# 알아둬야 할 것
- DataLoader 를 이용해서 중복되는 쿼리를 최적화할 수 있다. [링크](https://www.howtographql.com/advanced/1-server/) 아래부분 참고.
- A `fragment` is a collection of fields on a specific type. (graphql 타입 정의시 재사용성 높여주는 블럭이라 생각하면 된다.)
- Object & Scalar Types
    - In GraphQL, there are two different kinds of types.
    **Scalar types** represent concrete units of data. The GraphQL spec has five predefined scalars: as `String`, `Int`, `Float`, `Boolean`, and `ID`.
    **Object types** have fields that express the properties of that type and are composable. Examples of object types are the `User` or `Post` types we saw in the previous section. You can define **your own scalar and object types.** An often cited example for a custom scalar would be a `Date` type where the implementation needs to define how that type is validated, serialized, and deserialized. [참고링크](https://www.howtographql.com/advanced/2-more-graphql-concepts/)
- **enums** are special kinds of scalar types.
- An **interface** can be used to describe a type in an abstract way. It allows you to specify a set of fields that any concrete type, which implements this interface, needs to have. In many GraphQL schemas, every type is required to have an id field. Using interfaces, this requirement can be expressed by defining an interface with this field and then making sure that all custom types implement it: (상속관련) [참고링크](https://www.howtographql.com/advanced/2-more-graphql-concepts/)
- `Union` types can be used to express that a type should be either of a collection of other types. This brings up a different problem: In a GraphQL query where we ask to retrieve information about a Child but only have a Person type to work with, how do we know whether we can actually access this field? The answer to this is called `conditional fragments`:
    - ```
      {
        allPersons {
          name # works for `Adult` and `Child`
          ... on Child {
            school
          }
          ... on Adult {
            work
          }
        }
      }
      ```