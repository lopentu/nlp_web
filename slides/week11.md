---
marp: false
theme: default
paginate: true
header: NLP and Web Applications
---

# Week 11: React 複習＆實作
![bg right width:600](https://www.datocms-assets.com/45470/1631110818-logo-react-js.png?fm=webp)

## Sharon Shen
---
# 我是誰

---
# Outline
- CRA
- 複習 React 概念: Why React, React elements, React components, render, props, state, JSX, hook, 
- 今天來點寶可夢（實作）
  - 邊看 code 邊來講上述概念吧
  - 想想看如何切 components
  - 如何做 custom hook

---
# CRA
```
npx create-react-app web03-1
```
- Under the hood, we use webpack, Babel, ESLint, and other amazing projects to power your app. If you ever want an advanced configuration, you can ”eject” from Create React App and edit their config files directly.

- Whether you’re using React or another library, Create React App lets you focus on code, not build tools.
  
---
### webpack
- bundler: 將你的 js, css 等檔案 Bundle 變成單一的檔案
- loaders, css-loader, style loader 
  - 在 JavaScript 檔案中 require 一個 css 檔案。你可以 require 其他不只是 JavaScript 的檔案
  - 如果你 require 的檔案結尾是 .css，然會我們會使用 style 和 css loader，將 CSS 加入到 bundle
- plugin , minify bundles
  - 你可以透過 `UglifyJsPlugin` plugin minify 你的 bundle 檔案來做改善
- webpack 自帶了方便的 webpack-dev-server, 實際在瀏覽器看到我們的網站
[ref](https://neighborhood999.github.io/webpack-tutorial-gitbook/Part1/)

---
### babel
es6, es7 → es5
- `let` `const`
- Arrow Functions 
  ```javascript
  const x = (x, y) => x * y;
  ```
- Spread (...) Operator
  ``` javascript
  const cars1 = ["Saab", "Volvo", ..."BMW"];
  const cars2 = ["Fiat", "Toyota"];

  const combined = [cars1, ...cars2];
  ```
- class
  ```javascript
  class ClassName {
    constructor() { ... }
  }
  ```

---
### ```yarn eject```
- 使用這個指令後會將原本封裝在 CRA 的一些配置檔案都集中呈現在根目錄的 config 資料夾，就可以從這邊去調整 webpack。
- 看一下 `package.json`
- 看一下 `config` folder

---
### ```yarn add styled-components```
- 看一下 `package.json`
- 看一下 `node_modules`

---
# 上工啦，今天來點寶可夢
- 先看一下成品
  - 到 `nlp_web/lab/pokemons` 底下 
    - `git pull origin pokemon_version3_cart` 
    - `git checkout pokemon_version3_cart` 
    - `yarn start`
  
---
# 上工啦，今天來點寶可夢
- features
  - 寶可夢卡片購買列表
    - 用 `fetch` 來抓 API data
  - 寶可夢卡片互動
    - count button
    - Add to cart
      - 點擊 add to count btn 會出現 alert
  - 購買清單
    - 點擊 add to count btn, cart 內有資料會出現購買清單

*note: version3*

---
# 上工啦，今天來點寶可夢, different versions
- version1: simple version ; `git pull origin main` 
- version2: add custom hook `useFetch`; `git pull origin pokemon_version2_custom_hook` 
- version3: add cart info; `git pull origin pokemon_version3_cart`

*Note: slides 到 `main` branch 看最新的*
*Note: 切 branches demo 用，之後會把 brances 刪掉， `nlp_web/lab/pokemons` 只留 final version `pokemon_version3_cart`*

---
# React
- [Why react?](https://medium.com/%E9%BA%A5%E5%85%8B%E7%9A%84%E5%8D%8A%E8%B7%AF%E5%87%BA%E5%AE%B6%E7%AD%86%E8%A8%98/%E7%AD%86%E8%A8%98-why-react-424f2abaf9a2)
- [pokemon in vanilla JS](https://github.com/Nihaprezz/kanto-pokemon)

---
# React, DOM element vs. React element vs. React components
# DOM element
DOM 將一份 HTML 文件看作是一個樹狀結構的物件，讓我們可以方便直觀的存取樹中的節點 (node) 來改變其結構、樣式 (CSS) 或內容等

[visite this](https://summer10920.github.io/2020/04-20/js-baseclass-2/)

---
## React element
- 與瀏覽器的 DOM element 不同，React element 是單純的 object，而且很容易被建立。React DOM 負責更新 DOM 來符合 React element。
- An element describes what you want to see on the screen. 

```javascript
const root = ReactDOM.createRoot(
  document.getElementById('root')
);
const element = <h1>Hello, world</h1>; // react element
root.render(element);
```

---
## React component
- 概念上來說，component 就像是 JavaScript 的 function，它接收任意的參數（稱之為「props」）並且回傳描述畫面的 React element。
- 定義 component 最簡單的方法即是撰寫一個 Javascript function
  ```javascript
  function Welcome(props) {
    return <h1>Hello, {props.name}</h1>;
  }
  ```
  此 function 是一個符合規範的 React component，因為它接受一個「props」（指屬性 properties）物件並回傳一個 React element。我們稱之為 function component，因為它本身就是一個 JavaScript function。

---
## React component
你也可以使用 ES6 Class 來定義 component, 上述兩種 component 在 React 中是同等的。
```javascript
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

```javascript
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

---
# React, render
`<div id="root"></div>`
- 使用 React 建立應用程式時，通常會有一個單一的 root DOM node。所有在內的 element 都會透過 React DOM 做管理。
- The root can be used to render a React element into the DOM with render:
  ```javascript
  const root = ReactDOM.createRoot(
    document.getElementById('root')
   );
   const element = <h1>Hello, world</h1>;
  root.render(element);
  ```
---
# React, render
- 看一下 root `<div id="root" />`
*note: version1*

---
# React, 切分 components
Component 使你可以將 UI 拆分成獨立且可複用的程式碼，並且專注於各別程式碼的思考。
以經驗來說
- 如果一個 UI 中有一部分會被重複使用很多次（Card、Button、Alert）
- 或者它足夠複雜（App、CardContent、CardActions），則可以將它提取到獨立的 component。

*note: version1*

---
![fit](./images/pokemon_page_marked.png)

---
![fit](./images/pokemon_card_marked.png)

---
# React, JSX
## 什麼是 JSX
- 是一個 JavaScript 的語法擴充。透過這個語法來描述使用者介面的外觀
- 執行 JSX 會產生 React「element」。
- JSX 允許你使用 JavaScript 所有的功能。
  ```javascript
  const element = <h1>你好，世界！</h1>;
  ```
  
  ### 在 JSX 中嵌入 Expression
  ```javascript
  const name = 'Josh Perez';
  const element = <h1>Hello, {name}</h1>;
  ```

---
### 在 JSX 中嵌入 Expression

```javascript
function formatName(user) {
  return user.firstName+ ' ' + user.lastName;
}

const user = {
  firstName: 'Harper',
  lastName: 'Perez'
};

const element = (
  <h1>
    Hello, {formatName(user)}!
  </h1>
);
```
--- 
# JSX
- 透過這個語法來描述使用者介面的外觀, JSX 表示物件,  這種物件被稱呼為「React element」。你可以想像他們描述的是你想要在螢幕上看到的東西，React 會讀取這些物件並用這些描述來產生 DOM 並保持他們在最新狀態。
  
---
## 為什麼要使用 JSX
- 大部分人覺得在 JavaScript 程式碼中撰寫使用者介面的同時，這是一個很好的視覺輔助。
- 這也允許 React 顯示更有用的錯誤及警告訊息。
- [React 並不要求使用 JSX](https://zh-hant.reactjs.org/docs/react-without-jsx.html)


---
# 來看下程式碼
- 看下 components 如何拆分
- 看下 `sumPrices` in JSX
*note: version3*

---
# React, props vs. state
- props (short for “properties”) and state are both plain JavaScript objects.
- While both hold information that influences the output of render, they are different in one important way
  - props get passed to the component (similar to function parameters) 
  - whereas state is managed within the component (similar to variables declared within a function).
  
[read more](https://github.com/uberVU/react-guide/blob/master/props-vs-state.md)

*note: version1 props: handleAddToCart, pokemonUrl*

---
# React, hook
## 為什麼要使用 hook
- Hook 讓你不需要改變 component 階層就能重用 stateful 的邏輯。
  - 你很可能會發現一個 component 的「包裝地獄」，被 provider、consumer、[higher-order component](https://zh-hant.reactjs.org/docs/higher-order-components.html)、[render props](https://zh-hant.reactjs.org/docs/render-props.html) 以及其他抽象給層層圍繞。 → React 需要一個更好的 primitive 來共用 stateful 邏輯。
  - 使用 Hook，你可以從 component 抽取 stateful 的邏輯，如此一來它就可以獨立地被測試和重複使用。
  
---
## 為什麼要使用 hook
  - hook 讓你把一個 component 拆分成更小的 function，這基於什麼部分是相關的（像是設置一個 subscription 或是抓取資料，而不是強制基於 lifecycle 方法來分拆。

[ref](https://zh-hant.reactjs.org/docs/hooks-intro.html)
[document.title, subscription](https://zh-hant.reactjs.org/docs/hooks-effect.html)

---
# React, hook
- 什麼是 Hook？
  - Hook 是一個讓你可以使用 React 各項功能的特殊 function。
- 什麼時候該使用 Hook？
  - 以前當你寫一個 function component 需要增加一些 state 時，你必須轉換成 class。現在你可以直接在 function component 中使用 Hook。

---
### class component
```javascript
class Example extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }
```
### function component
```javascript
import React, { useState } from 'react';

function Example() {
  // 宣告一個新的 state 變數，我們稱作為「count」。
  const [count, setCount] = useState(0);
```
---
## 常用的 hook - `useState`
`useState` 是一個讓你增加 React state 到 function component 的 Hook。

---
```javascript
import React, { useState } from 'react';
function Example() {
  // 我們呼叫 useState Hook 宣告了一個新的 state 變數。並回傳了一對由我們命名的值。我們將代表點擊數的變數命名為 count
  // setState -> 更新 state 的 function
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>You clicked {count} times</p>
      {/** 當使用者點擊，我們就呼叫 setCount 並傳入新的值。然後 React 就會 re-render Example component，並傳入新的 count 值。 */}
      <button onClick={() => setCount(count + 1)}>
       Click me
      </button>
    </div>
  );
}
```

*note: version1, state: loading, error, pokemons, count*

---
## 常用的 hook - `useEffect`
[side effect](https://ithelp.ithome.com.tw/articles/10185780) 在這裡做
- 資料 fetch
- 設定 subscription
- 或手動改變 React component 中的 DOM 都是 side effect （或簡稱「effect」）

---
# 常用的 hook - `useEffect`
useEffect 有什麼作用？ 透過使用這個 Hook，你告訴 React 你的 component 需要在 render 後做一些事情。React 將記住你傳遞的 function（我們將其稱為「effect」），並在執行 DOM 更新之後呼叫它。 

---
# 常用的 hook - `useEffect`
每次 render 後都會執行 useEffect 嗎？ 是的！預設情況下，它在第一個 render 和隨後每一個更新之後執行。你可能會發現把 effect 想成發生在「render 之後」更為容易

---
# 來看下程式碼
- 看下打 API 的地方 (fetch)
- 再仔細看下互動的地方

*note: version1*

---
# React, customize your hook
`useFetch`
hook 讓你不需要改變 component 階層就能重用 stateful 的邏輯
  - loading
  - error
  - data

*note: version2*

---
# callback function `handleAddToCard` 
*note: version3*

---
# cart
*note: version3*

---
# lib: styled-components 
### ```yarn add styled-components```
- 為了要以「元件」為開發單位，需要限制 CSS 的作用範圍，以元件為 scope，換句話說就是，要讓每個元件的 CSS 都是獨立的，這樣就可以避免元件之間的 CSS 互相影響覆蓋。另外，可以讓元件容易維護，也更容易重複使用
  - 這段 CSS style 只會生效在這個元件內
  - 不用擔心改了會不會影響其他元件
  - 搬動元件時，不用額外搬動 CSS 檔
  
---
### ```yarn add styled-components```
- 提供了在 JavaScript 中直接撰寫 CSS 的介面，因為本體是 JavaScript，所以你可以做到：
  - 在 JavaScript 裡面寫 CSS
  - 在 JavaScript 裡面寫的 CSS 裡面寫 JavaScript
[ref](https://styled-components.com/docs/basics#installation)

---
# 可用 CRA 實作看看 😃

---