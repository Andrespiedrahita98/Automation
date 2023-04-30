from selenium import webdriver
import Actor
import Question
from selenium.webdriver.chrome.service import Service

class TestLogin:
    def test_login(self):
        actor = Actor.named("User")

        # Navegar a la página
        actor.attempts_to(NavigateTo("https://demoqa.com/text-box"))

        # Completar el formulario
        actor.attempts_to(FillInTextBox(By.ID, "userName"), "John Doe")
        actor.attempts_to(FillInTextBox(By.ID, "userEmail"), "johndoe@example.com")
        actor.attempts_to(FillInTextBox(By.ID, "currentAddress"), "123 Main St.")
        actor.attempts_to(FillInTextBox(By.ID, "permanentAddress"), "456 Oak Ave.")

        # Enviar el formulario
        actor.attempts_to(SubmitForm())

        # Verificar que el resultado es correcto
        actor.attempts_to(CheckResult(By.ID, "Name"), "John Doe")
        actor.attempts_to(CheckResult(By.ID, "Email"), "johndoe@example.com")
        actor.attempts_to(CheckResult(By.ID, "Current Address"), "123 Main St.")
        actor.attempts_to(CheckResult(By.ID, "Permanent Address"), "456 Oak Ave.")