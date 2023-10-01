
from PySide6.QtWidgets import QWidget,QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QRect,QSize
import requests
import os

class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        
        

        self.pic = QLabel(self)
        pixmap=QPixmap('/home/codingchaos/Desktop/amfoss-tasks/task-08/Poke-Search/assets/landing.jpg')
        self.pic.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.initUI()
        self.w = None        
       
    def initUI(self):
        self.setWindowTitle("Window")
        self.setStyleSheet("")
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 280, 40)
        text=""
        self.mainlabel=QLabel(text,self)
        self.mainlabel.setFixedHeight(300)
        self.mainlabel.setGeometry(500,200,280,50)
        
        
        
        
  

    
        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.search)
        
        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        
        
        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)

        
    def search(self):
        poke=self.textbox.text().lower()
        print(poke)
        res=requests.get("https://pokeapi.co/api/v2/pokemon/"+poke)
        if res.status_code!=200:
            return 0
        else:
            res_js=res.json()
            name=res_js["name"].capitalize()
            ability1=res_js["abilities"][0]["ability"]["name"].capitalize()
            ability2=res_js["abilities"][1]["ability"]["name"].capitalize()
            type=res_js["types"][0]["type"]["name"].capitalize()
            hp=res_js["stats"][0]["base_stat"]
            attack=res_js["stats"][1]["base_stat"]
            defense=res_js["stats"][2]["base_stat"]
            spec_attck=res_js["stats"][3]["base_stat"]
            spec_dfnc=res_js["stats"][4]["base_stat"]
            speed=res_js["stats"][5]["base_stat"]
            img_lnk=res_js["sprites"]["front_default"]

            
            text=f'''
        
Name:{name}
Abilities:{ability1},{ability2}
Types:{type}
Stats:

HP:{hp}
attack:{attack}
Defense:{defense}
Special-Attack:{spec_attck}
Special-Defense:{spec_dfnc}
Speed:{speed}

'''
            self.mainlabel.setText(text)
            
            
            res=requests.get(img_lnk)
            with open('temp.png','wb') as f:
                f.write(res.content)
                f.flush()
                
            pixmap2=QPixmap("/home/codingchaos/Desktop/amfoss-tasks/task-08/Poke-Search/assets/landing.jpg")
            self.pic.setPixmap(pixmap2)
            self.pic.setGeometry(50,250,0,40)
            print(img_lnk,name,ability1, ability2,type,hp,attack,defense,spec_attck,spec_dfnc,speed , sep="\n")
            return 0
    
    ## TO-DO ##

    # 1 #
    # Fetch the data from from the API.
    # Display the name, official artwork (image), abilities, types and stats when queried with a Pokémon name.
    # Add the background provided in assets

    # 2 #
    # Capture the Pokémon i.e. download the image.

    # 3 #
    # Display all the Pokémon captured with their respective names using a new window.

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication



    app = QApplication(sys.argv)
    window = SearchWindow()
    
    #resize(pixmap.height(),pixmap.width())
        
    window.show()
    sys.exit(app.exec())
