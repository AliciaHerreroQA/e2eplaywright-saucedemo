from playwright.sync_api import Page, expect


def test_comprar_datoscorrectos(page: Page):
    page.goto("https://www.saucedemo.com/")

    print("Given el usuario prueba a comprar un articulo y los datos son correctos")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    print("When el usuario añade un artículo al carrito")
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    print("And el usuario va al carrito de la compra")
    page.locator('.shopping_cart_link').click()

    print("And el usuario inicia la compra de los articulos")
    page.locator('[data-test="checkout"]').click()

    print("And el usuario rellena sus datos correctamente")
    page.locator('[data-test="firstName"]').fill("Alicia")
    page.locator('[data-test="lastName"]').fill("Tester")
    page.locator('[data-test="postalCode"]').fill("23456")
    page.locator('[data-test="continue"]').click()

    print("And el usuario finaliza la compra")
    page.locator('[data-test="finish"]').click()

    print("And el usuario comprueba que su compra se ha realizado con éxito")
    expect(page.locator("h2")).to_have_text("Thank you for your order!")


def test_comprar_datosincorrectos(page: Page):
    page.goto("https://www.saucedemo.com/")

    print("Given el usuario prueba a comprar un articulo y los datos son incorrectos")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    print("When el usuario añade un artículo al carrito")
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    print("And el usuario va al carrito de la compra")
    page.locator('.shopping_cart_link').click()
    page.locator('[data-test="checkout"]').click()

    print("And el usuario deja algun campo vacio")
    page.locator('[data-test="firstName"]').fill("")
    page.locator('[data-test="lastName"]').fill("Tester")
    page.locator('[data-test="postalCode"]').fill("")

    page.locator('[data-test="continue"]').click()

    print("And el usuario comprueba que su compra no se ha podido realizar")
    expect(page.locator('[data-test="error"]')).to_be_visible()

 






