import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from dlipower import PowerSwitch
import time

Ui_MainWindow, QtBaseClass = uic.loadUiType("outlet.ui")

class OutletController(QMainWindow):

    switch = None
    
    def __init__(self):
        super(OutletController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.Login)
        self.ui.btnAllOff.clicked.connect(self.allOff)
        self.ui.btnAllOn.clicked.connect(self.allOn)
        self.ui.btnRefresh.clicked.connect(self.refreshAll)
        self.ui.btnCycle.clicked.connect(self.cycleAll)
        self.ui.outlet1.clicked.connect(self.outletToggle)
        self.ui.outlet2.clicked.connect(self.outletToggle)
        self.ui.outlet3.clicked.connect(self.outletToggle)
        self.ui.outlet4.clicked.connect(self.outletToggle)
        self.ui.outlet5.clicked.connect(self.outletToggle)
        self.ui.outlet6.clicked.connect(self.outletToggle)
        self.ui.outlet7.clicked.connect(self.outletToggle)
        self.ui.outlet8.clicked.connect(self.outletToggle)
        #self.ui.btnStartSelectedScript.clicked.connect(self.startScript)
        #self.ui.btnStopSelectedScript.clicked.connect(self.stopScript)
        self.ui.btnRefreshScripts.clicked.connect(self.refreshScripts)
        #self.ui.btnStopAllScripts.clicked.connect(self.stopAllScripts)        

    def Login(self):
        ipAddress = self.ui.txtIpAddress.text()
        strUsername = self.ui.txtUser.text()
        strPassword = self.ui.txtPassword.text()
        #TODO ERROR HANDLING 
        switch = PowerSwitch(hostname=ipAddress, userid=strUsername, password=strPassword)
        self.enableOutletButtons()
        self.refreshAll(self.switch)
        self.refreshScripts(self.switch)
        return

    def enableOutletButtons(self):
        self.ui.grpOutlets.setEnabled(True)
        self.ui.outlet1.setEnabled(True)
        self.ui.outlet2.setEnabled(True)
        self.ui.outlet3.setEnabled(True)
        self.ui.outlet4.setEnabled(True)
        self.ui.outlet5.setEnabled(True)
        self.ui.outlet6.setEnabled(True)
        self.ui.outlet7.setEnabled(True)
        self.ui.outlet8.setEnabled(True)
        self.ui.btnAllOff.setEnabled(True)
        self.ui.btnAllOn.setEnabled(True)
        self.ui.btnCycle.setEnabled(True)
        self.ui.btnRefresh.setEnabled(True)
        self.ui.grpScripts.setEnabled(True)
        self.ui.cbAllScripts.setEnabled(True)
        self.ui.cbRunningScripts.setEnabled(True)
        self.ui.label_4.setEnabled(True)
        self.ui.label_5.setEnabled(True)
        self.ui.btnStartSelectedScript.setEnabled(True)
        self.ui.btnStopSelectedScript.setEnabled(True)
        self.ui.btnRefreshScripts.setEnabled(True)
        self.ui.btnStopAllScripts.setEnabled(True)
        return
    
    def refreshAll(self, switch=None):

        if switch:
            switchStatus = switch.statuslist()
        else:
            switchStatus = self.switch.statuslist()
            
        self.ui.outlet1.setText(switchStatus[0][1])
        self.ui.outlet1.setStyleSheet("background-color: green" if switchStatus[0][2] =="ON" else "background-color: red")

        self.ui.outlet2.setText(switchStatus[1][1])
        self.ui.outlet2.setStyleSheet("background-color: green" if switchStatus[1][2] =="ON" else "background-color: red")

        self.ui.outlet3.setText(switchStatus[2][1])
        self.ui.outlet3.setStyleSheet("background-color: green" if switchStatus[2][2] =="ON" else "background-color: red")

        self.ui.outlet4.setText(switchStatus[3][1])
        self.ui.outlet4.setStyleSheet("background-color: green" if switchStatus[3][2] =="ON" else "background-color: red")

        self.ui.outlet5.setText(switchStatus[4][1])
        self.ui.outlet5.setStyleSheet("background-color: green" if switchStatus[4][2] =="ON" else "background-color: red")

        self.ui.outlet6.setText(switchStatus[5][1])
        self.ui.outlet6.setStyleSheet("background-color: green" if switchStatus[5][2] =="ON" else "background-color: red")

        self.ui.outlet7.setText(switchStatus[6][1])
        self.ui.outlet7.setStyleSheet("background-color: green" if switchStatus[6][2] =="ON" else "background-color: red")

        self.ui.outlet8.setText(switchStatus[7][1])
        self.ui.outlet8.setStyleSheet("background-color: green" if switchStatus[7][2] =="ON" else "background-color: red")
        return

    def allOff(self):
        for i in range(1,9):
            self.switch.off(i)
            time.sleep(1)
        self.refreshAll()
        return

    def allOn(self):
        for i in range(1,9):
            self.switch.on(i)
            time.sleep(1)
        self.refreshAll()
        return

    def cycleAll(self):
        for i in range(1,9):
            if self.switch.status(i) == "ON":
                self.switch.off(i)
            else:
                self.switch.on(i)
            time.sleep(1)    
        self.refreshAll()
        return            
    
    def outletToggle(self):
        outletNum = self.sender().objectName()[-1:]
        if self.switch.status(int(outletNum)) == "ON":
            self.switch.off(int(outletNum))
        else:
            self.switch.on(int(outletNum))    
        self.refreshAll()
        return

    def refreshScripts(self, switch=None):
            if switch:
                self.ui.cbAllScripts.addItems(switch.listScripts("all"))
                for scriptName,scriptId in switch.listScripts("running"):
                    self.ui.cbRunningScripts.addItem(scriptName,scriptId)
            else:
                self.ui.cbAllScripts.addItems(self.switch.listScripts("all"))
                for scriptName,scriptId in self.switch.listScripts("running"):
                    self.ui.cbRunningScripts.addItem(scriptName,scriptId)
            return
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OutletController()
    window.show()
    sys.exit(app.exec_())
