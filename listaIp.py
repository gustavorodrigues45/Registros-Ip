import socket

def resolve_ips(computer_list, output_file):
    with open(output_file, 'w') as file:
        for computer in computer_list:
            try:
                ip = socket.gethostbyname(computer)
                file.write(ip + '\n')
            except socket.gaierror:
                file.write(f"Erro ao resolver IP para {computer}\n")

def generate_computer_list(start, end):
    computer_list = []
    for i in range(start, end+1):
        computer_list.append(f"info-d{i:02d} ")
    return computer_list

# Definindo os números inicial e final dos computadores
start_number = 1
end_number = 26

# Gerando a lista de nomes dos computadores
computers = generate_computer_list(start_number, end_number)

# Resolvendo os IPs e escrevendo no arquivo
output_file = 'ipsInfo.txt'
resolve_ips(computers, output_file)

print("IPs resolvidos e gravados em", output_file)
