import flet as ft


class Page2:
    def __init__(self,page: ft.Page):
        self.page = page
        page.bgcolor = ft.Colors.BLUE_ACCENT_700

    def construir(self):
        return ft.Column([
            ft.Text('Bem-vindo a tela 2!'),
            ft.ElevatedButton('Tela 1', on_click=lambda _: self.page.go('/tela1')),
            ft.ElevatedButton('Home', on_clicker=lambda _: self.page.go('/'))
        ])
