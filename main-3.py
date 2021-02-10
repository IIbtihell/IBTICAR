from PyQt5 import QtWidgets,uic

def main3():
    app.quit()

def main2():
    call9.show()


def main1():
    call1.show()
def main4():
    call9.show()
def main4():
    call9.show() 
def main5():
    np=call9.q1.text()
    email=call9.q2.text()
    tel=call9.q3.text()


    a1=call9.choix.currentText()
    quantiter=call9.spinBox.value()

    
    i=0
    S=0
    call6.show()
    if a1=="TESLA":
        i+=0
 
        call6.prod.setItem(i,0, QtWidgets.QTableWidgetItem("TESLA"))

        call6.prixuni.setItem(i,0, QtWidgets.QTableWidgetItem("11890DT"))

        call6.quan.setItem(i,0, QtWidgets.QTableWidgetItem(str(quantiter)))
        t1=int(quantiter)*11890
        S=S+t1

        call6.tableWidget_7.setItem(i,0, QtWidgets.QTableWidgetItem(str(t1)))

        f=open("valid.txt","a")

        f.write("\n")
        f.write("        article :      Voiture")
        f.write("\n")
        f.write("        prix unitaire : 11890DT")
        f.write("\n")
        f.write("        quantiter :"+a1)
        f.write("\n")
        f.write("        prix totale :"+str(t1))

        f.write("\n")
        f.close()
    if a1=="Nissan":
        i+=0
        call6.prixuni.insertRow(i)
        call6.prod.insertRow(i)

        call6.quan.insertRow(i)
        call6.tableWidget_7.insertRow(i)
        call6.prod.setItem(i,0, QtWidgets.QTableWidgetItem("Nissan"))

        call6.prixuni.setItem(i,0, QtWidgets.QTableWidgetItem("27608DT"))

        call6.quan.setItem(i,0, QtWidgets.QTableWidgetItem(str(quantiter)))
        t2=int(quantiter)*27608
        S=S+t2

        call6.tableWidget_7.setItem(i,0, QtWidgets.QTableWidgetItem(str(t2)))

        f=open("valid.txt","a")

        f.write("\n")
        f.write("        article :      Voiture")
        f.write("\n")
        f.write("        prix unitaire : 1189DT")
        f.write("\n")
        f.write("        quantiter :"+a1)
        f.write("\n")
        f.write("        prix totale :"+str(t2))

        f.write("\n")
        f.close()
    if a1=="BMW":
        i+=0
        call6.prixuni.insertRow(i)
        call6.prod.insertRow(i)

        call6.quan.insertRow(i)
        call6.tableWidget_7.insertRow(i)
        call6.prod.setItem(i,0, QtWidgets.QTableWidgetItem("BMW"))

        call6.prixuni.setItem(i,0, QtWidgets.QTableWidgetItem("12890DT"))

        call6.quan.setItem(i,0, QtWidgets.QTableWidgetItem(str(quantiter)))
        t3=int(quantiter)*12890
        S=S+t3

        call6.tableWidget_7.setItem(i,0, QtWidgets.QTableWidgetItem(str(t3)))

        f=open("valid.txt","a")

        f.write("\n")
        f.write("        article :      Voiture")
        f.write("\n")
        f.write("        prix unitaire : 1189DT")
        f.write("\n")
        f.write("        quantiter :"+a1)
        f.write("\n")
        f.write("        prix totale :"+str(t3))

        f.write("\n")
        f.close()
    if a1=="Chevrelot":
        i+=0
        call6.prixuni.insertRow(i)
        call6.prod.insertRow(i)

        call6.quan.insertRow(i)
        call6.tableWidget_7.insertRow(i)
        call6.prod.setItem(i,0, QtWidgets.QTableWidgetItem("Chevrelot"))

        call6.prixuni.setItem(i,0, QtWidgets.QTableWidgetItem("65470DT"))

        call6.quan.setItem(i,0, QtWidgets.QTableWidgetItem(str(quantiter)))
        t4=int(quantiter)*64370
        S=S+t4

        call6.tableWidget_7.setItem(i,0, QtWidgets.QTableWidgetItem(str(t4)))

        f=open("valid.txt","a")

        f.write("\n")
        f.write("        article :      Voiture")
        f.write("\n")
        f.write("        prix unitaire : 1189DT")
        f.write("\n")
        f.write("        quantiter :"+a1)
        f.write("\n")
        f.write("        prix totale :"+str(t4))

        f.write("\n")
        f.close()
    if a1=="Honda":
        i+=0
        call6.prixuni.insertRow(i)
        call6.prod.insertRow(i)

        call6.quan.insertRow(i)
        call6.tableWidget_7.insertRow(i)
        call6.prod.setItem(i,0, QtWidgets.QTableWidgetItem("Honda"))

        call6.prixuni.setItem(i,0, QtWidgets.QTableWidgetItem("36740DT"))

        call6.quan.setItem(i,0, QtWidgets.QTableWidgetItem(str(quantiter)))
        t5=int(quantiter)*36740
        S=S+t5

        call6.tableWidget_7.setItem(i,0, QtWidgets.QTableWidgetItem(str(t5)))

        f=open("valid.txt","a")

        f.write("\n")
        f.write("        article :      Voiture")
        f.write("\n")
        f.write("        prix unitaire : 1189DT")
        f.write("\n")
        f.write("        quantiter :"+a1)
        f.write("\n")
        f.write("        prix totale :"+str(t5))

        f.write("\n")
        f.close()
    if a1=="Kia":
        i+=0
        call6.prixuni.insertRow(i)
        call6.prod.insertRow(i)

        call6.quan.insertRow(i)
        call6.tableWidget_7.insertRow(i)
        call6.prod.setItem(i,0, QtWidgets.QTableWidgetItem("Kia"))

        call6.prixuni.setItem(i,0, QtWidgets.QTableWidgetItem("17889DT"))

        call6.quan.setItem(i,0, QtWidgets.QTableWidgetItem(str(quantiter)))
        t7=int(quantiter)*17889
        S=S+t7

        call6.tableWidget_7.setItem(i,0, QtWidgets.QTableWidgetItem(str(t7)))

        f=open("valid.txt","a")

        f.write("\n")
        f.write("        article :      Voiture")
        f.write("\n")
        f.write("        prix unitaire : 1189DT")
        f.write("\n")
        f.write("        quantiter :"+a1)
        f.write("\n")
        f.write("        prix totale :"+str(t7))

        f.write("\n")
        f.close()
    if a1=="Audi":
        i+=0
        call6.prixuni.insertRow(i)
        call6.prod.insertRow(i)

        call6.quan.insertRow(i)
        call6.tableWidget_7.insertRow(i)
        call6.prod.setItem(i,0, QtWidgets.QTableWidgetItem("Audi"))

        call6.prixuni.setItem(i,0, QtWidgets.QTableWidgetItem("85964DT"))

        call6.quan.setItem(i,0, QtWidgets.QTableWidgetItem(str(quantiter)))
        t8=int(quantiter)*85964
        S=S+t8

        call6.tableWidget_7.setItem(i,0, QtWidgets.QTableWidgetItem(str(t8)))

        f=open("valid.txt","a")

        f.write("\n")
        f.write("        article :      Voiture")
        f.write("\n")
        f.write("        prix unitaire : 1189DT")
        f.write("\n")
        f.write("        quantiter :"+a1)
        f.write("\n")
        f.write("        prix totale :"+str(t8))

        f.write("\n")
        f.close()
    if a1=="Fiat":
        i+=0
        call6.prixuni.insertRow(i)
        call6.prod.insertRow(i)

        call6.quan.insertRow(i)
        call6.tableWidget_7.insertRow(i)
        call6.prod.setItem(i,0, QtWidgets.QTableWidgetItem("Fiat"))

        call6.prixuni.setItem(i,0, QtWidgets.QTableWidgetItem("78049DT"))

        call6.quan.setItem(i,0, QtWidgets.QTableWidgetItem(str(quantiter)))
        t9=int(quantiter)*78049
        S=S+t9

        call6.tableWidget_7.setItem(i,0, QtWidgets.QTableWidgetItem(str(t9)))

        f=open("valid.txt","a")

        f.write("\n")
        f.write("        article :      Voiture")
        f.write("\n")
        f.write("        prix unitaire : 1189DT")
        f.write("\n")
        f.write("        quantiter :"+a1)
        f.write("\n")
        f.write("        prix totale :"+str(t9))

        f.write("\n")
        f.close()
    if a1=="Toyota":
        i+=0
        call6.prixuni.insertRow(i)
        call6.prod.insertRow(i)

        call6.quan.insertRow(i)
        call6.tableWidget_7.insertRow(i)
        call6.prod.setItem(i,0, QtWidgets.QTableWidgetItem("Toyota"))

        call6.prixuni.setItem(i,0, QtWidgets.QTableWidgetItem("46578DT"))

        call6.quan.setItem(i,0, QtWidgets.QTableWidgetItem(str(quantiter)))
        t10=int(quantiter)*46578
        S=S+t10

        call6.tableWidget_7.setItem(i,0, QtWidgets.QTableWidgetItem(str(t10)))

        f=open("valid.txt","a")

        f.write("\n")
        f.write("        article :      Voiture")
        f.write("\n")
        f.write("        prix unitaire : 1189DT")
        f.write("\n")
        f.write("        quantiter :"+a1)
        f.write("\n")
        f.write("        prix totale :"+str(t10))

        f.write("\n")
        f.close()
    call6.label_14.setText(np)
    call6.label_17.setText(email)
    call6.label_18.setText(tel)

    call6.label_2.setText("10/02/2021")
    call6.label_4.setText("10/02/2021")
    remis=(S/100)*2
    S2=S-remis
    tax=(S2/100)*23
    S3=S2-tax
    call6.label_5.setText(str(S))
    call6.label_6.setText("-"+(str(remis)))
    call6.label_7.setText((str(S2)))
    call6.label_8.setText("23%")
    call6.label_11.setText(str(tax))
    call6.label_12.setText(str(S3))
    
app=QtWidgets.QApplication([])
call=uic.loadUi('Welcome.ui')
call.Start.clicked.connect(main1)
call1=uic.loadUi('Shop.ui')

call9=uic.loadUi('untitled.ui')

call6=uic.loadUi('facture.ui')
call1.pushButton.clicked.connect(main2)
call9.valider.clicked.connect(main5)
call.show()

call.Start.clicked.connect(main1)


call6.prixuni.insertRow(0)
call6.prixuni.insertColumn(0)

call6.quan.insertRow(0)
call6.quan.insertColumn(0)

call6.prod.insertRow(0)
call6.prod.insertColumn(0)

call6.tableWidget_7.insertRow(0)
call6.tableWidget_7.insertColumn(0)


app.exec()

