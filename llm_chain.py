import os.path
from dotenv import load_dotenv

#from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

#from langchain_ollama import ChatOllama
#from langchain_ollama.llms import OllamaLLM
from langchain_community.chat_models import ChatOllama

from langchain_core.prompts import PromptTemplate
#from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.few_shot import FewShotPromptTemplate

import prompts

# .env 파일 환경변수 로드
load_dotenv()

# OpenAI API key 불러오기
OPENAI_KEY = os.environ.get("OPENAI_API_KEY")

# Ollama Host 서버 주소
OLLAMA_HOST = os.environ.get("OLLAMA_HOST")

#ollama_llm = OllamaLLM(model="EEVE",base_url=OLLAMA_HOST)

#프롬프트 설정
prompt = PromptTemplate.from_template(prompts.template)

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
    if model == "gpt-4o" or model == "gpt-4o-mini":
        # OpenAI API Key가 없으면 오류 출력 후 종료
        if not OPENAI_KEY:
            print('OpenAI API 키를 입력하세요!')
            raise ValueError("You need to set up your OpenAI API Key in '.env' file!")
        # OpenAI gpt-4o-mini 모델 설정
        llm = ChatOpenAI(
            model=model,
            temperature=0.5,
        )
    elif model == "Gemma2" or model == "EEVE" or model == "qwen2":
        if not OLLAMA_HOST:
            print('OLLAMA HOST 서버 주소를 설정해주세요!')
            raise ValueError("You need to set up your OLLAMA_HOST in '.env' file!")
        try:
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #p = '(?:http.*://)?(?P<host>[^:/ ]+).?(?P<port>[0-9]*).*'
            addr_temp = OLLAMA_HOST.replace("http://","")
            addr_temp = addr_temp.replace("https://","")
            addr_list = addr_temp.split(":")
            addr_list[1] = int(addr_list[1])
            addr = tuple(addr_list)
            print(addr)
            res = sock.connect_ex(addr)
            if res == 0:
                print(f"{OLLAMA_HOST} >>> CONNECTED")
            else:
                print(f"{OLLAMA_HOST} >>> NOT CONNECTED")
                raise ConnectionError("Ollama Host 연결에 실패했습니다.")
            sock.close()

        except Exception as e:
            print("Ollama 연결 에러 발생:", e)
            print("Please Check your Ollama Host URL")
            print("App을 종료합니다.")
            exit(-1)
            

        try:
            llm = ChatOllama(
                model="EEVE",
                temperature=0.5,
                base_url=OLLAMA_HOST
            )
        except Exception as e:
            print(str(e))

    llm_chain = few_shot_prompt | llm

    return llm_chain