# 🐍 Estudos de Python

Repositório com os exercícios práticos e arquivos de aula que fiz enquanto aprendo Python. Cada exercício parte de um enunciado em PDF e avança do básico (strings e `print`) até a organização do código em módulos e a leitura de arquivos JSON. O tema comum dos exercícios é a **insulina humana**: sequência de aminoácidos, peso molecular e percentual de erro.

Estes estudos fazem parte do programa **Desenvolvimento Web com Cloud AWS / Re/Start**, oferecido pela **Generation Brasil**.

- **Versão do Python:** 3.14
- **Editor:** VS Code

## 📸 Visão geral

O print abaixo mostra a estrutura das pastas e o exercício de módulos, que reúne funções, declaração de variáveis, estruturas condicionais, laços de repetição e importação de módulos.

![Exercício de módulos](PrintExercicio%20de%20modulos.png)

## 📚 Exercícios

### Exercício 1 — Limpeza de uma sequência com expressões regulares
Leitura de um arquivo de texto (`preproinsulin-seq.txt`) com a sequência "suja" copiada de um site e limpeza até sobrar só os 110 aminoácidos.
- Leitura de arquivo com `open()` e `with`
- Módulo `re` e `re.sub()` para remover números, barras (`//`), espaços, a palavra `ORIGIN` e quebras de linha
- Uma variável para cada etapa da limpeza, para acompanhar a transformação do texto

### Exercício 2 — Tipos de dados
Percorre uma lista com valores de tipos diferentes (`int`, `float`, `bool` e `str`, inclusive o texto `"0"`) e mostra o tipo e o valor de cada item.
- Listas e laço `for`
- Função `type()` e conversão com `str()`

### Exercício 3 — Variáveis, `print()` e peso molecular da insulina
- Variáveis com a sequência da pré-proinsulina e de suas partes, concatenação de strings com `+` e `print()`
- Dicionário com o peso de cada aminoácido
- Contagem com `count()` dentro de uma compreensão de dicionário
- Peso molecular aproximado com `sum()` e **percentual de erro** em relação ao peso real (5807.63), usando `abs()`

### Exercício de Funções 1 — Calculadora
Calculadora de terminal com as quatro operações básicas.
- `input()` e conversão de tipos (`float`)
- `if / elif / else` para escolher a operação
- Tratamento de **divisão por zero** e de **operação inválida**
- Laço `while` para repetir enquanto o usuário responder `s`
- Cada operação implementada como função (`somar`, `subtrair`, `multiplicar`, `dividir`)

### Exercício de Funções 2 — Cifra de César
Criptografia e descriptografia de mensagens com funções definidas pelo usuário.
- `getDoubleAlphabet`, `getMessage`, `getCipherKey`
- `encryptMessage`: laço `for`, `find()`, indexação de strings e `upper()`
- `decryptMessage`: reaproveita a `encryptMessage` com a chave **negativa**
- `runCaesarCipherProgram`: função principal que organiza o fluxo

### Exercício de Módulos — JSON
Separação do programa em módulos e leitura de dados externos.
- `files/insulin.json`: sequências, pesos dos aminoácidos e peso molecular real
- `jsonFileRead.py`: função `readJsonFile()` com `open`, `with`, `json.load` e `try/except IOError`
- `calcularPesoJson.py`: importa o módulo, acessa os dados por chaves e calcula o peso molecular e o percentual de erro

## 🗂️ Estrutura de pastas

> Ajuste os nomes abaixo conforme as pastas do seu repositório.

```
aulas-python/
├── (arquivos práticos das aulas)
├── (pastas dos exercícios 1, 2, 3 e de funções)
└── exercicioModulos/
    ├── files/
    │   └── insulin.json
    ├── jsonFileRead.py
    └── calcularPesoJson.py
```

## ▶️ Como executar

1. Clone o repositório:
   ```bash
   git clone <URL-DO-REPOSITORIO>
   ```
2. Entre na pasta do exercício desejado e execute o arquivo. Para o de módulos, rode a partir da própria pasta, para que o caminho `files/insulin.json` seja encontrado:
   ```bash
   cd aulas-python/exercicioModulos
   python calcularPesoJson.py
   ```

Saída esperada do exercício de módulos:

```
The rough molecular weight of insulin: 6696.42
Percent error: 15.3%
```

## 🎯 Conceitos praticados

`variáveis` · `strings` · `tipos de dados` · `listas` · `input/print` · `conversão de tipos` · `operadores` · `if/elif/else` · `while` · `for` · `funções (def/return)` · `dicionários` · `compreensão de dicionário` · `expressões regulares (re)` · `leitura de arquivos` · `módulos e import` · `JSON` · `try/except`

## 🚧 Status

Em andamento. Novos exercícios serão adicionados conforme o avanço dos estudos.
