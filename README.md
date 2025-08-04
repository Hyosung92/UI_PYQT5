# UI_PYQT5 repository
* PyQT5 설치
pip install pyqt5

* cairo 라이브러리가 설치되지 않은 경우
pip install pycairo
pip install cairosvg

* QT 디자이너에서 생성한 ui를 파이썬에서 load하는 방법
    (1) .ui 파일을 .py파일로 변환한 뒤 사용하기
        - 수정된 UI가 즉시 반영되진 않지만 배포에 적합
    (2) .ui 파일을 프로그램 runtime에 직접 로드하여 사용하기
        - ui 파일을 매번 실행 시 로드하므로 수정한 UI가 바로 반영되는 장점이 있지만, 배포에는 적합하지 않음