const presets = ['@babel/preset-react'];
const plugins = [
  '@babel/plugin-transform-template-literals',
  '@babel/plugin-transform-arrow-functions',
];

module.exports = { presets, plugins };

// 자바스크립트 파일이기 때문에 동적으로 설정값을 만들 수 있다. 