from crewai import Crew, Task
from registro import salvar_reuniao
from agents.clara import clara
from agents.milo import milo
from agents.vivi import vivi
from agents.nox import nox

# === FEEDBACK DO CEO (coloque aqui seus comentários antes da nova reunião) ===
feedback_do_ceo = """
✅ Gostei da definição inicial do MVP e da clareza na proposta de valor.

⚠️ No entanto, senti falta de sugestões sobre o modelo de pagamento negociável — aquele onde o cliente propõe um valor e os prestadores podem aceitar ou fazer contraproposta. Isso já havia sido discutido comigo anteriormente e precisa ser avaliado.

⚠️ Outra melhoria seria deixar mais claro como cada agente contribuiu na construção da decisão final.

➡️ Sugiro que a próxima rodada refine o modelo de monetização, explore a funcionalidade de pagamento com contraproposta e deixe mais explícita a atuação de cada agente.
"""

# === DESCRIÇÃO DA NOVA REUNIÃO (rodada 2) ===
tarefa = Task(
    description=(
        "Com base nas decisões da reunião anterior, aprofundem os seguintes pontos:\n"
        "- Como pode funcionar o modelo de pagamento baseado em proposta e contraproposta entre cliente e prestador?\n"
        "- Quais são os riscos e benefícios?\n"
        "- Como essa funcionalidade pode ser implementada de forma simples no MVP?\n"
        "- E como cada um dos agentes pode contribuir com esse desenvolvimento?\n\n"
        "Incorporem também o feedback do CEO da reunião anterior. Sejam objetivos, propositivos e específicos nas suas sugestões."
    ),
    expected_output=(
        "Uma proposta clara para a funcionalidade de negociação de preços, incluindo desafios técnicos, experiência do usuário e implicações estratégicas. "
        "Cada agente deve justificar sua contribuição e apontar como sua área impacta na proposta final."
    ),
    agent=clara,
    agents=[clara, milo, vivi, nox]
)

crew = Crew(
    tasks=[tarefa],
    verbose=True
)

resultado = crew.kickoff()

salvar_reuniao(
    nome_arquivo="reuniao_modelo_negociacao",
    titulo="Reunião 002 – Modelo de Pagamento com Negociação",
    conteudo=resultado,
    feedback_ceo=feedback_do_ceo
)

print("\n--- Resultado Final da Reunião ---\n")
print(resultado)
