# Teste_Target
## Respostas do Teste Técnico da Target

### 1)
`Q1.py`

No final do processamento, `SOMA` carrega o valor `91`

### 2)
`Q2.py`


### 3)
- a) 9
- b) 128
- c) ?
- d) ?
- e) 13
- f) ?

### 4)
- Basta ligar dois interruptores juntos, o 1º e o 2º, e checar uma das salas.
  - Se ela estiver acesa, então pertence a um dos dois interruptores.
  - Se ela estiver apagada, então pertence ao interruptor desligado, o 3º.
- Então, desligar um dos interruptores, o 1º, e checar novamente.
  - Se a sala visitada anteriormente estava apagada, então checar uma sala diferente, e:
    - Se esta sala estiver acesa, então pertence ao 2º interruptor.
      - Logo: Sala anterior = 3º interruptor, esta sala = 2º interruptor, e a sala restante = 1º interruptor
    - Se esta sala estiver apagada, então pertence ao 1º interruptor.
      - Logo: Sala anterior = 3º interruptor, esta sala = 1º interruptor, e a sala restante = 2º interruptor
  - Se a sala visitada anteriormente estava acesa, então ligar o 3º interruptor, checar uma sala diferente, e:
    - Se esta sala estiver acesa, então pertence ao 2º ou 3º interruptor.
      - Seria necessário uma 3º ida para diferenciar as duas salas...
    - Se esta sala estiver apagada, então pertence ao 1º interruptor.
      - Logo: Sala anterior = 2º interruptor, esta sala = 1º interruptor, e a sala restante = 3º interruptor

### 5)
`Q5.py`