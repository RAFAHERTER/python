valores = [10, 1, 2, 3, 4, 5, 6, 7]
seq_atual = []
melhor_sequencia = []
maior = num_seq = 0
for i, c in enumerate(valores):
    if i == 0:
        maior = c
        seq_atual.append(c)
    else:
        if c >= maior:
            seq_atual.append(c)
            maior = c
        elif c < maior:
            seq_atual = list()
            seq_atual.append(c)
            maior = c
        if len(seq_atual) > len(melhor_sequencia):
            melhor_sequencia = seq_atual
print(f'A maior sequência de números crescentes é \n{melhor_sequencia} com {len(melhor_sequencia)} elementos')


