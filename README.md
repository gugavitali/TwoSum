# Two Sum - LeetCode Solution

Este repositório contém uma solução para o problema "Two Sum" do LeetCode, implementada em Python.

## Descrição
O problema consiste em encontrar dois índices de um array de números inteiros onde a soma dos elementos seja igual a um alvo (`target`).

### Exemplo
#### Entrada:
```python
nums = [2, 7, 11, 15]
target = 9
```
#### Saída:
```python
[0, 1]  # Porque nums[0] + nums[1] = 2 + 7 = 9
```

## Implementação
O código utiliza um dicionário (`num_map`) para armazenar os valores e seus índices, permitindo encontrar rapidamente a solução em tempo **O(n)**.

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Dicionário para armazenar valores e seus índices
        
        for i, num in enumerate(nums):
            complement = target - num  # Valor necessário para atingir o target
            
            if complement in num_map:  # Verifica se já vimos esse valor antes
                return [num_map[complement], i]  # Retorna os índices
            
            num_map[num] = i  # Adiciona o número ao dicionário
```

## Melhorias possíveis
- Adicionar testes automatizados com `pytest`.
- Melhorar a interface de entrada de dados.

