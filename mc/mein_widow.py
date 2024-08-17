
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

app = QApplication([])

mein_window_ = QWidget()


rbutton1 = QRadioButton()
rbutton2 = QRadioButton()
rbutton3 = QRadioButton()
rbutton4 = QRadioButton()

minutes = QLabel()
answer = QLabel()

menu_button =  QPushButton()
rest_button =  QPushButton()
answer_button =  QPushButton()

box_minutes = QSpinBox()

radioGroup = QButtonGroup()

radioGroup.addButton(rbutton1)
radioGroup.addButton(rbutton2)
radioGroup.addButton(rbutton3)
radioGroup.addButton(rbutton4)

radioGroupBox = QGroupBox("вапріанти відповідей")

hloyout1 = QHBoxLayout()
hloyout2 = QHBoxLayout()
hloyout3 = QHBoxLayout()
hloyout4 = QHBoxLayout()

vloyout1  = QVBoxLayout()
vloyout2  = QVBoxLayout()


hloyout1.addWidget(menu_button)
hloyout1.addWidget(rest_button)
hloyout1.addWidget(box_minutes)
hloyout1.addWidget(minutes)

hloyout2.addWidget(answer, alignment = Qt.AlignLeft)

hloyout3.addLayout(vloyout1)
hloyout3.addLayout(vloyout2)

vloyout1  = QVBoxLayout()
vloyout2  = QVBoxLayout()


vloyout1.addWidget(rbutton1)
vloyout1.addWidget(rbutton2)

vloyout2.addWidget(rbutton3)
vloyout2.addWidget(rbutton4)

hbuttonlayour = QHBoxLayout()

hbuttonlayour.addLayout(vloyout1)
hbuttonlayour.addLayout(vloyout2)

hloyout4.addWidget(answer_button)

radioGroupBox.setLayout(hbuttonlayour)

hloyout3.addWidget(radioGroupBox)

mein_layout = QVBoxLayout()

mein_layout.addLayout(hloyout1)
mein_layout.addLayout(hloyout2)
mein_layout.addLayout(hloyout3)
mein_layout.addLayout(hloyout4)

mein_window_.setLayout(mein_layout)

mein_window_.show()
app.exec_()






















