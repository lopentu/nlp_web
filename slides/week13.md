---
marp: true
theme: default
paginate: true
header: NLP and Web Applications
---

<style>
  header { 
    position: absolute; 
    left: 1000px;
  }
</style>

<style>
blockquote {
    border-top: 0.1em dashed #555;
    font-size: 60%;
    margin-top: auto;
}
</style>

## Week 13

# Machine learning/NLP in Javascript with TensorFlow.js

![bg right width:500](https://www.gstatic.com/devrel-devsite/prod/ve6e6ebff6d326e85aedeebfd3fad7cfd85d0fc48cfc2ee55b5498d178a34d928/tensorflow/images/lockup.svg)

## 謝舒凱 台大語言所

---

# NLP, ML and Web Applications

---

# 回到課程的核心動機

web applications with NLP: why and how

---

# NLP, AI and Web Applications

- 語音辨識
- 自然語言處理
- 視覺辨識
- 搜尋
- 遊戲
- 聊天機器人
- 規劃排程

---

# 機器學習與深度學習

![bg](lavender)

---

# 基本概念

- 機器學習 (Machine Learning, ML) performs tasks based on data rather than explicit (coded) rules.

- 深度學習 (Deep Learning, DL) is a subset of ML that uses neural networks to learn from data.

- 典型的 ML 任務包括分類 (classification)、回歸 (regression)、聚類 (clustering)、降維 (dimensionality reduction)、推薦系統 (recommendation system) 等。

---

# 機器學習的類型日新月異

- supervised learning

- unsupervised learning

- reinforcement learning

- semi-supervised learning

- active learning

- transfer learning

- multi-task learning

- self-supervised learning

---

# Traing and testing data

<!-- 圖示 video3: 5:18-->

---

# 過度擬合 (overfitting)

- train the model which works well for the training data but not for the (unseen) testing data.

---

# Loss function

<!-- 3:7:34 -->

- a function that measures how well the model performs on the training data.

---

# 深度學習

- 深度學習是一種機器學習方法，它使用**多層**神經網路來模擬人類大腦的神經網路，並且使用大量的資料來訓練模型。

  - feed in input and produce output.
  - can be trained via `backpropagation` to improve the model.

- Configutation matters!

---

## Lab:

[Tensorflow playgound](https://playground.tensorflow.org/)

---

# Transformer

![bg](lavender)

---

#

- [Tensorflow] Google 開發的開源機器學習框架 (2015-)

- [PyTorch] Facebook 開發的開源機器學習框架 (2016-)

---

# 讓前端也可以做機器學習

- [Tensorflow.js]() (since 2018): Machine Learning library for JavaScript, which makes ML in the browser possible.[*]

- 可以充分利用 device features (e.g., camera, microphone, etc.); take advantage of user interaction; utilize the power of the device; help protect the user’s privacy.

- 讓 JS 前端工程師可直接使用 ML 模型 (也可以 import Python 模型)

> [*] can also use it with `node.js` for server side or backend development.

---

# 效能考量

![bg right width:500](https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/480px-Unofficial_JavaScript_logo_2.svg.png)

- `Tensorflow.js` 是在瀏覽器中執行的，所以效能會受到瀏覽器限制。但現在的瀏覽器已經足夠強大，可以執行複雜的模型。(**uses GPU in web browser**)

- Frontend (browser) or backend (node.js) development

 <!-- for js developer -->

---

# 不只有 TF.js 一家

- [ml5.js](https://ml5js.org/): 開源友善的架在 `TensorFlow.js` 之上。,

<!-- 舉例：https://julienrioux.medium.com/in-browser-ml-with-react-js-and-ml5-js-f3eeb5149404 -->

---

## Tensorflow.js 是什麼

TensorFlow makes it easy for beginners and experts to create machine learning models for desktop, mobile, web, and cloud.

- `Tensor` + `Flow`

- `TensorFlow.js`也支援 WebGL，因此即使在瀏覽器上，我們也能使用 GPU 來加快運算結果，不用擔心在瀏覽器上的效能限制。

---

# 安裝與執行

Install `tensorflow.js` in the **browser** and/or for **node.js** \*
兩種方式

- using the script tag

- installation from NPM and using a build tool like Parcel, WebPack, or Rollup.

```bash
npm install @tensorflow/tfjs
# or
yarn add @tensorflow/tfjs
```

如此可在本地端執行。

```js
import * as tf from "@tensorflow/tfjs";
```

> - optimizations in each environment are different.

---

# 我們先用 script tag 的方式

- Create a simple HTML file, ddd this script tag to the HTML file: (check [the latest](https://www.tensorflow.org/js/tutorials/setup#installation_from_npm))

```html
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@2.0.0/dist/tf.min.js"></script>
```

- Open the web console.
  - Run `tf.version` in the console to verify TensorFlow is setup and see which version is running.

---

## 測試一下

- 複製該網站上的 code sampe for script tag setup 程式碼到 HTML 檔案中，並且開啟瀏覽器的 console。

- 應該會得到類似以下結果：

```html
Tensor [[6.9452119],]
```

---

# WebGL optimizations

![bg right width:500](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsMlDZI7NR4vOkMzmZz-69rC3GIVW_LxxRlDASPk4n8c9nGUvfJGik6RqUEcOnWqrmGto&usqp=CAU)

- WebGL is a JavaScript API for rendering interactive 3D and 2D graphics within any compatible web browser without the use of plug-ins. check [this website](https://get.webgl.org/)

- used by `Tensorflow.js` to run on GPU (not used for visial graphics)

<!-- Graphic cars (GPU) is faster than CPU for matrix operations -->
<!-- tf.getbackend() -->

---

# 核心概念

張量、運算子、模型、層，以及訓練、記憶體管理方法，以及如何寫出簡潔（tidy）的程式碼。

---

# TensorFlow API

兩個一開始好用的部分

- low-level operation API

  - math operations to manipulate data
  - not easy
  - (similar to Eager Execution in TensorFlow Python API)

- high-level layers API
  - allows you to define complex model easily
  - (similar to Keras in TensorFlow Python API)

[擅用 tensorflow.js api docs](https://js.tensorflow.org/api/latest/)

---

# 張量 ｜ Tensor

---

# operations

---

# 如何利用 TF.js 完成一個機器學習專案

- 備料
- 探勘
- 定義模型
- 訓練與測試
- 預測

---

# 線性迴歸 linear regression

- import data [*]
- visualize data (via `tfjs-vis`)
- feature selection and labels; normalized the data into a form that is appropriate for the TensorFlow.js layers API.
- splitting data into training and testing sets

> [*] [kaggle](www.kaggle.com) 是個好地方

---

# Penguins

---

# NLP 應用實例

How to use tensorflow.js in react.js — Sentimental Analysis

---

# 期末報告![bg](lavender)
