
import numpy as np

class Dataset(object):
    """Esta calsse representa um dataset carregado a partir de um arquivo arff
        
        Atributes:
            _name: nome do dataset
            _data: contem os dados das amostras vindos do arff.
            data: contem os mesmos dados de _data mas no formato array do np
            _meta: contem o cabecalho do arquivo arff.
            _dataFrame: contem os dados do aquivo no formato DataFrame
            _utilizados nos classificadores
            _classes: contem a lista de classes encontradas no arff
            target: ontem os mesmos dados de _classes mas no formato array do np
            _mapping: contem o mapa das classes
            _scaled_data: contem os valores das amostras normalizados
    """
    _name = None
    data = None
    target = None
    _data = None
    _header = None
    _data_frame = None
    _features_classes = None
    _classes_map = None
    
    def __init__(self,data,header,data_frame,features_classes,class_map):
        """Construtor"""
        self._name = header.name
        self._data = data
        self._header = header
        self._data_frame = data_frame
        self._features_classes = features_classes
        self._classes_map = class_map
        
        self.data = np.array(data_frame)
        self.target = np.array(features_classes)
        
        
    def __exit__(self):
        """Destrutor"""
        del self._data
        del self._header
        del self._features_classes
        del self._classes_map
    
    def get_features(self):
        
        features = []
        classes = []
        for i in range(len(self._data)):
            f = []
            for j in range(0,len(self._data[i])-1):
                f.append(self._data[i][j])
            features.append(f)
            classes.append(self._data[i][-1])
        
        return features,classes
    
    def get_attributes_declarations(self):
        
        attributes_names = []
        attributes_values = []
        for name in self._header:
            attributes_names.append(name)
            value = None
            if self._header[name][0] == 'nominal':
                value = self._header[name][1]
            attributes_values.append(value)
        
        return attributes_names,attributes_values

    def get_class_name_by_index(self,index):
        """Retorna o nome da classe no index
            
            Retorna o nome da classe no indice index
            
            Args:
                index: indice da class no mapa de classes
                
            Returns:
                O nome da classe ou caso contrario None
        """
        for c in  self._classes_map.iteritems():
            if c[1] == index:
                return c[0]
        return None
    
    def get_name(self):
        """Retorna o nome do dataset"""
        return self._name
    
    
    def get_class_index_by_name(self, name):
        """Retorna o indoce da classe como nome name
            
            Args:
                name: nome da classe
                
            Returns:
                indice da classe
            
            Raises:
                IndexError: A classe nao foi encontrada
        """
        try:
            return self._classes_map[name]
        except IndexError:
            print "%s is not a valid key" % name
    