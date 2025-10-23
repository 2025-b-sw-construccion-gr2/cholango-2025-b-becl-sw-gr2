// app.js
const descuentos = require('./lib/descuentos');
const input = require('./lib/input');

async function main() {
  console.log("Bienvenido a la Calculadora de Descuentos y Promociones");

  try {
    const datos = await input.obtenerDatosUsuario();

    if (datos.opcion === '1') {
      const total = descuentos.aplicarDescuento(datos.precioUnitario, datos.cantidad, datos.valor);
      const subtotal = datos.precioUnitario * datos.cantidad;
      console.log(`Subtotal: $${subtotal.toFixed(2)} - Total con descuento: $${total.toFixed(2)}`);
    } else if (datos.opcion === '2') {
      const totalPromo = descuentos.aplicarPromocion(datos.cantidad, datos.precioUnitario, datos.promoX, datos.promoY);
      const subtotal = datos.precioUnitario * datos.cantidad;
      console.log(`Subtotal: $${subtotal.toFixed(2)} - Total con promoción: $${totalPromo.toFixed(2)}`);
    } else {
      console.log("Opción no válida. Use 1 o 2.");
    }

  } catch (error) {
    console.error("Error:", error.message);
  }
}

main();
