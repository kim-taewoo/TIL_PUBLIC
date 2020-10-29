const babel = require('@babel/core');
const fs = require('fs');

const filename = './src/code.js';
const source = fs.readFileSync(filename, 'utf8');
const presets = ['@babel/preset-react'];

// 웹팩의 첫 단계인 파싱 단계를 통해 AST(abstract syntax tree) 를 만들어 놓고, 
// 원하는 변환/생성 방법마다 재사용할 수 있다. 즉, 다양한 방법으로 컴파일할 때 바벨을 효율적으로 실행할 수 있다.
const { ast } = babel.transformSync(source, {
  filename,
  ast:true,
  code: false,
  presets,
  configFile: false,
});

const { code: code1 } = babel.transformFromAstSync(ast, source, {
  filename,
  plugins: ['@babel/plugin-transform-template-literals'],
  configFile: false,
});

const { code: code2 } = babel.transformFromAstSync(ast, source, {
  filename,
  plugins: ['@babel/plugin-transform-arrow-functions'],
  configFile: false,
});

console.log('code1:\n', code1);
console.log('code2:\n', code2);