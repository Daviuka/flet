import flet as ft

# Classe Nota
class Nota:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        self.status = "Aprovado" if nota >= 7.0 else "Reprovado"

    def __str__(self):
        return f"{self.nome} - Nota: {self.nota} ({self.status})"


# Função para atualizar a interface
def atualizar_interface(pagina, lista_notas, txt_nome, txt_nota, lbl_media, filter_aprovados=False, filter_reprovados=False):
   
    if filter_aprovados and filter_reprovados:
        filter_reprovados = False  # Desativa o filtro de reprovados se ambos forem ativados


    if filter_aprovados:
        lista_notas_filtrada = [nota for nota in lista_notas if nota.status == "Aprovado"]
    elif filter_reprovados:
        lista_notas_filtrada = [nota for nota in lista_notas if nota.status == "Reprovado"]
    else:
        lista_notas_filtrada = lista_notas

    # Exibe a lista de notas na interface
    lista_itens = []
    for nota in lista_notas_filtrada:
        lista_itens.append(
            ft.Row(
                controls=[
                    ft.Text(nota.__str__()),
                    ft.IconButton(ft.icons.EDIT, on_click=lambda e, n=nota: editar_nota(pagina, lista_notas, n, txt_nome, txt_nota, lbl_media)),
                    ft.IconButton(ft.icons.DELETE, on_click=lambda e, n=nota: excluir_nota(pagina, lista_notas, n, lbl_media))
                ]
            )
        )
    
    # Atualiza a lista de notas na tela
    lista_notas_column.controls = lista_itens
    
    # Calcula e exibe a média
    if lista_notas_filtrada:
        media = sum([nota.nota for nota in lista_notas_filtrada]) / len(lista_notas_filtrada)
    else:
        media = 0
    lbl_media.value = f"Média: {media:.2f}"
    
    # Atualiza a interface
    pagina.update()


# Função para adicionar uma nova nota
def adicionar_nota(pagina, lista_notas, txt_nome, txt_nota, lbl_media):
    nome = txt_nome.value
    try:
        nota = float(txt_nota.value)
        if nome and 0 <= nota <= 10:
            nova_nota = Nota(nome, nota)
            lista_notas.append(nova_nota)
            txt_nome.value = ""
            txt_nota.value = ""
            atualizar_interface(pagina, lista_notas, txt_nome, txt_nota, lbl_media, filter_aprovados=filter_aprovados_checkbox.value, filter_reprovados=filter_reprovados_checkbox.value)
            pagina.update()
        else:
            print("Nota inválida!")
    except ValueError:
        print("Digite uma nota válida!")


# Função para editar uma nota
def editar_nota(pagina, lista_notas, nota, txt_nome, txt_nota, lbl_media):
    txt_nome.value = nota.nome
    txt_nota.value = str(nota.nota)
    lista_notas.remove(nota)
    atualizar_interface(pagina, lista_notas, txt_nome, txt_nota, lbl_media)


# Função para excluir uma nota
def excluir_nota(pagina, lista_notas, nota, lbl_media):
    lista_notas.remove(nota)
    atualizar_interface(pagina, lista_notas, None, None, lbl_media)


# Função principal para a interface Flet
def main(pagina):
    lista_notas = []

    # Elementos da interface
    txt_nome = ft.TextField(label="Nome do Aluno")
    txt_nota = ft.TextField(label="Nota")
    lbl_media = ft.Text("Média: 0.00")
    btn_adicionar = ft.ElevatedButton("Adicionar Nota", on_click=lambda e: adicionar_nota(pagina, lista_notas, txt_nome, txt_nota, lbl_media))
    
    # Checkbox para filtrar alunos aprovados
    global filter_aprovados_checkbox
    filter_aprovados_checkbox = ft.Checkbox(label="Exibir apenas Aprovados", on_change=lambda e: atualizar_interface(pagina, lista_notas, txt_nome, txt_nota, lbl_media, filter_aprovados=e.control.value, filter_reprovados=filter_reprovados_checkbox.value))

    # Checkbox para filtrar alunos reprovados
    global filter_reprovados_checkbox
    filter_reprovados_checkbox = ft.Checkbox(label="Exibir apenas Reprovados", on_change=lambda e: atualizar_interface(pagina, lista_notas, txt_nome, txt_nota, lbl_media, filter_aprovados=filter_aprovados_checkbox.value, filter_reprovados=e.control.value))

    # Lista de notas
    global lista_notas_column
    lista_notas_column = ft.Column()

    # Definindo os controles da interface
    pagina.add(
        txt_nome,
        txt_nota,
        btn_adicionar,
        lista_notas_column,
        filter_aprovados_checkbox,
        filter_reprovados_checkbox,
        lbl_media
    )


# Executa o aplicativo Flet
ft.app(target=main)
