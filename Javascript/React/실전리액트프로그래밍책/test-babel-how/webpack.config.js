const path = require('path');

module.exports = {
  entry: './src/code.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'code.bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        use: 'babel-loader', // babel.config.js 설정값을 자동으로 이용한다.
      },
    ],
  },
  optimization: { minimizer: [] }, // 원래는 기본적인 압축처리를 하지만, 바벨 실행 결과를 보기 위해 잠시 끄도록 한다.
};
