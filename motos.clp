; -------- Plantillas / Tablas --------
(deftemplate usuario
   (slot nombre (type STRING))
   (slot presupuesto (type SYMBOL) (allowed-values Bajo Medio Alto))
   (slot experiencia (type SYMBOL) (allowed-values Principiante Intermedio Experto))
   (slot uso (type SYMBOL) (allowed-values Urbano Carretera Trabajo Deportivo Trocha))
   (slot estilo (type SYMBOL) (allowed-values Naked Deportiva Turismo Automática Doble-Proposito))
   (slot cilindraje (type SYMBOL) (allowed-values Bajo Medio Alto))
   (slot preferencia (type SYMBOL) (allowed-values Economía Potencia Comodidad Estética)))

(deftemplate motocicleta
   (slot nombre (type STRING))
   (slot presupuesto (type SYMBOL) (allowed-values Bajo Medio Alto))
   (slot experiencia (type SYMBOL) (allowed-values Principiante Intermedio Experto))
   (slot uso (type SYMBOL) (allowed-values Urbano Carretera Trabajo Deportivo Trocha))
   (slot estilo (type SYMBOL) (allowed-values Naked Deportiva Turismo Automática Doble-Proposito))
   (slot cilindraje (type SYMBOL) (allowed-values Bajo Medio Alto))
   (slot preferencia (type SYMBOL) (allowed-values Economía Potencia Comodidad Estética)))

(deftemplate recomendacion
   (slot nombre (type STRING))
   (slot moto (type STRING))
   (slot razon (type STRING)))

(deftemplate regla-activa
   (slot nombre))

; -------- Reglas --------

(defrule moto-economica (usuario (presupuesto Bajo))
   =>
   (assert (regla-activa (nombre moto-economica)))
   (assert (recomendacion
      (moto "")
      (razon "La moto debe tener un valor de venta asequible"))))

(defrule moto-economica-principiante (usuario (presupuesto Bajo) (experiencia Principiante))
   =>
   (assert (regla-activa (nombre moto-economica-principiante)))
   (assert (recomendacion
      (moto "")
      (razon "La moto debe ser fácil de manejar y de mantener"))))

(defrule moto-economia-medio-principiante-urbano-naked-bajo
   (usuario (nombre ?nombre) (presupuesto Medio) (experiencia Principiante) (uso Urbano) (estilo Naked) (cilindraje Bajo) (preferencia Economía))
   =>
   (assert (regla-activa (nombre moto-economia-medio-principiante-urbano-naked-bajo)))
   (assert (recomendacion
      (nombre ?nombre)
      (moto "Honda CB190R")
      (razon "Moto urbana, económica y fácil de manejar para principiantes con presupuesto medio."))))

(defrule moto-potencia-medio-intermedio-urbano-naked-medio
   (usuario (nombre ?nombre) (presupuesto Medio) (experiencia Intermedio) (uso Urbano) (estilo Naked) (cilindraje Medio) (preferencia Potencia))
   =>
   (assert (regla-activa (nombre moto-potencia-medio-intermedio-urbano-naked-medio)))
   (assert (recomendacion
      (nombre ?nombre)
      (moto "Yamaha FZ25")
      (razon "Moto urbana de media cilindrada, ideal para usuarios intermedios que buscan potencia."))))

(defrule moto-economia-bajo-principiante-trabajo-naked-bajo
   (usuario (nombre ?nombre) (presupuesto Bajo) (experiencia Principiante) (uso Trabajo) (estilo Naked) (cilindraje Bajo) (preferencia Economía))
   =>
   (assert (regla-activa (nombre moto-economia-bajo-principiante-trabajo-naked-bajo)))
   (assert (recomendacion
      (nombre ?nombre)
      (moto "Bajaj Boxer 150")
      (razon "Moto económica, resistente y eficiente para trabajo diario y principiantes."))))

(defrule moto-comodidad-alto-experto-carretera-turismo-alto
   (usuario (nombre ?nombre) (presupuesto Alto) (experiencia Experto) (uso Carretera) (estilo Turismo) (cilindraje Alto) (preferencia Comodidad))
   =>
   (assert (regla-activa (nombre moto-comodidad-alto-experto-carretera-turismo-alto)))
   (assert (recomendacion
      (nombre ?nombre)
      (moto "Suzuki V-Strom 650")
      (razon "Moto de turismo cómoda y potente, ideal para expertos y viajes largos en carretera."))))

(defrule moto-potencia-alto-intermedio-deportivo-deportiva-medio
   (usuario (nombre ?nombre) (presupuesto Alto) (experiencia Intermedio) (uso Deportivo) (estilo Deportiva) (cilindraje Medio) (preferencia Potencia))
   =>
   (assert (regla-activa (nombre moto-potencia-alto-intermedio-deportivo-deportiva-medio)))
   (assert (recomendacion
      (nombre ?nombre)
      (moto "Kawasaki Ninja 400")
      (razon "Moto deportiva de media cilindrada, potente y ágil para usuarios intermedios."))))

(defrule moto-economia-bajo-principiante-urbano-naked-bajo
   (usuario (nombre ?nombre) (presupuesto Bajo) (experiencia Principiante) (uso Urbano) (estilo Naked) (cilindraje Bajo) (preferencia Economía))
   =>
   (assert (regla-activa (nombre moto-economia-bajo-principiante-urbano-naked-bajo)))
   (assert (recomendacion
      (nombre ?nombre)
      (moto "AKT NKD 125")
      (razon "Moto económica, ligera y fácil de mantener, perfecta para trayectos urbanos cortos."))))

(defrule moto2-economia-bajo-principiante-urbano-naked-bajo
   (usuario (nombre ?nombre) (presupuesto Bajo) (experiencia Principiante) (uso Urbano) (estilo Naked) (cilindraje Bajo) (preferencia Economía))
   =>
   (assert (regla-activa (nombre moto2-economia-bajo-principiante-urbano-naked-bajo)))
   (assert (recomendacion
      (nombre ?nombre)
      (moto "Susuki AX4")
      (razon "Moto económica, ligera y fácil de mantener, perfecta para trayectos urbanos cortos."))))

(defrule moto-comodidad-medio-principiante-urbano-automatica-bajo
   (usuario (nombre ?nombre) (presupuesto Medio) (experiencia Principiante) (uso Urbano) (estilo Automática) (cilindraje Bajo) (preferencia Comodidad))
   =>
   (assert (regla-activa (nombre moto-comodidad-medio-principiante-urbano-automatica-bajo)))
   (assert (recomendacion
      (nombre ?nombre)
      (moto "Honda PCX 150")
      (razon "Moto automática, cómoda y práctica para principiantes en la ciudad."))))

(defrule moto-potencia-medio-principiante-urbano-naked-bajo
   (usuario (nombre ?nombre) (presupuesto Medio) (experiencia Principiante) (uso Urbano) (estilo Naked) (cilindraje Bajo) (preferencia Potencia))
   =>
   (assert (regla-activa (nombre moto-potencia-medio-principiante-urbano-naked-bajo)))
   (assert (recomendacion
      (nombre ?nombre)
      (moto "Suzuki Gixxer 150")
      (razon "Moto naked urbana, potente y manejable para principiantes con presupuesto medio."))))

(defrule moto-potencia-medio-intermedio-urbano-naked-medio
   (usuario (nombre ?nombre) (presupuesto Medio) (experiencia Intermedio) (uso Urbano) (estilo Naked) (cilindraje Medio) (preferencia Potencia))
   =>
   (assert (regla-activa (nombre moto-potencia-medio-intermedio-urbano-naked-medio)))
   (assert (recomendacion
      (nombre ?nombre)
      (moto "Suzuki Gixxer 250")
      (razon "Moto naked urbana de media cilindrada, ideal para usuarios intermedios que buscan potencia."))))

(defrule moto-estetica-alto-experto-carretera-deportiva-alto
   (usuario (nombre ?nombre) (presupuesto Alto) (experiencia Experto) (uso Carretera) (estilo Deportiva) (cilindraje Alto) (preferencia Estética))
   =>
   (assert (regla-activa (nombre moto-estetica-alto-experto-carretera-deportiva-alto)))
   (assert (recomendacion
      (nombre ?nombre)
      (moto "Suzuki HAYABUSA")
      (razon "Moto deportiva de alta cilindrada, considerada una superbike legendaria, perfecta para expertos que buscan máximo rendimiento y diseño llamativo."))))

(defrule moto-economia-medio-principiante-urbano-naked-bajo
   (usuario (nombre ?nombre) (presupuesto Bajo) (experiencia Principiante) (uso Urbano) (estilo Naked) (cilindraje Medio) (preferencia Economía))
   =>
   (assert (regla-activa (nombre moto-economia-medio-principiante-urbano-naked-bajo)))
   (assert (recomendacion
      (nombre ?nombre)
      (moto "Honda NAVI")
      (razon "Moto compacta y económica, ideal para ciudad. Combina la practicidad de un scooter con diseño de moto, perfecta para principiantes que buscan economía y facilidad de manejo."))))

(defrule moto-ppto-alto
   (usuario (nombre ?nombre) (presupuesto Alto))
   =>
   (assert (regla-activa (nombre moto-ppto-alto)))
   (assert (recomendacion
      (nombre ?nombre)
      (moto "")
      (razon "Puedes centrarte en modelos de alta cilindrada o deportivos, priorizando la calidad, seguridad y tecnología avanzada, como sistemas de control de tracción y frenos ABS. Considera motores de más de 500cc para mayor potencia y rendimiento"))))
