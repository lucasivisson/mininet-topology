import numpy as np
from scipy.stats import t

# Dados de largura de banda (Gbits/sec)
bandwidth = [32.9, 33.0, 33.2, 32.2, 31.7, 31.4, 31.5, 33.7, 32.3, 32.4]

# Calculando a média e o desvio padrão
media_bandwidth = np.mean(bandwidth)
desvio_padrao_bandwidth = np.std(bandwidth, ddof=1)

# Tamanho da amostra
n_bandwidth = len(bandwidth)
graus_de_lib_bandwidth = n_bandwidth - 1
confianca_bandwidth = 0.95

# Calculando o intervalo de confiança
erro_padrao_bandwidth = desvio_padrao_bandwidth / np.sqrt(n_bandwidth)
intervalo_bandwidth = t.interval(
    confianca_bandwidth, graus_de_lib_bandwidth, media_bandwidth, erro_padrao_bandwidth)

print(f"Intervalo de Confiança para Largura de Banda: {intervalo_bandwidth}")

# Dados de transferência (GBytes)
transferencia = [38.4, 38.4, 38.6, 37.5, 36.9, 36.6, 36.6, 39.2, 37.6, 37.8]

# Calculando a média e o desvio padrão
media_transferencia = np.mean(transferencia)
desvio_padrao_transferencia = np.std(transferencia, ddof=1)

# Tamanho da amostra
n_transferencia = len(transferencia)
graus_de_lib_transferencia = n_transferencia - 1
confianca_transferencia = 0.95

# Calculando o intervalo de confiança
erro_padrao_transferencia = desvio_padrao_transferencia / \
    np.sqrt(n_transferencia)
intervalo_transferencia = t.interval(
    confianca_transferencia, graus_de_lib_transferencia, media_transferencia, erro_padrao_transferencia)

print(f"Intervalo de Confiança para Transferência: {intervalo_transferencia}")
