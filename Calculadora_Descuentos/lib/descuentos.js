// descuentos.js
// Biblioteca de funciones de descuentos y promociones

/**
 * Aplica un descuento porcentual al precio total
 */
function aplicarDescuento(precioUnitario, cantidad, porcentaje) {
  if (porcentaje < 0 || porcentaje > 100) {
    throw new Error("El porcentaje debe estar entre 0 y 100");
  }
  const subtotal = precioUnitario * cantidad;
  return subtotal - (subtotal * porcentaje / 100);
}

/**
 * Calcula el total con promoción tipo "compra X y llévate Y gratis"
 * Por ejemplo, promoX = 2, promoY = 1 → "compras 2 y llevas 1 gratis"
 */
function aplicarPromocion(cantidad, precioUnitario, promoX, promoY) {
  const grupos = Math.floor(cantidad / (promoX + promoY));
  const resto = cantidad % (promoX + promoY);
  const pagados = (grupos * promoX) + Math.min(resto, promoX);
  return pagados * precioUnitario;
}

module.exports = {
  aplicarDescuento,
  aplicarPromocion
};