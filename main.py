import os.path
from dotenv import load_dotenv

from InquirerPy import inquirer, get_style
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from InquirerPy.utils import color_print

from langchain_community.callbacks.manager import get_openai_callback


from google_calendar import get_recent_event, google_calendar_api_service


from llm_chain import load_chain
from prompts import examples, template

# .env 파일 환경변수 로드
load_dotenv()

class AiCalendar:
    def __init__(self):
        self.model =""

    def set_model(self, model_name:str):
        self.model = model_name


if __name__ == '__main__':
    print("""\
  _   _    __   _   _    ___  _  _  __   _   ___
 / \ | |  / _| / \ | |  | __|| \| ||  \ / \ | o \\
| o || | ( (_ | o || |_ | _| | \\\\ || o ) o ||   /
|_n_||_|  \__||_n_||___||___||_|\_||__/|_n_||_|\\\\
""")
    print('APP Start!')

    app = AiCalendar()

    ######################################
    # LLM 모델 설정
    ######################################
    inquirer_style = get_style({"separator": "#98c379", "question": "#abb2bf"}, style_override=False)
    select_llm_model = inquirer.select(
        message="어떤 모델을 사용하시겠습니까?:",
        choices=[Separator("[OpenAI]"),
                 "GPT4o",
                 "GPT4o-mini",
                 Separator(),
                 Separator("[Ollama]"),
                 "Gemma2:9b", 
                 "EEVE:10.8b",
                 Separator(),
                 Choice(value=None, name="Exit")],
        default=None,
        style=inquirer_style
        )
    selected_llm_model = select_llm_model.execute()

    if not selected_llm_model:
        print("모델을 선택하지 않았습니다. 프로그램을 종료합니다.")
        exit()
    elif selected_llm_model == "GPT4o":
        print("GPT4o 모델을 사용하여 일정을 정리하겠습니다!")
        #app.set_model("gpt-4o")
        app.model = "gpt-4o"
    elif selected_llm_model == "GPT4o-mini":
        print("GPT4o-mini 모델을 사용하여 일정을 정리하겠습니다!")
        #app.set_model("gpt-4o-mini")
        app.model = "gpt-4o-mini"
    elif selected_llm_model == "Gemma2:9b":
        #app.set_model("Gemma2")
        app.model = "Gemma2"
    elif selected_llm_model == "EEVE:10.8b":
        #app.set_model("EEVE")
        app.model = "EEVE"

    ######################################
    # EXECUTE QUERY
    ######################################
    
    # 체인 불러오기
    chain = load_chain(app.model)

    print('구글 캘린더에서 일정을 불러옵니다.')
    # 질의 설정
    question = get_recent_event(google_calendar_api_service())

    print("\n전체 일정은 다음과 같습니다.\n-------------------------------\n")
    print(question)
    print('AI가 일정을 정리하고 있습니다.\n-------------------------------\n')
    
    if app.model == "gpt-4o" or app.model == "gpt-4o-mini":
        # stream 사용 스트리밍 방식으로 각 토큰을 출력. (실시간 출력)
        answer = chain.stream(question)
        for token in answer:
            print(token.content, end="", flush=True)
        
        # 토큰 사용량 확인
        #with get_openai_callback() as cb:
            # invoke 사용
            #answer = chain.invoke(question)
            #print(f"[답변]: {answer.content}")
        
            #print(f"\n\n총 사용된 토큰수: \t\t{cb.total_tokens}")
            #print(f"프롬프트에 사용된 토큰수: \t{cb.prompt_tokens}")
            #print(f"답변에 사용된 토큰수: \t{cb.completion_tokens}")
            #print(f"호출에 청구된 금액(USD): \t${cb.total_cost}")
    
    elif app.model == "Gemma2" or app.model ==  "EEVE":
        # stream 사용 스트리밍 방식으로 각 토큰을 출력. (실시간 출력)
        answer = chain.stream(question)
        for token in answer:
            print(token.content, end="", flush=True)

    print('\n\n\nAI가 정리한 일정이 도움이 되셨나요?\n\n성능 향상에 도움을 주세요!\n\nhttps://github.com/soonbro/isteam-ai-calendar\n')
    exit()
