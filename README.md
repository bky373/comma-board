## 게시판 API 서버 만들기

#### 서버 실행하기

- 터미널에서 venv 설정을 마친 후 

  ```set FLASK_APP=com-ma-board
  set FLASK_APP=com-ma-board
  set FLASK_ENV=development
  flask init-db
  flask run
  ```

  위와 같이 명령어를 입력해줍니다.

#### 과제 설명

- `schema.sql`에 있는 스키마와 튜플을 이용해 MySQL DB를 만들었습니다.
- `__init__.py`에 있는 `blueprint`와 `api resource`를 통해 각각의 기능에 접근할 수 있습니다.
- 우선 `board`, `boardArticle`, `user` 까지는 기능 구현을 시도해보았고,  `dashboard`는 아직 하지 못했습니다.
- 앞으로 지속적으로 수정해나가려 합니다ㅠㅠ..!