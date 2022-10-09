
# Created by mlittlehales, 08/10/2022

import h5py

class nexusFile():
    """
    A class used to manipulate Nexus files
    
    Attributes
    ----------
    file: .nxs 
        File you want to load into the class to print specific attributes
    
    tree: str
        The nexus file tree stored as a string

    various attributes:
        Created when running the file tree function to load all nexus data into attribute form
        
    """

    def __init__(self, filename):
        """
        Parameters
        ----------
        file: .nxs
            The file you want to load into the class
        
        """

        self.file = h5py.File(filename + '.nxs', 'r')
        self.tree = ''
        self.fileTree(self.file)

    def fileTree(self, val = None, pre = ''):
            """
            A recursive function used to print the full file tree of the nexus file
            
            is called when the class is made to set all attributes and tree

            Parameters:
            ----------
            val: None
                
            pre: str
                path string to reach current nexus directory in the heirarchy
            
            """
            numitems = len(val)
            for key, val in val.items():
                numitems -= 1
                if numitems == 0:
                    if type(val) == h5py._hl.group.Group:
                        self.tree += (pre + '/' + key + '\n')
                        self.fileTree(val, pre = pre + '/' + key)
                    else:
                        self.tree += (pre + '/' + key + '\n')
                        setattr(self, key, self.file[pre + '/' + key][()])
                else:
                    if type(val) == h5py._hl.group.Group:
                        self.tree += (pre + '/' + key + '\n')
                        self.fileTree(val, pre = pre + '/' + key)
                    else:
                        self.tree += (pre + '/' + key + '\n')
                        setattr(self, key, self.file[pre + '/' + key][()])


if __name__ == '__main__':
    filename = 'test'
    file = nexusFile(filename)
    print(file.path)




