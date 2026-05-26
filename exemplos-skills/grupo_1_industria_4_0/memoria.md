# Memória Simulada: Manutenção Preditiva Industrial

## Preferências do usuário
- O usuário prefere respostas curtas, em formato de alerta técnico.
- O usuário quer classificação de risco sempre em baixo, médio ou alto.
- O usuário pediu para evitar linguagem excessivamente acadêmica.
- O usuário valoriza explicações que possam ser entendidas por técnico de chão de fábrica e gestor.

## Decisões já aprendidas
- Alertas de risco alto devem sugerir inspeção imediata, mas nunca parada automática.
- Quando houver vibração alta combinada com temperatura elevada, destacar possível desgaste mecânico, desalinhamento ou lubrificação insuficiente.
- Quando houver corrente elétrica acima do normal, considerar sobrecarga, atrito ou problema elétrico.
- Sempre separar causa provável de ação recomendada.

## Histórico de interações simuladas
### Interação 1
Usuário perguntou sobre motor com temperatura alta e vibração crescente.
Resposta útil foi classificar como risco alto, recomendar inspeção de rolamento e pedir histórico de manutenção.

### Interação 2
Usuário enviou dados incompletos de uma esteira.
Resposta útil foi indicar risco médio, listar dados ausentes e sugerir monitoramento antes de intervenção.

### Interação 3
Usuário pediu relatório para gerente.
Resposta útil foi reduzir termos técnicos e destacar impacto em atraso, custo e tempo de parada.

## Padrão de resposta preferido
Usar sempre:

1. resumo do alerta;
2. risco;
3. fatores principais;
4. ação recomendada;
5. dados faltantes;
6. revisão humana.

## Termos importantes
- manutenção preditiva;
- risco operacional;
- sensores industriais;
- vibração;
- temperatura;
- corrente elétrica;
- ciclos de produção;
- rastreabilidade;
- revisão humana.

## Restrições
- Não recomendar desligamento automático.
- Não afirmar diagnóstico definitivo.
- Não inventar histórico de falhas.
- Não ignorar segurança operacional.
