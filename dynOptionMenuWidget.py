from tkinter import OptionMenu
from tkinter import _setit
import copy

class DynOptionMenu(OptionMenu):
    def __init__(self, master, variable, value, *values, **kwargs):
        kwargsCopy=copy.copy(kwargs)
        if 'highlightthickness' in kwargs.keys():
            del(kwargs['highlightthickness'])
        OptionMenu.__init__(self, master, variable, value, *values, **kwargs)
        self.config(highlightthickness=kwargsCopy.get('highlightthickness'))
        #self.menu=self['menu']
        self.variable=variable
        self.command=kwargs.get('command')

    def SetMenu(self,valueList,value=None):
        self['menu'].delete(0,'end')
        for item in valueList:
            self['menu'].add_command(label=item,
                    command=_setit(self.variable,item,self.command))
        if value:
            self.variable.set(value)
