# SMART MEETING
약속을 쉽게 잡을 수 있게 해주는 서비스
- 다음 앱으로 구성
    - main(메인 페이지)
    - post(게시물 관련 페이지)
    - accounts(로그인 기능 등)
- 데이터베이스 만드면서 테스트용으로 사용했던 html파일은 일단 sample폴더에 저장하였음 

## config
- 환경설정
- `templates` - `base.html`에는 모든 html의 공통되는 영역(헤더 영역, script영역 등)을 작성할 곳
- `static` - css, js등으로 구성

## main
- 캘린더
- Schedule테이블의 데이터를 참조하여 달력에 색깔로 일정을 표시
- 캘린더의 날짜를 클릭할 시, 그 날에 해당하는 일정들의 목록을 표시

#### 데이터베이스(models.py)
- Schedule 테이블
    - 모임에 참여하거나 탈퇴하면 데이터가 생성되거나 삭제됨
    - user / post / postID / title / time

## post
- 게시물(약속)을 볼 수 있고 등록할 수 있음
- `templates` - `post`에 게시물 관련 html로 구성
- 기능
    - 게시물 목록 보여주기
    - 게시물 작성하기
    - 게시물 자세히 보기
    - 모임에 참여하기
    - 모임에 탈퇴하기
    
#### 데이터베이스(models.py)
- Post 테이블
    - 게시물을 생성하거나 삭제하면 데이터가 생성되거나 삭제됨
    - author / title / time / type_meet / place / content / min_count / max-count / created_at / updated_at
    
## accounts
- 로그인, 로그아웃 구현
- 계정
    - studnet01
    - student02
    - student03
    