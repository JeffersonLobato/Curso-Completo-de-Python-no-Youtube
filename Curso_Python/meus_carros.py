from carros import CarrosEletricos

meu_carro = CarrosEletricos("Honda", "Civic", 2015)
meu_outro_carro = CarrosEletricos("Ford", "Focus", 2017)


meu_carro.bateria.mostra_bateria()

meu_carro.bateria.altera_bateria(56)

meu_carro.bateria.mostra_bateria()

meu_outro_carro.bateria.mostra_bateria()

meu_outro_carro.bateria.altera_bateria(70)

meu_outro_carro.bateria.mostra_bateria()