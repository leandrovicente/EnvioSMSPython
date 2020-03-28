from tkinter import *
from tkinter import messagebox
from telesign.messaging import MessagingClient
    
def EnviarSMS():
    customer_id = "04BD083E-0B86-4CF2-9579-046925D6505F"
    api_key = "dvzRWS678PiFerdWu6LlAaUMxQNtdoLn3x/f+WyZpGWqmXI4tSOhU2cvSz4IgAg2aHQhI5LSE9zyip7oxRUPaw=="
    phone_number = "55" + txtNumero.get()
    message = txtMensagem.get()
    message_type = "ARN"
    messaging = MessagingClient(customer_id, api_key)
    response = messaging.message(phone_number, message, message_type)
    if response.status_code == 200:
        messagebox.showinfo("success","SMS Enviado Com Sucesso")
    else:
        messagebox.showerror("error","Falha ao enviar SMS, Verifique o Numero é tente novamente")

main = Tk()
main.title('SMS Envio Python')
main.geometry('200x200')

# Define uma grade de 50 x 50 células na janela principal
rows = 0
while rows < 10:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1

txtNumero = Entry(main)
txtNumero.insert(0, 'Digite seu Numero')
txtNumero.grid(row=1, column=5, sticky='NS')

txtMensagem = Entry(main)
txtMensagem.insert(0, 'Digite sua Mensagem')
txtMensagem.grid(row=3, column=5, sticky='NS')

btnEnviar = Button(main, text='Enviar',command=EnviarSMS)
btnEnviar.grid(row=5, column=5, sticky='NESW')
main.mainloop()


