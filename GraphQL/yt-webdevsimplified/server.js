const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const {
  GraphQLSchema,
  GraphQLObjectType,
  GraphQLString,
  GraphQLList,
  GraphQLInt,
  GraphQLNonNull,
} = require('graphql');
const app = express();

// 더미 데이터
const authors = [
  { id: 1, name: 'J. K. Rowling' },
  { id: 2, name: '톨킨' },
  { id: 3, name: 'Brent Weeks' },
];

const books = [
  { id: 1, name: '해리포터와 마법사의 돌', authorId: 1 },
  { id: 2, name: '해리포터와 아즈카반의 죄수들', authorId: 1 },
  { id: 3, name: '해리포터와 불사조 기사단', authorId: 1 },
  { id: 4, name: '반지의 제왕', authorId: 2 },
  { id: 5, name: '두개의 탑', authorId: 2 },
  { id: 6, name: '왕의 귀환', authorId: 2 },
  { id: 7, name: 'The Way of Shadows', authorId: 3 },
  { id: 8, name: 'Beyond the Shadows', authorId: 3 },
];

const BookType = new GraphQLObjectType({
  name: 'Book',
  description: 'This represents a book written by an author',
  // 이미 Object 의 형태로 key 를 가진 경우라면, 따로 'resolve' 해주지 않아도 알아서 해당 키의 값이 매칭된다.
  // 커스텀하게 수정해주어야 되는 경우에는 당연히 resolve 를 해줘야 한다. 아래의 경우에선 author field.
  fields: () => ({
    id: { type: GraphQLNonNull(GraphQLInt) },
    name: { type: GraphQLNonNull(GraphQLString) },
    authorId: { type: GraphQLNonNull(GraphQLInt) },
    author: {
      type: AuthorType,
      // resolve 가 객체를 바로 반환하지 않고 함수를 값으로 가지는 이유는, 해당 resolve 과정중에 다른 GraphQLTypes 를 참조할 일이 많기 때문이다.
      // 즉, 해당 타입이 아직 정의되지 않은 상황일 수 있기 때문에,
      // 함수를 이용해서 모든 타입이 정의된 시점 이후에 resolve 가 정상적으로 실행되도록 돕는다.
      // resolve 는 첫번째 인자로 parent, 즉 현재 필드를 감싸고 있는 타입을 받는다.
      resolve: (book) => {
        return authors.find((author) => author.id === book.authorId);
      },
    },
  }),
});

const AuthorType = new GraphQLObjectType({
  name: 'Author',
  description: 'This represents a author of a book',
  fields: () => ({
    id: { type: GraphQLNonNull(GraphQLInt) },
    name: { type: GraphQLNonNull(GraphQLString) },
    books: {
      type: new GraphQLList(BookType),
      resolve: (author) => {
        return books.filter((book) => book.authorId === author.id);
      },
    },
  }),
});

const RootQueryType = new GraphQLObjectType({
  name: 'Query',
  description: 'Root Query',
  fields: () => ({
    book: {
      type: BookType,
      description: 'A Single Book',
      args: {
        id: { type: GraphQLInt },
      },
      resolve: (parent, args) => books.find((book) => book.id === args.id),
    },
    books: {
      type: new GraphQLList(BookType),
      description: 'List of all books',
      resolve: () => books,
    },
    authors: {
      type: new GraphQLList(AuthorType),
      description: 'List of all Authors',
      resolve: () => authors,
    },
    author: {
      type: AuthorType,
      description: 'A single Author',
      args: {
        id: { type: GraphQLInt },
      },
      resolve: (parents, args) =>
        authors.find((author) => author.id === args.id),
    },
  }),
});

const RootMutationType = new GraphQLObjectType({
  name: 'Mutation',
  description: 'Root Mutation',
  fields: () => ({
    addBook: {
      type: BookType,
      description: 'Add a book',
      args: {
        name: { type: GraphQLNonNull(GraphQLString) },
        authorId: { type: GraphQLNonNull(GraphQLInt) },
      },
      resolve: (parent, args) => {
        // 실제 db 를 쓴다면 id 증가시키거나 하는 작업이 필요없겠지
        const book = {
          id: books.length + 1,
          name: args.name,
          authorId: args.authorId,
        };
        books.push(book);
        return book;
      },
    },
    addAuthor: {
      type: AuthorType,
      description: 'Add an author',
      args: {
        name: { type: GraphQLNonNull(GraphQLString) },
      },
      resolve: (parent, args) => {
        // 실제 db 를 쓴다면 id 증가시키거나 하는 작업이 필요없겠지
        const author = {
          id: authors.length + 1,
          name: args.name,
        };
        authors.push(author);
        return author;
      },
    },
  }),
});

// Query section 을 정의하는 'schema'
const schema = new GraphQLSchema({
  query: RootQueryType,
  mutation: RootMutationType,
});

app.use(
  '/graphql',
  graphqlHTTP({
    schema: schema,
    graphiql: true, // 그래픽 인터페이스 제공
  })
);
app.listen(5000, () => console.log('server running'));
