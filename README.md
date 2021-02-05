## 게시판 API 서버 만들기

🔧 죄송하지만.. 전면적으로 리팩토링을 시도해보려 합니다...  <br>코드 리뷰를 해주신다면 너무 감사드리겠지만 변경 예정이라 <br>수고로움이 있으실 것 같습니다. 가능하다면 추후에 부탁을 드리고자 합니다..ㅠㅠ🔧



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
- 우선 `board`, `boardArticle`, `user` 까지는 수업자료를 토대로 기능 구현을 시도해보았고,  `dashboard`는 아직 하지 못했습니다.
- 앞으로 어떻게든 공부해서 꼭 기능을 완성하고 개선시켜보겠습니다!!!