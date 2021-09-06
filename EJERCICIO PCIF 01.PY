kilorec = float(input())
	fijo = 300
	iva = 0.20
	if kilorec<=300:
		pago = fijo
	else:
		if kilorec<=1000:
			pago = fijo+50*700+100*(kilorec-1000)
		else:
			pago = fijo+50*(kilorec-1000)
	montoiva = iva*pago
	pago = float(input())
	montoiva = float(input())
