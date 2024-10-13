# Static Method Real eg -- > Whatever is common is mark as static
# In this case, we do not need to inherit
# In Python we do not make classes static
class ExcelReader:

    @staticmethod
    def readexcelfile():
        print("Reading from Excel")
class MYSQLDBConnection:

    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")

class TC1:
    def runTC(self):
        ExcelReader.readexcelfile()

class TC2:
    def runTC2(self):
        MYSQLDBConnection.readMySQLFile()

tc1 = TC1()
tc1.runTC()
tc2 = TC2()
tc2.runTC2()


