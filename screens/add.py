from kivymd.uix.screen import MDScreen
from kivymd.uix.list import ThreeLineListItem
from datetime import datetime
from database.db import add_glucose  # Importa a função de salvar

class AddScreen(MDScreen):
    def save_value(self):
        # 1. Captura o que foi digitado
        value = self.ids.glucose_field.text
        
        if value.strip() != "":
            # 2. CHAMA A FUNÇÃO PARA SALVAR (Obrigatório para gravar no SQL)
            # A função add_glucose deve retornar (data, hora)
            data_salva, hora_salva = add_glucose(value)

            # 3. Localiza a tela 'home' para mostrar o dado imediatamente
            home_screen = self.manager.get_screen("home")
            
            # 4. Cria o item visual com as 3 informações
            new_item = ThreeLineListItem(
                text=f"Glicemia: {value} mg/dL",
                secondary_text=f"Data: {data_salva}",
                tertiary_text=f"Hora: {hora_salva}"
            )
            
            # 5. Adiciona à lista visual da Home
            home_screen.ids.glucose_list.add_widget(new_item)
            
            # 6. Limpa o campo e volta para a tela inicial
            self.ids.glucose_field.text = ""
            self.manager.current = "home"