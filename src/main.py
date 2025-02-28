import flet as ft
from .templates.page1 import Page1
from .templates.page2 import Page2


def main(page: ft.Page):
    page.title = 'Meu app de Páginas'
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 500
    page.window.height = 500

    def rotas(route):
        page.controls.clear()
        if route == '/':
            tela = Page1(page)
        elif route == '/tela2':
            tela = Page2(page)
        else:
            tela = Page1(page)

        page.add(tela.construir())
        page.update()

    page.on_route_change = lambda e: rotas(e.route)
    page.go('/')

ft.app(main)