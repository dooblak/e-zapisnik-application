let publicPath = process.env.NODE_ENV === 'production' ? 'posts/' : '/';

module.exports = {
  publicPath,
  productionSourceMap: false,
};
