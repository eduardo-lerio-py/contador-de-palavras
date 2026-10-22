# Contador de Palavras

Script em Python que recebe uma frase digitada no terminal, conta quantas palavras ela tem e mostra qual é a palavra mais frequente.

## Como funciona

1. A frase é convertida para minúsculas e a pontuação é removida.
2. O texto é dividido em palavras.
3. Cada palavra é contada.
4. O programa mostra o total de palavras e a que mais aparece.

## Requisitos

- Python 3.6 ou superior (usa f-strings)
- Nenhuma biblioteca externa: só a biblioteca padrão (`string`)

## Como rodar

```bash
python contador_palavras.py
```

Troque `contador_palavras.py` pelo nome real do seu arquivo.

## Exemplo de uso

```
Insira a frase: O gato viu o rato, e o rato fugiu!
Sua frase tem 9 palavras.
A palavra mais comum foi o, aparecendo 3 vezes.
```

Se a frase estiver vazia (ou tiver só pontuação), o programa avisa: `Não há palavras!`

## Observações

- Em caso de empate, vale a palavra que apareceu primeiro na frase.
- A pontuação é removida por completo, então `guarda-chuva` vira `guardachuva`.
