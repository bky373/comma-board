## ❛ Comma ❜ Board 소개

- **❛ Comma ❜**는 💻**Computer** **Engineering/Science**와 📐**Mathematics**의 합성어로, <u>컴퓨터 관련 지식과 수학</u>을 공부하는 사람들이(전공자가 아니더라도) 서로 정보를 공유할 수 있도록 만든 게시판입니다.
- 앞으로 어떻게 구현해나갈지는 아직 막막하지만.. 공부해가면서 부족한 부분들을 채워볼(?) 예정입니다.
- 우선, 웹 백엔드 과제 내용에 해당하는 API 구현은 모두 마쳤습니다. (중간에 수정사항이 있을지 모르지만.. 코드리뷰 해주시면 감사하겠습니다.)

### 개발 환경 준비

#### 1. 가상 환경 준비 ([참고](https://docs.python.org/ko/3/tutorial/venv.html))

- 아래 내용을 시작하기 전에, 터미널에서 (`clone or download`한) `comma_board` 디렉토리로 이동한다

- ```bash
  # 터미널에서 아래 명령어를 수행한다
  
  python -m venv venv  # 가상 환경 생성
  source [각자의 경로/comma_board]/venv/Scripts/activate  # 가상 환경 활성화
  (또는 cd [각자의 경로/comma_board]/venv/Scripts 입력 후 activate 입력)
  python -m pip install -r requirements.txt  # 필요한 모듈 설치
  ```

#### 2. 데이터베이스 접속 준비

- DB에 접속하기 위해 <u>설정파일</u>(`config.py`)의 `DB_URL 정보`를 `자신의 DB 정보`로 대체한다

- ```python
  # comma_board/config.py
  # user, pw, host, port, db 모두 자신의 DB 정보로 대체한다 
  
  DB_URL = 'mysql+pymysql://{user}:{pw}@{host}:{port}/{db}?charset=utf8'.format(
      user = mysecrets.dbuser,
      pw = mysecrets.dbpass,
      host = mysecrets.dbhost,
      port = mysecrets.dbport,
      db = mysecrets.dbname # 아래 내용 참고 
  )
  
  """
  추후 문제 없이 SQLAlchemy를 사용하려면 
  접속하려는 MySQL 서버에, 해당 이름의 db가 있어야 한다! 
  없다면, 터미널 또는 Workbench를 통해 db를 생성해준다
  (접속 및 생성 과정은 우선 이곳을 참조
  	-> https://dev.mysql.com/doc/refman/8.0/en/connecting-disconnecting.html)
  """
  ```

#### 3. 데이터베이스 초기화

- ```python
  flask db init  # 데이터베이스를 관리하는 초기 파일들이 담긴 migrations 디렉토리 생성
  flask db migrate  # 데이터베이스 모델 테이블 생성 및 변경(사실은 revision 파일이 생성됨)
  flask db upgrade  # 데이터베이스 갱신(위에서 생성된 revision 파일이 실행됨)
  ```

#### 4. 애플리케이션 설정 후 실행하기

- ```bash
  # 다시 터미널에서 
  # comma_board라는 이름의 최상위 패키지로 이동 후
  # 아래 명령어를 수행한다
  
  set FLASK_APP=comma_board  # FLASK_APP 환경 변수에 comma_board를 지정
  set FLASK_ENV=development  # 플라스크 실행 환경을 개발 환경으로 설정
  flask run  # 앱 실행하기
  ```

<br>

## API 소개

### User APIs: 

- 유저 SignUp / Login / Logout

1. **SignUp API** : *fullname*, *email*, *password* 을 입력받아 새로운 유저를 가입시킵니다.

2. **Login API** : *email*, *password* 를 입력받아 특정 유저로 로그인합니다.

3. **Logout API** : 현재 로그인 된 유저를 로그아웃합니다.

## 

### Board APIs:  

- 게시판 CRUD

1. **Create API** : *name* 을 입력받아 새로운 게시판을 만듭니다.
2. **Read API** : 현재 등록된 게시판 목록을 가져옵니다.
3. **Update API** : 기존 게시판의 *name* 을 변경합니다.
4. **Delete API** : 특정 게시판을 제거합니다.

## 

### BoardArticle APIs:  

- 게시판 글 CRUD

1. **Create API** : *title*, *content* 를 입력받아 특정 게시판에 새로운 글을 작성합니다.
2. **Read API** : 게시판의 글 목록을 가져오거나, 특정 게시판 글의 내용을 가져옵니다.
3. **Update API** : 게시판 글의 *title*, *content*를 변경합니다.
4. **Delete API** : 특정 게시판 글을 제거합니다.

## 

### Dashboard APIs

1. **RecentBoardArticle API** : 모든 게시판에 대해 각각의 게시판의 가장 최근 *n* 개의 게시판 글의 *title* 을 가져옵니다. (*k* 개의 게시판이 있다면 최대 *k \* n* 개의 게시판 글의 *title* 을 반환합니다.)



## 참고 자료

- [SQLAlchemy 모델 serialize하는 간단한 방법](https://www.kite.com/blog/python/flask-restful-api-tutorial/) 
- [API 에러를 JSON으로 반환하는 방법](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/#returning-api-errors-as-json)
- [Flask Tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/)
- [Jump To Flask](https://wikidocs.net/book/4542)
- [Flask-SQLAlchemy 사용시 json으로 데이터 가공하기](https://blog.naver.com/PostView.nhn?blogId=varkiry05&logNo=221485216965&categoryNo=107&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=search) (이 프로젝트에서는 사용 안 함)
- [SQLAlchemy Query를 Pandas DataFrame로 만들기](https://beomi.github.io/2017/10/21/SQLAlchemy-Query-to-Pandas-DataFrame/) (이 프로젝트에서는 사용 안 함)