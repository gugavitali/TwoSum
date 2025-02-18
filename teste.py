from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            if (aux := target - num) in num_map:
                return [num_map[aux], i]
            num_map[num] = i  
        return []

def main():
    while True:
        try:
            scan_input = input("\nEscolha a opção (1, 2, Python) ou digite 'sair' para encerrar: ").strip().lower()
            
            if scan_input == "sair":
                print("\nEncerrando o programa. Até mais!")
                break

            try:
                scan = int(scan_input)
            except ValueError:
                scan = scan_input

            match scan:
                case 1:
                    nums = [2, 7, 11, 15]
                    target = 9
                case 2:
                    nums = [3, 2, 4]
                    target = 6
                case "python":
                    nums = [3, 3]
                    target = 6
                case _:
                    print("\nOpção inválida! Tente novamente.")
                    continue

            result = Solution().twoSum(nums, target)
            print("\n----- Resultado -----")
            print(f"Números: {nums}")
            print(f"Target: {target}")
            print(f"Índices dos números que somam ao target: {result}")

        except Exception as e:
            print(f"\nOcorreu um erro: {e}")

if __name__ == '__main__':
    main()