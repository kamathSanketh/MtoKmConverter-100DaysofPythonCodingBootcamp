import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=200,pady=200)
input = tkinter.Entry()
input.grid(row=1, column=2)

def button_clicked() :
    temp = round(int(input.get()) * 1.609344)
    my_label3["text"] = temp
my_label1 = tkinter.Label(text="Miles")
my_label1.grid(row=1, column=3)

my_label2 = tkinter.Label(text="is equal to")
my_label2.grid(row=2, column=1)

my_label3 = tkinter.Label(text="0")
my_label3.grid(row=2, column=2)

my_label4 = tkinter.Label(text="Km")
my_label4.grid(row=2, column=3)

my_button = tkinter.Button(text="Calculate", command = button_clicked)
my_button.grid(row=3, column=2)



window.mainloop()