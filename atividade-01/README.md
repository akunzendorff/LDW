# PokéApp - Aplicação Flask de Pokémons

Uma aplicação web completa desenvolvida em Flask para gerenciar Pokémons favoritos e uma Pokédex detalhada.

## 🚀 Funcionalidades

### 📱 Página Inicial
- Interface atrativa com design responsivo
- Navegação intuitiva com navbar Bootstrap
- Estatísticas rápidas sobre a aplicação
- Cards informativos sobre as funcionalidades

### ❤️ Pokémons Favoritos (Lista Simples)
- **Visualizar**: Veja todos os seus Pokémons favoritos em cards organizados (3 colunas)
- **Remover**: Exclua Pokémons da lista com confirmação
- **Layout responsivo**: Adaptação automática para diferentes tamanhos de tela
- **Interface limpa**: Design centralizado sem formulário de adição
- **Prevenção de duplicatas**: Não permite adicionar o mesmo Pokémon duas vezes
- **Nota**: Adição de novos favoritos disponível via rota POST `/favoritos`

### 📚 Pokédex (Dicionários e Tabela)
- **Cadastro completo**: Adicione Pokémons com informações detalhadas:
  - Nome
  - Tipo (ex: Elétrico, Fogo/Voador)
  - Nível (1-100)
  - HP (Pontos de Vida)
  - Região (Kanto, Johto, Hoenn, etc.)
- **Visualização em tabela**: Interface organizada com:
  - Badges coloridas para tipos
  - Barra de progresso para HP
  - Numeração automática
  - Ações de remoção
- **Estatísticas automáticas**: Cálculo de médias e totais

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework CSS**: Bootstrap 5.3.0
- **Ícones**: Font Awesome 6.0.0
- **Arquitetura**: MVC (Model-View-Controller)

## 📁 Estrutura do Projeto

```
atividade-01/
├── app.py                 # Arquivo principal da aplicação
├── controllers/
│   └── routes.py         # Rotas e lógica de negócio
├── views/
│   ├── base.html         # Template base com navbar e footer
│   ├── index.html        # Página inicial
│   ├── favoritos.html    # Gerenciamento de favoritos (lista)
│   └── pokedex.html      # Pokédex completa (tabela)
└── static/
    └── css/
        └── style.css     # Estilos customizados
```

## 🚀 Como Executar

1. **Instale as dependências**:
   ```bash
   pip install flask
   ```

2. **Execute a aplicação**:
   ```bash
   python app.py
   ```

3. **Acesse no navegador**:
   - Local: http://127.0.0.1:4000
   - Rede: http://[SEU_IP]:4000

## 🌐 Configurações

- **Porta**: 4000
- **Host**: 0.0.0.0 (acessível externamente)
- **Debug**: Ativo
- **Template Folder**: views/

## 📋 Rotas Disponíveis

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial |
| `/favoritos` | GET, POST | Gerenciar lista de favoritos |
| `/pokedex` | GET, POST | Gerenciar Pokédex completa |
| `/remover_favorito/<nome>` | GET | Remover Pokémon dos favoritos |
| `/remover_pokemon/<index>` | GET | Remover Pokémon da Pokédex |

## 🎨 Características do Design

- **Tema**: Gradiente azul/roxo inspirado no universo Pokémon
- **Responsivo**: Adaptável a todos os dispositivos
- **Animações**: Efeitos suaves de hover e transição
- **Cards translúcidos**: Efeito glassmorphism
- **Ícones temáticos**: Font Awesome com cores personalizadas

## 📊 Funcionalidades Especiais

### Lista de Favoritos
- Armazenamento em lista Python simples
- Interface em cards responsivos
- Contagem automática de itens
- Validação de duplicatas

### Pokédex
- Armazenamento em lista de dicionários
- Tabela responsiva com Bootstrap
- Formulário com validação HTML5
- Cálculos estatísticos automáticos:
  - Total de Pokémons
  - Nível médio
  - HP médio
  - Número de regiões diferentes

## 🔧 Personalização

O arquivo `static/css/style.css` contém:
- Animações CSS customizadas
- Cores temáticas para tipos de Pokémon
- Estilos responsivos
- Efeitos visuais avançados

## 📝 Observações

- Os dados são armazenados em memória (perdidos ao reiniciar)
- Aplicação configurada para desenvolvimento
- Interface totalmente em português
- Compatível com navegadores modernos

## 🎯 Requisitos Atendidos

✅ **3 rotas principais**: Início, Favoritos, Pokédex  
✅ **Navbar com navegação**: Bootstrap responsivo  
✅ **Lista simples**: Gerenciamento de favoritos  
✅ **Dicionários em tabela**: Pokédex detalhada  
✅ **Arquivos estáticos**: CSS customizado  
✅ **Bootstrap**: Framework CSS integrado  
✅ **Porta 4000**: Configuração personalizada  
✅ **Host 0.0.0.0**: Acessibilidade externa  
✅ **Debug ativo**: Modo de desenvolvimento  

---

**Desenvolvido com ❤️ e Flask**