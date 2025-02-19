import flet as ft

def configuration(page: ft.Page):
    page.title="Esposa do Kayne West"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.height= 500
    page.window.width= 500
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = ft.padding.only(left=20)
    page.window.resizable = False