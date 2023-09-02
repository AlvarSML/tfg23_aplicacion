module.exports = {
  chainWebpack: (config) => {
    config.module
      .rule("vue")
      .use("vue-loader")
      .loader("vue-loader")
      .tap((options) =>
        Object.assign(options, {
          transformAssetUrls: {
            "v-img": ["src", "lazy-src"],
            "v-card": "src",
            "v-card-media": "src",
            "v-responsive": "src"
          }
        })
      );
  },

  transpileDependencies: ["vuetify"],

  pluginOptions: {
    vuetify: {
      // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
    }
  }
};
