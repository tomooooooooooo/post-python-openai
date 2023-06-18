# README

## OpenAI GPT-3.5-turbo API を利用したChatbot

このプロジェクトでは、OpenAIの強力な言語モデル GPT-3.5-turboを利用して、一般的な対話を行うチャットボットを実装します。

### 必要な環境

- Python 3.8以上
- OpenAI Pythonライブラリ
- python-dotenvライブラリ
- OpenAI APIキー

### インストール

1. リポジトリをクローンまたはダウンロードします。

```bash
git clone https://github.com/yourusername/project.git
```

2. 必要なパッケージをインストールします。

```bash
pip install openai python-dotenv
```

### 使用方法

1. `.env` ファイルを作成し、以下のようにOpenAI APIキーを設定します。

```bash
OPENAI_API_KEY=your-api-key
```

2. チャットボットにリクエストを送信します。

```python
import os
import openai
from dotenv import load_dotenv

load_dotenv(override=True)
load_dotenv(".env")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {
        "role": "user",
        "content": "あなたの質問"
    },
    ],
)
```

3. レスポンスを表示します。

```python
print(response.choices[0]["message"]["content"].strip())
```

### 注意

このコードは、APIキーを `.env` ファイルから取得し、ソースコードからAPIキーを除外しています。これは、APIキーなどの機密情報を安全に管理するための一般的な方法です。

### ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)をご覧ください。

### 貢献

フィードバック、質問、バグレポートなどは、いつでも歓迎します。GitHubのイシュートラッカーを使用してください。# README

## OpenAI GPT-3.5-turbo API を利用したChatbot

このプロジェクトでは、OpenAIの強力な言語モデル GPT-3.5-turboを利用して、一般的な対話を行うチャットボットを実装します。

### 必要な環境

- Python 3.8以上
- OpenAI Pythonライブラリ
- python-dotenvライブラリ
- OpenAI APIキー

### インストール

1. リポジトリをクローンまたはダウンロードします。

```bash
git clone https://github.com/yourusername/project.git
```

2. 必要なパッケージをインストールします。

```bash
pip install openai python-dotenv
```

### 使用方法

1. `.env` ファイルを作成し、以下のようにOpenAI APIキーを設定します。

```bash
OPENAI_API_KEY=your-api-key
```

2. チャットボットにリクエストを送信します。

```python
import os
import openai
from dotenv import load_dotenv

load_dotenv(override=True)
load_dotenv(".env")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {
        "role": "user",
        "content": "あなたの質問"
    },
    ],
)
```

3. レスポンスを表示します。

```python
print(response.choices[0]["message"]["content"].strip())
```

### 注意

このコードは、APIキーを `.env` ファイルから取得し、ソースコードからAPIキーを除外しています。これは、APIキーなどの機密情報を安全に管理するための一般的な方法です。


### 貢献

フィードバック、質問、バグレポートなどは、いつでも歓迎します。GitHubのイシュートラッカーを使用してください。

