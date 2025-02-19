import config
import flet as ft

def main(page: ft.Page):
    config.configuration(page)  # Chama a configuração do arquivo config.py
    
    tarefas = []  # Lista para armazenar as tarefas
    
    # Função para adicionar uma nova tarefa
    def adicionar(e):
        if not nova_tarefa.value:
            nova_tarefa.error_text = "Por favor, digite"
            nova_tarefa.update()
        else:
            nova_tarefa.error_text = None

            # Cria a tarefa com checkbox e botão de remover
            tarefa = ft.Row([])

            checkbox = ft.Checkbox(label=nova_tarefa.value)
            btn_remover = ft.IconButton(
                icon=ft.icons.DELETE_OUTLINED,
                tooltip='Remover tarefa',
                on_click=lambda e: remover_tarefa(tarefa)
            )
            btn_editar = ft.IconButton(
                icon=ft.icons.EDIT_OUTLINED,
                tooltip='Editar tarefa',
                on_click=lambda e: editar_tarefa(tarefa, checkbox, btn_editar, btn_remover)
            )

            # Adiciona a checkbox, o botão de remover e o botão de editar à tarefa
            tarefa.controls.extend([checkbox, btn_editar, btn_remover])

            # Adiciona a tarefa à lista de tarefas
            tarefas.append(tarefa)

            page.add(tarefa)
            nova_tarefa.value = ""
            nova_tarefa.focus()  # Foca o campo de texto após adicionar
            nova_tarefa.update()

    # Função para remover uma tarefa
    def remover_tarefa(tarefa):
        tarefas.remove(tarefa)  # Remove a tarefa da lista
        page.controls.remove(tarefa)
        page.update()

    # Função para editar uma tarefa
    def editar_tarefa(tarefa, checkbox, btn_editar, btn_remover):
        # Cria o campo de texto para editar a tarefa
        campo_editar = ft.TextField(value=checkbox.label, width=300)
        btn_salvar = ft.ElevatedButton('Salvar', on_click=lambda e: salvar_edicao(tarefa, campo_editar, checkbox, btn_editar, btn_remover))

        # Substitui a tarefa existente com o campo de edição
        tarefa.controls = [campo_editar, btn_salvar]

        page.update()

    # Função para salvar a edição de uma tarefa
    def salvar_edicao(tarefa, campo_editar, checkbox, btn_editar, btn_remover):
        if campo_editar.value:
            checkbox.label = campo_editar.value  # Atualiza a label da checkbox
            tarefa.controls = [checkbox, btn_editar, btn_remover]  # Restaura a tarefa com o novo nome
            page.update()

    # Função para exibir saudação
    def saudacao(e):
        if not txt_nome.value:
            txt_nome.error_text = 'Por favor, Digite o seu nome.'
            page.update()
        else:
            nome = txt_nome.value
            page.controls.clear()  # Limpa todos os controles da página
            page.add(ft.Text(f'Olá {nome}'))

    # Função para alternar entre temas claro e escuro
    def alterar_tema(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            btn_tema.icon = ft.icons.NIGHTS_STAY_OUTLINED
            btn_tema.tooltip = 'Alterar para tema escuro!'
            page.bgcolor = ft.colors.WHITE
        else:
            page.theme_mode = ft.ThemeMode.DARK
            btn_tema.icon = ft.icons.WB_SUNNY_OUTLINED
            btn_tema.tooltip = 'Alterar para o tema claro!'
            page.bgcolor = ft.colors.BLACK
        page.update()

    # Botão para alternar o tema
    btn_tema = ft.IconButton(
        icon=ft.icons.WB_SUNNY_OUTLINED,
        tooltip='Alterar o tema',
        on_click=alterar_tema
    )

    # Campo de texto para o nome
    txt_nome = ft.TextField(label='Seu nome?')
    page.add(ft.Row(
        [
            txt_nome,
            ft.ElevatedButton('Diga olá', on_click=saudacao),
            btn_tema
        ], alignment=ft.MainAxisAlignment.START  # Corrigido alinhamento
    ))

    # Campo de texto para adicionar uma nova tarefa
    nova_tarefa = ft.TextField(hint_text='O que você deseja adicionar?', width=300)
    page.add(ft.Row(
        [
            nova_tarefa,
            ft.ElevatedButton('Adicionar', on_click=adicionar)
        ]
    ))

    # Dropdown e botão para exibir a cor selecionada
    def button_clicked(e):
        output_text.value = f"Dropdown value is: {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=155,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
            ft.dropdown.Option("Yellow"),
            ft.dropdown.Option("Other options")
        ]
    )

    page.add(output_text, submit_btn, color_dropdown)

# Inicia o aplicativo
ft.app(main)
