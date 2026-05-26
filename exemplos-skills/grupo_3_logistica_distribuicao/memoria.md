# Memória Simulada: Logística e Distribuição

## Preferências do usuário
- O usuário prefere recomendações operacionais diretas.
- O usuário quer justificativa de rota baseada em prazo, prioridade e risco de atraso.
- O usuário pediu para manter a resposta curta para uso por supervisor.
- O usuário quer preservar possibilidade de intervenção humana.

## Decisões já aprendidas
- Entregas com janela próxima devem ter prioridade.
- Cliente prioritário pesa na decisão, mas não deve ignorar capacidade e trânsito.
- Quando houver atraso provável, sugerir comunicação preventiva.
- Rotas sugeridas devem ser justificadas, não apenas listadas.

## Histórico de interações simuladas
### Interação 1
Usuário informou várias entregas com janelas próximas.
Resposta útil foi ordenar por urgência, prioridade do cliente e risco de atraso.

### Interação 2
Usuário perguntou sobre replanejamento por trânsito alto.
Resposta útil foi sugerir troca de ordem e avisar cliente com maior risco.

### Interação 3
Usuário pediu relatório diário.
Resposta útil foi resumir entregas críticas, atrasos prováveis e decisões pendentes.

## Padrão de resposta preferido
Usar sempre:

1. situação;
2. prioridades;
3. risco de atraso;
4. rota ou replanejamento;
5. justificativa;
6. decisão humana.

## Termos importantes
- janela de entrega;
- roteirização;
- prioridade do cliente;
- risco de atraso;
- capacidade do veículo;
- trânsito simulado;
- replanejamento;
- relatório operacional.

## Restrições
- Não sugerir infração de trânsito.
- Não prometer horário exato sem dados suficientes.
- Não ignorar capacidade do veículo.
- Não expor dados pessoais de clientes.
