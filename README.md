# streamlit-with-ne

StreamlitでNW装置の状態の可視化やInterfaceに対しての何らかの操作を実行する簡易的なWebUIです

JANOG53で発表するLTのために簡易的に用意したデモです。

対象装置はJANOG(JApan Network Operators Group)にちなんで国産の装置を対象にしたかったので、
SEIKO SmartCS 2250を利用させていただきました。

```mermaid
sequenceDiagram
    Streamlit->>BackendPython: Call Get system information
    BackendPython->>SEIKO SmartCS 2250: GET : api/system/version
    SEIKO SmartCS 2250 -->> BackendPython:  Response : system  info
    BackendPython -->> Streamlit: Return : system  info
    Streamlit->>BackendPython: Call Get tty Configration
    BackendPython->>SEIKO SmartCS 2250: GET : api/serial/tty
    SEIKO SmartCS 2250 -->> BackendPython:  Response : tty info
    BackendPython -->> Streamlit: Return : tty info
    Streamlit->>BackendPython: Call Modify tty Configration
    BackendPython->>SEIKO SmartCS 2250: POST : api/serial/tty
    SEIKO SmartCS 2250 -->> BackendPython:  Response : result
    BackendPython -->> Streamlit: Return : result
```

# How to run

Python3.11.1で動作確認をしています。
おそらく3.6以降だったら動きます。

必要なpackageをinstallしてください

```
pip install -r requirements.txt
```

.env.sampleのip,password,user,passwordを指定してください。
以下の情報が必要になります。

- ip : コンソールサーバーのIPアドレス
- port : コンソールサーバーのREST Serverのport(Default80)
- user : RESET API用ユーザー名
- password :  REST API用ユーザーパスワード

```
source .env.sample
```

streamlitを起動します

```
streamlit run app.py
```
