# Framework Zilytics
# Um Framework de Ciência de Dados, Visualização e Análise de Dados
# Desenvolvedor: Josiel Soares
# Website: http://josielsoares.com
# Biblioteca de Lógica de Game para a Aplicação
import bge 
# Controlador atual do cenário
cont = bge.logic.getCurrentController()
# Stakeholder dono do código ligado no controlador
own = cont.owner
# A cena atual, poderia ser sc = own.scene
sc = bge.logic.getCurrentScene()
# Listagem de objetos do cena´io
obj = sc.objects
# Importando algumas bibliotecas
from random import uniform
from bge import render
from datetime import datetime


# A classe principal
class MyGraph():
    def screen_shot(self):  
        # horário local atual
        agora = datetime.now()
        tempo = agora.strftime("%d-%m-%Y-%H-%M-%S")      
        dir = bge.logic.expandPath("//")
        render.makeScreenshot(dir + 'zilytics_'+tempo+'.png')
    def plotar(self):
        # Ampliar a resolução do texto
        obj['txt_function'].resolution = 5
        sx = 0
        sy = 0
        sxy = 0
        sx2 = 0
        sy2 = 0
        # 'dados aqui, pontos 2d separados por vírgula "assim: (20,30), (25,50)
        data = [(5,7),(7,15),(8,9),(9,21),(12,12),(11,15),(12,22),(13,17),(20,
        25)]
        # Matemática e estatística para a modelagem da reta
        for k in data:
            print(k[0])
            sx += k[0] 
            sy += k[1]
            sxy += k[0]*k[1]
            sx2 += k[0]**2
            sy2 += k[1]**2            
            own.localPosition.x  = k[0]
            own.localPosition.z  = k[1]
            #posicionamos cada dado na área visível
            sc.addObject('circle', own)
        print('sx: ' + str(sx))
        print('sy: ' + str(sy))
        print('sxy: ' + str(sxy))
        print('sx2: ' + str(sx2))
        print('sy2: ' + str(sy2))
        # contagem do tamanho real dos dados
        n = len(data)
        print('n: ' + str(n))
        a = (n*(sxy)-(sx*sy))/(n*sx2-sx**2)
        b = ((sy*sx2)-(sx*sxy))/(n*(sx2)-(sx)**2)
        print('b: ' + str(b))
        print('a: ' + str(a))        
        own.localPosition.x  = 0
        own.localPosition.z  = a*0+b
        # Adicionamos no cenário a origem de cada segmento de reta
        orig = sc.addObject('orig_reta', own)        
        own.localPosition.x  = 30
        # Temos uma reta no plano cartesiano
        own.localPosition.z  = a*30+b
        # Adicionamos no cenário a extremidade de cada segmento de reta
        ext = sc.addObject('ext_reta', own)        
        own.localPosition.x  = (orig.localPosition.x + ext.localPosition.x)/2
        own.localPosition.z  = (orig.localPosition.z + ext.localPosition.z)/2
        # O carpinteiro vai pregar os pregos para delimitar o tamanho do arame
        r = sc.addObject('reta', own)        
        direction = ext.localPosition - orig.localPosition 
        # Eixo da inclinação da reta                  
        AXIS_X = 0  
        # Esticando o arame                         
        r.localScale = [direction.length,0.1, 0.1]                                        
        r.alignAxisToVect(direction, AXIS_X)
        # Modelagem da equação geral da reta
        if b > 0:
            obj['txt_function']['Text'] = 'f(x) = ' + str(round(a,2)) + 'x +' + str(round(b, 2))
        elif b < 0:
            obj['txt_function']['Text'] = 'f(x) = ' + str(round(a,2)) + 'x ' + str(round(b, 2))
        elif b == 0:
            obj['txt_function']['Text'] = 'f(x) = ' + str(round(a,2)) + 'x'
        # Calculamos a tela visível para criação de produto de visualização

        self.screen_shot()
def carpineiro():
    g = MyGraph()
    g.plotar()