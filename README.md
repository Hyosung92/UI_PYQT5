# UI_PYQT5 repository
* PyQT5 설치 & 제거
    - pip install pyqt5
    - pip uninstall pyqt5

* PySide6 설치 & 제거
    - pip install PySide6
    - pip uninstall PySide6

* QT 디자이너에서 생성한 ui를 파이썬에서 load하는 방법
    (1) .ui 파일을 .py파일로 변환한 뒤 사용하기
        - 수정된 UI가 즉시 반영되진 않지만 배포에 적합
    (2) .ui 파일을 프로그램 runtime에 직접 로드하여 사용하기
        - ui 파일을 매번 실행 시 로드하므로 수정한 UI가 바로 반영되는 장점이 있지만, 배포에는 적합하지 않음

* 명령어를 통한 리소스(.qrc) 파일 → 파이썬(.py) 파일 변환 방법
    (1) PyQt5
        a. pyrcc5 실행이 가능한 경우
            - pyrcc5.exe .\file.qrc -o .\file.py
        b. pyrcc5 실행이 불가능한 경우
            - python -m PyQt5.pyrcc_main qrc파일명 -o 파이썬파일명_rc.py (파이썬의 Python Debug Console 창에서 qrc 파일이 위치한 경로까지 이동 후)
    (2) PySide6
        - pyside6-uic ui_name.ui -o ui_name.py
    

* 명령어를 통한 .ui 파일 → .py 파일 변환 방법
    (1) PyQt5
        - pyuic5.exe .\file.ui -o .\file.py
