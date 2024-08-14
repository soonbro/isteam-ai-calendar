from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google_calendar import get_recent_event, google_calendar_api_service

from constants import *
from llm_chain import load_chain, OPENAI_MODELS, OLLAMA_MODELS

# API Key가 없으면 오류 출력 후 종료
if not OPENAI_KEY:
    print('OpenAI API 키를 입력하세요!')
    raise ValueError("You need to set up your OpenAI API Key in '.env' file!")
else:
    print('앱 실행 중...')

# FastAPI 초기화
app = FastAPI(title="IS TEAM AI CALENDAR API")

# 요청 모델 정의
class AskRequest(BaseModel):
    question: str

# 요청 모델 정의
class SummaryRequest(BaseModel):
    model: str
    question: str

def standardize_model_name(
        model_name: str,
        is_completion: bool = False,
    ) -> str:
    """
    Standardize the model name to a format that can be used in the OpenAI API.

    Args:
        model_name: Model name to standardize.
        is_completion: Whether the model is used for completion or not.
            Defaults to False.

    Returns:
        Standardized model name.

    """
    model_name = model_name.lower()
    if ".ft-" in model_name:
        model_name = model_name.split(".ft-")[0] + "-azure-finetuned"
    if ":ft-" in model_name:
        model_name = model_name.split(":")[0] + "-finetuned-legacy"
    if "ft:" in model_name:
        model_name = model_name.split(":")[1] + "-finetuned"
    if is_completion and (
        model_name.startswith("gpt-4")
        or model_name.startswith("gpt-3.5")
        or model_name.startswith("gpt-35")
        or ("finetuned" in model_name and "legacy" not in model_name)
    ):
        return model_name + "-completion"
    else:
        return model_name

def get_openai_token_cost_for_model(
    model_name: str, num_tokens: int, is_completion: bool = False
) -> float:
    """
    Get the cost in USD for a given model and number of tokens.

    Args:
        model_name: Name of the model
        num_tokens: Number of tokens.
        is_completion: Whether the model is used for completion or not.
            Defaults to False.

    Returns:
        Cost in USD.
    """
    model_name = standardize_model_name(model_name, is_completion=is_completion)
    if model_name not in OPENAI_MODEL_COST_PER_1K_TOKENS:
        raise ValueError(
            f"Unknown model: {model_name}. Please provide a valid OpenAI model name."
            "Known models are: " + ", ".join(OPENAI_MODEL_COST_PER_1K_TOKENS.keys())
        )
    return OPENAI_MODEL_COST_PER_1K_TOKENS[model_name] * (num_tokens / 1000)

def cal_cost(model_name,token_usage):
    # compute tokens and cost for this request
    completion_tokens = token_usage.get("completion_tokens", 0)
    prompt_tokens = token_usage.get("prompt_tokens", 0)
    
    if model_name in OPENAI_MODEL_COST_PER_1K_TOKENS:
        completion_cost = get_openai_token_cost_for_model(
            model_name, completion_tokens, is_completion=True
        )
        prompt_cost = get_openai_token_cost_for_model(model_name, prompt_tokens)
    else:
        completion_cost = 0
        prompt_cost = 0
    total_cost = prompt_cost + completion_cost
    return {
        "prompt_cost":f"${prompt_cost:.4f}",
        "completion_cost":f"${completion_cost:.4f}",
        "total_cost":f"${total_cost:.4f}",
    }

@app.get("/api/get_recent_event")
async  def  get_recent_event_endpoint ():
    """
    `Google Calendar API`에서 향후 10일간의 이벤트 수신
    """
    return {"events" : f"{get_recent_event(google_calendar_api_service())}"}

@app.post("/api/summary")
async def summarize_schedule(request: SummaryRequest):
    """
    `LLM model`으로 일정 요약

    Args:
        request: SummaryRequest

    Returns:
        {
            question: 일정,
            answer: AI 일정 요약 내용,
            cost: OpenAI API Usage Cost
        }
    
    """
    try:
        answer = load_chain(request.model).invoke(request.question)
        if request.model in OPENAI_MODELS:
            cost=cal_cost(answer.response_metadata["model_name"], answer.response_metadata["token_usage"])
            return {
                "question": request.question,
                "answer": answer.content,
                "cost": cost
            }
        elif request.model in OLLAMA_MODELS:
            return {
                "question": request.question,
                "answer": answer.content,
            }
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/api/healthchecker", tags=["hidden"], include_in_schema=False)
def healthchecker():
    return {"status": "success", "message": "Integrate FastAPI with Next.js (WIP)"}

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
