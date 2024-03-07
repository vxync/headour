import time
import os
import sys
from colorama import init, Fore

def clear_screen():
    # Limpa a tela do console
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_time_until_end_of_period(current_hour, current_minute, current_second):
    # Define os novos horários dos períodos
    periods = [(7, 20), (8, 10), (9, 0), (9, 50), (11, 0), (11, 50)]
    
    # Obtém o tempo atual em segundos
    current_total_seconds = current_hour * 3600 + current_minute * 60 + current_second
    
    # Encontra o período atual
    current_period = None
    for i, (period_hour, period_minute) in enumerate(periods):
        period_total_seconds = period_hour * 3600 + period_minute * 60
        if current_total_seconds < period_total_seconds:
            current_period = i
            break
    
    # Se já passou do último período do dia, retorna 0 segundos restantes
    if current_period is None:
        return "00:00:00"
    
    # Calcula os segundos restantes até o fim do período atual
    end_of_period_total_seconds = periods[current_period][0] * 3600 + periods[current_period][1] * 60
    time_until_end_of_period_seconds = end_of_period_total_seconds - current_total_seconds
    
    # Converte os segundos restantes em formato de hora específico ("HH:MM:SS")
    hours_until_end_of_period = time_until_end_of_period_seconds // 3600
    minutes_until_end_of_period = (time_until_end_of_period_seconds % 3600) // 60
    seconds_until_end_of_period = time_until_end_of_period_seconds % 60
    time_until_end_of_period_str = f"{hours_until_end_of_period:02d}:{minutes_until_end_of_period:02d}:{seconds_until_end_of_period:02d}"
    
    # Retorna o tempo até o fim do período atual no formato "HH:MM:SS"
    return time_until_end_of_period_str

def print_clock():
    clear_screen()
    while True:
        # Obtém o tempo atual
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min
        current_second = current_time.tm_sec

        # Calcula o tempo restante até o fim do período atual
        time_until_end_of_period = calculate_time_until_end_of_period(current_hour, current_minute, current_second)
        
        # Formata o tempo atual em uma string
        current_time_str = f"{current_hour:02d}:{current_minute:02d}:{current_second:02d}"
        
        # Define o período atual
        current_period = None
        periods = ["1st period", "2nd period", "3rd period", "interval", "4th period", "5th period"]
        for i, (period_hour, period_minute) in enumerate([(7, 20), (8, 10), (9, 0), (9, 50), (11, 0), (11, 50)]):
            if current_hour < period_hour or (current_hour == period_hour and current_minute < period_minute):
                current_period = periods[i]
                break
        


        if current_period is None:
            current_period = "waiting..."

        sys.stdout.write(f"\r{Fore.WHITE}{current_time_str} {Fore.WHITE}| {Fore.GREEN}{time_until_end_of_period} remaining {Fore.WHITE}| {Fore.YELLOW}{current_period}")
        sys.stdout.flush()
        


        # Aguarda 1 segundo antes de atualizar o relógio
        time.sleep(1)

# Chama a função principal para imprimir o relógio
print_clock()
