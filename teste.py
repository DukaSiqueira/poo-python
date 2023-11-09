def criar_conta(numero, titular, saldo, limite):
    return {"número": numero, "titular": titular, "saldo": saldo, "limite": limite}


def deposita(conta, valor):
    conta["saldo"] += valor


def saca(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print(conta["saldo"])
