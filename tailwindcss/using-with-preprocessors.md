[공식문서](https://tailwindcss.com/docs/using-with-preprocessors#using-post-css-as-your-preprocessor)

Tailwind 는 PostCSS Plugin 이다. 그래서 Sass, Less, Stylus 같은 것들과 함께 사용하는 데 아무런 문제가 없다. (예를 들어 [Autoprefixer](https://github.com/postcss/autoprefixer) 와 Tailwind 가 종류가 같다고 생각하면 된다. `Autoprefixer` 도 prefixer 를 붙이기 위해 다른 preprocessor 라이브러리에서 대부분 이용된다.)

**하지만** 사실상 preprocessor 를 사용할거라면 tailwindcss 를 사용하는 의미가 크게 없다. 애초에 tailwindcss 는 class 이름을 HTML 마크업에 직접 기재하는 방식으로 사용되어 직접 CSS 파일을 작성할 일이 크게 없는 장점 때문에 쓰는데, preprocessor 는 헤비하게 CSS 를 작성하기 위한 용도가 아닌가? 즉, tailwind 를 쓸거라면 그냥 tailwind 를 쓰는 게 맞다. CSS 에 자신 있으면 tailwind 쓰지 말고 preprocessor 를 쓰면 되고.
[PostCSS plugin 들 모아둔 GitHub repository](https://github.com/postcss/postcss/blob/main/docs/plugins.md)

즉, (CSS) preprocessor 의 기능 중에 필요한 게 있더라도, preprocessor 를 도입하기 보다는, 또다른 postCSS 플러그인을 찾아서 쓰는 게 더 이치에 맞다. 오히려 preprocessor 를 사용하게 되면 tailwind 문법과 섞여서 귀찮은 작업이 추가되고, 빌드타임만 길어진다. 
