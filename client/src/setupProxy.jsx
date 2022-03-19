// const proxy = require("http-proxy-middleware");

// module.exports = app => {
//   app.use(proxy("/api/*", { target: "http://localhost:5000/" }));
// };

const { createProxyMiddleware } = require('http-proxy-middleware');
module.exports = function(app) {
  app.use(
    '/record',
    createProxyMiddleware({
      target: 'http://localhost:5000',
      changeOrigin: true,
    })
  );
};