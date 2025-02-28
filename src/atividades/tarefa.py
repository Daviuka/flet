import flet as ft
import config
class Tarefa(ft.Row):
    def __init__ (self, texto):
        super().__init__() # importa o construtor da classe herdada
        self.checkbox = ft.Checkbox()
        self.texto_view = ft.Text(texto)
        self.editar_texto = ft.TextField(texto, vsible=False)
        self.btn_editar = ft.IconButton(icon=ft.Icon.EDIT, ON_CLICK=self.editar)
        self.btn_salvar = ft.IconButton(visible=False, icon=ft.Icons.SAVE, on_click=self.salvar) 

        self.controls = [
            self.editar_texto,
            self.texto_view,
            self.btn_editar,
            self.btn_salvar
        ]

    # função de editar
    def editar(self, e):
        self.btn_editar.visible = False
        self.btn_salvar.visible = True
        self.texto_view.visible = False
        self.editar_texto.visible = True
        self.update()

    # função de salvar         
    def salvar(self, e):
        self.btn_editar.visible = True
        self.btn_salvar.visible = False
        self.texto_view.visible = True
        self.editar_texto.visible = False
        self.texto_view.value = self.editar_texto.value
        self.update()
    

def main(page: ft.Page):
    config.configuracao(page)
    page.theme_mode = ft.ThemeMode.LIGHT

    tarefas = []

    def add_tarefa(e):
        nova_tarefa = Tarefa(texto=nova_tarefa_field.value)
        tarefas.append(nova_tarefa)
        lista_tarefas.controls.append(nova_tarefa)
        nova_tarefa_field.value = ''
        page.update()

    def remover_tarefa(e):
        for tarefa in tarefas[:]:
            if tarefa:
                lista_tarefas.controls.remove(tarefa)
                tarefas.remove(tarefa)
        page.update()


    btn_remover_tarefa = ft.ElevatedButton('Excluir', on_click=remover_tarefa)
    btn_add_tarefa = ft.ElevatedButton('Adicionar', on_click=add_tarefa)
    nova_tarefa_field = ft.TextField(label='Nova Tarefa')
    lista_tarefas = ft.Column()
    page.add(
        ft.Row([nova_tarefa_field, btn_add_tarefa],
               btn_remover_tarefa,
               lista_tarefas
    ))

ft.app(main)