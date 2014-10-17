from pandas import *
from copy import deepcopy

class OneXAll(object):
    """ Esta classe implemente um dataset um versos todos em um dataset
        multiclasse
        
        Atributes:
            ovall: e um dicionario que contem duas chaves transformando o
            multiclass em um problema de classe binaria:
                features: uma copia dos valores dos atributos de cada amostra
                class: que contem uma classe binaria
            data: contem o dataframe do dataset.
            classes: lista contendo o atributo classe de todas as amostras
            class_map: lista contendo o mapa das classes possiveis do problema
            por exemplo:
                key:pacu - index 0
                key:dourado = index 1
            """

    _ovall = None
    _data = None
    _classes = None
    _class_map = None
    
    def __init__(self,dataset, classes, class_map):
        """Inicia OneXAll e com um dataset e as classes de cada amostras
        
            Carrega o dataset de um problema multiclasse e as classes do mesmo
            Ao termino da execucao, sera retornada para cada classe um novo
            dataset da classe contra as outras classes do problema
            
            Args:
                dataset: dataset do problema multiclasse na forma de DataFrame.
                classes: um array numerico contendo as classes de cada amostra
                class_map: um dicionario contendo o par nome:indice das classes
            Returns:
                nada.
        """
        
        self._data = dataset
        self._classes = deepcopy(classes)
        self._class_map = deepcopy(class_map)
        
    
    def split_arff_one_x_all(self):
        """
            Cria arquivos contendo apenas duas classes de um problema
            multi classe, isto e, tornando o dataset 1 x all
        """
        
        #cabecalho do arquivo arff lido
        classes = self._meta['class'][1]
        
        #Cria um cabecalho de um arquivo arff
        ah = af.Arff_Header()
        ab = af.Arff_Body()
        
        
        #Percorre os atributos
        #att contem uma tupla contendo a enumeracao do atributo e seu nome
        for att in enumerate(self._meta):
            if att[1] != 'class':
                #Nome do atributo
                name = att[1]
                #Tipo do atributo
                att_type = self._meta[name][0]
                #Cria um novo atributo contendo um nome e um tipo
                ah.add_attribute(name,att_type)
        
        #Lista que contem as classes do problema
        binary_classes = self.get_binary_classes(classes)
        
        #Adiciona os atributos ao cabecalho (apenas os nomes e tipos)
        ab.add_features(self._data)
        
        #Para cada classe do problema um arquivo arff sera criado.
        for class_name in binary_classes.keys():
            
            #Cabecalho do arquivo
            #Nome do dataset
            ah.add_dataset_name(self._meta.name+"_"+class_name+"Xall")
            #Adiciona o atributo classe ao cabecalho
            ah.add_class_attribute(binary_classes[class_name])
            ah.release_class_attribute()
            
        
    def get_binary_classes(self,classes):
        """
            Este metodo retorna um dicionario onde, para cada classe, uma lista
            e retornada contendo a classe em questao e uma classe padrao
            
            Args:
                classes: uma lista contendo o nome das classes (nominal)
                
            Returns:
                binary_classes: Dicionario contendo todas as classes combinadas
                com a classe padrao.
                
                Por exemplo:
                classes= ['Dourado', 'Pacu', 'Pintado']
                dic{
                    'Dourado':['Dourado', 'foo']
                    'Pacu':['Pacu', 'foo']
                    'Pintado':['Pintado', 'foo']
                    }
        """
        
        #numero de classes
        number_of_classes = len(classes)
        
        #Dicionario contendo como chave o nome classe e como valor uma lista
        #contendo a classe e a calsse padrao.
        binary_classes = {}
        
        #Laco sobre as classes
        for class_name in classes:
            
            binary_class = []
            
            for index in range(number_of_classes):
                if class_name != classes[index]:
                    binary_class.append('foo')
                else:
                     binary_class.append(class_name)
            
            #Cria uma lista sem nomes duplicados
            binary_classes[class_name] = np.unique(binary_class)
            
        return binary_classes
            
    def get_one_x_all_of_class(self,classIndex):
        """Dada o indice da classe, retorna o dataset da classe contra todas
            as outras.
            
            Args:
                classIndex: Indice da classe.
            Returns:
                Uma tupla contendo as amostras de todo o dataset e as classes
                do dataset. A lista de classe por sua vez, torna-se binaria
                contendo a classe passada por parametro e o restante e uma
                classe default
        """
        for key,value in self._class_map.iteritems():
            if value == classIndex:
                return self._ovall[key]
        return None
    

