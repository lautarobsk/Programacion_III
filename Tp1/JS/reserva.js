function Reserva(origen, destino, fechaVuelo, clase, cantidadPasajes, ubicacion, numeroSilla, nombre, dni, fechaNacimiento, sexo) {
    this.origen = origen;
    this.destino = destino;
    this.fechaVuelo = fechaVuelo;
    this.clase = clase;
    this.cantidadPasajes = cantidadPasajes;
    this.ubicacion = ubicacion;
    this.numeroSilla = numeroSilla;
    this.nombre = nombre;
    this.dni = dni;
    this.fechaNacimiento = fechaNacimiento;
    this.sexo = sexo;

    this.mostrarInfo = function() {
        return `Reserva de ${this.nombre} (${this.dni})\n` +
               `Vuelo: ${this.origen} → ${this.destino} el ${this.fechaVuelo}\n` +
               `Clase: ${this.clase}, Asiento: ${this.ubicacion} ${this.numeroSilla}\n` +
               `Cantidad de pasajes: ${this.cantidadPasajes}`;
    };
}

