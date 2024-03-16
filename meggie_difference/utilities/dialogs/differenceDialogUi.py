# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'differenceDialogUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_differenceDialog(object):
    def setupUi(self, differenceDialog):
        differenceDialog.setObjectName("differenceDialog")
        differenceDialog.resize(499, 635)
        self.gridLayout = QtWidgets.QGridLayout(differenceDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(differenceDialog)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 465, 630))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBoxDifference = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxDifference.setObjectName("groupBoxDifference")
        self.formLayout = QtWidgets.QFormLayout(self.groupBoxDifference)
        self.formLayout.setObjectName("formLayout")
        self.labelCondition1 = QtWidgets.QLabel(self.groupBoxDifference)
        self.labelCondition1.setObjectName("labelCondition1")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.labelCondition1
        )
        self.comboBoxCondition1 = QtWidgets.QComboBox(self.groupBoxDifference)
        self.comboBoxCondition1.setObjectName("comboBoxCondition1")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.comboBoxCondition1
        )
        self.labelCondition2 = QtWidgets.QLabel(self.groupBoxDifference)
        self.labelCondition2.setObjectName("labelCondition2")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.labelCondition2
        )
        self.comboBoxCondition2 = QtWidgets.QComboBox(self.groupBoxDifference)
        self.comboBoxCondition2.setObjectName("comboBoxCondition2")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.comboBoxCondition2
        )
        self.pushButtonAdd = QtWidgets.QPushButton(self.groupBoxDifference)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.SpanningRole, self.pushButtonAdd
        )
        self.listWidgetDifferences = QtWidgets.QListWidget(self.groupBoxDifference)
        self.listWidgetDifferences.setSelectionMode(
            QtWidgets.QAbstractItemView.NoSelection
        )
        self.listWidgetDifferences.setObjectName("listWidgetDifferences")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.SpanningRole, self.listWidgetDifferences
        )
        self.pushButtonClear = QtWidgets.QPushButton(self.groupBoxDifference)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.SpanningRole, self.pushButtonClear
        )
        self.gridLayout_2.addWidget(self.groupBoxDifference, 0, 0, 1, 1)
        self.groupBoxBatching = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxBatching.setObjectName("groupBoxBatching")
        self.gridLayoutBatching = QtWidgets.QGridLayout(self.groupBoxBatching)
        self.gridLayoutBatching.setObjectName("gridLayoutBatching")
        self.batchingWidgetPlaceholder = QtWidgets.QWidget(self.groupBoxBatching)
        self.batchingWidgetPlaceholder.setMinimumSize(QtCore.QSize(300, 300))
        self.batchingWidgetPlaceholder.setObjectName("batchingWidgetPlaceholder")
        self.gridLayoutBatching.addWidget(self.batchingWidgetPlaceholder, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBoxBatching, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancel = QtWidgets.QPushButton(differenceDialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.pushButtonBatch = QtWidgets.QPushButton(differenceDialog)
        self.pushButtonBatch.setObjectName("pushButtonBatch")
        self.horizontalLayout.addWidget(self.pushButtonBatch)
        self.pushButtonApply = QtWidgets.QPushButton(differenceDialog)
        self.pushButtonApply.setObjectName("pushButtonApply")
        self.horizontalLayout.addWidget(self.pushButtonApply)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(differenceDialog)
        self.pushButtonCancel.clicked.connect(differenceDialog.reject)  # type: ignore
        self.pushButtonApply.clicked.connect(differenceDialog.accept)  # type: ignore
        self.pushButtonBatch.clicked.connect(differenceDialog.acceptBatch)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(differenceDialog)

    def retranslateUi(self, differenceDialog):
        _translate = QtCore.QCoreApplication.translate
        differenceDialog.setWindowTitle(
            _translate("differenceDialog", "Meggie - Difference")
        )
        self.groupBoxDifference.setTitle(
            _translate("differenceDialog", "Condition selection:")
        )
        self.labelCondition1.setText(_translate("differenceDialog", "Condition 1:"))
        self.labelCondition2.setText(_translate("differenceDialog", "Condition 2"))
        self.pushButtonAdd.setText(_translate("differenceDialog", "Add"))
        self.pushButtonClear.setText(_translate("differenceDialog", "Clear"))
        self.groupBoxBatching.setTitle(_translate("differenceDialog", "Batching"))
        self.pushButtonCancel.setText(_translate("differenceDialog", "Cancel"))
        self.pushButtonBatch.setText(_translate("differenceDialog", "Batch"))
        self.pushButtonApply.setText(_translate("differenceDialog", "Apply"))
