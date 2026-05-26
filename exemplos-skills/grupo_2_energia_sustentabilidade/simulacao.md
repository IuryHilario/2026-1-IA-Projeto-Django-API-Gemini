# Simulação de Perguntas e Respostas: Energia e Sustentabilidade

## Exemplo 1
**Pergunta do humano**

Uma sala de aula fica com ar-condicionado ligado das 7h às 22h, mas só tem aula até 18h. O consumo é alto no período da noite. O que recomendar?

**Resposta esperada do modelo**

1. **Diagnóstico resumido:** há provável uso de climatização fora do horário necessário.
2. **Oportunidade de economia:** reduzir funcionamento após o fim das aulas.
3. **Recomendação principal:** configurar desligamento programado após 18h30, mantendo margem para saída dos usuários.
4. **Impacto esperado:** alto.
5. **Risco para conforto:** baixo, se a sala realmente estiver desocupada.
6. **Próximos dados para melhorar a simulação:** ocupação real por horário, consumo por hora e temperatura interna.

## Exemplo 2
**Pergunta do humano**

O laboratório está com 10 pessoas, temperatura interna de 20 C e ar-condicionado no máximo. Posso sugerir economia?

**Resposta esperada do modelo**

1. **Diagnóstico resumido:** a temperatura interna pode estar abaixo do necessário para conforto.
2. **Oportunidade de economia:** ajuste gradual do setpoint do ar-condicionado.
3. **Recomendação principal:** testar temperatura entre 23 C e 24 C e monitorar conforto dos usuários.
4. **Impacto esperado:** médio.
5. **Risco para conforto:** baixo a médio, dependendo da umidade e da atividade no laboratório.
6. **Próximos dados para melhorar a simulação:** temperatura externa, umidade, consumo por hora e tipo de atividade.

## Exemplo 3
**Pergunta do humano**

O prédio tem pico de consumo entre 18h e 21h. A tarifa nesse horário é mais cara. Como explicar para a gestão?

**Resposta esperada do modelo**

1. **Diagnóstico resumido:** o maior consumo ocorre em período de tarifa mais alta.
2. **Oportunidade de economia:** deslocar atividades não críticas para horários fora do pico.
3. **Recomendação principal:** revisar horários de equipamentos, climatização e iluminação de áreas com baixa ocupação nesse período.
4. **Impacto esperado:** médio a alto.
5. **Risco para conforto:** médio, caso existam aulas ou atividades presenciais no horário.
6. **Próximos dados para melhorar a simulação:** calendário acadêmico, ocupação por ambiente e consumo separado por sala.

## Exemplo 4
**Pergunta do humano**

Tenho dados incompletos: só sei que uma sala administrativa consome muito e tem pouca ocupação. O que o modelo deve responder?

**Resposta esperada do modelo**

1. **Diagnóstico resumido:** há indício de consumo incompatível com baixa ocupação, mas a análise é preliminar.
2. **Oportunidade de economia:** verificar iluminação, climatização e equipamentos ligados sem uso.
3. **Recomendação principal:** medir consumo por horário e testar desligamento programado de equipamentos não essenciais.
4. **Impacto esperado:** médio.
5. **Risco para conforto:** baixo, se a ocupação realmente for baixa.
6. **Próximos dados para melhorar a simulação:** consumo por hora, temperatura interna, horário de funcionamento e quantidade de pessoas.

## Exemplo 5
**Pergunta do humano**

A biblioteca tem ocupação alta à tarde e consumo elevado. Podemos reduzir iluminação para economizar?

**Resposta esperada do modelo**

1. **Diagnóstico resumido:** a biblioteca tem consumo alto em período de uso intenso.
2. **Oportunidade de economia:** otimizar iluminação sem prejudicar leitura e segurança.
3. **Recomendação principal:** avaliar uso de luz natural, sensores por zona e desligamento apenas em áreas sem ocupação.
4. **Impacto esperado:** médio.
5. **Risco para conforto:** médio, pois iluminação inadequada pode prejudicar estudo.
6. **Próximos dados para melhorar a simulação:** mapa de ocupação, nível de iluminação, horários de uso e consumo por circuito.
