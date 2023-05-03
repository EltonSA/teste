import customtkinter as c
from PIL import ImageTk, Image
import posiciona

janela = c.CTk()
janela.geometry("380x320+610+153")
janela.title("Arquivit")
janela.resizable(width=1, height=1)


image = Image.open("img/login.png")
background_image = ImageTk.PhotoImage(image)

background_label = c.CTkLabel(janela, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Caixas de entrada
texto = c.CTkEntry(janela, placeholder_text="User")
texto.place_configure(width=83, height=1, x=91, y=83)


janela.mainloop()
