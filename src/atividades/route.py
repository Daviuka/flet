'''ER\-

#rotas

import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f'Rota Inicial: {page.route}'))

    def mudanca_rota(e: ft.RouteChangeEvent):
            page.add(ft.Text(f"Nova rota: {e.route}"))

    page.on_route_change = mudanca_rota
    page.update()

ft.app(main, view=ft.AppView.WEB_BROWSER)
'''
import flet as ft
import tarefa as tf

def main(page: ft.Page):
    page.title = "Rota de fuga"

    lista_tarefa = []
    lista_tarefa = ft.Column()

    tarefa = tf.Tarefa()
    def mudanca_rota(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Aplicativo flet"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                    ft.ElevatedButton("Visitar loja", on_click=lambda _: page.go("/loja")),
                    ft.ElevatedButton("Visitar contato", on_click=lambda _: page.go("/contato")),
                    ft.ElevatedButton("Visitar Tarefas", on_click=lambda _: page.go("/tarefas")),
                ],
            )
        )
        if page.route == "/loja":
            page.views.append(
                ft.View(
                    "/loja",
                    [
                        ft.AppBar(title=ft.Text("Loja"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.ElevatedButton("Ir para casa", on_click=lambda _: page.go("/")),
                    ],
                )
            )

        if page.route == "/contato":
            page.views.append(
                ft.View(
                    "/contato",
                    [
                        ft.AppBar(title=ft.Text("Contato"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.ElevatedButton("Ir para casa", on_click=lambda _: page.go("/")),
                    ],
                )
            )

        if page.route == "/tarefas":
            btn_remover_tarefa = ft.ElevatedButton('Excluir', on_click=tf.remover_tarefa),
            btn_add_tarefa = ft.ElevatedButton('Adicionar', on_click=tf.add_tarefa),
            nova_tarefa_field =ft.TextField(label ='Nova Tarefa')
            page.views.append(
                ft.View(
                    "/tarefas",
                    [
                        ft.AppBar(title=ft.Text("Tarefas"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.ElevatedButton("Ir para casa", on_click=lambda _: page.go("/")),
                    ],
                )
            )

        page.update()

    def visualizar_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = mudanca_rota
    page.on_view_pop = visualizar_pop
    page.go(page.route)


ft.app(main, view=ft.AppView.WEB_BROWSER)