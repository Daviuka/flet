import flet as ft

def main(page: ft.Page):
    # Configuração da janela
    page.title = 'Configuração de Página'
    #page.bgcolor= ft.Colors.WHITE70
    page.theme_mode= ft.ThemeMode.DARK
    #tamanho da janela
    #page.window.width = 500 # Largura
    #page.window.height = 800 # Altura
    #Alinhamento
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    # padding para o locais da janela
    #page.padding = ft.padding.all(100)
    page.padding= ft.padding.only(top=10,left=20, right=50, bottom=10)
    page.spacing = 50
    page.window.always_on_top= False # Deixar a janela em primeiro plano
    page.window.title_bar_hidden = False # Remover a barra da janela
    page.window.full_screen = False # deixar a janela cheia
    '''
    #Limitando o tamanho da Tela
    page.window.max_height = 600
    page.window.min_height = 600
    page.window.max_width = 600
    page.window.min_width = 600
    
    page.window.resizable = False
    '''
    def janela_evento(e):
        match e.data:
            case 'moved':
                print('Moveu a pagina')
            case 'resized':
                print('Redimencionou a página')
            case 'minimize':
                print('Minimizou a página')
            case _:
                print('Outra ação!')
    page.window.on_event = janela_evento

    def alterar_tema (e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            btn_tema.icon = ft.icons.NIGHTS_STAY_OUTLINED
            btn_tema.tooltip = 'Alterar para tema escuro!'
            page.bgcolor = ft.colors.WHITE
            t.bgcolor = ft.colors.BLACK
            t.color = ft.colors.WHITE
        else:
            page.theme_mode = ft.ThemeMode.DARK
            btn_tema.icon = ft.icons.WB_SUNNY_OUTLINED
            btn_tema.tooltip = 'Alterar para o tema claro!'
            page.bgcolor = ft.colors.BLACK
            t.bgcolor = ft.colors.WHITE
            t.color = ft.colors.BLACK
        page.update()

    btn_tema = ft.IconButton(
        icon=ft.icons.WB_SUNNY_OUTLINED,
        tooltip= 'Alterar o tema',
        on_click=alterar_tema
    )


    elementos = [
        ft.Text
            (value='Texto 1',
            size=20, 
            bgcolor = ft.colors.RED_900,
            color= ft.Colors.RED_300),
        ft.Text
            (value='Texto 2',
            size=20,
            bgcolor = ft.colors.RED_900,
            color= ft.Colors.RED_300),
        ft.Text
            (value='Texto 3',
            size=20,
            bgcolor = ft.colors.RED_900,
            color= ft.Colors.RED_300),
        ft.Text
            (value='Texto 4',
            size=20,
            bgcolor = ft.colors.RED_900,
            color= ft.Colors.RED_300)
    ]

   

    # Bloco de Texto
    t = ft.Text(
        value= 'Hello world', #valor que vai estar escrito
        size=80, #Tamanho da letra
        color= ft.Colors.DEEP_PURPLE_900,# A cor da Letra
        italic=True, # itálico
        weight= 'bold', # ft.FontWeigth.BOLD -- código que deixa largura da letra
        bgcolor= ft.Colors.WHITE70, # Mudar a cor do quadro
        font_family= 'Verdana'
        )
    #page.update()

    page.add(ft.Text(value='Texto dentro do add', size=50, weight=30))
    page.add(*elementos, t, btn_tema)

ft.app(main)