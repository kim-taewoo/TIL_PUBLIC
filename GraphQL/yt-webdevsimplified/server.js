const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { GraphQLSchema, GraphQLObjectType, GraphQLString } = require('graphql');
const app = express();

// Query section 을 정의하는 'schema'
const schema = new GraphQLSchema({
  query: new GraphQLObjectType({
    name: 'HelloWorld',
    fields: () => ({
      // 쿼리로 가져올 수 있는 필드들 정의
      message: { 
        type: GraphQLString, 
        resolve: () => 'Hello World!' },
    }),
  }),
});

app.use(
  '/graphql',
  graphqlHTTP({
    schema: schema,
    graphiql: true, // 그래픽 인터페이스 제공
  })
);
app.listen(5000, () => console.log('server running'));
