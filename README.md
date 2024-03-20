# SAKAK Backend Position Assignment - Apis

# 개요

해당 프로젝트는 SAKAK Backend Position Assignment - Apis에 대한 프로젝트입니다.

프로젝트는 Django를 이용해 구성되어 있으며, DB는 PostgreSQL을 사용합니다.

# 설치 및 실행 방법

## 1. 설치

프로젝트는 [poetry](https://python-poetry.org/docs/)를 사용하여 관리되고 있습니다.

dependency 설치

```bash
poetry install
```

## 2. 실행 방법

### 2.1. 로컬에서 실행 시

- 서버 실행

  poetry를 사용하여 실행

  ```bash
  poetry run python manage.py runserver
  ```

- 데이터 마이그레이션

  ```bash
  # 기본 마이그레이션
  poetry run python manage.py migrate

  # 초기 데이터 마이그레이션
  poetry run python manage.py task_migrate_data
  ```

- 테스트 실행

  ```bash
  poetry run pytest
  ```

### 2.2. Docker를 사용하여 실행 시

- Docker 이미지 빌드

  ```bash
  docker-compose up -d
  ```

- 데이터 마이그레이션

  - Docker 컨테이너에 접속

    ```bash
    docker-compose exec -it nutrient-api /bin/bash
    ```

  - 데이터 마이그레이션 실행

    ```bash
    # 기본 마이그레이션
    poetry run python3 manage.py migrate

    # 초기 데이터 마이그레이션
    poetry run python3 manage.py task_migrate_data
    ```