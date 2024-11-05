# -*- coding: utf-8 -*-
"""Sodiqova_M

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Or41I9lqdb-hZH9QQ4wAO6YKKN6eFEHj
"""

import pandas as pd
baza={
  "FISH": ["Sodiqova Mahliyo Safarali qizi", "Komilova Dinora Islomjon qizi","Sodiqov Asadbek Qambarali oʻgʻli", "Toʻxtasinov Xurshidbek Abduxofiz oʻgʻli", "Abdullayeva Robiya Otabek qizi", "Yoʻlchiyeva Sevara Baxtiyorjon qizi","Isoqjonova Muazzamxon Ulugʻbek qizi","Kabirov Behruz Shukrullo oʻgʻli", "Oxunova Sevinch Abduxofiz qizi", "Sodiqjonov Samandarbek Safarali oʻgʻli"],
  "Yoshi": [20, 19, 17,16,20,18,15,13,18,16],
  "Maktabi": [6, 6,4,5,9,17,14,23,24,48 ],
  "Jinsi": ["ayol", "ayol", "erkak","erkak", "ayol","ayol","ayol","erkak","ayol","erkak"],
  "Manzili": ["Beshariq", "Furqat","Zangiota","Sergeli","Zomin", "Oltiariq","Bagʻdod", "Sergeli","Beshariq","Chilonzor"]
}
db=pd.DataFrame(baza)
print(db)

filtr=db [db ['Jinsi'] == "ayol" ]
print (filtr)

filtr=db [ (db [ 'Jinsi'] == "ayol") &  (db ['Manzili']== "Beshariq")]
print (filtr)