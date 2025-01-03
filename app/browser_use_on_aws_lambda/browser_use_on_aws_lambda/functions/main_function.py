from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from browser_use.browser.browser import Browser, BrowserConfig
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()
browser = Browser(
    config=BrowserConfig(
        headless=True, extra_chromium_args=["--disable-gpu", "--single-process"]
    )
)


async def main():
    agent = Agent(
        task="www.inoue-kobo.com を開いて、最新の記事から3つを要約して、Markdownの表形式で表示してください。",
        llm=ChatOpenAI(model="gpt-4o-mini"),
        browser=browser,
    )
    result = await agent.run()
    logger.info(result)

    return result.final_result()


@logger.inject_lambda_context(log_event=True)
def lambda_handler(event: dict, context: LambdaContext):
    return asyncio.run(main())
