class Actor:
    def __init__(self, driver):
        self.driver = driver
    
    def abrir_pagina(self, url):
        self.driver.get(url)
    
    def ingresar_credenciales(self, username, password):
        username_input = self.driver.find_element_by_name('username')
        password_input = self.driver.find_element_by_name('password')
        username_input.send_keys(username)
        password_input.send_keys(password)
    
    def iniciar_sesion(self):
        login_button = self.driver.find_element_by_name('login')
        login_button.click()