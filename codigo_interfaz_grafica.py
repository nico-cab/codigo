import smtplib    # CONTROLA EL ENVÍO DE CORREOS
from tkinter import *   # CONTROLA LA INTERFAZ
from tkinter import messagebox  # CONTROLA LOS MENSAJES EMERGENTES
from PIL import ImageTk, Image   # CONTROLA LAS IMAGENES

# ---------------------FUNCIÓN SALIDA-------------------------------
def salida():
    salir = messagebox.askyesno(message='¿Seguro que desea cerrar el programa?\n'
                                'Los datos se borrarán y no serán guardados.', title='¿Salir?')

    if salir == TRUE:
        messagebox.showinfo(message='Gracias por usar el programa.', title='Cerrar')
        exit()



# ---------------------VALIDACION DE USUARIO Y CONTRASEÑA----------------------------------
def validar():
    try:
        user = entrada_usuario.get()
        password = entrada_contraseña.get()

        if user == '' or password == '':
            messagebox.showinfo(title='Error', message=f'Todos los campos deben estar llenos.')
        else:
            while user != 'admin' or password != '1234':
                incorrecto()
            else:
                messagebox.showinfo(title=f'Bienvenido {user}',
                                    message='Acabas de acceder al sistema de\ngestión de ventas.')
                frame_ventana1()
            return

    except Exception as f:
        messagebox.showinfo(title='Error', message=f'No válido.')
        print(f)

# ---------------------------------------BOTON SALIDA USUARIO--------------------------------------
def salir_usuario():
    cerrrar = messagebox.askyesno(message='¿Desea cerrar el programa?', title='¿Salir?')
    if cerrrar == TRUE:
        messagebox.showinfo(title='Inválido', message='No se logró ingresar al sistema.')
        exit()

#----------------------------------------------------------------------------------------------------------------------
# ---------------------VENTANA DE USUARIO-------------------------
# --------------------------DISEÑO VENTANA DE USUARIO---------------------------------
root = Tk()
root.title('Usuario')
root.geometry('324x200+500+200')
root.config(bg='#729B79')
root.resizable(False, False)
root.iconbitmap('user2.ico')

# ----------------------IMAGEN DE USUARIO--------------------------------------------------
imagen = ImageTk.PhotoImage(Image.open('logo1.png').resize((50, 50)))
label = Label(image=imagen)
label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
label.config(justify='center')

#-------------------------ETIQUETA DE USUARIO---------------------------------
label_usuario = Label(root, text='Usuario', font=('Arial', 12, 'bold'))
label_usuario.config(bg='#729B79')
label_usuario.grid(row=1, column=0, padx=10, pady=10, sticky='e')

#--------------ENTRADA DE USUARIO----------------------------------------------------
entrada_usuario = Entry(root)
entrada_usuario.config(bg='white', fg='black', font='Arial, 12', cursor='hand2')
entrada_usuario.grid(row=1, column=1, padx=10, pady=10)

# ----------------CONTRASEÑA-------------------
# --------------------ETIQUETA------------------------------
label_contraseña = Label(root, text='Contraseña', font=('Arial', 12, 'bold'))
label_contraseña.config(bg='#729B79')
label_contraseña.grid(row=2, column=0, padx=10, pady=10, sticky='e')
#------------------------------------------ENTRADA---------------------------
entrada_contraseña = Entry(root, show='•')
entrada_contraseña.config(bg='white', fg='black', font='Arial, 12', cursor='hand2')
entrada_contraseña.grid(row=2, column=1, padx=10, pady=10)

# -------------BOTON INGRESAR--------------

btn_ingresar = Button(root, text='Ingresar', width=10, command=validar, font='Arial, 12', activebackground='#00B4D8')
btn_ingresar.config(bg='#90E0EF', cursor='hand2')
btn_ingresar.grid(row=3, column=1, padx=10, pady=10, sticky='e')

# ------------------------------BOTON SALIR USUARIO--------------------------------------------

btn_salir_usuario = Button(root, text='Salir', width=10, command=salir_usuario, font='Arial, 12',
                           activebackground='#00B4D8')
btn_salir_usuario.config(bg='#90E0EF', cursor='hand2')
btn_salir_usuario.grid(row=3, column=0, padx=10, pady=10, sticky='w')



# -------------------------------VENTANA DE CONTRASEÑA INCORECTA------------------------------------
def incorrecto():

    # ---- DISEÑO DE LA VENTANA---------
    root.withdraw()
    ventana_in = Toplevel()
    ventana_in.title('Error')
    ventana_in.geometry('315x200+500+200')
    ventana_in.resizable(False, False)
    ventana_in.config(bg='#EE6055')
    ventana_in.iconbitmap('error1.ico')

    label_error = Label(ventana_in, text='Contraseña incorrecta\nAcceso denegado',
                        font=('Arial', 14, 'bold'), justify='center', activebackground='#00B4D8')
    label_error.place(x=56, y=50)
    label_error.config(bg='#EE6055')



#---------------------------VENTANA DE REGRESO AL USUARIO-----------------------------
    def regreso():
        ventana_in.withdraw()
        root.deiconify()


# -----------------------------BOTÓN REGRESAR------------------------------------------------------
    btn_regresar = Button(ventana_in,
                          text='Intentar de nuevo',
                          command=regreso,
                          cursor='hand2',
                          width=15,
                          font='Arial, 12',
                          activebackground='#00B4D8')
    btn_regresar.config(bg='#90E0EF')
    btn_regresar.place(x=89, y=110)

    ventana_in.mainloop()


# -------------------INTERFAZ PRINCIPAL INSTRUMENTOS-----------------------------------------------------------
# -------------------FUNCION FRAME_VENTANA-------------------

def frame_ventana1():
    # -------FUNCIÓN DE MEDIDORES---------
    # --------PRINCIPAL---------------------
    def frutas():
        try:
            #precio oximetro
            precio_mango = 185_000

            #precio glucometro
            precio_fresa = 169_050

            #precio tensiometro
            precio_mora = 215_000

            mango = int(entrada_mango.get())
            fresa = int(entrada_fresa.get())
            mora = int(entrada_mora.get())

            # -----------VALIDACION NUMEROS NEGATIVOS-------------------------

            if mango <= 0 or fresa <= 0 or mora <= 0:
                messagebox.showinfo(title='Error', message='No se permiten negativos.')
                return

            else:
                total_fru_vendidas = mango + fresa + mora
                frut_vendidas.set(total_fru_vendidas)

                total_mango = precio_mango * mango
                totmango.set(total_mango)

                total_fresa = precio_fresa * fresa
                totfresa.set(total_fresa)

                total_mora = precio_mora * mora
                totmora.set(total_mora)

                total_frutas = total_mango + total_fresa + total_mora
                tot_general_fru.set(total_frutas)

                descuento = calcular_descuento(total_frutas)

                aplicar_descuento = total_frutas - descuento
                set_discount.set(aplicar_descuento)

                resultado_descuento.set(descuento)

        except Exception as f:
            messagebox.showinfo(title='Error', message=f'Todos los campos deben estar llenos.')
            print(f)

#----------------------------------------------------------------------------------------------------------------------

    # ------CALCULO DEL DESCUENTO------------
    # --------SUBPROCESO------------------

    def calcular_descuento(total_frutas):

        descuento = 0

        if total_frutas > 500_000:
            descuento = total_frutas * 0.13

        else:
            if total_frutas > 560_000:
                descuento = total_frutas * 0.16
            else:
                descuento = 0

        return descuento

# ----------------------------------------------------------------------------------------------------------------------

# -------------DISEÑO DE LA VENTANA PRINCIPAL------------------
    frame_principal = Toplevel()
    root.withdraw()

    frame_principal.title('UNIDAD BIOMÉDICA')
    frame_principal.config(bg='#BACDB0')
    frame_principal.geometry('815x370+280+150')
    frame_principal.resizable(False, False)
    frame_principal.iconbitmap('biomedica2.ico')

    label = Label(frame_principal, text='Control de Ventas', justify='center', font=('Arial', 14, 'bold'))
    label.config(bg='#BACDB0')
    label.grid(row=0, column=0, padx=5, pady=4, columnspan=4)

    # -----------------------------CANTIDAD DE VENTAS-------------------------------
    # --------------------------------MANGO---------------------------------------------------------
    # ETIQUTA MANGO - OXIMETRO
    label_entrada_mango = Label(frame_principal, text='Oxímetro (und): ', font='Arial, 12')
    label_entrada_mango.config(bg='#BACDB0')
    label_entrada_mango.grid(row=1, column=0, padx=10, pady=10, sticky='e')

    # ENTRADA MANGO - OXIMETRO
    entrada_mango = Entry(frame_principal)
    entrada_mango.config(bg='white', fg='black', font='Arial, 12', cursor='hand2')
    entrada_mango.grid(row=1, column=1, padx=10, pady=10)



    # -------------------------FRESA---------------------------
    # ETIQUTA FRESA - GLUCOMETRO
    label_entrada_fresa = Label(frame_principal, text='Glucómetro (und): ', font='Arial, 12')
    label_entrada_fresa.config(bg='#BACDB0')
    label_entrada_fresa.grid(row=2, column=0, padx=10, pady=10, sticky='e')

    # ENTRADA FRESA - GLUCOMETRO
    entrada_fresa = Entry(frame_principal)
    entrada_fresa.config(bg='white', fg='black', font='Arial, 12', cursor='hand2')
    entrada_fresa.grid(row=2, column=1, padx=10, pady=10)



    # -------------------------MORA---------------------------
    # -----ETIQUTA MORA - TENSIOMETRO
    label_entrada_mora = Label(frame_principal, text='Tensiómetro (und): ', font='Arial, 12')
    label_entrada_mora.config(bg='#BACDB0')
    label_entrada_mora.grid(row=3, column=0, padx=10, pady=10, sticky='e')

    # ----ENTRDA MORA - TENSIOMETRO
    entrada_mora = Entry(frame_principal)
    entrada_mora.config(bg='white', fg='black', font='Arial, 12', cursor='hand2')
    entrada_mora.grid(row=3, column=1, padx=10, pady=10)



    # ----------------------ACUMULADO DE LAS VENTAS (TOTAL FRUTAS VENDIDAS)--------------------------------

    label_total_ventas = Label(frame_principal, text='Total de\nunidades vendidas: ', font='Arial, 12')
    label_total_ventas.config(bg='#BACDB0')
    label_total_ventas.grid(row=4, column=0, padx=10, pady=10)

    frut_vendidas = IntVar()
    salida_fru_vendidas = Entry(frame_principal, textvariable=frut_vendidas, state='readonly')
    salida_fru_vendidas.config(bg='white', fg='black', font='Arial, 12')
    salida_fru_vendidas.grid(row=4, column=1, padx=10, pady=10)





    #------------------------------------SALIDAS------------------------------------------------
    # ----------------------------VENTAS POR FRUTAS------------------

    # -------------------VENTAS ACUMULADAS DE MANGO----------------------

    label_salida_mango = Label(frame_principal, text='Valor Ventas Oxímetro $: ', font=('Arial', 12))
    label_salida_mango.config(bg='#BACDB0')
    label_salida_mango.grid(row=1, column=2, padx=10, pady=10, sticky='e')

    totmango = IntVar()
    salida_totmango = Entry(frame_principal, textvariable=totmango, state='readonly')
    salida_totmango.config(bg='white', fg='black', font='Arial, 12')
    salida_totmango.grid(row=1, column=3, padx=10, pady=10)



    # -------------------------VENTAS ACUMULADAS DE FRESA-----------------------

    label_salida_fresa = Label(frame_principal, text='Valor Ventas Glucómetro $: ', font='Arial, 12')
    label_salida_fresa.config(bg='#BACDB0')
    label_salida_fresa.grid(row=2, column=2, padx=10, pady=10, sticky='e')

    totfresa = IntVar()
    salida_totfresa = Entry(frame_principal, textvariable=totfresa, state='readonly')
    salida_totfresa.config(bg='white', fg='black', font='Arial, 12')
    salida_totfresa.grid(row=2, column=3, padx=10, pady=10)




    # -------------------------VENTAS ACUMULADAS DE MORA-----------------------

    label_salida_mora = Label(frame_principal, text='Valor Ventas Tensiómetro $:', font='Arial, 12')
    label_salida_mora.config(bg='#BACDB0', font='Arial, 12')
    label_salida_mora.grid(row=3, column=2, padx=10, pady=10, sticky='e')

    totmora = IntVar()
    salida_totmora = Entry(frame_principal, textvariable=totmora, state='readonly')
    salida_totmora.config(bg='white', fg='black', font='Arial, 12')
    salida_totmora.grid(row=3, column=3, padx=10, pady=10)



    # -------------------VENTAS TOTALES (SUMA DEL COSTO DE VENTA/FRUTA)--------------------

    label_salida_totales = Label(frame_principal, text='Valor Venta $: ', font='Arial, 12')
    label_salida_totales.config(bg='#BACDB0')
    label_salida_totales.grid(row=4, column=2, padx=10, pady=10, sticky='e')

    tot_general_fru = IntVar()
    salida_totgeneral = Entry(frame_principal, textvariable=tot_general_fru, state='readonly')
    salida_totgeneral.config(bg='white', fg='black', font='Arial, 12')
    salida_totgeneral.grid(row=4, column=3, padx=10, pady=10)



    # -------------------CÁLCULO DEL DESCUENTO---------------------

    label_descuento = Label(frame_principal, text='Descuento Recibido $: ', font='Arial, 12')
    label_descuento.config(bg='#BACDB0')
    label_descuento.grid(row=5, column=1, padx=10, pady=10, sticky='w')

    resultado_descuento = IntVar()
    salida_gen_descuento = Entry(frame_principal, textvariable=resultado_descuento, state='readonly')
    salida_gen_descuento.config(bg='white', fg='black', font='Arial, 12')
    salida_gen_descuento.grid(row=5, column=2, padx=10, pady=10)



    # ---------------------APLICAR EL DESCUENTO AL TOTAL FRUTAS---------------------------

    label_aplicar = Label(frame_principal, text='Valor con descuento $: ', font='Arial, 12')
    label_aplicar.config(bg='#BACDB0')
    label_aplicar.grid(row=6, column=1, padx=10, pady=10, sticky='w')

    set_discount = IntVar()
    salida_gen_discount = Entry(frame_principal, textvariable=set_discount, state='readonly')
    salida_gen_discount.config(bg='white', fg='black', font='Arial, 12')
    salida_gen_discount.grid(row=6, column=2, padx=10, pady=10)



    # ----------------------BOTONES (PROCESAR, LIMPIAR, CERRAR Y AYUDA)-----------------------
    #--------------BOTON PROCESAR-------------------
    btn = Button(frame_principal,
                 text='Procesar',
                 width=12,
                 height=1,
                 command=frutas,
                 font='Arial, 12',
                 activebackground='#00B4D8')
    btn.config(bg='#90E0EF', cursor='hand2')
    btn.grid(row=8,
             column=1,
             padx=10,
             pady=10,
             sticky='e')



    # --------------BOTON CERRAR-------------------
    btn1 = Button(frame_principal,
                  text='Cerrar',
                  width=12,
                  height=1,
                  command=salida,
                  font='Arial, 12',
                  activebackground='#00B4D8')
    btn1.config(bg='#90E0EF', cursor='hand2')
    btn1.grid(row=8,
              column=3,
              padx=10,
              pady=10,
              sticky='e')




# -----------------------FUNCIÓN LIMPIAR ENTRADAS FRUTAS VENTANA PRINCIPAL----------------------
    def limpiar():
        entrada_mango.delete('0', 'end')
        entrada_fresa.delete('0', 'end')
        entrada_mora.delete('0', 'end')
        salida_fru_vendidas.delete('1', 'end')
        frut_vendidas.set('')
        totmango.set('')
        totfresa.set('')
        totmora.set('')
        tot_general_fru.set('')
        resultado_descuento.set('')
        set_discount.set('')






# -----------------BOTÓN LIMPIAR ENTRADAS FRUTAS------------------------------
    btn2 = Button(frame_principal, text='Limpiar', width=12, height=1, command=limpiar, font='Arial, 12',
                  activebackground='#00B4D8')
    btn2.config(bg='#90E0EF', cursor='hand2')
    btn2.grid(row=8, column=2, padx=10, pady=10, sticky='e')



    # --------------FUNCION VENTANA AYUDA-------------------
    def ayuda():

        # -----------------------DISEÑO VENTANA AYUDA-----------------------
        frame_ayuda = Toplevel()
        frame_ayuda.title('Información')
        frame_ayuda.config(bg='#40916C')
        frame_ayuda.geometry('435x350+450+180')
        frame_ayuda.geometry('435x350+450+180')
        frame_ayuda.resizable(False, False)
        frame_ayuda.iconbitmap('pregunta1.ico')

        headed_uso_programa_label = Label(frame_ayuda, bg='#40916C', text='Uso del programa:',
                                          justify='center', font=('Arial', 12))
        headed_uso_programa_label.grid(row=0, column=0, pady=5, padx=5)

        headed_tener_cuenta_label = Label(frame_ayuda, bg='#40916C', text='Para tener en cuenta:',
                                          justify='center', font=('Arial', 12))
        headed_tener_cuenta_label.grid(row=2, column=0, padx=5, pady=5)

        instruccions_label = Label(frame_ayuda,
                                   bg='#40916C',
                                   text='1) Dar clcik sobre los espacios en blanco e ingresar la\n'
                                        '   cantidad (libras) de frutas.\n'
                                        '2) Presionar el botón PROCESAR para iniciar la ejecución.\n'
                                        '3) Para introducir nuevos valores, presionar LIMPIAR.\n'
                                        '4) Para salir del programa, presionar BORRAR.\n'
                                        '5) Para notificar un problema, presionar COMENTARIO',
                                   justify='left', font=('Arial', 12))
        instruccions_label.grid(row=1, column=0, pady=5, padx=5)

        instruccions_2_label = Label(frame_ayuda,
                                     bg='#40916C',
                                     text='a) Ingresar SOLAMENTE valores POSITIVOS.\n'
                                          'b) Ingresar valores enteros (ej.: 1, 2,...,etc.).\n'
                                          'c) El programa NO acumula los resultados.', justify='left',
                                     font=('Arial', 12))
        instruccions_2_label.grid(row=3, column=0, padx=5, pady=5)

        # --------------FUNCION SALIR DE LA VENTANA AYUDA-------------------

        def salir_ayuda():
            frame_ayuda.withdraw()

        # ------------------------------------BOTON CERRAR VENTANA AYUDA------------------------------

        close_button = Button(frame_ayuda,
                              text='Cerrar',
                              width=12,
                              height=1,
                              command=salir_ayuda,
                              font='Arial, 12',
                              activebackground='#00B4D8')
        close_button.config(bg='#90E0EF', cursor='hand2')
        close_button.grid(row=4,
                          column=0,
                          padx=5,
                          pady=10,
                          sticky='e')

        #--------------------------- FUNCION ENVIAR UN COMENTARIO DEL PROGRAMA (CORREO)------------------------

        def enviar_comentario():

            #----------------VENTANA COMENTARIO-------------------------
            frame_comment = Toplevel()
            frame_comment.config(bg='#C8B6FF')
            frame_comment.geometry('660x236+310+200')
            frame_comment.resizable(False, False)
            frame_comment.title('Notificar un problema')
            frame_comment.iconbitmap('enviar1.ico')

            label_mensaje1 = Label(frame_comment, text='Mensaje', bg='#C8B6FF', font=('Arial', 12))
            label_mensaje1.grid(row=1, column=0, padx=10, pady=10, sticky='e')

            label_titulo1 = Label(frame_comment, text='Asunto', bg='#C8B6FF', font=('Arial', 12))
            label_titulo1.grid(row=0, column=0, padx=10, pady=10, sticky='e')

            alert = Label(frame_comment, text='', font=('Arial', 12), fg='red', bg='#C8B6FF',)
            alert.grid(row=5, sticky='s', columnspan=3)

            mensaje_send = StringVar()
            headed = StringVar()

            # ------------------ENTRADA MENSAJE---------------------
            mensaje1 = Entry(frame_comment, width=40, textvariable=mensaje_send, font=('Arial', 12),
                             cursor='hand2')
            mensaje1.grid(row=1, column=1, padx=10, pady=10, sticky='w')

            #--------------------------ENTRADA ASUNTO---------------------------------------
            titulo1 = Entry(frame_comment, width=40, textvariable=headed, font=('Arial', 12),
                            cursor='hand2')
            titulo1.grid(row=0, column=1, pady=10, padx=10, sticky='w')

            scroll_horizontal = Scrollbar(frame_comment, command=mensaje1.xview)
            scroll_horizontal.grid(row=2, column=1, sticky='nsew', padx=5, pady=5)
            mensaje1.config(xscrollcommand=scroll_horizontal.set)



# -----------------------FUNCION ENVIAR MENSAJE--------------------------
            def enviar_mensaje():
                try:
                    message = mensaje_send.get()
                    asunto = headed.get()
                    if message == '' or asunto == '':
                        alert.config(text='Todos los campos deben estar llenos')
                        return
                    else:
                        message = 'Subject: {}\n\n{}'.format(asunto, message)
                        server = smtplib.SMTP(host='smtp.gmail.com', port=587)

                        server.starttls()
                        server.login(user='cabreratoronicolas@gmail.com', password='pfqsiejkgdurqemk')

                        server.sendmail(from_addr='cabreratoronicolas@gmail.com', to_addrs='variadosdocs@gmail.com',
                                        msg=message)
                        alert.config(text='El mensaje se ha enviado con éxito', fg='green')
                except Exception as e:
                    alert.config(text='Error al enviar el mensaje', fg='red')
                    print(e)

# -----------------------FUNCION LIMPIAR LOS CAMPOS DEL ENVIO DE CORREO------------------------------------
            def limpiar_campos():
                mensaje1.delete('0', 'end')
                titulo1.delete('0', 'end')
                alert.destroy()

# -----------------------FUNCION SALIR DE LA VENTANA ENVIO DE COMENTARIO-----------------------
            def salir_comment():
                frame_comment.withdraw()

# -----------------------BOTÓN ENVÍO DE EMAIL-----------------------
            btn_send_email = Button(frame_comment, text='Enviar', width=12, height=1,
                                    command=enviar_mensaje, font=('Arial', 12))
            btn_send_email.config(bg='#90E0EF', cursor='hand2')
            btn_send_email.grid(row=4, column=0, pady=10, padx=10)

# -----------------------BOTÓN LIMPIAR CAMPOS DE ENVIO EMAIL-----------------------
            btn_limpiar_campos = Button(frame_comment, text='Limpiar', width=12, height=1,
                                        command=limpiar_campos, font=('Arial', 12))
            btn_limpiar_campos.config(bg='#90E0EF', cursor='hand2')
            btn_limpiar_campos.grid(row=4, column=1, pady=10, padx=10)

# -----------------------BOTÓN DE SALIR DE LA VENTANA COMENTARIO-----------------------
            btn_salir_comment = Button(frame_comment, text='Salir', width=12, height=1,
                                       command=salir_comment, font=('Arial', 12))
            btn_salir_comment.config(bg='#90E0EF', cursor='hand2')
            btn_salir_comment.grid(row=4, column=2, pady=10, padx=10)


# -----------------------BOTÓN ABRIR VENTANA COMENTARIO-----------------------
        btn_enviar_comment = Button(frame_ayuda, text='Comentario',
                                    width=12,
                                    height=1,
                                    command=enviar_comentario,
                                    font='Arial, 12',
                                    activebackground='#00B4D8')
        btn_enviar_comment.config(bg='#90E0EF', cursor='hand2')
        btn_enviar_comment.grid(row=4,
                                column=0,
                                padx=10,
                                pady=10,
                                sticky='w')

    # --------------BOTON AYUDA   FRAME PRINCIPAL-------------------
    btn3 = Button(frame_principal, text='Ayuda',
                  width=12,
                  height=1,
                  command=ayuda,
                  font='Arial, 12',
                  activebackground='#00B4D8')
    btn3.config(bg='#90E0EF', cursor='hand2')
    btn3.grid(row=8,
              column=0,
              padx=10,
              pady=10,
              sticky='e')


root.mainloop()
