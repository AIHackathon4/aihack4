import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # .env 값을 환경변수로
client = OpenAI()  # OPENAI_API_KEY, OPENAI_BASE_URL 자동 사용


def ask(question: str) -> str:
    res = client.chat.completions.create(
        model=os.environ["LLM_MODEL"],
        messages=[
            {"role": "system", "content": "너는 친절한 도우미야. 모르면 모른다고 답해."},
            {"role": "user", "content": question},
        ],
    )
    print("사용 토큰:", res.usage.total_tokens)
    return res.choices[0].message.content


if __name__ == "__main__":
    print(ask("안녕! 한 문장으로 자기소개 해 줘."))
