examples = [
    {
        "question": """다음은 우리 팀 일정인데, 주간 회의에 간략하게 리뷰하려고 해.
주요 일정을 요약하고 작업 일정에 대해서는 주의 사항을 알려줘.
각 날짜마다 연차와 교육인원 수를 요약해줘.

향후 10일간의 일정입니다.

[일반일정]
2024-07-30(화) [IOS] 모바일 DRM 만료일
2024-07-30(화) 10:00 [팀장,량희,윤주]라이선스 축소 검토 회의
2024-07-30(화) 11:30 [영업] 매니저 간담회(플랜트 - 7/25 → 7/30 변경)
2024-08-01(목) 09:00 [윤주] Teams 사용현황 요청 (DWP)
2024-08-01(목) 11:00 [은철] 헬프데스크 월간회의
2024-08-02(금) 09:00 [태영,유림] AI 프로젝트 주간회의
2024-08-02(금) 13:30 IS팀 주간회의
2024-08-05(월) 09:30 [보임자] SM팀장 워크샵
2024-08-05(월) 11:00 [보임자]IT지원팀 주간회의
2024-08-06(화) 10:00 [충훈] 고스트패스 PoC 사전 회의
2024-08-08(목) 11:30 [영업] 매니저 간담회(운영1)

[작업]
2024-07-30(화) 16:00 [충훈,성진] 웹방화벽 교체 작업
2024-07-30(화) 17:00 [성진] 모바일 DRM 인증서 갱신 작업
2024-07-30(화) 20:00 [성진] DLP 개선 작업

[연차]
2024-07-30(화) [은철]오후반차
2024-07-30(화) 08:00 [성진] 오전반차 (보상)
2024-07-31(수) [은철]연차
2024-07-31(수) [유림]패밀리휴가 분할
2024-08-01(목) [상훈, 선아] 개인연차
2024-08-02(금) [명섭, 선아, 영미] 개인연차

[교육]
2024-07-30(화) 10:00 [순형,정연] 7월 바이트 클래스 - 데이터베이스 인덱스 개념과 활용
2024-08-06(화) [3차] 시큐어 코딩 과정
2024-08-07(수) [4차] 시큐어 코딩 과정
2024-08-08(목) [충훈,재영] ITSAC 사용자교육
2024-08-09(금) [성진] ITSAC 사용자교육
""",
        "answer": """**건설IS팀 AI Calendar가 향후 10일간의 일정을 요약합니다!😎**

# 건설IS팀 일정 요약 (2024-07-30 ~ 2024-08-09)

주요 일정과 작업 일정은 다음과 같습니다.

**주요일정:**
- 2024-07-30(화): [IOS] 모바일 DRM 만료일
- 2024-07-31(수) 08:00: [태영] 아이멤버/ECM 연계방안 협의
- 2024-08-01(목) 09:00: [윤주] Teams 사용현황 요청 (DWP)
- 2024-08-01(목) 11:00: [은철] 헬프데스크 월간회의
- 2024-08-02(금) 09:00: [태영, 유림] AI 프로젝트 주간회의
- 2024-08-02(금) 13:30: IS팀 주간회의
- 2024-08-05(월) 09:30: [보임자] SM팀장 워크샵
- 2024-08-05(월) 11:00: [보임자] IT지원팀 주간회의
- 2024-08-06(화) 10:00: [충훈] 파트너사 PoC 사전 회의
- 2024-08-08(목) 11:30: [영업] 매니저 간담회(운영1)
- 2024-08-09(금) 09:00: [태영, 유림] AI 프로젝트 주간회의
- 2024-08-09(금) 13:30: IS팀 주간회의

**작업:**
- 2024-07-30(화) 16:00: [충훈, 성진] 웹방화벽 교체 작업
- 2024-07-30(화) 17:00: [성진] 모바일 DRM 인증서 갱신 작업
- 2024-07-30(화) 20:00: [성진] DLP 개선 작업
- 2024-08-02(금) 10:00: [충훈, 성진] DOCS SSO 연동테스트
- 2024-08-06(화) 17:00: [태영] MOIN 포탈 공용계정 PW변경

# 연차 및 교육

연차 및 교육 일정은 다음과 같습니다.

### 연차 및 교육 인원 요약
- **2024-07-30 (화)**:
  - 연차: 은철 (오후반차), 성진 (오전반차)
  - 교육: 순형, 정연 (10:00 7월 바이트 클래스)
  - 공석인원: 성진(오전), 은철(오후)

- **2024-07-31 (수)**:
  - 연차: 은철, 유림 (패밀리휴가 분할)
  - 공석인원: 은철, 유림 (2명)

- **2024-08-01 (목)**:
  - 연차: 상훈, 선아
  - 공석인원: 상훈, 선아 (2명)

- **2024-08-02 (금)**:
  - 연차: 명섭, 선아, 영미
  - 공석인원: 명섭, 선아, 영미 (3명)

- **2024-08-06 (화)**:
  - 교육: 3차 시큐어 코딩 과정

- **2024-08-07 (수)**:
  - 교육: 4차 시큐어 코딩 과정

- **2024-08-08 (목)**:
  - 교육: 충훈, 재영 (ITSAC 사용자교육)
  - 공석인원: 충훈, 재영 (2명)

- **2024-08-09 (금)**:
  - 교육: 성진 (ITSAC 사용자교육)
  - 공석인원: 성진 (1명)
  
### 주의 사항
1. **연차 관리:** 
   - 7월 30일과 31일에 은철이 연차를 사용하므로, 그 기간 동안 은철이 참석하는 회의나 작업에 대한 조정이 필요합니다.
   - 유림은 7월 31일 패밀리휴가로 부재하므로, 관련 업무에 대한 대체 인력 배치가 필요합니다.
   - 8월 1일과 2일에는 상훈, 선아, 명섭, 영미가 연차를 사용하므로, 해당 일자에 중요한 업무가 있다면 미리 조정해야 합니다.

2. **작업 일정:** 
   - 7월 30일에 진행되는 웹방화벽 교체 작업과 모바일 DRM 인증서 갱신 작업 후, 모바일 DRM 만료일이 같은 날이므로 주의가 필요합니다.
   - 8월 2일에 DOCS SSO 연동테스트가 예정되어 있으므로, 이와 관련된 준비가 필요합니다.

3. **교육 일정:** 
   - 8월 6일에 시큐어 코딩 과정이 진행되며, 이 날 연차를 사용하는 인원이 없으므로 교육 참석이 원활할 것으로 보입니다.
   - 교육이 끝난 후 8월 9일에 ITSAC 사용자교육이 있으므로, 교육 참석자들의 피드백을 수집하는 것도 좋습니다.
""",
    },
]

# 템플릿 설정
template = """Question:

다음은 우리 팀 일정인데, 주간 회의에 간략하게 리뷰하려고 해.
주요 일정을 요약하고 작업 일정에 대해서는 주의 사항을 알려줘.
각 날짜마다 연차와 교육인원 수를 요약해줘.

{question}

Answer:

**건설IS팀 AI Calendar가 향후 10일간의 일정을 요약합니다!😎**

# 건설IS팀 일정 요약 (2024-07-30 ~ 2024-08-09)

주요 일정과 작업 일정은 다음과 같습니다.

**주요일정:**
- 2024-07-30(화): [IOS] 모바일 DRM 만료일
- 2024-07-31(수) 08:00: [태영] 아이멤버/ECM 연계방안 협의
- 2024-08-01(목) 09:00: [윤주] Teams 사용현황 요청 (DWP)
- 2024-08-01(목) 11:00: [은철] 헬프데스크 월간회의
- 2024-08-02(금) 09:00: [태영, 유림] AI 프로젝트 주간회의
- 2024-08-02(금) 13:30: IS팀 주간회의
- 2024-08-05(월) 09:30: [보임자] SM팀장 워크샵
- 2024-08-05(월) 11:00: [보임자] IT지원팀 주간회의
- 2024-08-06(화) 10:00: [충훈] 파트너사 PoC 사전 회의
- 2024-08-08(목) 11:30: [영업] 매니저 간담회(운영1)
- 2024-08-09(금) 09:00: [태영, 유림] AI 프로젝트 주간회의
- 2024-08-09(금) 13:30: IS팀 주간회의

**작업:**
- 2024-07-30(화) 16:00: [충훈, 성진] 웹방화벽 교체 작업
- 2024-07-30(화) 17:00: [성진] 모바일 DRM 인증서 갱신 작업
- 2024-07-30(화) 20:00: [성진] DLP 개선 작업
- 2024-08-02(금) 10:00: [충훈, 성진] DOCS SSO 연동테스트
- 2024-08-06(화) 17:00: [태영] MOIN 포탈 공용계정 PW변경

# 연차 및 교육

연차 및 교육 일정은 다음과 같습니다.

### 연차 및 교육 인원 요약
- **2024-07-30 (화)**:
  - 연차: 은철 (오후반차), 성진 (오전반차)
  - 교육: 순형, 정연 (10:00 7월 바이트 클래스)
  - 공석인원: 성진(오전), 은철(오후)

- **2024-07-31 (수)**:
  - 연차: 은철, 유림 (패밀리휴가 분할)
  - 공석인원: 은철, 유림 (2명)

- **2024-08-01 (목)**:
  - 연차: 상훈, 선아
  - 공석인원: 상훈, 선아 (2명)

- **2024-08-02 (금)**:
  - 연차: 명섭, 선아, 영미
  - 공석인원: 명섭, 선아, 영미 (3명)

- **2024-08-06 (화)**:
  - 교육: 3차 시큐어 코딩 과정

- **2024-08-07 (수)**:
  - 교육: 4차 시큐어 코딩 과정

- **2024-08-08 (목)**:
  - 교육: 충훈, 재영 (ITSAC 사용자교육)
  - 공석인원: 충훈, 재영 (2명)

- **2024-08-09 (금)**:
  - 교육: 성진 (ITSAC 사용자교육)
  - 공석인원: 성진 (1명)
  
### 주의 사항
1. **연차 관리:** 
   - 7월 30일과 31일에 은철이 연차를 사용하므로, 그 기간 동안 은철이 참석하는 회의나 작업에 대한 조정이 필요합니다.
   - 유림은 7월 31일 패밀리휴가로 부재하므로, 관련 업무에 대한 대체 인력 배치가 필요합니다.
   - 8월 1일과 2일에는 상훈, 선아, 명섭, 영미가 연차를 사용하므로, 해당 일자에 중요한 업무가 있다면 미리 조정해야 합니다.

2. **작업 일정:** 
   - 7월 30일에 진행되는 웹방화벽 교체 작업과 모바일 DRM 인증서 갱신 작업 후, 모바일 DRM 만료일이 같은 날이므로 주의가 필요합니다.
   - 8월 2일에 DOCS SSO 연동테스트가 예정되어 있으므로, 이와 관련된 준비가 필요합니다.

3. **교육 일정:** 
   - 8월 6일에 시큐어 코딩 과정이 진행되며, 이 날 연차를 사용하는 인원이 없으므로 교육 참석이 원활할 것으로 보입니다.
   - 교육이 끝난 후 8월 9일에 ITSAC 사용자교육이 있으므로, 교육 참석자들의 피드백을 수집하는 것도 좋습니다.
"""
