import json
import os


class JsonRepository:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def ler(self):
        if not os.path.exists(self.caminho_arquivo):
            return {}

        with open(self.caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            if not conteudo:
                return {}
            return json.loads(conteudo)

    def salvar(self, dados):
        with open(self.caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def gerar_novo_id(self, dados):
        if not dados:
            return "1"
        return str(max(map(int, dados.keys())) + 1)

    def deletar_e_reindexar(self, dados, item_id):
        if item_id not in dados:
            return None

        del dados[item_id]

        dados_reindexados = {}
        for indice, chave_antiga in enumerate(sorted(dados.keys(), key=int), start=1):
            dados_reindexados[str(indice)] = dados[chave_antiga]

        self.salvar(dados_reindexados)
        return dados_reindexados