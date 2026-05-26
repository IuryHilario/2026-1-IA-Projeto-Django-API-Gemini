# Simulação de Perguntas e Respostas: Logística e Distribuição

## Exemplo 1
**Pergunta do humano**

Tenho três entregas: A vence às 10h e é cliente prioritário, B vence às 12h e C vence às 10h30 com trânsito alto. Qual deve ir primeiro?

**Resposta esperada do modelo**

1. **Situação operacional:** existem duas entregas com janela próxima e uma delas tem trânsito alto.
2. **Entregas prioritárias:** A primeiro, C em seguida e B depois.
3. **Risco de atraso:** médio a alto para C.
4. **Sugestão de rota ou replanejamento:** iniciar por A e reavaliar o caminho para C antes de seguir para B.
5. **Justificativa:** A combina cliente prioritário e menor prazo; C tem janela próxima e trânsito alto; B tem prazo mais folgado.
6. **Pontos para decisão humana:** confirmar distância real, capacidade do veículo e disponibilidade do motorista.

## Exemplo 2
**Pergunta do humano**

O veículo suporta 500 kg. Tenho pedidos de 300 kg, 250 kg e 100 kg. Como responder?

**Resposta esperada do modelo**

1. **Situação operacional:** a soma dos três pedidos ultrapassa a capacidade do veículo.
2. **Entregas prioritárias:** priorizar pedidos com janela mais próxima ou cliente mais crítico.
3. **Risco de atraso:** médio, se for necessário dividir a rota.
4. **Sugestão de rota ou replanejamento:** montar uma rota com até 500 kg e planejar segunda viagem ou outro veículo para o restante.
5. **Justificativa:** respeitar capacidade evita falha operacional e risco de segurança.
6. **Pontos para decisão humana:** informar janelas de entrega, prioridade dos clientes e disponibilidade de frota.

## Exemplo 3
**Pergunta do humano**

Uma entrega para farmácia atrasou 40 minutos por trânsito. O cliente é prioritário. O que sugerir?

**Resposta esperada do modelo**

1. **Situação operacional:** há atraso em entrega de cliente prioritário.
2. **Entregas prioritárias:** manter a farmácia como prioridade e revisar as próximas entregas.
3. **Risco de atraso:** alto para a entrega atual e médio para entregas seguintes.
4. **Sugestão de rota ou replanejamento:** comunicar o cliente, verificar rota alternativa e reordenar entregas de menor urgência.
5. **Justificativa:** cliente prioritário e atraso em andamento exigem ação imediata.
6. **Pontos para decisão humana:** confirmar se a rota alternativa é viável e se outro veículo pode apoiar.

## Exemplo 4
**Pergunta do humano**

Quero justificar para o supervisor por que uma rota foi alterada no meio do dia.

**Resposta esperada do modelo**

1. **Situação operacional:** a rota foi alterada por mudança nas condições operacionais.
2. **Entregas prioritárias:** destacar entregas afetadas por janela de horário, prioridade do cliente ou atraso.
3. **Risco de atraso:** informar se o risco ficou baixo, médio ou alto após a alteração.
4. **Sugestão de rota ou replanejamento:** apresentar a nova sequência de entregas.
5. **Justificativa:** explicar que a alteração buscou reduzir atraso, respeitar prioridade e manter capacidade do veículo.
6. **Pontos para decisão humana:** registrar a alteração e validar com o supervisor responsável.

## Exemplo 5
**Pergunta do humano**

Tenho 12 entregas no dia. Posso enviar todas para o Gemini analisar?

**Resposta esperada do modelo**

1. **Situação operacional:** a lista pode ser grande para uma análise detalhada em uma única resposta.
2. **Entregas prioritárias:** enviar primeiro as entregas com janela próxima, cliente prioritário ou maior risco de atraso.
3. **Risco de atraso:** preliminar até receber os dados resumidos.
4. **Sugestão de rota ou replanejamento:** agrupar por região, janela de entrega e capacidade do veículo.
5. **Justificativa:** reduzir o volume de dados melhora a qualidade da resposta e respeita limite de contexto.
6. **Pontos para decisão humana:** o supervisor deve validar a rota final.
