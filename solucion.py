class Persona:
    def __init__(self,nombre,apellido,edad,dni):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__edad=edad
        self.__dni=dni

    def __str__(self):
        datos = 'Nombre: '+ self.__nombre
        datos += '\nApellido: '+ self.__apellido
        datos += '\nEdad: '+ str(self.__edad)
        datos += '\nDNI: '+ str(self.__dni)
        return datos
        
class Cuenta:
    def __init__(self,titular,cantidad=0):
        self.__titular=titular
        self.__cantidad=cantidad
    def __str__(self):
        return '\n'+str(self.__titular)+ '\nCantidad: '+str(self.__cantidad)+'\n'
        
    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        datos = str(self.__titular) + ' $' + str(self.__cantidad)
        return datos

    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self,cantidad):
        self.__cantidad -= cantidad

    def saldoDeudor(self):
        saldoTotal=0
        if self.__cantidad < 0:
            saldoTotal += self.__cantidad
            return saldoTotal

class Banco:
    
    def __init__(self,cuentas=None,nombre='Galicia'):
        self.__nombre=nombre
        if cuentas != None:
            self.__cuentas=cuentas
        else:
            self.__cuentas = []

    def __str__(self):
        cadena='Banco: '+self.__nombre
        for i in self.__cuentas:
            cadena+= str(i)+'\n'
        return cadena

    @property
    def cuentas(self):
        return self.__cuentas

    def agregar(self,nuevaCuenta):
        self.__cuentas.append(nuevaCuenta)
    
cuenta1=Banco([Cuenta(Persona('Pepe','Juarez',2553234,43),-125000)])
cuenta2=Banco([Cuenta(Persona('Jose','Gimenez',24333222,42),-10000)])
cuenta3=Banco([Cuenta(Persona('Manuel','Paez',29334232,28),-6000)])
cuenta4=Banco([Cuenta(Persona('Pedro','Serrano',32545234,21),24000)])

cuentasBanco=Banco([cuenta1,cuenta2,cuenta3])
cuentasBanco.agregar(cuenta4)
cuentasBanco.agregar(Banco([Cuenta(Persona('Luis','Perez',24333255,35),200000)]))
print(cuentasBanco)
