Aplicacion mi_cita
Proyecto desarrollado en Python con Djando y Django Rest Framework (DRF). 
Gestión de  Reservas
Este es un proyecto básico de gestión de reserva de citas con un estilista profesional desarrollado con Django y Django Rest Framework (DRF). Incluye funcionalidades para gestionar Cliente, Profesionales Estilistas, citas y sus historiales de atencion.
Requisitos
•	Python 3.8 o superior
•	Django 4.0 o superior
•	Django Rest Framework
Instalación
1.	Clonar este repositorio:
2.	git clone https://github.com/wilmmes/ApiDjango.git
3.	cd ApiDjango
4.	Crear un entorno virtual y actívalo:
5.	python -m venv venv
6.	venv\Scripts\activate
7.	Instalar las dependencias:
8.	pip install -r requirements.txt
9.	Realizar las migraciones:
10.	python manage.py makemigrations
11.	python manage.py migrate
12.	Crear un superusuario:
13.	python manage.py createsuperuser
14.	Iniciar el servidor:
15.	python manage.py runserver
    
Para probar las APIs directamente desde el navegador con Django REST Framework:
Ve a las URLs que configuraste para las APIs:
http://127.0.0.1:8000/api/clientes/
http://127.0.0.1:8000/api/profesionales/
http://127.0.0.1:8000/api/citas/
http://127.0.0.1:8000/api/custom/
Usa las opciones de la interfaz para realizar operaciones GET, POST, PUT, y DELETE sobre los datos.
