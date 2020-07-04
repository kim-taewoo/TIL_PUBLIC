const path = require('path');
const rules = [
  {
    test: /\.tsx/,
    exclude: /node_modules/,
    loader: 'babel-loader',
  },
];
module.exports = {
  target: 'web',
  mode: 'development',
  entry: './src/index.tsx',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
  module: { rules },
  // extensions 내에 적힌 확장자는 `import` 할 때 확장자를 적어주지 않아도 된다
  resolve: {
    extensions: ['.ts', '.tsx', '.js'],
  },
  devServer: {
    contentBase: './',
    port: 5000,
  },
};
