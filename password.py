from cProfile import label
from tkinter import *
from tkinter import messagebox

from extraction_data import * 
from genitique import *
from tkinter import ttk

M = []
P = []


C = []
list_pilote = []
list_fonction = []
X = []
cout_totale = 0
list_formation = []
exe=0
cout_totale_ancien = 0

def Execution():

    global M
    global P
    global C
    global cout_totale
    global exe
    global imp
    global cout_totale_ancien
    
    if(exe==0 and imp==0) :
        for i in range(len(M)):
            fancien ,x, f = GA(np.array(P[i], dtype=int), np.array(M[i]), np.array(C[i]))
            X.append(x)
            cout_totale_ancien += fancien
            cout_totale += f
            #print(cout_totale)
        coutfrm = LabelFrame(
            Frame_execute, text="Profit actuelle", pady=10, bd=10, fg="black", font=("Courrier", 20, "bold"))
        coutfrm.place(x=390, y=104)
        label_cout=Label(coutfrm ,font=fonts ,text=cout_totale)
        label_cout.pack()
        cout_ancien_frm = LabelFrame(
            Frame_execute, text="Profit totale ancien", pady=10, bd=10, fg="black", font=("Courrier", 20, "bold"))
        cout_ancien_frm.place(x=360, y=0)
        label_cout=Label(cout_ancien_frm ,font=fonts ,text=cout_totale_ancien)
        label_cout.pack()
        exe=1
    else:
        messagebox.showinfo(
            title="Message", message="Verifier si vous avez bien importer les donnees et si vous n'avez pas deja executer")
    matrice_grid(X)


Grid = []


def matrice_grid(X):
    global Grid
    global list_pilote
    global list_formation
    mois = []
    list_formation = extract_formation_liste(entree3.get(), int(entree.get()))
    i = 0
    while i < len(X):
        L = X[i]
        S = ""

        for k in range(0, len(list_pilote)):

            for j in range(0, len(L)-1):
                if (L[j][k] == 1):
                    S = S+list_formation[j].upper()+"-"+str(random.randint(1,28))+"-|"

            mois.append(S[:-1])

            S = ""

        Grid.append(mois)
        mois = []
        i = i+1
    traduire_matrice_grid(Grid)


def traduire_matrice_grid(grid):
    L = []
    M = []
    tree.tag_configure('critical', background="red", foreground="black")
    for i in range(0, len(list_pilote)):
        L.append(list_pilote[i])
        L.append(list_fonction[i])
        for j in range(0, 12):
            L.append(grid[j][i])
        if (i % 2 == 0):
            print("hello")
            tree.insert(parent='', index='end', iid=i, text="",
                        values=L, tags=('critical',))
        else:
            tree.insert(parent='', index='end', iid=i, text="",
                        values=L)
        L = []
    



def Frame_import():
    HideAllFrames()
    Frame_import.pack(fill="both", expand=1)


def Frame_execute():
    HideAllFrames()
    Frame_execute.pack(fill="both", expand=1)


def Frame_formation():
    HideAllFrames()
    Frame_formation.pack(fill="both", expand=1)


def HideAllFrames():
    Frame_import.pack_forget()
    Frame_execute.pack_forget()
    Frame_formation.pack_forget()

window= Tk()
window.geometry("720x480")
window.iconbitmap("air algerie.ico")
window.title("Air algerie")


def valide():
    global acceder
    if(Entry_password.get()=="souhila" and Entry_username.get()=="souhila"):
        
        window.config(menu=my_menu)
        Frame_import.pack(fill="both", expand=1)
        frame_login.forget()
    else:
        messagebox.showinfo(title="Attention!!",message="Verifier le mot de passe et le nom d'utilisateur")
        

def cancel():
   Entry_username.delete(0,END)
   Entry_password.delete(0,END)
def Exit():
    HideAllFrames()
    menu1=Menu(window)
    window.config(menu=menu1)
    cancel()
    frame_login.place(x=0,y=0)
    

my_menu = Menu(window, font=("Courrier", 30, "bold"), bg="red", fg="black")
my_menu.add_command(label="Import", command=Frame_import)
my_menu.add_command(label="Executer traitement", command=Frame_execute)
my_menu.add_command(label="Nos formation", command=Frame_formation)
my_menu.add_command(label="Se déconnecter", command=Exit)
frame_login = Frame(window, width=720, height=480, bg="red")
frame_login.place(x=0,y=0)
fonts=("serif",25,"bold")
photo = PhotoImage(file=r"air-algerie.png").subsample(3,3)
photo18 = PhotoImage(file=r"1-min-23.png").subsample(2,3)
canvas = Canvas(frame_login, width=720, height=480)
canvas.create_image(50, 0, anchor=NW, image=photo)
canvas.create_image(500, 25, anchor=NW, image=photo18)
canvas.place(x=0, y=0)
canvas.create_text(110, 220, font=fonts, text="Nom d'utilisateur")
canvas.create_text(110, 290, font=fonts, text="Mot de passe")

Entry_username = Entry(canvas,  justify="center", font=fonts)
Entry_username.place(x=220, y=200)
Entry_password = Entry(canvas, show="*",justify="center", font=fonts)
Entry_password.place(x=220, y=270)

photo1 = PhotoImage(file=r"icons8-login-96.png")
button_Valider = Button(canvas, text="Connexion", command=valide, image=photo1, highlightthickness=0,  relief=FLAT)
button_Valider.place(x=600, y=210)
photo2 = PhotoImage(file=r"icons8-cancel-96.png")
button_Cancel = Button(canvas, text="Cancel",
                       command=cancel, image=photo2, highlightthickness=0,  relief=FLAT)
button_Cancel.place(x=80, y=380)
frame_binome = Frame(canvas, width=470, height=50)
frame_binome.place(x=250, y=430)
label_binome = Label(frame_binome, text="Créer par :Mouhoub Souhila et ouafi melissa\n Encadré par: Madame Ait Abdeslam",font=("Arial",15,"bold")).place(x=0,y=0)
#frames
Frame_import = Frame(window, borderwidth=2, relief=GROOVE,
                     bd=0, highlightthickness=0)


# frame 1
Frame1 = Frame(Frame_import, borderwidth=2, relief=GROOVE,
               bd=0, highlightthickness=0)
Frame1.pack(side=TOP)

# frame 2
Frame2 = Frame(Frame_import, borderwidth=2, relief=GROOVE,
               bd=0, highlightthickness=0)
Frame2.pack(side=BOTTOM)
# frame 11
Frame11 = Frame(Frame1, borderwidth=2, relief=GROOVE,
                bd=0, highlightthickness=0)
Frame11.pack(side=LEFT)
# frame 12
Frame12 = Frame(Frame1, borderwidth=2, relief=GROOVE,
                bd=0, highlightthickness=0)
Frame12.pack(side=RIGHT)
width = 300
height = 300
image = PhotoImage(file="air-algerie.png").subsample(2, 2)
canvas = Canvas(Frame11, width=width, height=height,
                bd=0, highlightthickness=0)
canvas.create_image(height/2, width/2, image=image)
canvas.pack(expand=YES)
# entrée
nbrfrmlbl = LabelFrame(
    Frame12, text="Nombre de formation", pady=10, bd=10, fg="black")
nbrfrmlbl.pack()
value = StringVar()
value.set("9")

entree = Spinbox(nbrfrmlbl, from_=0, to=1000000000,
                 textvariable=value, width=48, bd=1)
entree.pack()

# entrée
nbrpltlbl = LabelFrame(Frame12, text="Nombre de pilote",
                       pady=10, bd=10, fg="black")
nbrpltlbl.pack()
value2 = StringVar()
value2.set("49")
entree2 = Spinbox(nbrpltlbl, from_=0, to=1000000000,
                  textvariable=value2, width=48, bd=1)
entree2.pack()

lienlblfrm = LabelFrame(
    Frame12, text="Fichier Excel chemin", pady=10, bd=10, fg="black")
lienlblfrm.pack()

value3 = StringVar()
value3.set("input.xlsx")
entree3 = Entry(lienlblfrm, textvariable=value3, width=50, bd=1)
entree3.pack()

imp = 1


def recupere():
    global imp
    global M
    global P
    global C
    global list_pilote
    global list_fonction
    C = extract_C(entree3.get(), int(entree.get()), int(entree2.get()))
    P = extract_P(entree3.get(), int(entree.get()), int(entree2.get()))
    M = extract_M(entree3.get(), int(entree.get()), int(entree2.get()))
    list_pilote = extract_pilote_liste(entree3.get(), int(entree2.get()))
    list_fonction = extract_fonction_liste(entree3.get(), int(entree2.get()))
    if (imp == 1):
        width = 100
        height = 100
        image7 = PhotoImage(file="icons8-data-quality-100.png").subsample(2,2)
        canvas1 = Canvas(Frame2, width=720, height=480)
        canvas1.create_image(0, 0, anchor=NW, image=image7)
        canvas1.place(x=0, y=0)
        lbl = Label(Frame2, text="Les donnees sont bien importer\n Vous pouvez lancer l'execution",
                    font=("Helvetica", 27, "bold"))
        lbl.pack()
        imp = 0
    else:
        messagebox.showinfo(
            title="Message", message="Vous avez deja importer les donnees!!")

photo3 = PhotoImage(file="import.png").subsample(7, 7)


btn_imp = Button(Frame12, text="importer", relief=FLAT,
                 cursor="arrow", borderwidth=3, font=("Courrier", 30, "bold"), command=recupere, bd=10,
                 image=photo3).pack()


Frame_execute = Frame(window, borderwidth=2, relief=GROOVE,
                      bd=0, highlightthickness=0)



#Execution objet
prmexfrm = LabelFrame(
    Frame_execute, text="Exécuter", pady=10, bd=10, fg="black", font=("Courrier", 30, "bold"),width=700,height=150)
prmexfrm.place(x=60, y=0)


photo8 = PhotoImage(file=r"execute.png").subsample(5, 5)

btn_imp = Button(prmexfrm, text="Execution", relief=FLAT,
                 cursor="arrow", borderwidth=3, font=("Courrier", 30, "bold"), command=Execution, bd=10, image=photo8).pack(side=TOP)


#tree view

tree = ttk.Treeview(Frame_execute, columns=(1,14, 2, 3, 4, 5, 6, 7,
                    8, 9, 10, 11, 12, 13), height=12, show="headings")
tree.place(x=50, y=214, width=600, height=200)
s_e = Scrollbar(tree)
s_e.config(command=tree.yview)
s_e.pack(side=RIGHT, fill=Y)


tree.heading(1, text="Pilote")
tree.column(1, width=40)
tree.heading(14, text="Fonction")
tree.column(14, width=40)
tree.heading(2, text="Janvier")
tree.column(2, width=40)
tree.heading(3, text="fevrier")
tree.column(3, width=40)
tree.heading(4, text="mars")
tree.column(4, width=40)
tree.heading(5, text="avril")
tree.column(5, width=40)
tree.heading(6, text="mai")
tree.column(6, width=40)
tree.heading(7, text="juin")
tree.column(7, width=40)
tree.heading(8, text="Juillet")
tree.column(8, width=40)
tree.heading(9, text="Aout")
tree.column(9, width=40)
tree.heading(10, text="Septembre")
tree.column(10, width=40)
tree.heading(11, text="Octobre")
tree.column(11, width=40)
tree.heading(12, text="Novembre")
tree.column(12, width=40)
tree.heading(13, text="Decembre")
tree.column(13, width=40)
style = ttk.Style()
style.theme_use("xpnative")
style.map("Treeview")
photo12 = PhotoImage(file=r"icons8-sauvegarder-30.png")


def Sauvegarder():
    out_file="output.xlsx"
    global Grid
    global list_pilote
    global list_formation
    workbook = xlsxwriter.Workbook(out_file)
    worksheet = workbook.add_worksheet("Sheet")
    Mois = ["fonction","janvier", "fevrier", "mars", "avril", "mai", "juin",
            "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]
    for i in range(13):
        worksheet.write(0, i+1, Mois[i])
  
    for i in range(len(list_pilote)):
        worksheet.write(i+1, 0, list_pilote[i])
        worksheet.write(i+1, 1, list_fonction[i])
        for j in range(12):
           
            worksheet.write(i+1, j+2, Grid[j][i])
    messagebox.showinfo(
        title="Message", message="Votre emploi du temp est bien sauvegarder dans le fichier'output.xlsx'")

    workbook.close()


btn_sauv = Button(Frame_execute, text="Sauvegarder", relief=FLAT,
                 cursor="arrow", command=Sauvegarder, bd=10,image=photo12)
btn_sauv.place(x=300,y=420)
style.map(btn_sauv)


Frame_formation = Frame(window, borderwidth=2, relief=GROOVE,
                        bd=0, highlightthickness=0)

                    
photo10 = PhotoImage(file=r"avion.png")
canvas4 = Canvas(Frame_formation, width=720, height=480)
canvas4.create_image(100, 50, anchor=NW, image=photo10)
canvas4.create_text(200, 250, text="Detail", font=fonts, fill="black")
canvas4.place(x=0, y=0)

label_frm_formation_name = LabelFrame(
    Frame_formation, text="Formation", pady=10, bd=10, fg="black", font=("Courrier", 30, "bold"),width=200,height=100)
label_frm_formation_name.place(x=300,y=0)

listeProduits = ["Simu ATR.72-500",
                 "Simu ATR.72-600", "Simu B737-NG", "Simu A330-200", "DGR",
                 "CRM", "SMS", "SSP"]

listeCombo = ttk.Combobox(label_frm_formation_name, values=listeProduits)


listeCombo.pack()
detail = [["3 jours", "Kouba", "6 mois"], [
    "5 jours", "Paris/Toulouse /Madrid", "6 mois"]
    , [
    "3 jours", "Kouba", "6 mois"], [
    "4 jours", "Paris/Madrid", "6 mois"]
    , [
    "une journee", "sol", "2ans"]
    , [
    "une journee", "sol", "3ans"]
    , [
    "une journee", "sol", "4ans"]
    , [
    "une journee", "sol", "3ans"]]

def action(event):
    global detail
    global label_frm
    global label_lieu
    global label_duree
    global label_validite
	# Obtenir l'élément sélectionné
    select = listeCombo.get()
    label_frm.destroy()
    label_duree.destroy()
    label_lieu.destroy()
    label_validite.destroy()

    if(select=="Simu ATR.72-500"):
        label_frm = Label(label_frm_formation_detail, text=select, pady=5,
                      bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_frm.place(x=0,y=0)
        label_duree = Label(label_frm_formation_detail, text="Duree  "+detail[0][0], pady=5,
                      bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_duree.place(x=0, y=50)
        label_lieu = Label(label_frm_formation_detail, text="Lieu  "+detail[0][1], pady=5,
                        bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_lieu.place(x=0, y=100)
        label_validite = Label(label_frm_formation_detail, text="Validite  "+detail[0][2], pady=5,
                        bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_validite.place(x=0, y=150)
    if (select == "Simu ATR.72-600"):
        label_frm = Label(label_frm_formation_detail, text=select, pady=5,
                          bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_frm.place(x=0, y=0)
        label_duree = Label(label_frm_formation_detail, text="Duree  "+detail[1][0], pady=5,
                            bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_duree.place(x=0, y=50)
        label_lieu = Label(label_frm_formation_detail, text="Lieu  "+detail[1][1], pady=5,
                           bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_lieu.place(x=0, y=100)
        label_validite = Label(label_frm_formation_detail, text="Validite  "+detail[1][2], pady=5,
                               bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_validite.place(x=0, y=150)
    if (select == "Simu B737-NG"):
        label_frm = Label(label_frm_formation_detail, text=select, pady=5,
                          bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_frm.place(x=0, y=0)
        label_duree = Label(label_frm_formation_detail, text="Duree  "+detail[2][0], pady=5,
                            bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_duree.place(x=0, y=50)
        label_lieu = Label(label_frm_formation_detail, text="Lieu  "+detail[2][1], pady=5,
                           bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_lieu.place(x=0, y=100)
        label_validite = Label(label_frm_formation_detail, text="Validite  "+detail[2][2], pady=5,
                               bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_validite.place(x=0, y=150)
    if (select == "Simu A330-200"):
        label_frm = Label(label_frm_formation_detail, text=select, pady=5,
                          bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_frm.place(x=0, y=0)
        label_duree = Label(label_frm_formation_detail, text="Duree  "+detail[3][0], pady=5,
                            bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_duree.place(x=0, y=50)
        label_lieu = Label(label_frm_formation_detail, text="Lieu  "+detail[3][1], pady=5,
                           bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_lieu.place(x=0, y=100)
        label_validite = Label(label_frm_formation_detail, text="Validite  "+detail[3][2], pady=5,
                               bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_validite.place(x=0, y=150)
    if (select == "DGR"):
        label_frm = Label(label_frm_formation_detail, text=select, pady=5,
                          bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_frm.place(x=0, y=0)
        label_duree = Label(label_frm_formation_detail, text="Duree  "+detail[4][0], pady=5,
                            bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_duree.place(x=0, y=50)
        label_lieu = Label(label_frm_formation_detail, text="Lieu  "+detail[4][1], pady=5,
                           bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_lieu.place(x=0, y=100)
        label_validite = Label(label_frm_formation_detail, text="Validite  "+detail[4][2], pady=5,
                               bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_validite.place(x=0, y=150)
    if (select == "CRM"):
        label_frm = Label(label_frm_formation_detail, text=select, pady=5,
                          bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_frm.place(x=0, y=0)
        label_duree = Label(label_frm_formation_detail, text="Duree  "+detail[5][0], pady=5,
                            bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_duree.place(x=0, y=50)
        label_lieu = Label(label_frm_formation_detail, text="Lieu  "+detail[5][1], pady=5,
                           bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_lieu.place(x=0, y=100)
        label_validite = Label(label_frm_formation_detail, text="Validite  "+detail[5][2], pady=5,
                               bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_validite.place(x=0, y=150)
    if (select == "SMS"):
        label_frm = Label(label_frm_formation_detail, text=select, pady=5,
                          bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_frm.place(x=0, y=0)
        label_duree = Label(label_frm_formation_detail, text="Duree  "+detail[6][0], pady=5,
                            bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_duree.place(x=0, y=50)
        label_lieu = Label(label_frm_formation_detail, text="Lieu  "+detail[6][1], pady=5,
                           bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_lieu.place(x=0, y=100)
        label_validite = Label(label_frm_formation_detail, text="Validite  "+detail[6][2], pady=5,
                               bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_validite.place(x=0, y=150)    
    if (select == "SSP"):
        label_frm = Label(label_frm_formation_detail, text=select, pady=5,
                          bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_frm.place(x=0, y=0)
        label_duree = Label(label_frm_formation_detail, text="Duree  "+detail[7][0], pady=5,
                            bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_duree.place(x=0, y=50)
        label_lieu = Label(label_frm_formation_detail, text="Lieu  "+detail[7][1], pady=5,
                           bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_lieu.place(x=0, y=100)
        label_validite = Label(label_frm_formation_detail, text="Validite  "+detail[7][2], pady=5,
                               bd=10, fg="black", font=("Courrier", 20, "bold"))
        label_validite.place(x=0, y=150)

    
       


listeCombo.bind("<<ComboboxSelected>>", action)

label_frm_formation_detail =Frame(
    Frame_formation,  pady=10, bd=10, width=400, height=300)
label_frm_formation_detail.place(x=250, y=250)
label_frm = Label(label_frm_formation_detail, pady=10,
                  bd=10, fg="black", font=("Courrier", 20, "bold"))
label_frm.place(x=0, y=0)
label_duree = Label(label_frm_formation_detail, pady=10,
                    bd=10, fg="black", font=("Courrier", 20, "bold"))
label_duree.place(x=0, y=50)
label_lieu = Label(label_frm_formation_detail, pady=10,
                   bd=10, fg="black", font=("Courrier", 20, "bold"))
label_lieu.place(x=0, y=100)
label_validite = Label(label_frm_formation_detail, pady=10,
                       bd=10, fg="black", font=("Courrier", 20, "bold"))
label_validite.place(x=0, y=150)
window.mainloop()

