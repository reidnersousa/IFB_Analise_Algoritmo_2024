import numpy as np
import math
import random


def gerando_amostra(N):
  sequencia = np.random.randint(1, N + 1, N)
  return sequencia


def eh_multiplo(N,qtd_partes):
  return N % qtd_partes ==0
