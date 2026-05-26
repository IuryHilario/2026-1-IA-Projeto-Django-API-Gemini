# Memória Simulada: Cibersegurança e Priorização de Incidentes

## Preferências do usuário
- O usuário prefere resumo técnico curto para analistas.
- O usuário quer severidade sempre explícita: baixa, média, alta ou crítica.
- O usuário pediu para separar anomalia de incidente confirmado.
- O usuário quer reduzir falsos positivos sem ignorar risco real.

## Decisões já aprendidas
- Muitas falhas de login seguidas de sucesso aumentam severidade.
- Acesso a endpoint administrativo pesa na prioridade.
- Erros HTTP 500 após comportamento suspeito devem ser investigados.
- Eventos devem preservar logs e trilha de auditoria.

## Histórico de interações simuladas
### Interação 1
Usuário enviou alerta com várias falhas de login.
Resposta útil foi classificar como alta severidade e pedir correlação por IP e usuário.

### Interação 2
Usuário perguntou se podia bloquear automaticamente um IP.
Resposta útil foi recomendar validação humana e checagem de falso positivo antes de ação.

### Interação 3
Usuário pediu resumo para analista.
Resposta útil foi listar indicadores observados, hipótese e próximos passos de investigação.

## Padrão de resposta preferido
Usar sempre:

1. resumo;
2. severidade;
3. indicadores;
4. hipótese;
5. investigação;
6. falso positivo;
7. restrições.

## Termos importantes
- anomalia;
- incidente;
- severidade;
- falso positivo;
- logs;
- autenticação;
- endpoint sensível;
- auditoria;
- revisão humana.

## Restrições
- Não apagar logs.
- Não recomendar ação destrutiva automática.
- Não ensinar exploração ofensiva.
- Não afirmar comprometimento sem evidência suficiente.
