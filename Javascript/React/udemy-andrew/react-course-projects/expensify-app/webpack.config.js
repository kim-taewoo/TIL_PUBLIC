// webpack.js.org
// entry => output

const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

// module.exports = {
module.exports = (env) => {
  console.log(env);
  const isProduction = env === 'production';
  return {
    entry: './src/app.js',
    output: {
      path: path.join(__dirname, 'public', 'dist'),
      filename: 'bundle.js'
    },
    module: {
      rules: [{
        loader: 'babel-loader',
        test: /\.js$/,
        exclude: /node_modules/
      }, {
        test: /\.s?css$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: [
            {
              loader: 'css-loader',
              options: {
                sourceMap: true
              }
            },
            {
              loader: 'sass-loader',
              options: {
                sourceMap: true
              }
            }
          ]
        })
        // use: [
        //   'style-loader',
        //   'css-loader',
        //   'sass-loader'
        // ]
      }]
    },
    plugins: [
      new ExtractTextPlugin("styles.css"),
    ],
    devtool: isProduction ? 'source-map' : 'inline-source-map',
    devServer: {
      contentBase: path.join(__dirname, 'public'),
      historyApiFallback: true,
      publicPath: '/dist/'
    }
  };
}