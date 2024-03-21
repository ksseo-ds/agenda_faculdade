#classes_novas.py
class Faculdade:
    cursos = []
    def __init__(self, faculdade) -> None:
        self.eventos_do_curso = []
        self.materias_do_curso = []
        self.faculdade = faculdade

        

    
    
    @property
    def faculdade(self):
        return self._faculdade
    
    @faculdade.setter
    def faculdade(self, value):
        self._faculdade = value

        # Verifica se o curso já está na lista antes de adicioná-lo
        if not any(curso.faculdade == self.faculdade for curso in Faculdade.cursos):
            Faculdade.cursos.append(self) # fazo appendna lista de Faculdade.cursos
        
        


    @classmethod
    def listar(cls):
        return cls.cursos         
        
    def listar_eventos(self):
        return self.eventos_do_curso
    
    def __str__(self):
        return self._faculdade
################################

class Materia(Faculdade):
    materias = []

    def __init__(self, faculdade, materia, dependencia) -> None:
        

        Faculdade.__init__(self, faculdade)#AQUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        self.materia = materia
        self.dependencia = dependencia 


        
    @property
    def materia(self):
        return self._materia

    @materia.setter
    def materia(self, value):
        self._materia = value
        #verificar se a materia está sendo criada duas vezes
        
        if not any(materia.materia == self.materia for materia in Materia.materias):
            Materia.materias.append(self)# estava fazendo o append da meteria.self no Faculdade.Curso, mas deveria listar apenas instancias de Faculdade
            
            

    @classmethod
    def listar(cls):
        return cls.materias

    def listar_materias_curso(self): # melhorar pois a implementação exige evento.materia.listar_materias_curso()
        return self.materia_curso
    
    def __str__(self):
        return self._materia
############################################
    
class Evento:

    eventos = []
    def __init__(self,curso, materia, dependencia,tipo, evento, data) -> None:
        self.curso = Faculdade(curso)
        self.materia = Materia(curso, materia, dependencia)
        self.dependencia = dependencia
        self.tipo = tipo
        self.evento = evento
        self.data = data
     
        Evento.eventos.append(self)


        self.materia.materia_curso.append(self)
        self.curso.eventos_do_curso.append(self) # retirei o .curso
    
    @classmethod
    def listar(cls):
        return [print(i) for i in cls.eventos]
   
    @classmethod
    def listar(cls):
        return cls.eventos
    
    @property
    def curso(self):
        return self._curso.curso.curso
    
    @curso.setter
    def curso(self, value):
        self._curso = Faculdade(value)
    
    def __str__(self) -> str:
        return self._curso
