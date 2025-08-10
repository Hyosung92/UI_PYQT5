import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)

DATA_FILE = "data.json"  # 저장할 파일 이름

class DataTableApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Table Example")
        self.resize(600, 400)

        # 레이아웃
        layout = QVBoxLayout()

        # 표 위젯 생성
        self.table = QTableWidget(0, 3)  # 행:0, 열:3
        self.table.setHorizontalHeaderLabels(["Name", "ID", "Command"])
        layout.addWidget(self.table)

        # 입력창
        input_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("ID")
        self.command_input = QLineEdit()
        self.command_input.setPlaceholderText("Command")
        input_layout.addWidget(self.name_input)
        input_layout.addWidget(self.id_input)
        input_layout.addWidget(self.command_input)
        layout.addLayout(input_layout)

        # 버튼
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Add")
        remove_btn = QPushButton("Remove")
        save_btn = QPushButton("Save")
        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(remove_btn)
        btn_layout.addWidget(save_btn)
        layout.addLayout(btn_layout)

        # 버튼 이벤트 연결
        add_btn.clicked.connect(self.add_data)
        remove_btn.clicked.connect(self.remove_data)
        save_btn.clicked.connect(self.save_data)

        # 레이아웃 설정
        self.setLayout(layout)

        # 저장된 데이터 불러오기
        self.load_data()

    def add_data(self):
        """입력한 데이터 표에 추가"""
        name = self.name_input.text().strip()
        id_val = self.id_input.text().strip()
        cmd = self.command_input.text().strip()

        if not name or not id_val or not cmd:
            QMessageBox.warning(self, "입력 오류", "모든 필드를 입력하세요.")
            return

        row_pos = self.table.rowCount()
        self.table.insertRow(row_pos)
        self.table.setItem(row_pos, 0, QTableWidgetItem(name))
        self.table.setItem(row_pos, 1, QTableWidgetItem(id_val))
        self.table.setItem(row_pos, 2, QTableWidgetItem(cmd))

        # 입력창 초기화
        self.name_input.clear()
        self.id_input.clear()
        self.command_input.clear()

    def remove_data(self):
        """선택한 행 삭제"""
        selected = self.table.currentRow()
        if selected >= 0:
            self.table.removeRow(selected)
        else:
            QMessageBox.warning(self, "선택 오류", "삭제할 행을 선택하세요.")

    def save_data(self):
        """현재 표 데이터를 JSON으로 저장"""
        data_list = []
        for row in range(self.table.rowCount()):
            name = self.table.item(row, 0).text()
            id_val = self.table.item(row, 1).text()
            cmd = self.table.item(row, 2).text()
            data_list.append({"Name": name, "ID": id_val, "Command": cmd})

        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)

        QMessageBox.information(self, "저장 완료", f"{DATA_FILE}에 저장되었습니다.")

    def load_data(self):
        """JSON 파일에서 데이터 불러오기"""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                try:
                    data_list = json.load(f)
                    for item in data_list:
                        row_pos = self.table.rowCount()
                        self.table.insertRow(row_pos)
                        self.table.setItem(row_pos, 0, QTableWidgetItem(item["Name"]))
                        self.table.setItem(row_pos, 1, QTableWidgetItem(item["ID"]))
                        self.table.setItem(row_pos, 2, QTableWidgetItem(item["Command"]))
                except json.JSONDecodeError:
                    QMessageBox.warning(self, "로드 오류", "JSON 파일 형식이 잘못되었습니다.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = DataTableApp()
    win.show()
    sys.exit(app.exec_())