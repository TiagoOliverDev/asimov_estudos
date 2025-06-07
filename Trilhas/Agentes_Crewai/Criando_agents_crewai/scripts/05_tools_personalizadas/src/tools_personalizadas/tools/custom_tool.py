from crewai.tools import BaseTool
import yfinance as yf
import json
from typing import Type

from pydantic import BaseModel, Field

class RetornaCotacaoAtualInput(BaseModel):
    '''Argumentos da tool RetornaCotacaoAtual'''
    acao: str = Field(description='Ticker da ação conforme Yahoo Finance (ex: AAPL para Apple, PETR4.SA para Petrobras, etc)')


class RetornaCotacaoAtual(BaseTool):
    name: str = 'Retorna cotação atual'
    description: str = 'Obtém a cotação mais recente de uma ação através da API do Yahoo Finance'
    args_schema: Type[BaseModel] = RetornaCotacaoAtualInput

    def _run(self, acao: str) -> str:
        try:
            ticker = yf.Ticker(acao)
            dados = ticker.history(period="1d")  

            if not dados.empty:
                ultima_linha = dados.iloc[-1]
                return json.dumps({
                    "acao": acao,
                    "preco_atual": ultima_linha["Close"],
                    "ultima_atualizacao": ultima_linha.name.strftime("%Y-%m-%d %H:%M:%S"),
                })
            else:
                return json.dumps({"erro": "Nenhum dado encontrado para a ação fornecida."})
        except Exception as e:
            return json.dumps({"erro": str(e)})