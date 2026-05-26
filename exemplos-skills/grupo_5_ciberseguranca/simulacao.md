# Simulação de Perguntas e Respostas: Cibersegurança

## Exemplo 1
**Pergunta do humano**

Um IP externo teve 35 falhas de login em 5 minutos e depois conseguiu acessar o usuário admin. Também acessou /admin. Qual prioridade?

**Resposta esperada do modelo**

1. **Resumo do incidente:** houve múltiplas falhas seguidas de sucesso em conta privilegiada e acesso a endpoint sensível.
2. **Severidade:** crítica.
3. **Indicadores observados:** alto número de tentativas, sucesso após falhas, usuário admin e endpoint /admin.
4. **Hipótese principal:** possível força bruta bem-sucedida ou credencial comprometida.
5. **Ação recomendada para investigação:** correlacionar IP, sessão, horário, MFA, localização simulada e ações realizadas.
6. **Possível falso positivo:** teste interno autorizado ou automação conhecida.
7. **Restrições de segurança:** não apagar logs nem bloquear automaticamente sem validação do analista.

## Exemplo 2
**Pergunta do humano**

Um usuário comum teve 3 falhas de login e depois acessou normalmente do mesmo IP de sempre. É incidente?

**Resposta esperada do modelo**

1. **Resumo do incidente:** há poucas falhas de login seguidas de acesso bem-sucedido em padrão aparentemente conhecido.
2. **Severidade:** baixa.
3. **Indicadores observados:** baixo número de falhas, IP recorrente e usuário comum.
4. **Hipótese principal:** erro de senha ou tentativa legítima do próprio usuário.
5. **Ação recomendada para investigação:** verificar se o IP e horário são compatíveis com o histórico do usuário.
6. **Possível falso positivo:** provável falso positivo, se o comportamento for comum para esse usuário.
7. **Restrições de segurança:** registrar o evento e evitar ação restritiva sem evidência adicional.

## Exemplo 3
**Pergunta do humano**

Vários IPs acessaram /api/login com muito volume e retornos 429. Como resumir?

**Resposta esperada do modelo**

1. **Resumo do incidente:** há volume elevado de requisições ao endpoint de login com sinais de limitação por excesso de tentativas.
2. **Severidade:** alta.
3. **Indicadores observados:** muitos IPs, endpoint de autenticação, grande volume e códigos 429.
4. **Hipótese principal:** possível ataque distribuído de força bruta ou varredura automatizada.
5. **Ação recomendada para investigação:** agrupar por IP, região simulada, usuário-alvo e período; verificar se houve sucesso de login.
6. **Possível falso positivo:** teste de carga ou integração mal configurada.
7. **Restrições de segurança:** preservar logs e validar com o analista antes de qualquer bloqueio.

## Exemplo 4
**Pergunta do humano**

Um endpoint retornou erro 500 depois de uma sequência de acessos incomuns. Isso é crítico?

**Resposta esperada do modelo**

1. **Resumo do incidente:** houve acesso incomum seguido de erro interno no servidor.
2. **Severidade:** média a alta, dependendo do endpoint e do usuário envolvido.
3. **Indicadores observados:** padrão de acesso incomum e resposta HTTP 500.
4. **Hipótese principal:** possível tentativa de exploração, erro de aplicação ou uso inesperado da API.
5. **Ação recomendada para investigação:** verificar endpoint, payload, usuário, IP, logs da aplicação e eventos próximos.
6. **Possível falso positivo:** erro legítimo causado por bug ou entrada inválida não maliciosa.
7. **Restrições de segurança:** não expor detalhes técnicos sensíveis nem alterar logs.

## Exemplo 5
**Pergunta do humano**

Posso pedir para o modelo bloquear automaticamente um IP suspeito?

**Resposta esperada do modelo**

1. **Resumo do incidente:** o pedido envolve uma ação de contenção que pode afetar usuários legítimos.
2. **Severidade:** depende dos indicadores do IP suspeito.
3. **Indicadores observados:** ainda não foram informados eventos suficientes para justificar bloqueio.
4. **Hipótese principal:** pode haver comportamento malicioso, mas também pode ser falso positivo.
5. **Ação recomendada para investigação:** revisar volume, endpoints, sucesso de autenticação, histórico e impacto antes de bloquear.
6. **Possível falso positivo:** IP compartilhado, proxy corporativo, teste autorizado ou integração legítima.
7. **Restrições de segurança:** o modelo não deve executar bloqueio automático; a decisão deve ser do analista humano.
