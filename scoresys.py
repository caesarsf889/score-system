# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:38:23 2020

@author: caesa
"""

import sys  
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMainWindow, QApplication,QWidget, QRadioButton,QWidget,QCheckBox,QInputDialog,QLineEdit, QPushButton, QMessageBox
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import ( QLabel, QHBoxLayout)
from PyQt5.QtGui import QPainter,QPixmap,QIcon
from PyQt5.QtWidgets import QAction

Ui_MainWindow, QtBaseClass = uic.loadUiType("scoresys.ui")



score_list = list()





class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        
        
        
        self.ui.add_btn.clicked.connect(self.add_member)
        self.ui.cal_btn.clicked.connect(self.cal_standard)
        
        
        exit = QAction(QIcon("icons/Blue_Flower.icon"),"Exit",self )
        exit.setShortcut("Ctrl+Q")
        exit.triggered.connect(self.close)
        self.statusBar()
        
        menubar = self.menuBar()
        file = menubar.addMenu("&File")
        file.addAction(exit)
        
    
    
    
    
    def paintEvent(self,event):
        painter = QPainter(self)
        pixmap = QPixmap("wjsn.jpg")
        painter.drawPixmap(self.rect(),pixmap)
       
        



    def cal_standard(self):
        
        self.ui.show_box_2.clear()
        
        score_sort = sorted(score_list, key = lambda s:float(s[1]) , reverse = True)

        frontend_sum = 0
        backend_sum = 0


        for i in range(int(len(score_sort) / 2 )):
            
            frontend_sum = float(score_sort[i][1]) + frontend_sum
            print(score_sort[i][1])
            print("DI" + str(i)) 
            
        print(frontend_sum)
        frontend_mean = frontend_sum / (len(score_sort)/2)
        frontend_result = "The front-end standard is " +  str(frontend_mean)
        self.ui.show_box_2.append(frontend_result)
        
        
        for i in range(int(len(score_sort) / 2 )  , int(len(score_sort)) ):
            
            backend_sum = float(score_sort[i][1]) + backend_sum
            print(score_sort[i][1])
            print("DI" + str(i)) 
        print(backend_sum)
        backend_mean = backend_sum / (len(score_sort)/2)
        backend_result = "The back-end standard is " +  str(backend_mean)
        self.ui.show_box_2.append(backend_result)
            
       
        
        
        
        
        
        #for i in range(len(score_sort)):
            
           # show_each = "Number  " +  str(score_list[i][0]) + "grade =  "  + str(score_list[i][1]) 
            #self.ui.show_box.append(show_each)
           
       
    
        
        
    
        
    def add_member(self):
        
        empty = ""
        
        add_member = str(self.ui.Number.toPlainText())
        add_score =  str(self.ui.Score.toPlainText())
        
        
        
        if(empty != add_member and empty !=add_score):
            
            add_member = float(add_member)
            add_score = float(add_score)
            
            
            
            self.ui.Score.setStyleSheet("background-color: rgb(255,255,255)")
            
            has_been_defined = False
        
        
            for i in range(len(score_list)):
            
                if (score_list[i][0] == add_member):
                    self.ui.Number.setStyleSheet("background-color: rgb(255,179,179)")
                    has_been_defined = True
                    pass
        
                else:
                    pass
                
                
            
            if(not(has_been_defined)):
                self.ui.Number.setStyleSheet("background-color: rgb(255,255,255)")
                    
                    
                    
                score_list.insert(0,[])
                score_list[0].insert(0,add_member)
                score_list[0].insert(1,add_score)
                        
                box_show = " Number  " +  str(score_list[0][0]) + "  grade =  "  + str(score_list[0][1]) 
                        
                #self.ui.show_box.insertPlainText(box_show)
                self.ui.show_box.append(box_show)
                self.ui.member_box.setText("Member :  " + str(len(score_list)))
                self.ui.Number.clear()
                self.ui.Score.clear()
            
            
        else:
            
            if(empty == add_member):
                
                self.ui.Number.setStyleSheet("background-color: rgb(255,179,179)")
            elif(empty != add_member):
                
                self.ui.Number.setStyleSheet("background-color: rgb(255,255,255)")
                pass
            
            
            if(empty == add_score):
                self.ui.Score.setStyleSheet("background-color: rgb(255,179,179)")
            
            elif(empty == add_score):
                self.ui.Score.setStyleSheet("background-color: rgb(255,255,255)")
                
                pass
        
        
        
        
        
        
       
        
        
        
            
       # else:
            
        #        add_score = float(self.ui.Score.toPlainText())
        
        
        
        
        
        
        
        
        
       

        
    
         
    
        
        
        
    
   
    
    
    

    
        
    
    
    
    
          
       # if a ==1 and b==1 and c==1:
           
            #sum_score = float(guo_wen) + float(ying_wen) +float(shu_xue)
            #average_score = sum_score / 3 
            #result_str = "SUM = "+ str(sum_score) +  "   " + "Average Score = "+ str(average_score)
            #msg = QMessageBox()
            #msg.setWindowTitle("score_result")
            #msg.setIcon(QMessageBox.Information)
            #msg.setText("SUN AND Average Score:" +  result_str)
            #msg.setDetailedText(result_str)
            #x = msg.exec_()
                
            
    
            
            
            
        #QMessageBox.about(self, "Title", "SUN AND Average Score:" )
        #QMessageBox.about(self, str(sum_score),str(average_score)
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())



