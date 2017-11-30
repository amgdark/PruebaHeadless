# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver

@step(u'Dado que ingreso la url "([^"]*)"')
def dado_que_ingreso_la_url_group1(step, url):
    # chromedriver = '/Users/alexmau/Documents/PruebaHeadless/lib/chromedriver'
    world.driver = webdriver.Chrome('chromedriver')
    import os

	
    puerto = os.environ['PUERTO']
    world.driver.get('http://localhost:'+puerto+'/admin')
@step(u'Y en las cajas de texto el usuario "([^"]*)" y la contraseña "([^"]*)"')
def y_en_las_cajas_de_texto_el_usuario_group1_y_la_contrasena_group2(step, usuario, password):
    world.driver.find_element_by_name("username").send_keys(usuario)
    world.driver.find_element_by_name("password").send_keys(password)

@step(u'Cuando presiono el botón ingresar')
def cuando_presiono_el_boton_ingresar(step):
    world.driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[3]/input').click()

@step(u'Entonces puedo ver el mensaje "([^"]*)"')
def entonces_puedo_ver_el_mensaje_group1(step, mensaje):
    esperado = world.driver.find_element_by_id('user-tools').text
    assert mensaje in esperado, esperado + 'es diferente a '+mensaje

@step(u'Entonces puedo ver el mensaje de error "([^"]*)"')
def entonces_puedo_ver_el_mensaje_de_error_group1(step, mensaje):
    esperado = world.driver.find_element_by_class_name('errornote').text
    assert mensaje in esperado, esperado + 'es diferente a '+mensaje
    finalizar_driver()


def finalizar_driver():
    world.driver.get("http://localhost:8001/admin/logout/")
    world.driver.quit()
    