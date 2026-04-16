# Web Scraping de Preços

Este projeto realiza web scraping para extrair nomes e preços de produtos em uma página web de demonstração.

O script utiliza Selenium para automatizar a navegação e coletar os dados diretamente dos elementos HTML da página.

## ⚙️ Como funciona

O código busca elementos específicos através de seletores (como tags, classes ou XPath) para capturar:

- Nome do produto
- Preço do produto

Esses dados são então salvos em um arquivo `.csv`.

## ⚠️ Observações importantes

Este método depende da estrutura HTML da página.

Ou seja, para funcionar em outros sites, é necessário ajustar os seletores utilizados no código (tags, classes ou atributos), pois cada site possui uma estrutura diferente.

## 🧰 Tecnologias utilizadas

- Python
- Selenium
- ChromeDriver

## 🎯 Objetivo

Projeto criado para estudo de automação web e web scraping.
