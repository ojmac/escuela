# -*- coding: utf-8 -*-
{
    'name': "escuelaMod",

    'summary': "Gestión de escuela",

    'description': """
Módulo para Gestión Empresarial 2º Dam
    """,

    'author': "Óscar Macarrón",
    
    # Categoría más específica
    'category': 'Education',
    'version': '0.1',

    # Dependencias
    'depends': ['base'],

    # Archivos cargados
    'data': [
        # Seguridad (definición de acceso)
        'security/ir.model.access.csv',
        
        # Menús y acciones deben cargarse primero
        'views/actions.xml',
        'views/menu_views.xml',
          # Asegúrate de que este archivo exista y contenga las definiciones de acciones
        
        # Vistas
         
        'views/estudiante_view.xml',
        'views/asignatura_view.xml',
        'views/grupo_view.xml',
        
        # Reportes
        'reports/report.xml',
        
        # Archivos adicionales
        'reports/templates.xml',
    ],
    
    # Cargar datos de demostración si es necesario
    'demo': [
        'demo/demo.xml',
    ],

    # Módulo instalable y como aplicación
    'installable': True,
    'application': True,
}


