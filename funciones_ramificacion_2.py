#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ipywidgets as widgets
from IPython.display import display

def manejar_dropdown(dropdown_widget, w1_adn_protenia_text, w2_file_upload, w3_dropdown):

    def on_dropdown_change(change):
        
        selected = change['new']
        
        if selected == "1. Copiar secuencia":
            w1_adn_protenia_text.layout.display = 'inline-flex'
            w2_file_upload.layout.display = 'none'
            w3_dropdown.layout.display = 'none'
        elif selected == "2. Subir archivo":
            w1_adn_protenia_text.layout.display = 'none'
            w2_file_upload.layout.display = 'inline-flex'
            w3_dropdown.layout.display = 'inline-flex'
        else:
            w1_adn_protenia_text.layout.display = 'none'
            w2_file_upload.layout.display = 'none'
            w3_dropdown.layout.display = 'none'


    dropdown_widget.observe(on_dropdown_change, names='value')



# In[ ]:




