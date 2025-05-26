from playwright.sync_api import Page, expect


def test_comprar_datoscorrectos(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Login
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    #Añado artículo
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    #Voy al carrito
    page.locator('.shopping_cart_link').click()

    #Inicio checkout
    page.locator('[data-test="checkout"]').click()

    #Relleno datos correctos
    page.locator('[data-test="firstName"]').fill("Alicia")
    page.locator('[data-test="lastName"]').fill("Tester")
    page.locator('[data-test="postalCode"]').fill("23456")
    page.locator('[data-test="continue"]').click()

    #Finalizo compra
    page.locator('[data-test="finish"]').click()

    #Verifico mensaje de éxito
    expect(page.locator("h2")).to_have_text("Thank you for your order!")


def test_comprar_datosincorrectos(page: Page):
    page.goto("https://www.saucedemo.com/")

    #Login
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    #Añado artículo
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    #Voy al carrito
    page.locator('.shopping_cart_link').click()
    page.locator('[data-test="checkout"]').click()

    #Dejo campos vacíos
    page.locator('[data-test="firstName"]').fill("")
    page.locator('[data-test="lastName"]').fill("Tester")
    page.locator('[data-test="postalCode"]').fill("")

    page.locator('[data-test="continue"]').click()

    #Verifico mensaje de error
    expect(page.locator('[data-test="error"]')).to_be_visible()

 






