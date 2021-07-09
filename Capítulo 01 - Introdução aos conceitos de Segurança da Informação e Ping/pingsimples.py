import os  # Importa o módulo ou biblioteca os (integra os programas e recursos do S.O)

print("#" * 60)  # Imprimindo # 60 vezes

ip_ou_host = input("Digite o Ip ou host a ser verificado: ")
# Criamos uma variável que vai receber do usuário um Ip 

print("#" * 60)  # Imprimindo # 60 vezes

os.system('ping -n 6 {}'.format(ip_ou_host))
# Chamando system da biblioteca os - comando ping -n -num de pacotes que serão {}

print("#" * 60)  # Imprimindo # 60 vezes