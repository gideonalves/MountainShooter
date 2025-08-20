#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name      # Nome da entidade
        self.surf = pygame.image.load('./asset/' + name + '.png')      # Superfície gráfica (ex: imagem)
        self.rect = self.surf.get_rect(left=position[0], top=position[1])      # Retângulo de posição/tamanho
        self.speed = 0    # Velocidade

    @abstractmethod
    def move(self, ):
        pass
