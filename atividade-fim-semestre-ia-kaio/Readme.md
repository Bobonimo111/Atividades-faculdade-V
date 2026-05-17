## Como Iniciar o Projeto

1. **Criar e ativar o ambiente virtual** (recomendado):
   ```bash
   py -m venv .venv
   .venv\Scripts\Activate
   ```

2. **Instalar as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar o notebook** (análise exploratória e modelo):
   ```bash
   jupyter notebook analise.ipynb
   ```
   Ou abra o arquivo `analise.ipynb` no VS Code e execute as células.

4. **Executar o app Streamlit** (interface interativa):
   ```bash
   streamlit run streamlit_app.py
   ```

> **Nota**: O dataset é baixado automaticamente pelo `kagglehub` na primeira célula do notebook. A aba "Consultor IA" do app requer uma chave da API Gemini (inserida no próprio app ou no notebook).

**N°Aluno**: 48 William Rodrigues da costa santos

**Base Kaggle** : Bank Marketing	

**Link** : kaggle.com/datasets/henriqueyamahata/bank-marketing
Tipo : Classificação

**Dor / Contexto do Negócio**	:  Uma corretora de investimentos quer migrar clientes de poupança para produtos de maior rentabilidade

**Pergunta a Responder com IA**	: Qual cliente de poupança tem perfil para aceitar uma proposta de investimento em CDB ou fundo de renda fixa?

**Como a IA Generativa Vai Ajudar**: O agente gera roteiro de proposta de investimento 	personalizada com linguagem financeira acessível por perfil.																

																	