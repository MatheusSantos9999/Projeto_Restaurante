class Pagamento:
    def __init__(self, nome:str, numero_pagamento:int, forma_pagamento:str, valor_total:float, data_hora:str):
        self.nome_pagador = nome
        self.numero_comanda = numero_pagamento
        self.forma_pagamento = forma_pagamento
        self.valor_total_pago = valor_total
        self.data_hora_pagamento = data_hora
