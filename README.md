# streamlit-with-ne

StreamlitでNW装置の状態の可視化やInterfaceに対しての何らかの操作を実行する簡易的なWebUIです

JANOG53で発表するLTのために簡易的に用意したデモです。

対象装置はJANOG(JApan Network Operators Group)にちなんで国産の装置を対象にしたかったので、
SEIKO SmartCS 2250を利用させていただきました。

sequenceDiagram
    Streamlit->>BackendPython: Call Get tty Configration
    BackendPython->>SEIKO SmartCS 2250: REST : hogehoge