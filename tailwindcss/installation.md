- npm 으로 tailwindcss 만 설치하면 나중에 빌드할 때 어차피 에러 메시지가 뜨게 된다. 따라서 설치할 때 `npm i -D tailwindcss postcss autoprefixer` 를 해서 3가지 라이브러리를 설치해주어야 한다. 

```json
// package.json
"scripts": {
  "build-css": "tailwindcss build src/styles.css -o public/styles.css"
},
```

