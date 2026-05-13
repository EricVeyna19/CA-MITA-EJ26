# p160-ventas.py
# Simular un sistema de control de ventas

import os


class Venta:
    def __init__(self, articulo, cantidad, precio):
        self.articulo = articulo
        self.cantidad = cantidad
        self.precio = precio
        self.total = cantidad * precio

    def __str__(self):
        return (
            f'Articulo: {self.articulo:<15} '
            f'Cantidad: {self.cantidad:>10.2f} '
            f'Precio: ${self.precio:>10,.2f} '
            f'Total: ${self.total:>10,.2f}'
        )


class Cliente:
    def __init__(self, rfc, nombre, domicilio, correo):
        self.rfc = rfc
        self.nombre = nombre
        self.domicilio = domicilio
        self.correo = correo
        self.ventas = list()

    def agregarVenta(self, venta):
        self.ventas.append(venta)

    def totalVentas(self):
        total = 0
        for venta in self.ventas:
            total += venta.total
        return total

    def __str__(self):
        return (
            f'Cliente -> [ '
            f'Nombre: {self.nombre:<20} '
            f'RFC: {self.rfc:<12} '
            f'Domicilio: {self.domicilio:<20} '
            f'Correo: {self.correo:<30} '
            f']'
        )


class Tienda:
    def __init__(self, nombre, domicilio, propietario):
        self.nombre = nombre
        self.domicilio = domicilio
        self.propietario = propietario
        self.clientes = list()

    def agregarCliente(self, cliente):
        self.clientes.append(cliente)

    def totalVentas(self):
        total = 0
        for cliente in self.clientes:
            total += len(cliente.ventas)
        return total

    def totalImporteVentas(self):
        total = 0
        for cliente in self.clientes:
            total += cliente.totalVentas()
        return total

    def __str__(self):
        return (
            f'Tienda -> [ '
            f'Nombre: {self.nombre}, '
            f'Domicilio: {self.domicilio}, '
            f'Propietario: {self.propietario} '
            f']'
        )


def main():

    print('\033[H\033[J')
    os.system('cls' if os.name == 'nt' else 'clear')

    print('Inicio del programa en la funcion main() principal:\n')

    # tienda
    mitienda = Tienda(
        nombre='Ferreteria Las Lomas',
        domicilio='Av Luis Moya 345',
        propietario='Carlos Castaneda'
    )

    # clientes
    mitienda.agregarCliente(
        Cliente(
            rfc='JELI120240',
            nombre='Felipe Calderon',
            domicilio='Las Lomas 123',
            correo='calde@msn.com'
        )
    )

    mitienda.agregarCliente(
        Cliente(
            rfc='PEÑA121250',
            nombre='Enrique Peña',
            domicilio='5 de Mayo 321',
            correo='quique@gmail.com'
        )
    )

    mitienda.agregarCliente(
        Cliente(
            rfc='AMLO101145',
            nombre='Andres Lopez',
            domicilio='Palacio Nacional 321',
            correo='peje@yahoo.com'
        )
    )

    mitienda.agregarCliente(
        Cliente(
            rfc='GELA666666',
            nombre='Xochitl Gelatinas',
            domicilio='Danone 123',
            correo='xochitl@presidencia.gob.mx'
        )
    )

    # ventas a los clientes
    mitienda.clientes[0].agregarVenta(
        Venta(articulo='Martillo', cantidad=10, precio=60.5)
    )

    mitienda.clientes[0].agregarVenta(
        Venta(articulo='Pala', cantidad=2, precio=1170.55)
    )

    mitienda.clientes[1].agregarVenta(
        Venta(articulo='Clavo', cantidad=2.5, precio=160.34)
    )

    mitienda.clientes[1].agregarVenta(
        Venta(articulo='Cinta de Aislar', cantidad=5, precio=71.34)
    )

    mitienda.clientes[1].agregarVenta(
        Venta(articulo='Pinzas', cantidad=10, precio=650.33)
    )

    mitienda.clientes[2].agregarVenta(
        Venta(articulo='Thiner', cantidad=50, precio=65.00)
    )

    # Reporte 
    print(f'\nReporte de Ventas: {mitienda}\n')

    print(f'Total de clientes       : {len(mitienda.clientes)}')
    print(f'Total ventas realizadas : {mitienda.totalVentas()}')

    print('\nClientes:')
    for cliente in mitienda.clientes:
        print(cliente)

    print('\nVentas de cada cliente:')

    for cliente in mitienda.clientes:
        print(f'\n{cliente.rfc} - {cliente.nombre} - Total: ${cliente.totalVentas():,.2f}')
        print('-' * 80)

        if len(cliente.ventas) == 0:
            print('Este cliente no tiene ventas registradas.')
        else:
            for venta in cliente.ventas:
                print(f'- {venta}')

    print(f'\nTotal importe ventas : ${mitienda.totalImporteVentas():,.2f}')

    # Reporte
    print('\nREPORTE RESUMEN')
    print('=' * 80)
    print(f'Nombre de la tienda       : {mitienda.nombre}')
    print(f'Domicilio                 : {mitienda.domicilio}')
    print(f'Propietario               : {mitienda.propietario}')
    print(f'Total de clientes         : {len(mitienda.clientes)}')
    print(f'Total de ventas realizadas: {mitienda.totalVentas()}')
    print(f'Total vendido             : ${mitienda.totalImporteVentas():,.2f}')

    if mitienda.totalVentas() > 0:
        promedio = mitienda.totalImporteVentas() / mitienda.totalVentas()
        print(f'Promedio por venta        : ${promedio:,.2f}')
    else:
        print('Promedio por venta        : $0.00')

    print('=' * 80)


# Programa principal
if __name__ == '__main__':
    main()