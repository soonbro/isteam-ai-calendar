from datetime import datetime, timedelta
import os.path
from dotenv import load_dotenv

from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

load_dotenv()

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
TIMEZONE = 'Asia/Seoul'

#기타 일정 Calendar ID
CAL_ID_SCHEDULE = os.environ.get("CAL_ID_SCHEDULE")
#작업 일정 Calendar ID
CAL_ID_INFRA = os.environ.get("CAL_ID_INFRA")
#연차 일정 Calendar ID
CAL_ID_DAYOFF = os.environ.get("CAL_ID_DAYOFF")
#교육 일정 Calendar ID
CAL_ID_EDU = os.environ.get("CAL_ID_EDU")

def google_calendar_api_service():
    """
    ## Construct Google Calendar API Service.
    구글 캘린더 API 서비스 생성

    `credentials.json` 설정 필요.  `token.json`에 토큰 저장

    Returns:
        service: A Resource object with methods for interacting with the Google Calendar service.
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
    
    #TODO: token이 유효해도 refresh_token으로 새로운 access_token 발급 받아 사용하자
    
    service = build('calendar', 'v3', credentials=creds)
    return service

def get_week_name(date):
    """
    ### get_week_name
    날짜에서 한글 요일명을 얻는다.

    Args:
        date - YYYY-MM-DD
    """
    t = ['월', '화', '수', '목', '금', '토', '일']
    return t[date.weekday()]

def get_recent_event_string(service, calendarId):
    """
    ### Get Recent Event String
    Args:
        service: Google Calendar API Service.
        calendarId: string, Google Calendar ID
    Returns:
        recent_event: string, 향후 10일 간의 event 문자열.

    """
    eventFrom = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    eventTo = datetime.utcnow() + timedelta(days=10)
    eventTo = eventTo.isoformat() + 'Z'
    recent_event = ''
    events_result = service.events().list(calendarId=calendarId, timeMin=eventFrom,
                                        # maxResults=50, 
                                        timeMax=eventTo,
                                        singleEvents=True,
                                        orderBy='startTime').execute()
    # dict -> list
    events = events_result.get('items', [])

    if not events:
        recent_event = '없음' + '\n'
    for event in events:
        if 'dateTime' in event['start'].keys():
            recent_event = recent_event + event['start']['dateTime'][:16].replace('T', 
                                                                                    '(' + get_week_name(datetime.strptime(event['start']['dateTime'][:10], 
                                                                                    '%Y-%m-%d').date()) + ') ') + \
                                                                            ' ' + event['summary'] + '\n'

        else:
            # 종일 일정인 경우 날짜의 From to 를 비교하여 2일이상에 걸쳐 있으면 2010-01-01~2010-01-01 이런형식으로 보여준다.
            # Timzone 형식에 따라 end 날짜가 하루씩 크기 때문에 하루를 뺀것과 비교한다.
            startDate = datetime.strptime(event['start']['date'], '%Y-%m-%d').date()
            startDate = str(startDate) + '(' + get_week_name(startDate) + ')'
            endDate = datetime.strptime(event['end']['date'], '%Y-%m-%d').date() + timedelta(days=-1)
            endDate = str(endDate) + '(' + get_week_name(endDate) + ')'
            recent_event = recent_event + startDate
            if startDate != endDate :
                # print(event)
                recent_event = recent_event + '~' + endDate
            recent_event += ' ' + event['summary'] + '\n'

    return recent_event

def get_recent_event(service):
    # 일반일정 가져오기
    recent_event =  '향후 10일간의 일정입니다.\n\n'
    recent_event += '[일반일정]\n'
    recent_event += get_recent_event_string(service, CAL_ID_SCHEDULE)
    recent_event += '\n[작업]\n'
    recent_event += get_recent_event_string(service, CAL_ID_INFRA)
    recent_event += '\n[연차]\n'
    recent_event += get_recent_event_string(service, CAL_ID_DAYOFF)
    recent_event += '\n[교육]\n'
    recent_event += get_recent_event_string(service, CAL_ID_EDU)
    
    #TODO: 팀즈 알리미 웹훅 연동
    #send_ms_teams_board_msg('팀 일정 알림', recent_event.replace('\n', '<br/>'), 'https://calendar.google.com', TEAMS_CONNECTOR_CAL_URL)
    
    return recent_event

if __name__ == '__main__':
    """
    for module TEST..
    """
    print("Google Calendar API Service 세팅 중...")
    try:
        service = google_calendar_api_service()
    except Exception as err:
        print(str(err))
    print("Google Calendar API Service 세팅 완료!!")
    print("일정을 불러오고 있습니다...")
    print(get_recent_event(service)) # 테스트 출력