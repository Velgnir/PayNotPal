from src.SETTINGS import CONFIGGER
from src.CommandLine import arguments
from src.SQLHANDLER import SQLHANDLER
class mind_controller:
    def __init__(self,argv):
        plan = arguments.parse(argv)

        confile = plan.get('-con',"config.ini")
        self.conf = CONFIGGER(confile)
        self.advanced = True
        self.SQLer = SQLHANDLER(self.conf.database)
        self.main()

    def main(self):
        show = ['s','sh','show','display','d','p','print']
        advanced = ['ct']
        ending = ["end","break"]

        while(True):
            deed = input("what's next?\n")
            if(deed in show):
                self.display_mode()
            elif(deed in advanced and self.advanced):
                if(deed == 'ct'):
                    self.advenced_create_table()
            elif (deed == "editing"):
                self.editing_mode()
            elif (deed in ending):
                break
            elif(deed == "help"):
                print("Ur loser")
            else:
                print("Unknown command")

        #print("process in run")
    def display(self):
        tables = self.SQLer.list_tables()[1:]
        length = max([len(x) for x in tables])+6+len(str(len(tables)))
        print("-"*length)
        for i,table in enumerate(tables):
            message = f"| {i+1}. {table}"
            print(message+" "*(length-len(message)-1)+"|")
        print("-"*length)
        return tables

    def display_mode(self):


        tables = self.display()

        next = int(input())-1

        try:
            self.SQLer.display_table(tables[next])
        except(Exception):
            pass
    def editing_mode(self):
        pass
    def advenced_create_table(self):
        name = input('Please, enter the name of the desired table:')
        vals = []
        print("Now, add column information")
        while(True):
            red = input()
            if(len(red)==0):
                break
            try:
                self.SQLer._validate_column_definition(red)
                vals.append(red)
            except:
                print("Incorrect Line, please fuck off")
        self.SQLer.create_table(name,vals)
    def find(self):
        pass
    def add_table(self):
        print("finna do some bullshit")
    def filter(self):
        pass
    def suggestions(self):
        print()

    def who_to_pay(self):
        print("PAY ME")
