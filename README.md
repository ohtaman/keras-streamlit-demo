# keras-streamlit-demo

Streamlit を使って Keras のモデルをテンポよく開発するデモです。

## インストールと Streamlit の起動

### Graphviz のインストール

- Ubuntu の場合
```
$ sudo apt install graphviz
```

- Mac の場合


### Poetry を使う場合

```bash
$ cd keras-streamlit-demo
$ poetry install
$ poetry shell
(.ven) $ streamlit run --server.runOnSave true main.py
```

### pip を使う場合

```bash
$ cd keras-streamlit-demo
$ pip install tensorflow streamlit pydot
$ streamlit run --server.runOnSave true main.py
```



