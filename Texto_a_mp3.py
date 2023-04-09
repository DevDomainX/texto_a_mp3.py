#!/bin/env python
#Author: Hacker NoDo
from gtts import gTTS 
from colorama import init, Fore, Back,Style

print(Fore.GREEN+'''****     **          *******
/**/**   /**         /**////**
/**//**  /**  ****** /**    /**  ******
/** //** /** **////**/**    /** **////**
/**  //**/**/**   /**/**    /**/**   /**
/**   //****/**   /**/**    ** /**   /**
/**    //***//****** /*******  //******
//      ///  //////  ///////    //////
\n''')
print(Fore.RED+'''
8b    d8 88***Yb 88888
88b  d88 88__dP   .dP
88YbdP88 88***  o `Yb
88 YY 88 88     YbodP
\n\n''')

print(Fore.YELLOW+"Hacker NoDo => canal oficial = https://youtube.com/@hackerNoDo\n\n")

 
# Texto a convertir en audio 

mytext = str(input("\n\nIngresa el texto a convertir a audio: "))

  
# Realizamos la conversión del texto a voz 
tts = gTTS(text=mytext, lang="es-us", slow=False) 


# Finalmente guardamos el archivo de Audio

tts.save("Hacker NoDo.mp3")
contador = 0

for contador in range(100):
	contador +=1
	print(Fore.GREEN+"Creando archivo.....",contador,"%")
print(Fore.YELLOW+"Tu archivo esta listo")
print("Busca tu Audio.mp3 en tu administrador con el nombre de: Hacker NoDo.mp3 generalmente qurda en la misma caperta que esta el scrip para ver comando: ls ")