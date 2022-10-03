function calcularFatorialRecursivamente(n) {
  if (n === 1) {
    return 1;
  }

  return n * calcularFatorialRecursivamente(n - 1);
}

function calcularFatorial(fatorial) {
  if (isNaN(fatorial)) {
    return "Não existe fatorial de um texto";
  }

  if (!Number.isInteger(fatorial) || fatorial < 0) {
    return "Não existe fatorial de um número não natural";
  }

  if (fatorial === 0 || fatorial === 1) {
    return 1;
  }

  return calcularFatorialRecursivamente(fatorial);
}
