#!/usr/bin/python
# -*- coding: utf-8 -*-  # Define a codificação do arquivo como UTF-8

# Importa o módulo de imagem do pygame
import pygame.image
# Importa classes úteis do pygame
from pygame import Surface, Rect
from pygame.font import Font

# Importa constantes definidas em outro arquivo
from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW

# Define a classe Menu
class Menu:
    def __init__(self, window):
        self.window = window  # Janela principal onde o menu será desenhado
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()  # Carrega a imagem de fundo do menu
        self.rect = self.surf.get_rect(left=0, top=0)  # Define a posição da imagem de fundo

    def run(self):
        menu_option = 0  # Índice da opção atualmente selecionada no menu

        # Carrega e inicia a música de fundo do menu
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)  # Reproduz em loop infinito

        # Loop principal do menu
        while True:
            # Desenha a imagem de fundo na janela
            self.window.blit(source=self.surf, dest=self.rect)

            # Desenha os títulos do menu
            self.menu_text(text_size=50, text="Mountain", text_color=COLOR_ORANGE, text_center_pos=(WIN_WIDTH / 2, 70))
            self.menu_text(text_size=50, text="Shooter", text_color=COLOR_ORANGE, text_center_pos=(WIN_WIDTH / 2, 120))

            # Desenha as opções do menu
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    # Se for a opção selecionada, usa cor amarela
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_ORANGE, text_center_pos=(WIN_WIDTH / 2, 200 + 25 * i))
                else:
                    # Caso contrário, usa cor branca
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=(WIN_WIDTH / 2, 200 + 25 * i))
            pygame.display.flip()  # Atualiza a tela com as mudanças

            # Verifica os eventos do pygame (teclado, mouse, etc.)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha a janela do pygame
                    quit()         # Encerra o programa

                if event.type == pygame.KEYDOWN:
                    # Se a tecla pressionada for seta para baixo
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1  # Vai para a próxima opção
                        else:
                            menu_option = 0  # Volta para a primeira opção

                    # Se a tecla pressionada for seta para cima
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1  # Vai para a opção anterior
                        else:
                            menu_option = len(MENU_OPTION) - 1  # Vai para a última opção
                    if event.key == pygame.K_RETURN: # ENTER
                        return  MENU_OPTION[menu_option]


    # Função auxiliar para desenhar texto na tela
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)  # Define a fonte e o tamanho
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # Renderiza o texto como superfície
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)  # Centraliza o texto na posição desejada
        self.window.blit(source=text_surf, dest=text_rect)  # Desenha o texto na janela