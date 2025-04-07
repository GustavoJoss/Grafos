import zipfile
import os

class Grafo:
    def __init__(self):
        self.adjacencia = {}
        self.vertices_requeridos = set()
        self.arestas_requeridas = []
        self.depot = None
        self.capacidade = None
        self.veiculos = None

    def adicionar_vertice(self, v):
        if v not in self.adjacencia:
            self.adjacencia[v] = []

    def adicionar_aresta(self, u, v):
        self.adicionar_vertice(u)
        self.adicionar_vertice(v)
        self.adjacencia[u].append(v)
        self.adjacencia[v].append(u)

    def grau_dos_vertices(self):
        graus = [len(vizinhos) for vizinhos in self.adjacencia.values()]
        return min(graus), max(graus)

    def componentes_conexas(self):
        visitado = set()
        componentes = 0

        def dfs(v):
            visitado.add(v)
            for vizinho in self.adjacencia[v]:
                if vizinho not in visitado:
                    dfs(vizinho)

        for v in self.adjacencia:
            if v not in visitado:
                componentes += 1
                dfs(v)
        return componentes

    def densidade(self):
        n = len(self.adjacencia)
        m = sum(len(v) for v in self.adjacencia.values()) // 2
        if n <= 1:
            return 0
        return 2 * m / (n * (n - 1))

    def estatisticas(self):
        print("Quantidade de vértices:", len(self.adjacencia))
        print("Quantidade de arestas:", len(self.arestas_requeridas))
        print("Vértices requeridos:", len(self.vertices_requeridos))
        print("Arestas requeridas:", len(self.arestas_requeridas))
        print("Densidade:", round(self.densidade(), 4))
        print("Componentes conexas:", self.componentes_conexas())
        grau_min, grau_max = self.grau_dos_vertices()
        print("Grau mínimo:", grau_min)
        print("Grau máximo:", grau_max)

    def carregar_arquivo(self, caminho):
        with open(caminho, 'r', encoding='utf-8', errors='ignore') as f:
            linhas = f.readlines()

        secao = None
        for linha in linhas:
            linha = linha.strip()
            if linha.startswith('Depot Node'):
                self.depot = int(linha.split(':')[1])
            elif linha.startswith('Capacity'):
                self.capacidade = int(linha.split(':')[1])
            elif linha.startswith('#Vehicles'):
                self.veiculos = int(linha.split(':')[1])
            elif linha.startswith('ReN.'):
                secao = 'ReN'
            elif linha.startswith('ReE.'):
                secao = 'ReE'
            elif linha.startswith('N') and secao == 'ReN':
                partes = linha.split()
                no = int(partes[0][1:])
                self.vertices_requeridos.add(no)
                self.adicionar_vertice(no)
            elif linha.startswith('E') and secao == 'ReE':
                partes = linha.split()
                if len(partes) < 3 or not partes[1].isdigit():
                    continue  
                u = int(partes[1])
                v = int(partes[2])
                self.arestas_requeridas.append((u, v))
                self.adicionar_aresta(u, v)


if __name__ == "__main__":
    caminho_zip = "202501_selected_instances.zip"
    pasta_destino = "instancias_extraidas"

    with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
        zip_ref.extractall(pasta_destino)

    caminho_exemplo = None
    for root, dirs, files in os.walk(pasta_destino):
        for file in files:
            if file.endswith(".dat"):
                caminho_exemplo = os.path.join(root, file)
                break
        if caminho_exemplo:
            break

    if caminho_exemplo:
        print(f"🗂️  Processando: {caminho_exemplo}")
        grafo = Grafo()
        grafo.carregar_arquivo(caminho_exemplo)
        grafo.estatisticas()
    else:
        print("Nenhum arquivo .dat encontrado no zip extraído.")
