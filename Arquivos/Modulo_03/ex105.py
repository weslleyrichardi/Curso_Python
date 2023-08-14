def notas(*nota, sit = False):
    planilha = {}
    planilha["Total"] = len(nota),
    planilha["Maior"] = max(nota),
    planilha["Menor"] = min(nota),
    planilha["Media"] = sum(nota)/len(nota)
    if sit:
        if planilha["Media"] >= 7:
            planilha["Situação"] = "Boa"
        else:
            planilha["Situação"] = "Ruim"
    return planilha        
    
    


resp = notas(2, 8.6, sit=True)
print(resp)
