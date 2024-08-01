# LOTTE E&C IS TEAM AI CALENDAR

롯데건설 IS팀 AI 캘린더 - by. Soonbro

![Alt text](images/isteam_ai_calendar_key_visual.png)

> ## 🚧🏗️THIS PROJECT IS STILL WORK IN PROGRESS (WIP)🏗️🚧
>
> 🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧
>
> ⚠️ 아직 개발 중인 프로젝트입니다.
>
> 2024-08-01 - Add Model Select CLI and ADD Ollama models

![Alt text](images/image.png)

## 사용법

### Python 패키지 설치

```bash
pip install -r requirements.txt
```

### 환경변수 세팅 (set ENV)

```bash
$ cp .env.example .env
$ vi .env
```

- Google Calendar ID 세팅
- OpenAI API Key
- (Option) Ollama Host Server Address (default: localhost)

### Google Calendar API

구글 캘린더 API를 사용하기 위해 Google Cloud API 및 서비스 설정  
사용자 인증정보 생성 후 `credentials.json` 파일을 받아 프로젝트 루트 경로에 위치.  
(Set Google Calendar API and OAuth. `credentials.json` File to Project root folder.)

### 실행 (UI 개발 예정)

```
$ python main.py
$ python3 main.py
```

## 프로젝트 세팅

### 프로젝트 폴더 생성

```bash
mkdir isteam-ai-calendar
cd isteam-ai-calendar
```

VSCode 실행  
`code .`

### python 가상환경 생성

```bash
python -m venv .venv
ls -a
```

`./  ../  .venv/`

### (선택) .gitingnore 파일 생성

```bash
echo '.venv' >> .gitignore
cat .gitignore
```

`.venv`

### 가상환경 activate

Windows

```bash
. .venv/Scripts/activate
```

Linux or Mac

```bash
. .venv/bin/activate
```

`(.venv)`

### 가상환경 activate 확인

```bash
which python
```

```bash
/c/Users/Soonbro/Dev/AI/isteam-ai-calendar/\Users\Soonbro\Dev\AI\isteam-ai-calendar\.venv/Scripts/python
(.venv)
```

### 구글 캘린더 API 관련 패키지 설치

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 토큰 생성 스크립트

API 사용을 위해 Google Cloud 설정 필요
https://console.cloud.google.com/apis/credentials

`API 및 서비스 > 사용자 인증 정보`

`+ 사용자 인증 정보 만들기`

OAuth 2.0 클라이언트 ID 생성 및 json 파일 download

`credentials.json` 파일 project root로 이동

> `credentials.json` 파일로 OAuth 인증 및 토큰 저장 샘플
> [calendar_quickstart github link](https://github.com/googleworkspace/python-samples/blob/master/calendar/quickstart/quickstart.py)

```python
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START calendar_quickstart]
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def main():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      print(start, event["summary"])

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()
# [END calendar_quickstart]
```

https://developers.google.com/calendar/api/quickstart/python?hl=ko

### AI 관련 패키지 설치

```bash
pip install openai langchain langchain-community langchain-openai
```
