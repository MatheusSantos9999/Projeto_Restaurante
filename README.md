🍽️ Sistema de Simulação de Restaurante

Um sistema modular desenvolvido em Python para simulação e gerenciamento de um ambiente de restaurante. O projeto abrange desde o controle de cardápio e estoque até a gestão de comandas, pagamentos, geração de dados fictícios (Faker), persistência e emissão de relatórios.

📂 Estrutura do Projeto

A arquitetura do projeto é dividida em módulos independentes e especializados:

├── Cardapio/               # Gerenciamento de itens do cardápio (ex: inserir_item.py)
├── ControleComanda/        # Gestão de comandas dos clientes (ex: comanda.py)
├── ControleEstoque/        # Controle de inventário e insumos (ex: estoque.py)
├── ControlePagamento/      # Processamento de pagamentos e fechamento (ex: pagamento.py)
├── EstruturaDados/         # Implementação de estruturas customizadas (ex: fila.py, lista_encadeada.py)
├── GeradorFaker/           # Geração de dados simulados/mockados (ex: gerador.py)
├── Persistencia/           # Manipulação e salvamento de dados
├── Relatorio/              # Geração de relatórios gerenciais e operacionais (ex: relatorio.py)
├── .gitignore              # Arquivos ignorados pelo controle de versão
└── main.py                 # Ponto de entrada principal da aplicação


🚀 Funcionalidades Principais

Gestão de Cardápio (Cardapio/): Cadastro, atualização e consulta de pratos, bebidas e itens disponíveis para os clientes.

Controle de Comandas (ControleComanda/): Abertura, lançamento de consumo, fechamento e acompanhamento de pedidos por mesa ou cliente utilizando estruturas de dados eficientes.

Controle de Estoque (ControleEstoque/): Monitoramento de insumos, baixa automática de estoque conforme os pedidos são realizados e alertas de reposição.

Processamento de Pagamento (ControlePagamento/): Simulação de diferentes formas de pagamento e fechamento de contas.

Estruturas de Dados Personalizadas (EstruturaDados/): Uso de filas e listas encadeadas para gerenciar o fluxo de atendimento e pedidos de forma otimizada.

Geração de Dados (GeradorFaker/): Criação rápida de dados realistas (clientes, produtos, comandas) para testes e simulações em larga escala.

Relatórios (Relatorio/): Emissão de resumos de vendas, consumo de estoque e desempenho do restaurante.

Persistência de Dados (Persistencia/): Mecanismos para salvar e carregar o estado da aplicação.

⚙️ Pré-requisitos e Instalação

Certifique-se de ter o Python 3.8+ instalado em sua máquina.

Clone o repositório ou baixe os arquivos do projeto:

git clone <url-do-repositorio>
cd <nome-da-pasta-do-projeto>


(Opcional) Crie e ative um ambiente virtual:

python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate


Instale as dependências necessárias (caso utilize bibliotecas externas como a Faker):

pip install -r requirements.txt


▶️ Como Executar

Para iniciar a simulação do sistema, execute o arquivo principal (main.py) na raiz do projeto:

python main.py


Siga as instruções exibidas no terminal ou na interface configurada para interagir com o sistema do restaurante.

🛠️ Tecnologias Utilizadas

Python: Linguagem principal utilizada no desenvolvimento da lógica de negócios.

Estruturas de Dados Nativas e Customizadas: Filas e Listas Encadeadas implementadas para simular o fluxo de atendimento.

Faker: Biblioteca para geração de dados de teste (mock).
