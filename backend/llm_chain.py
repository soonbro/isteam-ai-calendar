from constants import *
##### OpenAI #####
#from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

##### Ollama #####
#from langchain_ollama import ChatOllama
#from langchain_ollama.llms import OllamaLLM
from langchain_community.chat_models import ChatOllama

##### Parser #####
from langchain_core.output_parsers import StrOutputParser

##### Prompt Template #####
from langchain_core.prompts import PromptTemplate
#from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.few_shot import FewShotPromptTemplate

##### My Prompt #####
import prompts as prompts #./prompt.py

##############################################################
#  프롬프트 설정
##############################################################
zero_shot_template = PromptTemplate.from_template(prompts.template)
"""Zero-Shot Prompt"""

prompt = PromptTemplate.from_template(prompts.template)
"""One-Shot Prompt"""

example_prompt = PromptTemplate.from_template(
    "Question:\n{question}\nAnswer:\n{answer}"
)


few_shot_prompt = FewShotPromptTemplate(
    examples=prompts.examples,
    example_prompt=example_prompt,
    suffix="Question:\n{question}\n답변 마지막에는 [오늘의 한 마디]라는 타이틀 아래에 답변과 관련된 유머를 추가해 줘.\n\nAnswer:",
    input_variables=["question"],
)
"""Few-Shot Prompt"""


##############################################################
#  체인
##############################################################
def load_chain(model):
    """
    프롬프트와 llm으로 langchain 생성  
    (Default : gpt4o-mini, need OpenAI API Key)

    Args:
      model: string, llm model name.
    Returns:
      llm_chain: Any, langchain's llm model chain
    """
    print(f'{model} 모델을 불러오고 있습니다.')
    if model in OPENAI_MODELS:
        # OpenAI API Key가 없으면 오류 출력 후 종료
        if not OPENAI_KEY:
            print('OpenAI API 키를 입력하세요!')
            raise ValueError("You need to set up your OpenAI API Key in '.env' file!")
        # OpenAI gpt-4o-mini 모델 설정
        llm = ChatOpenAI(
            model=model,
            temperature=0.7,
        )
    elif model in OLLAMA_MODELS:
        if not OLLAMA_HOST:
            print('OLLAMA HOST 서버 주소를 설정해주세요!')
            raise ValueError("You need to set up your OLLAMA_HOST in '.env' file!")
        try:
            """
            OLLAMA HOST 서버 연결 확인
            """
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # .env의 OLLAMA_HOST가 http://HOST:PORT 형식인데 socket으로 연결 체크 하려면 (HOST,PORT) 튜플 형식이 필요.
            # 파싱 방법 1 : urllib.parse.urlparse 모듈 사용
            # 파싱 방법 2 : 정규식 사용 p = '(?:http.*://)?(?P<host>[^:/ ]+).?(?P<port>[0-9]*).*'
            # 귀찮다 그냥 대충 해보자
            addr_temp = OLLAMA_HOST.replace("http://","")
            addr_temp = addr_temp.replace("https://","") # 혹시나 https일 경우
            addr_list = addr_temp.split(":")
            addr_list[1] = int(addr_list[1])
            addr = tuple(addr_list)
            res = sock.connect_ex(addr)
            if res == 0:
                print(f"{OLLAMA_HOST} >>> CONNECTED")
            else:
                print(f"{OLLAMA_HOST} >>> NOT CONNECTED")
                raise ConnectionError("Ollama Host 연결에 실패했습니다.")
            sock.close()

        except Exception as e:
            #연결 예외 발생 시 종료
            print("Ollama 연결 에러 발생:", e)
            print("Please Check your Ollama Host URL")
            print("App을 종료합니다.")
            exit(-1)
            
        try:
            llm = ChatOllama(
                model=model,
                temperature=0.7,
                base_url=OLLAMA_HOST
            )
        except Exception as e:
            print(str(e))

    #parser = StrOutputParser()
    llm_chain = few_shot_prompt | llm #| parser

    return llm_chain
