import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse

from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAI, ChatOpenAI

from pydantic import BaseModel
import json
import prompts

# .env 파일 환경변수 로드
load_dotenv()

# OpenAI API key 불러오기
OPENAI_KEY = os.environ.get("OPENAI_API_KEY")

# API Key가 없으면 오류 출력 후 종료
if not OPENAI_KEY:
    print('OpenAI API 키를 입력하세요!')
    raise ValueError("You need to set up your OpenAI API Key in '.env' file!")
    exit()
else:
    print('앱 실행 중...')



example_prompt = PromptTemplate.from_template(
    "Question:\n{question}\nAnswer:\n{answer}"
)

# 퓨샷 프롬프트
few_shot_prompt = FewShotPromptTemplate(
    examples=prompts.examples,
    example_prompt=example_prompt,
    suffix="Question:\n{question}\nAnswer:",
    input_variables=["question"],
)

##############################################################
#  체인
##############################################################
def load_chain():
    """
    프롬프트와 llm으로 langchain 생성  
    (Default : gpt4o-mini, need OpenAI API Key)

    Args:
      model: string, llm model name.
    Returns:
      llm_chain: Any, langchain's llm model chain
    """
    # 템플릿 정의 # 프롬프트 설정
    prompt = PromptTemplate.from_template(prompts.template)

    # 모델 생성
    model = ChatOpenAI(
             #  api_key = OPENAI_KEY
             #, 
             temperature = 0.7
             #, streaming   = True
             #, batch_size  = 50
             , model="gpt-4o-mini"
             )

    # 파서 생성 - (이게 필요한가?)    
    parser = StrOutputParser()

    # 체인 생성
    chain = few_shot_prompt | model | parser

    return chain


# FastAPI 초기화
app = FastAPI()

# 요청 모델 정의
class AskRequest(BaseModel):
    question: str



@app.post("/ask")
async def ask_question(request: AskRequest):
    try:
        answer = load_chain().invoke(request.question)
        return {"question": request.question, "answer": answer}
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.post("/ask")
async def ask_question(request: AskRequest):
    try:
        answer = load_chain().invoke(request.question)
        return {"question": request.question, "answer": answer}
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Fast API 서버 실행
if __name__ == "__main__":
    import uvicorn
    print("""\
  _   _    __   _   _    ___  _  _  __   _   ___
 / \ | |  / _| / \ | |  | __|| \| ||  \ / \ |  ☆ \\
| o || | ( (_ | o || |_ | _| | \\\\ || o ) o ||    /
|_n_||_|  \__||_n_||___||___||_|\_||__/|_n_||_|\\_\\
                                      - by. Soonbro
""")
    print('API Server Start!')
    uvicorn.run(app, host="0.0.0.0", port=8000)
