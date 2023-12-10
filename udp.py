import numpy as np
from scipy.stats import t

bandwidth = [1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05]

media_bandwidth = np.mean(bandwidth)
desvio_padrao_bandwidth = np.std(bandwidth, ddof=1)

n_bandwidth = len(bandwidth)
graus_de_lib_bandwidth = n_bandwidth - 1
confianca_bandwidth = 0.95

erro_padrao_bandwidth = desvio_padrao_bandwidth / np.sqrt(n_bandwidth)
intervalo_bandwidth = t.interval(
    confianca_bandwidth, graus_de_lib_bandwidth, media_bandwidth, erro_padrao_bandwidth)

print(f"Intervalo de Confiança para Largura de Banda: {intervalo_bandwidth}")

jitter = [0.009, 0.004, 0.003, 0.006, 0.005, 0.003, 0.004, 0.006, 0.006, 0.008]

media_jitter = np.mean(jitter)
desvio_padrao_jitter = np.std(jitter, ddof=1)

n_jitter = len(jitter)
graus_de_lib_jitter = n_jitter - 1
confianca_jitter = 0.95

erro_padrao_jitter = desvio_padrao_jitter / np.sqrt(n_jitter)
intervalo_jitter = t.interval(
    confianca_jitter, graus_de_lib_jitter, media_jitter, erro_padrao_jitter)

print(f"Intervalo de Confiança para Jitter: {intervalo_jitter}")

lost_total_datagrams = [0/895, 0/895, 0/895, 0 /
                        895, 0/895, 0/895, 0/895, 0/895, 0/895, 0/895]

print(
    "Assim, em casos onde não há falhas, não é necessário aplicar métodos complexos de intervalo de confiança para proporções. A taxa de perda é determinada como zero com certeza, e o intervalo de confiança é [0, 1].")
