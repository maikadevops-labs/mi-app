def total_con_iva(monto: float, iva: float = 0.21) -> float:
    """Devuelve el monto con IVA, redondeado a 2 decimales."""
    return round(monto * (1 + iva), 2)
