const path = require('path');

module.exports = {
  devServer: {
      proxy: {
          '/api': {
              target: 'http://localshot:7000',
              changeOrigin: true,
              pathRewrite: {
                  '^/api': ''
              }
          }
      }
  }
}