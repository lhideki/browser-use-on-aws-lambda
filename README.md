# AWS LambdaでBrowser Useを動かす(browser-use-on-aws-lambda)

AWS LambdaでBrowser Useを動かすためのテンプレートです。

## 開発環境の構築方法

pyvenv を利用して Python 仮想環境を作成することを推奨します。

```bash
python -m venv .venv
```

```bash
. .venv/bin/activate
pip install -r app/browser_use_on_aws_lambda/requirements.txt
pip install -r app/browser_use_on_aws_lambda/requirements-dev.txt
pip install -r cdk/requirements.txt
pip install -r cdk/requirements-dev.txt
```

## デプロイ手順

### 事前に作成するリソース

OpenAI API Keyを取得した上で、以下のファイルを作成してください。

* .env

### デプロイ手順

```bash
cd cdk
AWS_DEFAULT_REGION=ap-northeast-1 cdk synth # CFnが意図した通り出力されることを確認します。
AWS_DEFAULT_REGION=ap-northeast-1 cdk diff # 差分を確認します。
AWS_DEFAULT_REGION=ap-northeast-1 cdk deploy
```

## テストの実行方法

デプロイ後にLambdaのAWSコンソールでテストを実行するか、AWS CLIとして以下の内容について共有させてください。

```bash
aws lambda invoke --function-name browser-use-on-aws-lambda-MainFunction output.txt
```

## Developer's Note

### LambdaでPlaywrightを動かすための注意点

`browser-use` では、ブラウザの操作に `Playwright` を使用しています。[How to run Playwright with Python in AWS Lambda](https://www.cloudtechsimplified.com/playwright-aws-lambda-python/)に記載があるように、LambdaでPlaywrightを動かすためには、Chromeの引数として以下の設定が必要です。

* --disable-gpu
* --single-process

Lambdaは実行できるけど、Playwright(browser-use)がPageのLoadで失敗する場合は、上記の設定を確認してください。browser-useでは、以下のように設定しています。

```python
browser = Browser(
    config=BrowserConfig(
        headless=True, extra_chromium_args=["--disable-gpu", "--single-process"]
    )
)
agent = Agent(
        ...
        browser=browser,
    )
```

## 参考文献

* [How to run Playwright with Python in AWS Lambda](https://www.cloudtechsimplified.com/playwright-aws-lambda-python/)
* [GitHub - browser-use](https://github.com/browser-use/browser-use)