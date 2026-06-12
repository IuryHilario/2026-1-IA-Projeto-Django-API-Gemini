# Simulação de Perguntas e Respostas: Detecção de Anomalias e Priorização de Incidentes

---

## Exemplo 1 — Ataque de força bruta com sucesso em conta privilegiada

**Pergunta do analista**

Um IP externo desconhecido fez 42 tentativas de login em 4 minutos, todas com falha. Em seguida, o acesso foi bem-sucedido no usuário `sysadmin`. O endpoint `/api/admin/users` foi acessado com resposta 200. Evento ocorreu às 03h17. Como classifico?

**Resposta esperada do modelo**

1. **Resumo do evento:** sequência extensa de falhas seguida de autenticação bem-sucedida em conta com perfil privilegiado, com acesso a endpoint administrativo em horário atípico.
2. **Severidade calculada:** crítica.
3. **Fatores que influenciaram a severidade:** volume elevado de falhas, sucesso em conta privilegiada, IP externo desconhecido, endpoint sensível e horário fora do padrão operacional.
4. **Classificação:** suspeita de incidente confirmado — múltiplos indicadores simultâneos elevam a confiança.
5. **Hipótese principal:** possível comprometimento de credencial ou ataque de força bruta bem-sucedido.
6. **Ações recomendadas para investigação:** correlacionar sessão, geolocalização simulada do IP, histórico do usuário `sysadmin`, uso de MFA e ações realizadas após o acesso ao endpoint.
7. **Avaliação de falso positivo:** baixa probabilidade — a combinação de fatores é atípica para acesso legítimo, especialmente no horário registrado.
8. **Decisão sugerida para o analista:** escalar imediatamente; considerar suspensão temporária da conta enquanto a investigação é realizada.
9. **Restrições do assistente:** nenhuma ação de contenção será executada automaticamente; a decisão é do analista humano.

---

## Exemplo 2 — Acesso recorrente com poucas falhas e usuário comum

**Pergunta do analista**

Um usuário comum teve 2 falhas de login às 09h45 e depois acessou normalmente pelo mesmo IP que sempre usa. Não acessou nenhum endpoint sensível. Devo tratar como incidente?

**Resposta esperada do modelo**

1. **Resumo do evento:** poucas falhas de autenticação seguidas de acesso bem-sucedido em IP recorrente, por usuário sem perfil privilegiado, em horário comercial.
2. **Severidade calculada:** baixa.
3. **Fatores que influenciaram a severidade:** baixo número de falhas, IP com histórico compatível, usuário comum e horário esperado.
4. **Classificação:** anomalia leve — desvio mínimo do padrão, sem indicadores de ameaça real.
5. **Hipótese principal:** erro de digitação de senha ou troca recente de credencial pelo próprio usuário.
6. **Ações recomendadas para investigação:** verificar se o IP e o horário são consistentes com o histórico do usuário; nenhuma ação adicional necessária se confirmado.
7. **Avaliação de falso positivo:** alta probabilidade de falso positivo — comportamento dentro do esperado para usuário legítimo.
8. **Decisão sugerida para o analista:** registrar o evento e manter monitoramento; sem necessidade de escalonamento.
9. **Restrições do assistente:** não recomendar restrição de acesso sem evidência adicional.

---

## Exemplo 3 — Pico de volume distribuído no endpoint de autenticação

**Pergunta do analista**

Nos últimos 10 minutos, 87 IPs diferentes fizeram requisições ao `/api/auth/login` com retornos 429 (Too Many Requests). Não houve sucesso de autenticação registrado até o momento. Como resumo para o painel de alertas?

**Resposta esperada do modelo**

1. **Resumo do evento:** alto volume de requisições distribuídas ao endpoint de autenticação com respostas de limitação de taxa; nenhum sucesso registrado até o momento.
2. **Severidade calculada:** alta.
3. **Fatores que influenciaram a severidade:** grande quantidade de IPs distintos, endpoint de autenticação como alvo e volume anormal concentrado em curto período.
4. **Classificação:** suspeita — características de ataque distribuído, mas sem autenticação bem-sucedida confirmada.
5. **Hipótese principal:** possível ataque de força bruta distribuído (credential stuffing) ou varredura automatizada de credenciais.
6. **Ações recomendadas para investigação:** agrupar IPs por sub-rede e região simulada; verificar se os logins tentados têm padrão de usuários reais; monitorar se ocorrer sucesso de autenticação nos próximos minutos.
7. **Avaliação de falso positivo:** possível — teste de carga não autorizado ou integração mal configurada poderiam gerar esse padrão. Verificar com a equipe de desenvolvimento.
8. **Decisão sugerida para o analista:** manter monitoramento ativo; acionar equipe de desenvolvimento para confirmar ausência de testes planejados antes de escalonar.
9. **Restrições do assistente:** não bloquear IPs automaticamente; aguardar validação do analista.

---

## Exemplo 4 — Erro 500 após sequência de acessos incomuns

**Pergunta do analista**

Um usuário acessou 15 endpoints diferentes em 3 minutos, incluindo `/api/internal/config`. Na última requisição, o servidor retornou HTTP 500. O IP é externo, nunca visto antes. Isso é crítico?

**Resposta esperada do modelo**

1. **Resumo do evento:** varredura acelerada de múltiplos endpoints por IP externo desconhecido, com acesso a recurso interno e erro de servidor na última requisição.
2. **Severidade calculada:** alta.
3. **Fatores que influenciaram a severidade:** IP externo desconhecido, velocidade de acesso a múltiplos endpoints, acesso a recurso de configuração interna e resposta HTTP 500.
4. **Classificação:** suspeita — padrão compatível com enumeração de API ou tentativa de exploração.
5. **Hipótese principal:** possível reconhecimento automatizado de superfície de ataque ou tentativa de exploração de endpoint de configuração.
6. **Ações recomendadas para investigação:** revisar payload das requisições ao `/api/internal/config`; verificar logs de aplicação para entender a causa do erro 500; correlacionar com outros eventos do mesmo IP.
7. **Avaliação de falso positivo:** moderada — cliente externo mal configurado ou teste de integração podem gerar padrão similar; porém, o acesso a endpoint interno é preocupante.
8. **Decisão sugerida para o analista:** investigar o payload e a resposta do erro 500 antes de classificar como incidente confirmado; considerar restrição temporária se não houver justificativa para o acesso.
9. **Restrições do assistente:** não alterar permissões nem apagar logs de aplicação; decisão de contenção é do analista.

---

## Exemplo 5 — Analista questiona sobre automação de resposta a incidentes

**Pergunta do analista**

O assistente pode, após identificar severidade crítica, bloquear automaticamente o IP e revogar a sessão do usuário suspeito para agilizar a contenção?

**Resposta esperada do modelo**

1. **Resumo do evento:** solicitação de ação automática de contenção baseada em classificação de severidade pelo assistente.
2. **Severidade calculada:** depende dos indicadores do incidente em questão; a severidade em si não autoriza ação automática.
3. **Fatores que influenciaram a severidade:** não aplicável — a pergunta é sobre processo, não sobre um evento específico.
4. **Classificação:** não se aplica; trata-se de uma questão sobre escopo do assistente.
5. **Hipótese principal:** a intenção é reduzir o tempo de resposta, mas automação sem revisão humana aumenta o risco de falsos positivos com impacto operacional.
6. **Ações recomendadas para investigação:** antes de qualquer contenção, revisar: o IP é compartilhado? há MFA ativo? a sessão ainda está em uso? existem outros usuários afetados?
7. **Avaliação de falso positivo:** ações automáticas de bloqueio em IPs compartilhados ou proxies corporativos podem interromper acessos legítimos de múltiplos usuários.
8. **Decisão sugerida para o analista:** o analista deve ser o responsável pela decisão de bloqueio ou revogação; o assistente pode preparar o resumo e a recomendação, mas não executa a ação.
9. **Restrições do assistente:** bloqueio automático, revogação de sessão e alteração de permissões não fazem parte do escopo deste assistente; a ação de contenção deve ser executada e validada por um analista humano.