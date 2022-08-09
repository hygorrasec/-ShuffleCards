# -*- coding: utf-8 -*-

import random
from typing import Dict, List, Tuple

NAIPES = '♠ ♡ ♢ ♣'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

BARALHO = List[Tuple[str, str]]


def criar_baralho(aleatorio: bool = False) -> BARALHO:
    '''Cria um baralho com 52 cartas em listas de tuplas.'''
    baralho: BARALHO = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho: BARALHO) -> Tuple[BARALHO, BARALHO, BARALHO, BARALHO]:
    '''Gerencia a mão de cartas de acordo com o baralho gerado.'''
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


def jogar() -> None:
    '''Inicia um jogo de cartas para 4 jogadores.'''
    cartas: BARALHO = criar_baralho(aleatorio=True)
    jogadores: List[str] = 'Jogador_1 Jogador_2 Jogador_3 Jogador_4'.split()
    maos: Dict[str, BARALHO] = {j: m for j, m in zip(
        jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta: str = ' '.join(f'{j}{c}' for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()
