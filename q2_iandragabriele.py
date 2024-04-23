import unittest
from q1_iandragabriele import *

class TestAcoesDePagamento(unittest.TestCase):
    def test_pagamento_em_dinheiro(self):
        #testando se o resultado é uma string
        resultado = processar_transacao(pagamento_em_dinheiro, deposito_bancario, pagamento_credito, obter_detalhes_transacao(tipo_transacao))
        self.assertIsInstance(resultado, str, "O resultado necessita ser do tipo string")
    def test_deposito_bancario(self):
        #testando se o resultado é o esperado
        resultado = processar_transacao(pagamento_em_dinheiro, deposito_bancario, pagamento_credito, obter_detalhes_transacao(tipo_transacao))
        self.assertEqual(resultado, {"cliente": "Usuario", "tipo": "deposito_bancario",
                                      "banco": "Bradesco", "status": "confirmado"})
    def test_pagamento_credito(self):
        resultado = processar_transacao(pagamento_em_dinheiro, deposito_bancario, pagamento_credito, obter_detalhes_transacao(tipo_transacao))
        self.assertEqual(resultado, {"cliente": "Usuario", "tipo": "credito",
                                      "cartao": "Mastercard", "status": "confirmado"})

if __name__ == "__main__":
    unittest.main()
