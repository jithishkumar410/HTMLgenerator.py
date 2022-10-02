import webbrowser as w
######################################################################################################
class Site:
    def __init__(self,fname):
        self.fname=fname
        self.comf=fname+".html"

        file=open(self.comf,'w+')

        file.write("""
        <!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<h1>Welcome html framework</h1>
</body>
</html>

""")
########################################################################################################
    def clean(self):
        self.file = open(self.comf, 'w+')
        self.file.write("")
######################################################################################################################
    def title(self,tname):
        self.tname=tname
        self.file = open(self.comf, 'w+')
        self.file.write(f"""
                                      <!doctype html>
                              <html lang="en">
                              <head>
                                  <meta charset="UTF-8">
                                  <meta name="viewport"
                                        content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                                  <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                  <title>{self.tname}</title>
                              </head>
                              <body>

                              </body>
                              </html>

                              """)

########################################################################################################################3
    def greet(self,nam):
        file = open(self.comf, 'a')
        file.write(f"<h1>Hello {nam}</h1>")
########################################################################################################
    def table(self):
        self.clean()
        self.row =""
        self.col =""
        self.coll=""

        self.a = int(input("Enter the number rows:"))
        self.b = int(input("Enter the number columns:"))
        for i in range(self.a):
           self.rowdata=input(f"Enter the row data {i+1}:")
           self.row=self.row+f'''<th class="row{i}" style="border:1px solid black;font-size:1.5rem">{self.rowdata}<th>\n'''
        for i in range(self.b):
            for i in range(self.b):
                self.columndata = input(f"Enter the column data {i+1}:")
                self.col = self.col + f''' <td class="col{i}{j}" style="border:1px solid black; color: red;font-size:1.5rem">{self.columndata}<td>\n'''
            self.coll = self.coll + f"<tr>{self.col}</tr>"
            self.col = ""

        self.table = f'''<table style="border:1px solid black;"><tr>{self.row}</tr><tr>{self.col}</tr></table>'''

        self.file = open(self.comf, 'a')

        self.file.write(f"""
                <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            
            <title>Document</title>
        </head>
        <body>
        {self.table}
        </body>
        </html>

        """)
#############################################################################################################################3
    def tablecb(self):
        self.clean()
        self.row = ""
        self.col = ""
        self.coll = ""

        self.a = int(input("Enter the number rows:"))
        self.b = int(input("Enter the number columns:"))
        for i in range(self.a):
            if i==0:
                self.rowdata = input(f"Enter the row data {i+1}:")
                self.row = self.row + f'''<th class="row{i}" style="border:1px solid black;font-size:1.5rem">{self.rowdata}<th>\n'''
            else:
                self.rowdata = input(f"Enter the row data {i+1}:")
                self.row = self.row+ f''' <td style="border:1px solid black;font-size:1.5rem">{self.rowdata}<td>\n'''
        for i in range(self.b):
            for j in range(self.b):
                if j == 0:
                    self.columndata = input(f"Enter the column data {i+1}:")
                    self.col = self.col + f'''<th class="col{i}{j}" style="border:1px solid black;font-size:1.5rem">{self.columndata}<th>\n'''
                else:
                    self.columndata = input(f"Enter the column data {i+1}:")
                    self.col = self.col + f''' <td class="col{i}{j}" style="border:1px solid black;font-size:1.5rem">{self.columndata}<td>\n'''
            self.coll = self.coll + f"<tr>{self.col}</tr>"
            self.col = ""



        if self.row != "" and self.coll != "":
            self.table = f'''<table style="border:1px solid black;"><tr>{self.row}</tr><tr>{self.coll}</tr></table>'''

        self.file = open(self.comf, 'a')

        self.file.write(f"""
                   <!doctype html>
           <html lang="en">
           <head>
               <meta charset="UTF-8">
               <meta name="viewport"
                     content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
               <meta http-equiv="X-UA-Compatible" content="ie=edge">

               <title>Document</title>
           </head>
           <body>
           {self.table}
           </body>
           </html>

           """)
################################################################################################################################
    def tablebh(self):
        self.clean()
        self.row = ""
        self.col = ""
        self.coll =""
        self.a = int(input("Enter the number rows:"))
        self.b = int(input("Enter the number columns:"))
        for i in range(self.a):
            self.rowdata = input(f"Enter the row data {i+1}:")
            self.row = self.row + f''' <th class="row{i}" style="border:1px solid black;font-size:1.5rem">{self.rowdata}<th>\n'''
        for i in range(self.b):
            for j in range(self.b):
                if  j==0:
                    self.columndata = input(f"Enter the column data {j+1}:")
                    self.col = self.col + f'''<th class="col{i}{j}" style="border:1px solid black;font-size:1.5rem">{self.columndata}<th>\n'''
                else:
                    self.columndata = input(f"Enter the column data {j+1}:")
                    self.col = self.col + f''' <td class="col{i}{j}" style="border:1px solid black;font-size:1.5rem">{self.columndata}<td>\n'''

            self.coll = self.coll + f"<tr>{self.col}</tr>"
            self.col = ""


        self.table = f'''<table style="border:1px solid black;"><tr>{self.row}</tr><tr>{self.coll}</tr></table>'''

        self.file = open(self.comf, 'a')

        self.file.write(f"""
                        <!doctype html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport"
                          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">

                    <title>Document</title>
                </head>
                <body>
                {self.table}
                </body>
                </html>

                """)
##################################################################################################################################
    def tablecbl(self):
        self.clean()
        self.row = ""
        self.col = ""
        self.coll=""
        self.a = int(input("Enter the number rows:"))
        self.b = int(input("Enter the number columns:"))
        for i in range(self.a+1):
            if i == 0:

                self.row = self.row + f''' <th class="row{i}" style="border:1px solid black;font-size:1.5rem"><th>\n'''
            else:
                self.rowdata = input(f"Enter the row head {i}:")
                self.row = self.row + f''' <th class="row{i}" style="border:1px solid black;font-size:1.5rem">{self.rowdata}<th>\n'''
        for i in range(self.b + 1):
            for j in range(self.b + 1):
                if j== 0:
                    self.columndata = input(f"Enter the column head:")
                    self.col = self.col + f'''<th class="col{i}{j}" style="border:1px solid black;font-size:1.5rem">{self.columndata}<th>\n'''
                else:
                    self.columndata = input(f"Enter the column data{i}:")
                    self.col = self.col + f''' <td class="col{i}{j}" style="border:1px solid black;font-size:1.5rem">{self.columndata}<td>\n'''
            self.coll = self.coll + f"<tr>{self.col}</tr>"
            self.col=""

        if self.row != "" and self.coll != "":
            self.table = f'''<table style="border:1px solid black;"><tr>{self.row}</tr><tr>{self.coll}</tr></table>'''

        self.file = open(self.comf, 'a')

        self.file.write(f"""
                                    <!doctype html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <meta name="viewport"
                                      content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                                <meta http-equiv="X-UA-Compatible" content="ie=edge">

                                <title>Document</title>
                            </head>
                            <body>
                            {self.table}
                            </body>
                            </html>

                            """)
################################################################################################################################

    def check(self):
        w.open(self.comf)
###################################################################################################################################
s=Site("fht")
s.tablebh()






s.check()



