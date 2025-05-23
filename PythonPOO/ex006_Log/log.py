from pathlib import Path
import datetime
import time

caminhos = []
for j in range(20):
    agora = str(datetime.datetime.now())
    caminhoUnitario = ''
    for i in agora:
        if i.isalnum():
            caminhoUnitario = caminhoUnitario + i
    caminhoUnitario = Path(__file__).parent / caminhoUnitario
    time.sleep(0.1)
    caminhos.append(caminhoUnitario)


class Log:
    def _log(self, msg): #não é pra usar
        raise NotImplementedError('Implemente o método log')
    def sucessWarning(self, msgEscrita):
        return self._log(f'Sucess: {msgEscrita}')#essa parte que tá dentro dos parênteses vai ser o argumento para o _log() msg lá em baixo
    def errorWarning(self, msg):
        return self._log(f'Error: {msg}')
        
class LogFileMixin(Log):
    def _log(self, msgComposta):
        print(msgComposta)#esse print msg ta printando aquela parte inteira da linha 5,  --> f'Sucess: {msg}' <-- isso
        for caminho in caminhos:
            with open(caminho, 'w+') as arquivo:
                arquivo.write(msgComposta)

msg1 = LogFileMixin()

msg1.sucessWarning('Foi :)') # o Foi :) é a mensagem Escrita por mim, e quando for modificada, vira a mensagem Composta