def verificar_colera_interactivo():
    sintomas = {
        'diarrea_acuosa': input("¿Presenta diarrea acuosa? (si/no): ").lower(),
        'vómitos': input("¿Presenta vómitos? (si/no): ").lower(),
        'fiebre': input("¿Presenta fiebre? (si/no): ").lower(),
        'deshidratación': input("¿Presenta deshidratación? (si/no): ").lower(),
        'fatiga_extrema': input("¿Presenta fatiga extrema? (si/no): ").lower(),
        'calambres_estomacales': input("¿Presenta calambres estomacales? (si/no): ").lower(),
        'epidemia': input("¿Hay una epidemia de cólera en la región? (si/no): ").lower(),
        'exposición_al_agua_contaminada': input("¿Ha estado expuesto(a) al agua contaminada? (si/no): ").lower(),
        'exposición_a_alimentos_contaminados': input("¿Ha consumido alimentos contaminados? (si/no): ").lower(),
        'historial_de_viaje_a_áreas_endémicas': input("¿Tiene un historial de viaje a áreas endémicas de cólera? (si/no): ").lower(),
        'historial_de_brotes_en_la_región': input("¿Hay un historial de brotes de cólera en la región? (si/no): ").lower(),
        'historial_de_brotes_en_la_comunidad': input("¿Hay un historial de brotes de cólera en la comunidad? (si/no): ").lower(),
        'contacto_con_personas_infectadas': input("¿Ha estado en contacto con personas infectadas? (si/no): ").lower(),
        'falta_de_acceso_a_agua_potable': input("¿Hay falta de acceso a agua potable en la región? (si/no): ").lower(),
        'historial_de_exposición_a_aguas_residuales_contaminadas': input("¿Ha estado expuesto(a) a aguas residuales contaminadas? (si/no): ").lower(),
        'consumo_de_mariscos_crudos': input("¿Ha consumido mariscos crudos? (si/no): ").lower(),
        'signos_de_shock': input("¿Presenta signos de shock? (si/no): ").lower(),
      
    }

    if (sintomas['diarrea_acuosa'] == 'si' and sintomas['vómitos'] == 'si') or \
        (sintomas['diarrea_acuosa'] == 'si' and sintomas['fiebre'] == 'si' and sintomas['deshidratación'] == 'si') or \
        (sintomas['fatiga_extrema'] == 'si' and sintomas['diarrea_acuosa'] == 'si') or \
        (sintomas['vómitos'] == 'si' and sintomas['diarrea_acuosa'] == 'si') or \
        (sintomas['epidemia'] == 'si' and sintomas['diarrea_acuosa'] == 'si' and sintomas['fiebre'] == 'si') or \
        (sintomas['exposición_al_agua_contaminada'] == 'si' and sintomas['diarrea_acuosa'] == 'si') or \
        (sintomas['calambres_estomacales'] == 'si' and sintomas['diarrea_acuosa'] == 'si') or \
        (sintomas['historial_de_brotes_en_la_región'] == 'si' and sintomas['diarrea_acuosa'] == 'si') or \
        (sintomas['historial_de_brotes_en_la_comunidad'] == 'si' and sintomas['diarrea_acuosa'] == 'si') or \
        (sintomas['historial_de_viaje_a_áreas_endémicas'] == 'si' and sintomas['diarrea_acuosa'] == 'si') or \
        (sintomas['exposición_a_alimentos_contaminados'] == 'si' and sintomas['diarrea_acuosa'] == 'si' and sintomas['fiebre'] == 'si') or \
        (sintomas['contacto_con_personas_infectadas'] == 'si' and sintomas['diarrea_acuosa'] == 'si') or \
        (sintomas['falta_de_acceso_a_agua_potable'] == 'si' and sintomas['diarrea_acuosa'] == 'si' and sintomas['fiebre'] == 'si') or \
        (sintomas['signos_de_shock'] == 'si' and sintomas['diarrea_acuosa'] == 'si') or \
        (sintomas['consumo_de_mariscos_crudos'] == 'si' and sintomas['diarrea_acuosa'] == 'si'):
        print("El paciente podría tener cólera.")
    else:
        print("El paciente probablemente no tiene cólera.")

# Verificar síntomas
verificar_colera_interactivo()
