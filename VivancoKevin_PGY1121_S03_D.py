'''Fotocopia con login'''
#Login
flag=True;
#Poner nombres en la boleta
impresionBN=False;
impresioncolor=False;
fotocopia=False;
anillado=False;
preciofinal=0
descfinal=0

print("\nBienvenido a impresiones DuocUC, Inicie sesión para utilizar este beneficio.")

while flag==True:
    try:
        user=str(input("\nIngrese su nombre de usuario: "))
        password=int(input("Ingrese su contraseña:"))
        if (user=="fcalfun" and password==1234)or(user=="kvivanco" and password==3327):
            print(f"\n!Bienvenido {user}¡")
            flag2=True
            #Aquí comienza el segundo menú
            while flag2==True:
                try:
                    print("\n----------Menú Impresiones DuocUC----------")
                    print("\n(1) Seleccione su rol en la institución.")
                    print("(2) Tipo se servicio.")
                    print("(3) Pago.")
                    print("(4) Anular pedido.")
                    opcion=int(input("\nSeleccione una opcioón presente en el menú: "))

                    if opcion==1:
                        flag3=True
                        try:
                            #Aquí comienza el menú del rango de institución.
                            while flag3==True:
                                print("\n----------Menú rol en la institucion----------")
                                print("\n(1) Estudiante Diurno (10 porciento de descuento).")
                                print("(2) Estudiante Vespertino (20 porciento de descuento).")
                                print("(3) Administrativo (Sin descuento aplicable).")
                                opcion_b=int(input("\nSeleccione solo UN rago por impresión:"))
                                if opcion_b==1:
                                    descuento=10/100;
                                    flag3=False;
                                elif opcion_b==2:
                                    descuento=20/100;
                                    flag3=False;
                                elif opcion_b==3:
                                    descuento=0;
                                    flag3=False;
                                else:
                                    print("Solo debe ingresar el número de opciones presentes en el menú, vuelva a intentarlo.")
                        except ValueError:
                            print("El menú solo admite números como opción, vuelva a intentarlo.");

                    elif opcion==2:
                        flag4=True
                        #Aquí comienza el menú de impresiones.
                        try:
                            while flag4==True:
                                print("\n----------Menú Tipo de servivio----------")
                                print("(1) Impresión B/N $150")
                                print("(2) Impresión Color $300")
                                print("(3) Fotocopias $80")
                                print("(4) Anillados $5000")
                                print("(5) volver al menú")
                                opcion_c=int(input("\nSeleccione el o los servicios que desea utilizar: "))
                                if opcion_c==1:
                                    cantidadBN=int(input("¿Cuántas unidades desea llevar?: "))
                                    totalBN=cantidadBN*150
                                    preciofinal+=totalBN
                                    descuentoBN=totalBN*descuento;
                                    impresionBN=True;
                                elif opcion_c==2:
                                    cantidadcolor=int(input("¿Cuántas unidades desea llevar?: "))
                                    totalcolor=cantidadcolor*300
                                    preciofinal+=totalcolor
                                    descuentocolor=totalcolor*descuento
                                    impresioncolor=True;
                                elif opcion_c==3:
                                    cantidadfoto=int(input("¿Cuántas unidades desea llevar?: "))
                                    totalfoto=cantidadfoto*80
                                    preciofinal+=totalfoto
                                    descuentofoto=totalfoto*descuento
                                    fotocopia=True;
                                elif opcion_c==4:
                                    cantidadani=int(input("¿Cuántas unidades desea llevar?: "))
                                    totalani=cantidadani*5000
                                    preciofinal+=totalani
                                    descuentoani=totalani*descuento
                                    anillado=True;
                                elif opcion_c==5:
                                    flag4=False;
                                else:
                                    print("Solo debe ingresar el número de opciones presentes en el menú, vuelva a intentarlo.");
                        except ValueError:
                            print("El menú solo admite números como opción, vuelva a intentarlo.")
                    elif opcion==3:
                        flag5=True
                        #Aquí comienza la Boleta.
                        print("\n          Servicio de fotocopiado          \n")
                        print("-------------------------------------------\n")
                        if impresionBN==True:
                            print(f"{cantidadBN} Hojas B/N ${totalBN}")
                            print(f"Descuento {descuentoBN}")
                            descfinal+=descuentoBN;
                        if impresioncolor==True:
                            print(f"{cantidadcolor} Hojas B/N ${totalcolor}")
                            print(f"Descuento {descuentocolor}")
                            descfinal+=descuentocolor;
                        if fotocopia==True:
                            print(f"{cantidadfoto} Hojas B/N ${totalfoto}")
                            print(f"Descuento {descuentofoto}")
                            descfinal+=descuentofoto;
                        if anillado==True:
                            print(f"{cantidadani} Hojas B/N ${totalani}")
                            print(f"Descuento {descuentoani}")
                            descfinal+=descuentoani;
                        print(f"Subtotal {preciofinal}\n")
                        print("-------------------------------------------\n")
                        print(f"Total a pagar: {preciofinal-descfinal}\n")
                        print(f"\t¡Gracias por su compra!")
                        flag=False;
                        flag2=False;

                    elif opcion==4:
                        print("\nBoleta Anulada.");
                        cantidadBN=0
                        totalBN=0
                        descuentoBN=0
                        cantidadcolor=0
                        totalcolor=0
                        descuentocolor=0
                        cantidadfoto=0
                        totalfoto=0
                        descuentofoto=0
                        cantidadani=0
                        totalani=0
                        descuentoani=0
                        descfinal=0
                        preciofinal=0
                    else:
                        print("Solo debe ingresar el número de opciones presentes en el menú, vuelva a intentarlo.")
                except ValueError:
                    print("El menú solo admite números como opción, vuelva a intentarlo.")
        else:
            print("\nUsuario y/o contraseña incorrectos, vuelva a intentarlo")
    except ValueError:
        print("La contraseña solo admite números, no carácteres.")