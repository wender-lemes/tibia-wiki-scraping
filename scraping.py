from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.tibiawiki.com.br/wiki/Criaturas").content

soup = BeautifulSoup(html, 'html.parser')

tabelasPaginaPrincipal = soup.findAll("table")

tabelaCategorias = tabelasPaginaPrincipal[6]

categorias = tabelaCategorias.findAll("a")

for categoria in categorias:
	linkCategoria = 'https://www.tibiawiki.com.br' + categoria.get('href')
	nomeCategoria = categoria.text
	if nomeCategoria:
		paginaCategoria = requests.get(linkCategoria).content
		soupPaginaCategoria = BeautifulSoup(paginaCategoria, 'html.parser')

		tabelas = soupPaginaCategoria.findAll("table", id="tabelaDPL")
		tabelaDesejada = tabelas[0]
		primeiraLinha = tabelaDesejada.find("tr")

		linhas = []

		for proximaLinha in primeiraLinha.findNextSiblings():
			if proximaLinha.name == 'tr':
				linhas.append(proximaLinha)

		for linha in linhas:
			colunas = linha.findAll("td")
			nome = colunas[0].find("a").string
			hp = colunas[2].text.strip()
			xp = colunas[3].text.strip()
			charms = colunas[4].text.strip()
			link = 'https://www.tibiawiki.com.br' + colunas[0].find("a").get('href')
			print (nomeCategoria + ';', nome + ';', hp + ';', xp + ';', link + ';', charms + ';')
