# Form implementation generated from reading ui file 'ankimorphs/ui/settings_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        SettingsDialog.resize(923, 497)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=SettingsDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.note_filters_tab = QtWidgets.QWidget()
        self.note_filters_tab.setObjectName("note_filters_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.note_filters_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.note_filters_table = QtWidgets.QTableWidget(parent=self.note_filters_tab)
        self.note_filters_table.setObjectName("note_filters_table")
        self.note_filters_table.setColumnCount(7)
        self.note_filters_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(6, item)
        self.verticalLayout_3.addWidget(self.note_filters_table)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.deleteRowPushButton = QtWidgets.QPushButton(parent=self.note_filters_tab)
        self.deleteRowPushButton.setObjectName("deleteRowPushButton")
        self.horizontalLayout_2.addWidget(self.deleteRowPushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.addNewRowPushButton = QtWidgets.QPushButton(parent=self.note_filters_tab)
        self.addNewRowPushButton.setObjectName("addNewRowPushButton")
        self.horizontalLayout_2.addWidget(self.addNewRowPushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.note_filters_tab, "")
        self.extra_fields_tab = QtWidgets.QWidget()
        self.extra_fields_tab.setObjectName("extra_fields_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.extra_fields_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(parent=self.extra_fields_tab)
        self.label.setStyleSheet("margin-bottom: 10px;")
        self.label.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.treeWidget = QtWidgets.QTreeWidget(parent=self.extra_fields_tab)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout_5.addWidget(self.treeWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.extra_fields_tab, "")
        self.tags_tab = QtWidgets.QWidget()
        self.tags_tab.setObjectName("tags_tab")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tags_tab)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(parent=self.tags_tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.tags_tab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(parent=self.tags_tab)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(parent=self.tags_tab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(parent=self.tags_tab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tagReadyLineEdit = QtWidgets.QLineEdit(parent=self.tags_tab)
        self.tagReadyLineEdit.setObjectName("tagReadyLineEdit")
        self.verticalLayout_7.addWidget(self.tagReadyLineEdit)
        self.tagNotReadyLineEdit = QtWidgets.QLineEdit(parent=self.tags_tab)
        self.tagNotReadyLineEdit.setObjectName("tagNotReadyLineEdit")
        self.verticalLayout_7.addWidget(self.tagNotReadyLineEdit)
        self.tagLearnCardNowLineEdit = QtWidgets.QLineEdit(parent=self.tags_tab)
        self.tagLearnCardNowLineEdit.setObjectName("tagLearnCardNowLineEdit")
        self.verticalLayout_7.addWidget(self.tagLearnCardNowLineEdit)
        self.tagKnownManuallyLineEdit = QtWidgets.QLineEdit(parent=self.tags_tab)
        self.tagKnownManuallyLineEdit.setObjectName("tagKnownManuallyLineEdit")
        self.verticalLayout_7.addWidget(self.tagKnownManuallyLineEdit)
        self.tagKnownAutomaticallyLineEdit = QtWidgets.QLineEdit(parent=self.tags_tab)
        self.tagKnownAutomaticallyLineEdit.setObjectName("tagKnownAutomaticallyLineEdit")
        self.verticalLayout_7.addWidget(self.tagKnownAutomaticallyLineEdit)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_10.addItem(spacerItem2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.restoreTagsPushButton = QtWidgets.QPushButton(parent=self.tags_tab)
        self.restoreTagsPushButton.setObjectName("restoreTagsPushButton")
        self.horizontalLayout_7.addWidget(self.restoreTagsPushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.verticalLayout_12.addLayout(self.verticalLayout_10)
        self.tabWidget.addTab(self.tags_tab, "")
        self.preprocess_tab = QtWidgets.QWidget()
        self.preprocess_tab.setObjectName("preprocess_tab")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.preprocess_tab)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.preprocessIgnoreSquareCheckBox = QtWidgets.QCheckBox(parent=self.preprocess_tab)
        self.preprocessIgnoreSquareCheckBox.setObjectName("preprocessIgnoreSquareCheckBox")
        self.verticalLayout_9.addWidget(self.preprocessIgnoreSquareCheckBox)
        self.preprocessIgnoreRoundCheckBox = QtWidgets.QCheckBox(parent=self.preprocess_tab)
        self.preprocessIgnoreRoundCheckBox.setObjectName("preprocessIgnoreRoundCheckBox")
        self.verticalLayout_9.addWidget(self.preprocessIgnoreRoundCheckBox)
        self.preprocessIgnoreSlimCheckBox = QtWidgets.QCheckBox(parent=self.preprocess_tab)
        self.preprocessIgnoreSlimCheckBox.setObjectName("preprocessIgnoreSlimCheckBox")
        self.verticalLayout_9.addWidget(self.preprocessIgnoreSlimCheckBox)
        self.preprocessIgnoreSuspendedCheckBox = QtWidgets.QCheckBox(parent=self.preprocess_tab)
        self.preprocessIgnoreSuspendedCheckBox.setObjectName("preprocessIgnoreSuspendedCheckBox")
        self.verticalLayout_9.addWidget(self.preprocessIgnoreSuspendedCheckBox)
        self.preprocessIgnoreNamesMizerCheckBox = QtWidgets.QCheckBox(parent=self.preprocess_tab)
        self.preprocessIgnoreNamesMizerCheckBox.setObjectName("preprocessIgnoreNamesMizerCheckBox")
        self.verticalLayout_9.addWidget(self.preprocessIgnoreNamesMizerCheckBox)
        self.preprocessIgnoreNamesFileCheckBox = QtWidgets.QCheckBox(parent=self.preprocess_tab)
        self.preprocessIgnoreNamesFileCheckBox.setObjectName("preprocessIgnoreNamesFileCheckBox")
        self.verticalLayout_9.addWidget(self.preprocessIgnoreNamesFileCheckBox)
        self.verticalLayout_13.addLayout(self.verticalLayout_9)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.restorePreprocessPushButton = QtWidgets.QPushButton(parent=self.preprocess_tab)
        self.restorePreprocessPushButton.setObjectName("restorePreprocessPushButton")
        self.horizontalLayout_8.addWidget(self.restorePreprocessPushButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout_13.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.preprocess_tab, "")
        self.skip_tab = QtWidgets.QWidget()
        self.skip_tab.setObjectName("skip_tab")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.skip_tab)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.skipKnownCheckBox = QtWidgets.QCheckBox(parent=self.skip_tab)
        self.skipKnownCheckBox.setObjectName("skipKnownCheckBox")
        self.verticalLayout_11.addWidget(self.skipKnownCheckBox)
        self.skipAlreadySeenCheckBox = QtWidgets.QCheckBox(parent=self.skip_tab)
        self.skipAlreadySeenCheckBox.setObjectName("skipAlreadySeenCheckBox")
        self.verticalLayout_11.addWidget(self.skipAlreadySeenCheckBox)
        self.skipNotificationsCheckBox = QtWidgets.QCheckBox(parent=self.skip_tab)
        self.skipNotificationsCheckBox.setObjectName("skipNotificationsCheckBox")
        self.verticalLayout_11.addWidget(self.skipNotificationsCheckBox)
        self.verticalLayout_20.addLayout(self.verticalLayout_11)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_20.addItem(spacerItem6)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.restoreSkipPushButton = QtWidgets.QPushButton(parent=self.skip_tab)
        self.restoreSkipPushButton.setObjectName("restoreSkipPushButton")
        self.horizontalLayout_11.addWidget(self.restoreSkipPushButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.verticalLayout_20.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.skip_tab, "")
        self.recalc_tab = QtWidgets.QWidget()
        self.recalc_tab.setObjectName("recalc_tab")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.recalc_tab)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.recalcBeforeSyncCheckBox = QtWidgets.QCheckBox(parent=self.recalc_tab)
        self.recalcBeforeSyncCheckBox.setObjectName("recalcBeforeSyncCheckBox")
        self.verticalLayout_21.addWidget(self.recalcBeforeSyncCheckBox)
        self.recalcReadKnownMorphsFolderCheckBox = QtWidgets.QCheckBox(parent=self.recalc_tab)
        self.recalcReadKnownMorphsFolderCheckBox.setObjectName("recalcReadKnownMorphsFolderCheckBox")
        self.verticalLayout_21.addWidget(self.recalcReadKnownMorphsFolderCheckBox)
        self.recalcSuspendKnownCheckBox = QtWidgets.QCheckBox(parent=self.recalc_tab)
        self.recalcSuspendKnownCheckBox.setObjectName("recalcSuspendKnownCheckBox")
        self.verticalLayout_21.addWidget(self.recalcSuspendKnownCheckBox)
        self.recalcMoveKnownNewCardsToTheEndCheckBox = QtWidgets.QCheckBox(parent=self.recalc_tab)
        self.recalcMoveKnownNewCardsToTheEndCheckBox.setObjectName("recalcMoveKnownNewCardsToTheEndCheckBox")
        self.verticalLayout_21.addWidget(self.recalcMoveKnownNewCardsToTheEndCheckBox)
        self.verticalLayout_17.addLayout(self.verticalLayout_21)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.shiftNewCardsCheckBox = QtWidgets.QCheckBox(parent=self.recalc_tab)
        self.shiftNewCardsCheckBox.setObjectName("shiftNewCardsCheckBox")
        self.horizontalLayout_13.addWidget(self.shiftNewCardsCheckBox)
        self.dueOffsetSpinBox = QtWidgets.QSpinBox(parent=self.recalc_tab)
        self.dueOffsetSpinBox.setMaximum(50000)
        self.dueOffsetSpinBox.setObjectName("dueOffsetSpinBox")
        self.horizontalLayout_13.addWidget(self.dueOffsetSpinBox)
        self.label_20 = QtWidgets.QLabel(parent=self.recalc_tab)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_13.addWidget(self.label_20)
        self.offsetFirstMorphsSpinBox = QtWidgets.QSpinBox(parent=self.recalc_tab)
        self.offsetFirstMorphsSpinBox.setMaximum(1000)
        self.offsetFirstMorphsSpinBox.setObjectName("offsetFirstMorphsSpinBox")
        self.horizontalLayout_13.addWidget(self.offsetFirstMorphsSpinBox)
        self.label_21 = QtWidgets.QLabel(parent=self.recalc_tab)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_13.addWidget(self.label_21)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem8)
        self.verticalLayout_17.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(3, 10, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_16 = QtWidgets.QLabel(parent=self.recalc_tab)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.recalcIntervalSpinBox = QtWidgets.QSpinBox(parent=self.recalc_tab)
        self.recalcIntervalSpinBox.setObjectName("recalcIntervalSpinBox")
        self.horizontalLayout_6.addWidget(self.recalcIntervalSpinBox)
        self.label_17 = QtWidgets.QLabel(parent=self.recalc_tab)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_6.addWidget(self.label_17)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_17.addLayout(self.horizontalLayout_6)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.toolbarStatsUseSeenRadioButton = QtWidgets.QRadioButton(parent=self.recalc_tab)
        self.toolbarStatsUseSeenRadioButton.setObjectName("toolbarStatsUseSeenRadioButton")
        self.recalcToolbarKnownRadioButtonGroup = QtWidgets.QButtonGroup(SettingsDialog)
        self.recalcToolbarKnownRadioButtonGroup.setObjectName("recalcToolbarKnownRadioButtonGroup")
        self.recalcToolbarKnownRadioButtonGroup.addButton(self.toolbarStatsUseSeenRadioButton)
        self.verticalLayout_14.addWidget(self.toolbarStatsUseSeenRadioButton)
        self.toolbarStatsUseKnownRadioButton = QtWidgets.QRadioButton(parent=self.recalc_tab)
        self.toolbarStatsUseKnownRadioButton.setObjectName("toolbarStatsUseKnownRadioButton")
        self.recalcToolbarKnownRadioButtonGroup.addButton(self.toolbarStatsUseKnownRadioButton)
        self.verticalLayout_14.addWidget(self.toolbarStatsUseKnownRadioButton)
        self.verticalLayout_17.addLayout(self.verticalLayout_14)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.unknownsFieldShowsInflectionsRadioButton = QtWidgets.QRadioButton(parent=self.recalc_tab)
        self.unknownsFieldShowsInflectionsRadioButton.setObjectName("unknownsFieldShowsInflectionsRadioButton")
        self.recalcUnknownFieldRadioButtonGroup = QtWidgets.QButtonGroup(SettingsDialog)
        self.recalcUnknownFieldRadioButtonGroup.setObjectName("recalcUnknownFieldRadioButtonGroup")
        self.recalcUnknownFieldRadioButtonGroup.addButton(self.unknownsFieldShowsInflectionsRadioButton)
        self.verticalLayout_22.addWidget(self.unknownsFieldShowsInflectionsRadioButton)
        self.unknownsFieldShowsLemmasRadioButton = QtWidgets.QRadioButton(parent=self.recalc_tab)
        self.unknownsFieldShowsLemmasRadioButton.setObjectName("unknownsFieldShowsLemmasRadioButton")
        self.recalcUnknownFieldRadioButtonGroup.addButton(self.unknownsFieldShowsLemmasRadioButton)
        self.verticalLayout_22.addWidget(self.unknownsFieldShowsLemmasRadioButton)
        self.verticalLayout_17.addLayout(self.verticalLayout_22)
        spacerItem10 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_17.addItem(spacerItem10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.restoreRecalcPushButton = QtWidgets.QPushButton(parent=self.recalc_tab)
        self.restoreRecalcPushButton.setObjectName("restoreRecalcPushButton")
        self.horizontalLayout_9.addWidget(self.restoreRecalcPushButton)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        self.verticalLayout_17.addLayout(self.horizontalLayout_9)
        self.verticalLayout_18.addLayout(self.verticalLayout_17)
        self.tabWidget.addTab(self.recalc_tab, "")
        self.shortcuts_tab = QtWidgets.QWidget()
        self.shortcuts_tab.setObjectName("shortcuts_tab")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.shortcuts_tab)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_14 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_16.addWidget(self.label_14)
        self.label_13 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_16.addWidget(self.label_13)
        self.label_10 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_16.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_16.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_16.addWidget(self.label_12)
        self.label_7 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_16.addWidget(self.label_7)
        self.label_15 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_16.addWidget(self.label_15)
        self.label_18 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_16.addWidget(self.label_18)
        self.horizontalLayout_5.addLayout(self.verticalLayout_16)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.shortcutRecalcKeySequenceEdit = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcutRecalcKeySequenceEdit.setObjectName("shortcutRecalcKeySequenceEdit")
        self.verticalLayout_15.addWidget(self.shortcutRecalcKeySequenceEdit)
        self.shortcutSettingsKeySequenceEdit = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcutSettingsKeySequenceEdit.setObjectName("shortcutSettingsKeySequenceEdit")
        self.verticalLayout_15.addWidget(self.shortcutSettingsKeySequenceEdit)
        self.shortcutKnownAndSkipKeySequenceEdit = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcutKnownAndSkipKeySequenceEdit.setObjectName("shortcutKnownAndSkipKeySequenceEdit")
        self.verticalLayout_15.addWidget(self.shortcutKnownAndSkipKeySequenceEdit)
        self.shortcutLearnNowKeySequenceEdit = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcutLearnNowKeySequenceEdit.setObjectName("shortcutLearnNowKeySequenceEdit")
        self.verticalLayout_15.addWidget(self.shortcutLearnNowKeySequenceEdit)
        self.shortcutViewMorphsKeySequenceEdit = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcutViewMorphsKeySequenceEdit.setObjectName("shortcutViewMorphsKeySequenceEdit")
        self.verticalLayout_15.addWidget(self.shortcutViewMorphsKeySequenceEdit)
        self.shortcutFrequencyFileGeneratorKeySequenceEdit = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcutFrequencyFileGeneratorKeySequenceEdit.setObjectName("shortcutFrequencyFileGeneratorKeySequenceEdit")
        self.verticalLayout_15.addWidget(self.shortcutFrequencyFileGeneratorKeySequenceEdit)
        self.shortcutReadabilityReportGeneratorKeySequenceEdit = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcutReadabilityReportGeneratorKeySequenceEdit.setObjectName("shortcutReadabilityReportGeneratorKeySequenceEdit")
        self.verticalLayout_15.addWidget(self.shortcutReadabilityReportGeneratorKeySequenceEdit)
        self.shortcutKnownMorphsExporterKeySequenceEdit = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcutKnownMorphsExporterKeySequenceEdit.setObjectName("shortcutKnownMorphsExporterKeySequenceEdit")
        self.verticalLayout_15.addWidget(self.shortcutKnownMorphsExporterKeySequenceEdit)
        self.horizontalLayout_5.addLayout(self.verticalLayout_15)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.verticalLayout_24.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_8 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_19.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_19.addWidget(self.label_9)
        self.label_19 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_19.addWidget(self.label_19)
        self.horizontalLayout_12.addLayout(self.verticalLayout_19)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.shortcutBrowseReadyKeySequenceEdit = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcutBrowseReadyKeySequenceEdit.setObjectName("shortcutBrowseReadyKeySequenceEdit")
        self.verticalLayout_23.addWidget(self.shortcutBrowseReadyKeySequenceEdit)
        self.shortcutBrowseAllKeySequenceEdit = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcutBrowseAllKeySequenceEdit.setObjectName("shortcutBrowseAllKeySequenceEdit")
        self.verticalLayout_23.addWidget(self.shortcutBrowseAllKeySequenceEdit)
        self.shortcutBrowseReadyLemmaKeySequenceEdit = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcutBrowseReadyLemmaKeySequenceEdit.setObjectName("shortcutBrowseReadyLemmaKeySequenceEdit")
        self.verticalLayout_23.addWidget(self.shortcutBrowseReadyLemmaKeySequenceEdit)
        self.horizontalLayout_12.addLayout(self.verticalLayout_23)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem13)
        self.verticalLayout_24.addLayout(self.horizontalLayout_12)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_24.addItem(spacerItem14)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.restoreShortcutsPushButton = QtWidgets.QPushButton(parent=self.shortcuts_tab)
        self.restoreShortcutsPushButton.setObjectName("restoreShortcutsPushButton")
        self.horizontalLayout_10.addWidget(self.restoreShortcutsPushButton)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem15)
        self.verticalLayout_24.addLayout(self.horizontalLayout_10)
        self.verticalLayout_25.addLayout(self.verticalLayout_24)
        self.tabWidget.addTab(self.shortcuts_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.restoreAllDefaultsPushButton = QtWidgets.QPushButton(parent=SettingsDialog)
        self.restoreAllDefaultsPushButton.setObjectName("restoreAllDefaultsPushButton")
        self.horizontalLayout.addWidget(self.restoreAllDefaultsPushButton)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem16)
        self.ankimorphs_version_label = QtWidgets.QLabel(parent=SettingsDialog)
        self.ankimorphs_version_label.setObjectName("ankimorphs_version_label")
        self.horizontalLayout.addWidget(self.ankimorphs_version_label)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem17)
        self.cancelPushButton = QtWidgets.QPushButton(parent=SettingsDialog)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        self.savePushButton = QtWidgets.QPushButton(parent=SettingsDialog)
        self.savePushButton.setObjectName("savePushButton")
        self.horizontalLayout.addWidget(self.savePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "AnkiMorph Settings"))
        item = self.note_filters_table.horizontalHeaderItem(0)
        item.setText(_translate("SettingsDialog", "Note Type"))
        item = self.note_filters_table.horizontalHeaderItem(1)
        item.setText(_translate("SettingsDialog", "Tags"))
        item = self.note_filters_table.horizontalHeaderItem(2)
        item.setText(_translate("SettingsDialog", "Field"))
        item = self.note_filters_table.horizontalHeaderItem(3)
        item.setText(_translate("SettingsDialog", "Morphemizer"))
        item = self.note_filters_table.horizontalHeaderItem(4)
        item.setText(_translate("SettingsDialog", "Morph Priority"))
        item = self.note_filters_table.horizontalHeaderItem(5)
        item.setText(_translate("SettingsDialog", "Read"))
        item = self.note_filters_table.horizontalHeaderItem(6)
        item.setText(_translate("SettingsDialog", "Modify"))
        self.deleteRowPushButton.setText(_translate("SettingsDialog", "Delete Selected Row"))
        self.addNewRowPushButton.setText(_translate("SettingsDialog", "Add New Row"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.note_filters_tab), _translate("SettingsDialog", "Note Filters"))
        self.label.setText(_translate("SettingsDialog", "<html><head/><body><p>AnkiMorphs can automatically add special fields to your cards and populate them.</p><p>Read the <a href=\"https://mortii.github.io/anki-morphs/user_guide/setup/settings/extra-fields.html\"><span style=\" text-decoration: underline; color:#8783ff;\">guide</span></a> for more info.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.extra_fields_tab), _translate("SettingsDialog", "Extra Fields"))
        self.label_2.setText(_translate("SettingsDialog", "One unknown morph"))
        self.label_3.setText(_translate("SettingsDialog", "Multiple unknown morphs"))
        self.label_6.setText(_translate("SettingsDialog", "Learn card now"))
        self.label_5.setText(_translate("SettingsDialog", "Set known and skip"))
        self.label_4.setText(_translate("SettingsDialog", "All morphs known"))
        self.restoreTagsPushButton.setText(_translate("SettingsDialog", "Restore Default Tags Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tags_tab), _translate("SettingsDialog", "Tags"))
        self.preprocessIgnoreSquareCheckBox.setText(_translate("SettingsDialog", "ignore content in square brackets []"))
        self.preprocessIgnoreRoundCheckBox.setText(_translate("SettingsDialog", "ignore content in round brackets（）"))
        self.preprocessIgnoreSlimCheckBox.setText(_translate("SettingsDialog", "ignore content in slim round brackets ()"))
        self.preprocessIgnoreSuspendedCheckBox.setText(_translate("SettingsDialog", "Ignore content in suspended cards"))
        self.preprocessIgnoreNamesMizerCheckBox.setText(_translate("SettingsDialog", "Ignore names found by the morphemizer"))
        self.preprocessIgnoreNamesFileCheckBox.setText(_translate("SettingsDialog", "Ignore names found in names.txt"))
        self.restorePreprocessPushButton.setText(_translate("SettingsDialog", "Restore Default Preprocess Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.preprocess_tab), _translate("SettingsDialog", "Preprocess"))
        self.skipKnownCheckBox.setText(_translate("SettingsDialog", "Skip cards with only known morphs"))
        self.skipAlreadySeenCheckBox.setText(_translate("SettingsDialog", "Skip cards that have unknown morphs already seen today"))
        self.skipNotificationsCheckBox.setText(_translate("SettingsDialog", "Show \"skipped x cards\" notifications"))
        self.restoreSkipPushButton.setText(_translate("SettingsDialog", "Restore Default Skip Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.skip_tab), _translate("SettingsDialog", "Skip"))
        self.recalcBeforeSyncCheckBox.setText(_translate("SettingsDialog", "Automatically Recalc before Anki sync"))
        self.recalcReadKnownMorphsFolderCheckBox.setText(_translate("SettingsDialog", "Read files in \'known-morphs\' folder and register morphs as known"))
        self.recalcSuspendKnownCheckBox.setText(_translate("SettingsDialog", "Suspend new cards with only known morphs"))
        self.recalcMoveKnownNewCardsToTheEndCheckBox.setText(_translate("SettingsDialog", "Move new cards that only have known morphs to the end of the due queue"))
        self.shiftNewCardsCheckBox.setText(_translate("SettingsDialog", "Shift new cards that are not the first to have the unknown morph, by"))
        self.label_20.setText(_translate("SettingsDialog", "due, for the first"))
        self.label_21.setText(_translate("SettingsDialog", "morphs"))
        self.label_16.setText(_translate("SettingsDialog", "Morphs are considered known when they have a learning interval of"))
        self.label_17.setText(_translate("SettingsDialog", "days or more"))
        self.toolbarStatsUseSeenRadioButton.setText(_translate("SettingsDialog", "U and A shows seen morphs (reviewed at least once)"))
        self.toolbarStatsUseKnownRadioButton.setText(_translate("SettingsDialog", "U and A shows known morphs (specified above)"))
        self.unknownsFieldShowsInflectionsRadioButton.setText(_translate("SettingsDialog", "am-unknowns field shows morph inflections"))
        self.unknownsFieldShowsLemmasRadioButton.setText(_translate("SettingsDialog", "am-unknowns field shows morph lemmas"))
        self.restoreRecalcPushButton.setText(_translate("SettingsDialog", "Restore Default Recalc Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recalc_tab), _translate("SettingsDialog", "Recalc"))
        self.label_14.setText(_translate("SettingsDialog", "Run recalc"))
        self.label_13.setText(_translate("SettingsDialog", "Open settings"))
        self.label_10.setText(_translate("SettingsDialog", "Set card as known and skip"))
        self.label_11.setText(_translate("SettingsDialog", "Learn card now"))
        self.label_12.setText(_translate("SettingsDialog", "View card morphemes"))
        self.label_7.setText(_translate("SettingsDialog", "Frequency File Generator"))
        self.label_15.setText(_translate("SettingsDialog", "Readability Report Generator"))
        self.label_18.setText(_translate("SettingsDialog", "Known Morphs Exporter"))
        self.label_8.setText(_translate("SettingsDialog", "Browse ready cards with same unknown morph (inflection)"))
        self.label_9.setText(_translate("SettingsDialog", "Browse all cards with same unknown morph (inflection)"))
        self.label_19.setText(_translate("SettingsDialog", "Browse ready cards with the same unknown morph (lemma)"))
        self.restoreShortcutsPushButton.setText(_translate("SettingsDialog", "Restore Default Shortcut Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shortcuts_tab), _translate("SettingsDialog", "Shortcuts"))
        self.restoreAllDefaultsPushButton.setText(_translate("SettingsDialog", "Restore All Default Settings"))
        self.ankimorphs_version_label.setText(_translate("SettingsDialog", "AnkiMorphs version: x"))
        self.cancelPushButton.setText(_translate("SettingsDialog", " Cancel"))
        self.savePushButton.setText(_translate("SettingsDialog", " Save"))
