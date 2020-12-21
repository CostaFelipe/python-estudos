horas = int(input('Digite as horas: '))
taxa  = float(input('Digite a taxa: '))

if horas > 40:
    extra_taxa = int(horas - 40) * 1.5 * 10
    pagamento = (horas * taxa) + extra_taxa
else:
    pagamento = horas * taxa

print(pagamento)

