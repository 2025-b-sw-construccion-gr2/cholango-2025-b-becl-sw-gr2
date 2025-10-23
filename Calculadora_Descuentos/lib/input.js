// input.js
const readline = require('readline');

function obtenerDatosUsuario() {
  return new Promise((resolve) => {
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });

    console.log("\nOpciones:");
    console.log("1. Descuento porcentual");
    console.log("2. Promoción tipo X por Y");

    rl.question("Seleccione una opción (1-2): ", (opcion) => {
      rl.question("Ingrese el precio unitario: ", (precioStr) => {
        rl.question("Ingrese la cantidad de productos: ", (cantidadStr) => {

          if (opcion === '1') {
            rl.question("Ingrese el porcentaje de descuento: ", (porcentajeStr) => {
              rl.close();
              resolve({
                opcion,
                precioUnitario: parseFloat(precioStr),
                cantidad: parseInt(cantidadStr),
                valor: parseFloat(porcentajeStr)
              });
            });
          } else if (opcion === '2') {
            rl.question("Ingrese cuántos productos se pagan (X): ", (xStr) => {
              rl.question("Ingrese cuántos productos se llevan gratis (Y): ", (yStr) => {
                rl.close();
                resolve({
                  opcion,
                  precioUnitario: parseFloat(precioStr),
                  cantidad: parseInt(cantidadStr),
                  promoX: parseInt(xStr),
                  promoY: parseInt(yStr)
                });
              });
            });
          } else {
            rl.close();
            resolve({ opcion: '0' }); // opción no válida
          }

        });
      });
    });
  });
}

module.exports = {
  obtenerDatosUsuario
};
