def calculate(value, rate):
    return value * (1 + rate / 100)


def main(initial_value, rate, frequency, period_value):
    first_iteration = True
    for time in range(frequency):
        if first_iteration:
            result = calculate(initial_value, rate)
            result += period_value
            first_iteration = False
        else:
            result = calculate(result, rate)
            result += period_value
    return round(float(result), 2)


if __name__ == '__main__':
    initial_value = int(input("Entre com o valor inicial:\n"))
    rate = float(input("Entre com a taxa %:\n"))
    frequency = int(input("Entre com a frequencia de investimento:\n"))
    period_value = int(input("Valor mensal:\n"))
    final_result = main(initial_value, rate, frequency, period_value)
    print(f"seu valor no final de {frequency} meses sera de: R${final_result}")
