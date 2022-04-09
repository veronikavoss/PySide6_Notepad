from PySide6.QtWidgets import *
from PySide6.QtGui import *
from notepad_ui import Ui_NotePad
import os

current_path=os.path.dirname(os.path.abspath(__file__))
image_path=os.path.join(current_path,'image')

class FindWindow(QDialog):
    def __init__(self,parent):
        QDialog.__init__(self,parent)
        self.show()
        
        self.parent_text=parent.plainTextEdit
        self.cursor=parent.plainTextEdit.textCursor()
        self.next_button.clicked.connect(self.set_next_button)
        self.cancel_button.clicked.connect(self.set_cancel_button)
    
    def keyReleaseEvent(self,event):
        print(self.line_edit.text())
        if self.line_edit.text():
            self.next_button.setEnabled(True)
        else:
            self.next_button.setEnabled(False)
    
    def set_cursor(self):
        print(self.cursor.selectionStart(),self.cursor.selectionEnd())
    
    def set_next_button(self):
        print('next')
    
    def set_cancel_button(self):
        self.close()

class File(QMainWindow,Ui_NotePad):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(os.path.join(image_path,'notepad_icon.png')))
        self.pte=self.plainTextEdit
        self.original_document=self.pte.toPlainText()
        self.path=None
        self.text_changed=False
        self.plainTextEdit.textChanged.connect(self.checking_modify_document)
        self.checking_modify_document()
        
        self.filter_option='텍스트 문서 (*.txt);;모든 파일 (*.*)'
    
    def checking_modify_document(self):
        if self.original_document!=self.pte.toPlainText():
            self.text_changed=True
            print('modify',self.text_changed)
        else:
            self.text_changed=False
            print('not_modify',self.text_changed)
        self.update_title()
    
    def update_title(self):
        if self.text_changed:
            self.setWindowTitle('*{} - 메모장'.format(os.path.basename(self.path) if self.path else '제목 없음'))
        else:
            self.setWindowTitle('{} - 메모장'.format(os.path.basename(self.path) if self.path else '제목 없음'))
    
    def run_new_file(self):
        if self.text_changed:
            self.save_question_messagebox()
            if self.get_messagebox_button==0:
                if not self.path:
                    self.run_save_as()
                else:
                    self.run_save()
            elif self.get_messagebox_button==1:
                self.set_new_file()
            elif self.get_messagebox_button==2:
                return
        self.set_new_file()
        self.update_title()
    
    def set_new_file(self):
        self.plainTextEdit.clear()
        self.original_document=self.pte.toPlainText()
        self.text_changed=False
        self.path=None
    
    def run_open_file(self):
        if self.text_changed:
            self.save_question_messagebox()
            if self.get_messagebox_button==0:
                if not self.path:
                    self.run_save_as()
                else:
                    self.run_save()
            elif self.get_messagebox_button==2:
                return
            self.set_open_file()
        else:
            self.set_open_file()
    
    def set_open_file(self):
        path,_=QFileDialog.getOpenFileName(self,'열기','',self.filter_option)
        if path:
            try:
                with open(path,'r',encoding='ansi') as r:
                    text=r.read()
                    self.original_document=text
                    r.close()
            except Exception as e:
                print(e)
            else:
                print(path)
                self.path=path
                self.pte.setPlainText(text)
    
    def save_question_messagebox(self):
        messagebox=QMessageBox()
        messagebox.setWindowTitle('메모장')
        messagebox.setText('변경 내용을 {}에 저장 하시겠습니까?'.format(os.path.basename(self.path) if self.path else '제목 없음'))
        messagebox.addButton('저장(S)',QMessageBox.YesRole)
        messagebox.addButton('저장 안 함(N)',QMessageBox.NoRole)
        messagebox.addButton('취소',QMessageBox.RejectRole)
        self.get_messagebox_button=messagebox.exec_()
    
    def run_save(self):
        if not self.path:
            self.run_save_as()
        else:
            try:
                with open(self.path,'w',encoding='ansi') as w:
                    w.write(self.pte.toPlainText())
                    w.close()
            except Exception as e:
                print(e)
            else:
                self.original_document=self.pte.toPlainText()
                self.checking_modify_document()
    
    def run_save_as(self):
        path,_=QFileDialog.getSaveFileName(self,'다른 이름으로 저장','',self.filter_option)
        document=self.pte.toPlainText()
        if not path:
            return
        else:
            try:
                with open(path,'w',encoding='ansi') as w:
                    w.write(document)
                    w.close()
            except Exception as e:
                print(e)
            else:
                self.path=path
                self.original_document=self.pte.toPlainText()
                self.checking_modify_document()
    
    def closeEvent(self, event):
        if self.text_changed:
            self.save_question_messagebox()
            if self.get_messagebox_button==0:
                if not self.path:
                    self.run_save_as()
                else:
                    self.run_save()
            elif self.get_messagebox_button==1:
                return
            elif self.get_messagebox_button==2:
                event.ignore()

class Edit(File):
    def run_del(self):
        QTextCursor.clearSelection(self.plainTextEdit)
    def run_find(self):
        FindWindow(self)
    # def run_next_find(self):
    #     self.plainTextEdit.()
    # def run_(self):
    #     self.plainTextEdit.()
    # def run_(self):
    #     self.plainTextEdit.()
    # def run_(self):
    #     self.plainTextEdit.()

