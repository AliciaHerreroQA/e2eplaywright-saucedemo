from playwright.sync_api import Page, expect

def test_usuario_valido(page:Page):      
    print("Given el usuario prueba que el usuario sea valido")
    page.goto("https://www.saucedemo.com/") #abre la página que voy a probar
    page.get_by_placeholder("Username").type("standard_user")
    page.get_by_placeholder("Password").type("secret_sauce")
    page.get_by_role("button", name="Login").click()



def test_contraseña_incorrecta(page:Page):
    print("And el usuario prueba que la contraseña sea valida")
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Password").type("malacontraseña")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible


def test_usuario_contraseña_vacio(page:Page):
    print("And el usuario prueba la pagina con el usuario y la contraseña vacia")
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("button", name="Login").click()
    
    expect(page.get_by_text("Username is required")).to_be_visible