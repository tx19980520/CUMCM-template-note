# A general rectangular cellular automata
# Version:1.1
# Last edit: 12/19/2013 by Yu
# If you have any question about the script, feel free to send me an email dz316424@126.com

# ********** Global Variables ********** #
NEIGHBORHOODTYPE = ('von', 'moore', 'custom')

# ********** getneighbors ********** #
def getmooreneighbors(size = 1):
    '''
        Create Moore styple neighborhood region, in which 1 means valid negihbor. The default size is 1.
        
        Parameters:
            size      - The size of neighborhood region
            
        Example of Moore neighbor:
        
        size = 1
        1 1 1
        1 P 1
        1 1 1
        
        size = 2
        1 1 1 1 1
        1 1 1 1 1
        1 1 P 1 1
        1 1 1 1 1
        1 1 1 1 1
    '''
    totalsize = 2 * size + 1
    region = [];
    temp = [1] * totalsize;
    for i in range(totalsize):
        region.insert(0, temp);
    region[size][size] = 2
    return region

def getvonneighboors(size = 1):
    '''
        Create Von Neumann styple neighborhood region, in which 1 means valid 
        negihbor. The default size is 1.
        
        Parameters:
            size      - The size of neighborhood region
            
        Example of Von Neumann neighborhood:
        
        size = 1
        0 1 0
        1 P 1
        0 1 0
        
        size = 2
        0 0 1 0 0
        0 1 1 1 0
        1 1 P 1 1
        0 1 1 1 0
        0 0 1 0 0
    '''

    region = []
    temp =[0] * (2 * size + 1)
    for row in range(size + 1):
        region.insert(0, temp.copy())
    for row in range(size + 1):
        region[row][size - row:size + row + 1] = [1] * (2 * row + 1)
    for row in range(size - 1, -1, -1):
        region.insert(size + 1, region[row].copy())
    region[size][size] = 2
    return region    
        
# ********** neighborhood region retrival methods ********** #
GETNEIGHBORS = {NEIGHBORHOODTYPE[0] : getvonneighboors, \
                NEIGHBORHOODTYPE[1] : getmooreneighbors, \
                NEIGHBORHOODTYPE[2] : None}    

# ********** rule objext ********** #
class rulebuilder:
    '''
        Provide method to specify and build the CA rule
    '''    
    
    def __init__(self, rule, *neighbor):
        '''
            Initilize the CA rule builder.
            
            Parameter:
                rule         - The function indicating how the focused cell is influenced by its environment.
                neighbor     - Parameters to set up neighborhood region. Two ways to specify the neighborhood region:
                               1) Use a predifined neighborhood regions
                               2) Neighbor parameters: type & szie
                
            Note:
            1. The rule function should follow syntax as:
            
                rule(value, neighbors)
                
                Parameter:
                    value     - The value or object of central cell
                    neighbors - The neighborhoods: 
                                1) If the influence is oriented, input the neighborhood region
                                2) If not, input a list of neighborhood
                                
                Return: The value or object of central cell
        '''

        self.rule = rule
         
        if len(neighbor) == 1:
            # the input is a predefined array
            self.neighborregion(neighbor)
        else:
            # build the environment array
            self.setneighbors(neighbor[0], neighbor[1])
        
    # ********** methods ********** #    
    def setneighbors(self, ntype, nsize):
        '''
            Specify the neighbor region
            
            Parameters:
                ntype     - The type of neighborhood, including:
                            1. von: Von Neumann
                            2. moore: Moore
                            3. custom: Customeized neighborhood region
                nsize     - The region size
        '''
        
        if ntype not in NEIGHBORHOODTYPE:
            raise ValueError('\'{0} is not built-in neighborhood type. \''.format(ntype))
        
        if ntype != 'custom':
            self.ntype = ntype

            # the distance of central pixel to the T, B, L, R border of the neighbor region
            self.__pmargin= (nsize, nsize, nsize, nsize)
            
            global GETNEIGHBORS
            setregion = GETNEIGHBORS[ntype]
            self.nregion = setregion(nsize)
        else:
            raise ValueError('To specify customized neighborhood region, please use setnregion().')

    def setnregion(self, nregion):
        '''
            Specify the costomized neighborhood region.
            
            Parameter:
                region - The neighborhood region
        '''
        self.ntype = 'custom'
        self.nregion = nregion
        
        # get margin of the central cell
        (rcount, ccount) = (len(nregion), len(nregion[0]))
        flag = False
        for rownum in range(rcount):
            if 2 in nregion[rownum]:
                colnum = nregion[rownum].index(2)

                # the distance of central pixel to the T, B, L, R border of the neighbor region
                self.__pmargin = (rownum, rcount - rownum - 1, 
                                  colnum, ccount - colnum - 1)
                flag = True
                break

        if not flag:
            raise Exception('The central cell should be labled using 2.')

    def setrule(self, rule):
        '''
            Set the transformation rule for each pixel
            
            Parameters:
                rule - Transformation rule with style rule(pixelvalue, neighbors).
        '''
        self.rule = rule
        
    def build(self):
        '''
            Build the transformation rules for CA model
        '''

        def getblock(r, c, rmax, cmax, data):
            '''
                Get the neighborhood region of pixels except those located near the borders of the environment
            '''
            nonlocal self
            return [row[c - self.__pmargin[2] : c + self.__pmargin[3] + 1] for row in data[r - self.__pmargin[0] : r + self.__pmargin[1] + 1]]       
            
        def getvalueblock(neighborsdata):
            '''
                Get the data of neighbors. for those that are not valid neighborhood, their data remain None.
            '''
            nonlocal self
            for rownum in range(self.__pmargin[0] + self.__pmargin[1] + 1):
                for colnum in range(self.__pmargin[2] + self.__pmargin[3] + 1):
                    if self.nregion[rownum][colnum] == 0:
                        neighborsdata[rownum][colnum] = None                     
            return neighborsdata
            
        def rule(r, c, rmax, cmax, agent, envi, layercount):
            
            nonlocal self
            
            if not (self.__pmargin[0] <= r <= rmax - self.__pmargin[1]) & \
                   (self.__pmargin[2] <= c <= cmax - self.__pmargin[3]):
                   return agent[r][c]
            
            if layercount > 1:
                nenvi = []
                nagent = []
                for index in range(layercount):
                    nenvi.append(getvalueblock(getblock(r, c, rmax, cmax, envi[index])))
                    nagent.append(getvalueblock(getblock(r, c, rmax, cmax, agent[index])))
                return self.rule(agent[r][c], nagent, nagent)
            else:
                nenvi = getblock(r, c, rmax, cmax, envi)
                nagent = getblock(r, c, rmax, cmax, agent)
                return self.rule(agent[r][c], getvalueblock(nagent), getvalueblock(nenvi))
    
        return rule
        
# ********** CA object ********** #
class CA(object):
    '''
        Generalized rectangular cellular automata model
    '''    
    
    def __init__(self, envi, agent, rule):
        '''
            Parameters:
                envi   - Environment for evolution, multiple layers are allowed.
                agent  - The initial distribution of agents of evolution.
                rule   - Evolution rules. Got from rulebuilder.build()  
        '''
        self.setdata(envi, agent, rule)
        
    # ********** Method ********** #
               
    def setdata(self, agent, envi, rule):
        '''
            Reset the state and configuration of the CA model 
            
            Parameters:
                envi   - Environment for evolution, multiple layers are allowed.
                agent  - The initial distribution of agents of evolution.
                rule   - Evolution rules. Got from rulebuilder.build()  
        '''        
        
        # Size of environment
        if len(envi) == 3:
            self.gridsize = (len(envi[0]), len(envi[0][0]))
        else:
            self.gridsize = (len(envi), len(envi[0]))        
        
        # Evolution time
        self.time = 0
                
        # Initial grid (environment)
        self.__envi = envi            
        
        # Detect whether it is a multilayer environment
        self.__layercount = len(envi)
        try:
            temp = envi[0][0][0]
        except:
            self.__layercount = 1
        
        # Data
        self.agent = agent
        
        # Regulation
        self.__rule = rule
        
        # Evolution history record
        self.history = {}         
        
    def evolve(self, times = 1, returnresult = False, storehistory = False):
        '''
            Evolve the CA model
            
            Parameter:
                times            - Evolution time
                returnresult     - Whether to reuturn the final evolution result
                storehistory     - Whether to store the re of each evolutio in self.history
        '''
        
        for t in range(times):
            temp = self.agent 
            temp = [[self.__rule(r, c, self.gridsize[0] - 1, self.gridsize[1] - 1, \
                                 self.agent, self.__envi, self.__layercount) \
                          for c in range(self.gridsize[1])] \
                          for r in range(self.gridsize[0])]
            self.agent = temp
            self.time+=1
    
            if storehistory:
                self.store()        
        
        if returnresult:
            return self.agent
            
    def evolveiter(self, times, storehistory = False):
        '''
            Get the evolution iterator
            
            Parameter:
                maxtimes - Maximum evolution time
        '''
        self.__storehistory = storehistory
        self.__itermaxtimes = times
        return self.__iter__()
                
    def __iter__(self):
        self.__itertimes = 0
        return self
        
    def __next__(self):
        if self.__itertimes <= self.__itermaxtimes:
            return self.evolve(1, True, self.__storehistory)
        else:
            raise StopIteration
            
    def store(self):
        '''
            Store the current evolution result
        '''
        if self.time not in self.history.keys():
            self.history[self.time] = self.agent.copy()