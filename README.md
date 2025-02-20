# Terminal Stopwatch

터미널에서 실행되는 스톱워치 애플리케이션입니다. ASCII 아트를 활용한 큰 숫자 디스플레이와 랩 타임 기능을 제공합니다.

![Stopwatch Demo](stopwatch_final3.gif)

## 특징

- 큰 숫자로 시간 표시 (ASCII 아트)
- 랩 타임 기록 기능
- 키보드 단축키로 간편한 조작
- 시:분:초 형식의 시간 표시 (1시간 이상 시)
- 분:초 형식의 시간 표시 (1시간 미만 시)

## 설치 방법

Poetry를 사용한 설치:
```bash
poetry add terminal-stopwatch
```

Pip를 사용한 설치:
```bash
pip install terminal-stopwatch
```

## 사용 방법

### 패키지로 실행
```python
from terminal_stopwatch.main import main

main()
```

### 명령줄에서 실행
```bash
# Poetry 환경에서
poetry run python -m terminal_stopwatch

# 일반 Python 환경에서
python -m terminal_stopwatch
```

## 키 조작 방법

- `s` - 시작/일시정지
- `l` - 랩 타임 기록
- `r` - 초기화
- `q` - 종료
- `Ctrl+C` - 강제 종료

## 프로젝트 구조

```
terminal_stopwatch/
├── __init__.py        # 패키지 초기화
├── constants.py       # 상수 정의
├── models.py          # 데이터 모델 (TimeDisplay)
├── terminal.py        # 터미널 제어
├── input_handler.py   # 입력 처리
├── stopwatch.py       # 스톱워치 로직
└── main.py           # 메인 실행 파일
```

## 개발 환경 설정

1. 저장소 클론:
```bash
git clone https://github.com/taejun0622/stopwatch.git
cd stopwatch
```

2. Poetry 환경 설정:
```bash
poetry install
```

3. 개발 모드로 실행:
```bash
poetry run python run.py
```

## 의존성

- Python 3.11+
- colorama
- pyfiglet

## 라이선스

MIT License

## 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Author

- taejun (dugudugu0622@gmail.com)
- GitHub: [@taejun](https://github.com/taejun)

## Changelog

### [1.0.0] - 2024-02-20
- Initial Release
- Basic stopwatch functionality
- Published to PyPI 
