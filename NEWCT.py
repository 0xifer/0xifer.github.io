# REQUIREMENTS:
# py -m pip install clipboard


import os        # Used to clear the screen
import time      # Used for the sleep function
import pyperclip # Used to copy the output to your clipboard
from getpass import getpass   # Used to create an invisible input


def Sleep(x):
	try:
		Sleep(x)
	except KeyboardInterrupt:	
		os.system('')
################################################################################################################
#                                                 GET T2E + T2D                                                #
################################################################################################################
def T2E(): # Text 2 Encrypt function
	global text_raw, text_raw_backup
	try:
		text_raw = input('\n\033[1;36mText to encrypt: \033[1;33m') # Get the text to encrypt from the user
		if len(text_raw) <= 0 or text_raw.isspace():
			raise ValueError
		text_raw_backup = text_raw # Get a backup of 'text_raw'
	except ValueError:
		print('COULD NOT ENCRYPT THE TEXT. PLEASE TRY AGAIN')
		sleep(1)
		T2E()


def T2D(): # Text 2 Decrypt function
	global text_raw, text_raw_backup
	try:
		text_raw = input('\n\033[1;36mText to decrypt: \033[1;33m') # Get the text to encrypt from the user
		if len(text_raw) <= 0 or text_raw.isspace():
			raise ValueError
		text_raw_backup = text_raw # Get a backup of 'text_raw'
	except ValueError:
		print('COULD NOT DECRYPT THE TEXT. PLEASE TRY AGAIN')
		sleep(1)
		T2D()

################################################################################################################
#                                       MAIN FUNCTION OF THE CIPHER TOOL                                       #
################################################################################################################
def Main():
	try:
		global use_lang, text_raw, text_raw_backup
		os.system('mode 57,20 && title Cipher Tool ~ By: 0xifer && cls')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
		print('       \033[1;31m╔═════════════════════\033[1;36m═══════════════════╗')
		print('       \033[1;31m║           -WELCOME T\033[1;36mO CIPHER-          ║')
		print('       \033[1;31m║        ╔════════════\033[1;36m═══════════╗       \033[1;36m║')
		print('       \033[1;31m╠════════╣  ENTER \033[1;33m"H"\033[1;36m  FOR HELP  ╠═══════╣')
		print('       \033[1;31m║        ╚════════════\033[1;36m═══════════╝       \033[1;36m║')
		print('       \033[1;31m║ TYPE \033[1;33m"CMD" \033[1;31mAND VIEW  \033[1;36mLIST OF COMMANDS  ║')
		print('       \033[1;31m╚═════════════════════\033[1;36m═══════════════════╝')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;0m')
		use_lang = input('\033[1;36mAlphabet \033[1;31m/ \033[1;36mGoto: \033[1;33m').lower() # Request alphabet/goto from the user
	################################################################################################################
	#                                   FIND WHAT LANGUAGE AND RUN THAT FUNCTION                                   #
	################################################################################################################
		if use_lang == 'r':
			Reverse()
		if use_lang == 'se':
			S_ENCRYPT()
		if use_lang == 'sd':
			S_DECRYPT()
		if use_lang == 'ae':
			A_ENCRYPT()
		if use_lang == 'ad':
			A_DECRYPT()
		if use_lang == 'e':
			N_ENCRYPT()
		if use_lang == 'd':
			N_DECRYPT()
		if use_lang == 'mt':
			MT()
		if use_lang == 'rmt':
			RMT()
		if use_lang == 'alg':
			ALG()
		if use_lang == 'h':
			HELP4USER()
			Main() 
		if use_lang == 'cmd':
			cmds()
			Main()
		if use_lang == 'l':
			list_langs()
			Main()
		if use_lang == 'rya':
			T2E()
			lang_rya()
			Output()
			Main()
		if use_lang == 'lazy':
			T2E()
			lang_lazy()
			Output()
			Main()
		if use_lang == '0x':
			T2E()
			lang_0x()
			Output()
			Main()
		if use_lang == '0xq':
			T2E()
			lang_0xq()
			Output()
			Main()
		if use_lang == 'leet':
			lang_leet()
			T2E()
			lang_leet2()
			Output()
			Main()
		if use_lang == 'binary':
			T2E()
			lang_binary()
			Output()
			Main()
		if use_lang == 'crazy':
			T2E()
			lang_crazy()
			Output()
			Main()
		if use_lang == 'crazy2':
			T2E()
			lang_crazy2()
			Output()
			Main()
		if use_lang == 'bw':
			T2E()
			lang_backwards()
			Output()
			Main()
		if use_lang == '3r':
			T2E()
			lang_3R()
			Output()
			Main()
		if use_lang == '3l':
			T2E()
			lang_3L()
			Output()
			Main()
		if use_lang == '2r':
			T2E()
			lang_2R()
			Output()
			Main()
		if use_lang == '2l':
			T2E()
			lang_2L()
			Output()
			Main()
		if use_lang == '1r':
			T2E()
			lang_1R()
			Output()
			Main()
		if use_lang == '1l':
			T2E()
			lang_1L()
			Output()
			Main()
		if use_lang == 'uc':
			T2E()
			lang_UC()
			Output()
			Main()
		if use_lang == 'lc':
			T2E()
			lang_LC()
			Output()
			Main()
		if use_lang == 'vr':
			lang_VR()
			Output()
			Main()
	except:
		print('FAILED TO LOAD "{}"'.format(use_lang))
		sleep(1)
		Main()

################################################################################################################
#                                                   REVERSE                                                    #
################################################################################################################
def Reverse():
	try:
		os.system('mode 57,23 && title Reverse && cls')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
		print('                  \033[1;33m╔══════════════════╗')
		print('        ╔═════════╣\033[1;31mWelcome to Reverse\033[1;33m╠═════════╗')
		print('        ║         ╚══════════════════╝         ║')
		print('        ║\033[1;33m1. \033[1;36mEnter the alphabet to decrypt from \033[1;33m║')
		print('        ║      \033[1;33m2. \033[1;36mEnter the encrypted text     \033[1;33m║')
		print('        ║         \033[1;31mENTER \033[1;33m"B" \033[1;31mTO GO BACK         \033[1;33m║')
		print('        ║ ╔══════════════════════════════════╗ ║')
		print('        ╚═╣\033[1;35mTo see preset languages, enter \033[1;33m"L"\033[1;33m╠═╝')
		print('          ╚══════════════════════════════════╝')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
		R_use_lang = input('\033[1;36mAlphabet: \033[1;33m').lower()
		if R_use_lang == 'b':
			Main()
		if R_use_lang == 'l':
			list_langs()
			Reverse()
		if R_use_lang == 'rya':
			T2D()
			lang_rya()
			Output()
			Reverse()
		if R_use_lang == 'lazy':
			T2D()
			lang_lazy()
			Output()
			Reverse()
		if R_use_lang == '0x':
			T2D()
			lang_R_0x()
			Output()
			Reverse()
		if R_use_lang == '0xq':
			T2D()
			lang_R_0xq()
			Output()
			Reverse()
		if R_use_lang == 'leet':
			lang_leet()
			T2D()
			lang_R_leet2()
			Output()
			Reverse()
		if R_use_lang == 'binary':
			T2D()
			lang_R_binary()
			Output()
			Reverse()
		if R_use_lang == 'crazy':
			T2D()
			lang_R_crazy()
			Output()
			Reverse()
		if R_use_lang == 'crazy2':
			T2D()
			lang_R_crazy2()
			Output()
			Reverse()
		if R_use_lang == 'bw':
			T2D()
			lang_backwards()
			Output()
			Reverse()
		if R_use_lang == '3r':
			T2D()
			lang_3L()
			Output()
			Reverse()
		if R_use_lang == '3l':
			T2D()
			lang_3R()
			Output()
			Reverse()
		if R_use_lang == '2r':
			T2D()
			lang_2L()
			Output()
			Reverse()
		if R_use_lang == '2r':
			T2D()
			lang_2R()
			Output()
			Reverse()
		if R_use_lang == '1r':
			T2D()
			lang_1L()
			Output()
			Reverse()
		if R_use_lang == '1l':
			T2D()
			lang_1R()
			Output()
			Reverse()
		if R_use_lang == 'uc':
			T2D()
			lang_LC()
			Output()
			Reverse()
		if R_use_lang == 'lc':
			T2D()
			lang_UC()
			Output()
			Reverse()
		INV_OPT()
		Reverse()
	except:
		print('FAILED TO LOAD THE {} FUNCTION'.format(R_use_lang))
		sleep(1)
		Reverse()

################################################################################################################
#                         OUTPUT FOR ENCRYPTED TEXT / SAVING OUTPUT FOR ENCRYPTED TEXT                         #
################################################################################################################
def Output():
	try:
		try:
			global use_lang, text_raw, text_raw_backup
			os.system('mode 57,20 && title Output && cls')
			print('	   \033[1;31m╔═══════════════════\033[1;36m════════════════╗')
			print('	   \033[1;31m║        CIPHERED TE\033[1;36mXT BELOW        ║')
			print('	   \033[1;31m╚═══════════════════\033[1;36m════════════════╝')
			print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
			print('\n\033[1;33m' + text_raw + '\n')
			print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
			output_options = input('\033[1;33m"C" \033[1;36m= COPY \033[1;31m/ \033[1;33m"S" \033[1;35m= SAVE: \033[1;33m').lower()
			if len(output_options) <= 0 or output_options.isspace():
				raise ValueError
		except ValueError:
			print('FUCKIN IDIOT, ITS A SIMPLE "C" OR "S". IF YO BITCH ASS IS TRYNA LEAVE JUST DO "B" FOR BEING A LIL "BITCH"')
			Sleep()	
			Output()
	################################################################################################################
	#                                                  COPY OUTPUT                                                 #
	################################################################################################################
		try:
			if output_options == 'c':
				pyperclip.copy(text_raw)
				print('\033[1;31mTHERE WAS AN ERROR COPYING THE TEXT')
				Sleep(1)
				Output()
				print('                         \033[1;36m╔════════╗')
				print('	                 ║ \033[1;33mCOPIED \033[1;36m║')
				print('	                 ╚════════╝')
				Sleep(.7)
		except:
			print('\033[1;31mTHERE WAS AN ERROR COPYING THE TEXT')
			Sleep(1)
			Output()
	################################################################################################################
	#                                                  SAVE OUTPUT                                                 #
	################################################################################################################
		if output_options == 's':
			try:
				def Ask4FileName():
					try:
						global save_output_A_name
						save_output_A_name = input('\033[1;36mEnter the name for this file: \033[1;33m')
						if len(save_output_A_name) <= 0 or save_output_A_name.isspace():
							raise ValueError
					except ValueError:
						print('FAILED READING THE FILE NAME. PLEASE TRY AGAIN')
						sleep(1)
						Ask4FileName()
				print('\n                \033[1;31m╔═════════\033[1;36m═════════╗')
				print('       \033[1;31m╔════════╣ CHOOSE A\033[1;36mN OPTION ╠════════╗')
				print('       \033[1;31m║        ╚═════════\033[1;36m═════════╝        ║')
				print('       \033[1;31m║    \033[1;33mR \033[1;31m= \033[1;36mReplace / Create TXT file   ║')
				print('       \033[1;31m║       \033[1;33mA \033[1;31m= \033[1;36mAdd / Create TXT file    ║')
				print('       \033[1;31m╚══════════════════\033[1;36m══════════════════╝')
				save_output = input('\033[1;36mEnter option \033[1;33m"R" \033[1;31m/ \033[1;33m"A"\033[1;36m: \033[1;33m').lower() # Ask user if they wanna replace the text file or add on to a txt file
				if len(save_output) <= 0 or save_output.isspace():
					raise ValueError
			except ValueError:
				print('FUCKIN IDIOT, ITS A SIMPLE "C" OR "S". IF YO BITCH ASS IS TRYNA LEAVE JUST DO "B" FOR BEING A LIL "BITCH"')
				Sleep()	
				Output()
			try:
				if save_output == "r":
					Ask4FileName()
					SO_R_N = open(save_output_R_name, 'w')
					print('\n    \033[1;35m╔════════════════════════════════════════╗')
					print('    ║    \033[1;33mDo you want to add labels for the   \033[1;35m║')
					print('    ║          \033[1;33mlanguage and the text?        \033[1;35m║')
					print('    ╚════════════════════════════════════════╝')
					print('                  \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
					save_output_R_labels = input('\033[1;36mAdd labels?: \033[1;33m').lower()
					if len(save_output) <= 0 or save_output.isspace():
						raise ValueError
				if save_output_R_labels.startswith('y'):
					if use_lang == 'leet':
						print('Input = ' + text_raw_backup + '\nLanguage = ' + use_lang + ' / LEVEL-' + str(leet_level) + '\nOutput = ' + text_raw, file = SO_R_N)
					else:
						print('Input = ' + text_raw_backup + '\nLanguage = ' + use_lang + '\nOutput = ' + text_raw, file = SO_R_N)
				if save_output_R_labels.startswith('n'):
					if use_lang == 'leet':
						print(text_raw_backup + '\n' + use_lang + '-' + str(leet_level) + '\n' + text_raw, file = SO_R_N)
					else:
						print(text_raw_backup + '\n' + use_lang + '\n' + text_raw, file = SO_R_N)
				print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
				print('\033[1;31mSuccessfully saved to ' + '\033[1;33m"' + save_output_R_name)
				print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
				Sleep(2) # Wait
			except ValueError:
				print('FAILED TO GET "LABEL" DETAILS')
				Sleep(1)
				Output()
			try:
				if save_output == "a":
					Ask4FileName()
					SO_A_N = open(save_output_A_name, 'a')
					print('\n \033[1;35m╔═══════════════════════════════════════════════╗')
					print(' ║ \033[1;33mDo you want to add a header before the output \033[1;35m║')
					print(' ║   \033[1;33minside the TXT file as a way of spotting?   \033[1;35m║')
					print(' ╚═══════════════════════════════════════════════╝')
					print('                  \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
					save_output_A_header = input('\033[1;36mAdd a header?: \033[1;33m').lower()
					if save_output_A_header.startswith('y'):
						print('\n    \033[1;35m╔════════════════════════════════════════╗')
						print('    ║    \033[1;33mDo you want to add labels for the   \033[1;35m║')
						print('    ║          \033[1;33mlanguage and the text?        \033[1;35m║')
						print('    ╚════════════════════════════════════════╝')
						print('                 \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
						save_output_A_header_label = input('\033[1;36mAdd labels?: \033[1;33m').lower()
						if save_output_A_header_label.startswith('y'):
							print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\nInput = ' + text_raw_backup + '\nLanguage = ' + use_lang + '\nOutput = ' + text_raw, file = SO_A_N)
						if save_output_A_header_label.startswith('n'):
							print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\n' + text_raw_backup + '\n' + use_lang + '\n' + text_raw, file = SO_A_N)
					if save_output_A_header.startswith('n'):
						print('\n    \033[1;35m╔════════════════════════════════════════╗')
						print('    ║    \033[1;33mDo you want to add labels for the   \033[1;35m║')
						print('    ║          \033[1;33mlanguage and the text?        \033[1;35m║')
						print('    ╚════════════════════════════════════════╝')
						print('                 \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
						save_output_A_header_label = input('\033[1;36mAdd labels?: \033[1;33m').lower()
						if save_output_A_header_label.startswith('y'):
							print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\nInput = ' + text_raw_backup + '\nLanguage = ' + use_lang + '\nOutput = ' + text_raw, file = SO_A_N) # Print this into the save file
						if save_output_A_header_label.startswith('n'):
							print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\n' + text_raw_backup + '\n' + use_lang + '\n' + text_raw, file = SO_A_N) # Print this into the save file
						print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
						print('\033[1;31mSuccessfully saved to ' + '\033[1;33m"' + save_output_A_name)
						print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
						Sleep(2) # Wait
			except ValueError:
				print('FAILED TO GET "HEADER" DETAILS')
				Sleep(1)
				Output()
	except:
		print('AN UNEXPECTED ERROR OCCURED. PLEASE TRY AGAIN')
		Sleep(1)
		Output()
################################################################################################################


def ENC_ADD_LABELS():
	print('\n     \033[1;35m╔════════════════════════════════════════╗')
	print('     ║    \033[1;33mDo you want to add labels for the   \033[1;35m║')
	print('     ║         \033[1;33mInput / Code(s) / Output?      \033[1;35m║')
	print('     ╚════════════════════════════════════════╝')
	print('                  \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
################################################################################################################


def ENC_Output(ENC_USED):
	try:
		global text_raw, text_raw_backup, inputcode_1, inputcode_2, inputcode_3, inputcode_4, inputcode_5, inputcode_6, inputcode_7, inputcode_8, inputcode_9, inputcode_10, inputcode_11, inputcode_13, inputcode_14, inputcode_15, inputcode_16, inputcode_17, inputcode_18, inputcode_19, inputcode_20, inputcode_21
		ENC_BACKUP = ENC_USED
		os.system('title Output [Encrypter/Decrypter] && cls')
		print('	   \033[1;31m╔═══════════════════\033[1;36m════════════════╗')
		print('	   \033[1;31m║        CIPHERED TE\033[1;36mXT BELOW        ║')
		print('	   \033[1;31m╚═══════════════════\033[1;36m════════════════╝')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
		print('\n\033[1;33m' + text_raw + '\n')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
		output_options = input('\033[1;33m"C" \033[1;36m= COPY \033[1;31m/ \033[1;33m"S" \033[1;35m= SAVE: \033[1;33m').lower()
		if len(output_options) <= 0 or output_options.isspace():
			raise ValueError
	except ValueError:
		print('INVALID OPTION. PLEASE TRY AGAIN')
		Sleep(1)
		ENC_Output(ENC_BACKUP)
################################################################################################################
#                                                ENC COPY OUTPUT                                               #
################################################################################################################
	if output_options == 'c':
		try: 
			pyperclip.copy(text_raw)
		except:
			print('\033[1;31mTHERE WAS AN ERROR COPYING THE TEXT')
			Sleep(1)
			ENC_Output()
		else:
			print('                         \033[1;36m╔════════╗')
			print('	                 ║ \033[1;33mCOPIED \033[1;36m║')
			print('	                 ╚════════╝')
			Sleep(.7) # Wait
################################################################################################################
#                                                ENC SAVE OUTPUT                                               #
################################################################################################################
	try:
		if output_options == 's':
			print('\n                \033[1;31m╔═════════\033[1;36m═════════╗')
			print('       \033[1;31m╔════════╣ CHOOSE A\033[1;36mN OPTION ╠════════╗')
			print('       \033[1;31m║        ╚═════════\033[1;36m═════════╝        ║')
			print('       \033[1;31m║    \033[1;33mR \033[1;31m= \033[1;36mReplace / Create TXT file   ║')
			print('       \033[1;31m║       \033[1;33mA \033[1;31m= \033[1;36mAdd / Create TXT file    ║')
			print('       \033[1;31m╚══════════════════\033[1;36m══════════════════╝')
			save_output = input('\033[1;36mEnter option \033[1;33m"R" \033[1;31m/ \033[1;33m"A"\033[1;36m: \033[1;33m').lower() # Ask user if they wanna replace the text file or add on to a txt file
			if save_output == "r":
				try:
					save_output_R_name = input('\033[1;36mEnter the name for this file: \033[1;33m') # Get the name of the text file to replace
					SO_R_N = open(save_output_R_name, 'w')
					ENC_ADD_LABELS()
					save_output_R_labels = input('\033[1;36mAdd labels?: \033[1;33m').lower()
					if len(save_output_R_labels) <= 0 or save_output_R_labels.isspace():
						raise ValueError
						ENC_Output()
				except ValueError:
					print('INVALID OPTION. PLEASE TRY AGAIN')
				if save_output_R_labels.startswith('y'):
					try:
						if ENC_USED == 'ne' or ENC_USED == 'nd':
							print('Input = ' + text_raw_backup + '\nSeperator = ' + NE_Seperator + '\n\nCode = ' + str(inputcode_1) + '\n\nOutput = ' + text_raw, file = SO_R_N)
					except:
						print('FAILED TRYING TO LOAD NORMAL ENCRYPTER/DECRYPTER LABELS. PLEASE TRY AGAIN.')
						Sleep(1)
						ENC_Output()
					try:
						if ENC_USED == 'ae' or ENC_USED == 'ad':
							print('Input = ' + text_raw_backup + '\nSeperator = ' + AE_Seperator + '\n\nCode #1 = ' + str(inputcode_1) + '\nCode #2 = ' + str(inputcode_2) + '\nCode #3 = ' + str(inputcode_3) + '\nCode #4 = ' + str(inputcode_4) + '\nCode #5 = ' + str(inputcode_5) + '\n\nOutput = ' + text_raw, file = SO_R_N)
					except:
						print('FAILED TRYING TO LOAD ADVANCED ENCRYPTER/DECRYPTER LABELS. PLEASE TRY AGAIN.')
						Sleep(1)
						ENC_Output()
					try:
						if ENC_USED == 'se' or ENC_USED == 'sd':
							print('Input = ' + text_raw_backup + '\nSeperator = ' + SE_Seperator + '\n\nCode #1 = ' + str(inputcode_1) + '\nCode #2 = ' + str(inputcode_2) + '\nCode #3 = ' + str(inputcode_3) + '\nCode #4 = ' + str(inputcode_4) + '\nCode #5 = ' + str(inputcode_5) + '\nCode #6 = ' + str(inputcode_6) + '\nCode #7 = ' + str(inputcode_7) + '\nCode #8 = ' + str(inputcode_8) + '\nCode #9 = ' + str(inputcode_9) + '\nCode #10 = ' + str(inputcode_10) + '\nCode #11 = ' + str(inputcode_11) + '\nCode #12 = ' + str(inputcode_13) + '\nCode #13 = ' + str(inputcode_14) + '\nCode #14 = ' + str(inputcode_15) + '\nCode #15 = ' + str(inputcode_16) + '\nCode #16 = ' + str(inputcode_17) + '\nCode #17 = ' + str(inputcode_18) + '\nCode #18 = ' + str(inputcode_19) + '\nCode #19 = ' + str(inputcode_20) + '\nCode #20 = ' + str(inputcode_21) + '\n\nOutput = ' + text_raw, file = SO_R_N)
					except:
						print('FAILED TRYING TO LOAD SUPER ENCRYPTER/DECRYPTER LABELS. PLEASE TRY AGAIN.')
						Sleep(1)
						ENC_Output()
				if save_output_R_labels == "n":
					try:
						if ENC_USED == 'ne':
							print(text_raw_backup + '\n' + NE_Seperator + '\n' + str(inputcode_1) + '\n\n' + text_raw, file = SO_R_N)
					except:
						print('FAILED TRYING TO SAVE THE NORMAL ENCRYPTER LABELS TO {}. PLEASE TRY AGAIN.'.format(save_output_R_name))
						Sleep(1)
						ENC_Output()
					try:
						if ENC_USED == 'ae':
							print(text_raw_backup + '\n' + AE_Seperator + '\n' + str(inputcode_1) + '\n' + str(inputcode_2) + '\n' + str(inputcode_3) + '\n' + str(inputcode_4) + '\n' + str(inputcode_5) + '\n\n' + text_raw, file = SO_R_N)
					except:
						print('FAILED TRYING TO SAVE THE ADVANCED ENCRYPTER LABELS TO {}. PLEASE TRY AGAIN.'.format(save_output_R_name))
						Sleep(1)
						ENC_Output()
					try:
						if ENC_USED == 'se':
							print(text_raw_backup + '\n' + SE_Seperator + '\n' + str(inputcode_1) + '\n' + str(inputcode_2) + '\n' + str(inputcode_3) + '\n' + str(inputcode_4) + '\n' + str(inputcode_5) + '\n' + str(inputcode_6) + '\n' + str(inputcode_7) + '\n' + str(inputcode_8) + '\n' + str(inputcode_9) + '\n' + str(inputcode_10) + '\n' + str(inputcode_11) + '\n' + str(inputcode_13) + '\n' + str(inputcode_14) + '\n' + str(inputcode_15) + '\n' + str(inputcode_16) + '\n' + str(inputcode_17) + '\n' + str(inputcode_18) + '\n' + str(inputcode_19) + '\n' + str(inputcode_20) + '\n' + str(inputcode_21) + '\n\n' + text_raw, file = SO_R_N)
					except:
						print('FAILED TRYING TO SAVE THE SUPER ENCRYPTER LABELS TO {}. PLEASE TRY AGAIN.'.format(save_output_R_name))
						Sleep(1)
						ENC_Output()
					try:
						if ENC_USED == 'nd':
							print(text_raw_backup + '\n' + ND_Seperator + '\n' + str(inputcode_1) + '\n\n' + text_raw, file = SO_R_N)
					except:
						print('FAILED TRYING TO SAVE THE NORMAL DECRYPTER LABELS TO {}. PLEASE TRY AGAIN.'.format(save_output_R_name))
						Sleep(1)
						ENC_Output()
					try:
						if ENC_USED == 'ad':
							print(text_raw_backup + '\n' + AD_Seperator + '\n' + str(inputcode_1) + '\n' + str(inputcode_2) + '\n' + str(inputcode_3) + '\n' + str(inputcode_4) + '\n' + str(inputcode_5) + '\n\n' + text_raw, file = SO_R_N)
					except:
						print('FAILED TRYING TO SAVE THE ADVANCED DECRYPTER LABELS TO {}. PLEASE TRY AGAIN.'.format(save_output_R_name))
						Sleep(1)
						ENC_Output()
					try:
						if ENC_USED == 'sd':
							print(text_raw_backup + '\n' + SD_Seperator + '\n' + str(inputcode_1) + '\n' + str(inputcode_2) + '\n' + str(inputcode_3) + '\n' + str(inputcode_4) + '\n' + str(inputcode_5) + '\n' + str(inputcode_6) + '\n' + str(inputcode_7) + '\n' + str(inputcode_8) + '\n' + str(inputcode_9) + '\n' + str(inputcode_10) + '\n' + str(inputcode_11) + '\n' + str(inputcode_13) + '\n' + str(inputcode_14) + '\n' + str(inputcode_15) + '\n' + str(inputcode_16) + '\n' + str(inputcode_17) + '\n' + str(inputcode_18) + '\n' + str(inputcode_19) + '\n' + str(inputcode_20) + '\n' + str(inputcode_21) + '\n\n' + text_raw, file = SO_R_N)
					except:
						print('FAILED TRYING TO SAVE THE SUPER DECRYPTER LABELS TO {}. PLEASE TRY AGAIN.'.format(save_output_R_name))
						Sleep(1)
						ENC_Output()
				print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
				print('\033[1;31mSuccessfully saved to ' + '\033[1;33m"' + save_output_R_name)
				print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
				Sleep(2) # Wait
	
			if save_output == "a":
				save_output_A_name = input('\n\033[1;36mEnter the name for this file: \033[1;33m')
				SO_A_N = open(save_output_A_name, 'a')
				print('\n \033[1;35m╔═══════════════════════════════════════════════╗')
				print(' ║ \033[1;33mDo you want to add a header before the output \033[1;35m║')
				print(' ║   \033[1;33minside the TXT file as a way of spotting?   \033[1;35m║')
				print(' ╚═══════════════════════════════════════════════╝')
				print('                  \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
				save_output_A_header = input('\033[1;36mAdd a header?: \033[1;33m').lower()
				try:
					if save_output_A_header.startswith('y'):
						ENC_ADD_LABELS()
						save_output_A_header_label = input('\033[1;36mAdd labels?: \033[1;33m').lower()
						if len(save_output_A_header_label) <= 0 or save_output_A_header_label.isspace():
							raise ValueError
				except ValueError:
					
					ENC_Output(ENC_BACKUP)
				if save_output_A_header_label == "y":
					try:
						if ENC_USED == 'ne' or ENC_USED == 'nd':
							print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\nInput = ' + text_raw_backup +  '\n\nCode = ' + inputcode_1 + '\n\nOutput = ' + text_raw, file = SO_A_N)
					except:
						print('FAILED TRYING TO SAVE THE NORMAL ENCRYPTER/DECRYPTER HEADER+LABELS TO {}. PLEASE TRY AGAIN.'.format(save_output_A_name))
						Sleep(1)
						ENC_Output()
					try:
						if ENC_USED == 'ae' or ENC_USED == 'ad':
							print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\nInput = ' + text_raw_backup +  '\n\nCode #1 = ' + inputcode_1 + '\nCode #2 = ' + inputcode_2 + '\nCode #3 = ' + inputcode_3 + '\nCode #4 = ' + inputcode_4 + '\nCode #5 = ' + inputcode_5 + '\n\nOutput = ' + text_raw, file = SO_A_N)
					except:
						print('FAILED TRYING TO SAVE THE ADVANCED ENCRYPTER/DECRYPTER HEADER+LABELS TO {}. PLEASE TRY AGAIN.'.format(save_output_A_name))
						Sleep(1)
						ENC_Output()
					try:
						if ENC_USED == 'se' or ENC_USED == 'sd':
							print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\nInput = ' + text_raw_backup +  '\n\nCode #1 = ' + inputcode_1 + '\nCode #2 = ' + inputcode_2 + '\nCode #3 = ' + inputcode_3 + '\nCode #4 = ' + inputcode_4 + '\nCode #5 = ' + inputcode_5 + '\nCode #6 = ' + inputcode_6 + '\nCode #7 = ' + inputcode_7 + '\nCode #8 = ' + inputcode_8 + '\nCode #9 = ' + inputcode_9 + '\nCode #10 = ' + inputcode_10 + '\nCode #11 = ' + inputcode_11 + '\nCode #12 = ' + inputcode_13 + '\nCode #13 = ' + inputcode_14 + '\nCode #14 = ' + inputcode_15 + '\nCode #15 = ' + inputcode_16 + '\nCode #16 = ' + inputcode_17 + '\nCode #17 = ' + inputcode_18 + '\nCode #18 = ' + inputcode_19 + '\nCode #19 = ' + inputcode_20 + '\nCode #20 = ' + inputcode_21 + '\n\nOutput = ' + text_raw, file = SO_A_N)
					except:
						print('FAILED TRYING TO SAVE THE SUPER ENCRYPTER/DECRYPTER HEADER+LABELS TO {}. PLEASE TRY AGAIN.'.format(save_output_A_name))
						Sleep(1)
						ENC_Output()
				if save_output_A_header_label == "n":
					try:
						if ENC_USED == 'ne' or ENC_USED == 'nd':
							print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\n' + text_raw_backup + '\n\n' + inputcode_1 + '\n\n' + text_raw, file = SO_A_N)
					except:
						print('FAILED TRYING TO SAVE THE NORMAL ENCRYPTER/DECRYPTER HEADER TO {}. PLEASE TRY AGAIN.'.format(save_output_A_name))
						Sleep(1)
						ENC_Output()
					try:
						if ENC_USED == 'ae' or ENC_USED == 'ad':
							print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\n' + text_raw_backup + '\n\n' + inputcode_1 + '\n' + inputcode_2 + '\n' + inputcode_3 + '\n' + inputcode_4 + '\n' + inputcode_5 + '\n\n' + text_raw, file = SO_A_N)
					except:
						print('FAILED TRYING TO SAVE THE ADVANCED ENCRYPTER/DECRYPTER HEADER TO {}. PLEASE TRY AGAIN.'.format(save_output_A_name))
						Sleep(1)
						ENC_Output()
					try:
						if ENC_USED == 'se' or ENC_USED == 'sd':
							print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\n' + text_raw_backup + '\n\n' + inputcode_1 + '\n' + inputcode_2 + '\n' + inputcode_3 + '\n' + inputcode_4 + '\n' + inputcode_5 + '\n' + inputcode_6 + '\n' + inputcode_7 + '\n' + inputcode_8 + '\n' + inputcode_9 + '\n' + inputcode_10 + '\n' + inputcode_11 + '\n' + inputcode_13 + '\n' + inputcode_14 + '\n' + inputcode_15 + '\n' + inputcode_16 + '\n' + inputcode_17 + '\n' + inputcode_18 + '\n' + inputcode_19 + '\n' + inputcode_20 + '\n' + inputcode_21 + '\n\n' + text_raw, file = SO_A_N)
					except:
						print('FAILED TRYING TO SAVE THE SUPER ENCRYPTER/DECRYPTER HEADER TO {}. PLEASE TRY AGAIN.'.format(save_output_A_name))
						Sleep(1)
						ENC_Output()
			if save_output_A_header.startswith('n'):
					ENC_ADD_LABELS()
					save_output_A_header_label = input('\033[1;36mAdd labels?: \033[1;33m').lower()
					if save_output_A_header_label.startswith('y'):
						print('Input = ' + text_raw_backup + '\nLanguage = ' + use_lang + '\nOutput = ' + text_raw, file = SO_A_N) # Print this into the save file
					if save_output_A_header_label.startswith('n'):
						print(text_raw_backup + '\n' + use_lang + '\n' + text_raw, file = SO_A_N) # Print this into the save file
					print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
					print('\033[1;31mSuccessfully saved to ' + '\033[1;33m"' + save_output_A_name)
					print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
					Sleep(2) # Wait
	except:
		print('AN UNEXPECTED ERROR OCCURED. PLEASE TRY AGAIN')
		Sleep(1)
		ENC_Output()
################################################################################################################

################################################################################################################
#                                                     HELP                                                     #
################################################################################################################
def HELP4USER():
	try:
		os.system('mode 57,30 && title Help && cls')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
		print(' \033[1;33m╔═════════════════════════════════════════════════════╗')
		print(' ║                         \033[1;37mMAIN                        \033[1;33m║')
		print(' ║  \033[1;32mTo start: \033[1;36mChoose a language that you want to use.  \033[1;33m║')
		print(' ║      \033[1;36mTo see all languages available, type "\033[1;33mL\033[1;36m".      \033[1;33m║')
		print(' ║   \033[1;32mNext: \033[1;36mEnter the text that you want to translate   \033[1;33m║')
		print(' ║             \033[1;36minto the language you have chosen       \033[1;33m║')
		print(' ╠═════════════════════════════════════════════════════╣')
		print(' ║                       \033[1;37mCRYPTERS                      \033[1;33m║')
		print(' ║    \033[1;36mThere are 3 different \033[32mEncrypt \033[1;36m/ \033[31mDecrypt \033[1;36mtools    \033[1;33m║')
		print(' ║    Each one has a certain amount of code options    ║')
		print(' ║    \033[1;36mNormal Crypters   \033[1;33m-  \033[1;31m"1" Code   \033[1;33m- \033[1;35m1 ~ 9999       \033[1;0m\033[1;33m║')
		print(' ║    \033[1;36mAdvanced Crypters \033[1;33m-  \033[1;31m"5" Codes  \033[1;33m- \033[1;35m1 ~ 9999       \033[1;0m\033[1;33m║')
		print(' ║    \033[1;36mSuper Crypters    \033[1;33m-  \033[1;31m"20" Codes \033[1;33m- \033[1;35m1 ~ 100,000    \033[1;0m\033[1;33m║')
		print(' ╠═════════════════════════════════════════════════════╣')
		print(' ║             \033[1;37mMULTI-LANGUAGE  TRANSLATORS             \033[1;33m║')
		print(' ║ \033[1;36mIf you are trying to encrypt a text/string with two \033[1;33m║')
		print(' ║  \033[1;36mor more languages at a time, then you can use the  \033[1;33m║')
		print(' ║  \033[1;36mMulti-Language Translator. Enter the language you  \033[1;33m║')
		print(' ║   \033[1;36mwant to use and then the text you want to use.    \033[1;33m║')
		print(' ║  \033[1;36mYou can then enter another language and it will    \033[1;33m║')
		print(' ║  \033[1;36mkeep translating the new text to the new language  \033[1;33m║')
		print(' ╠═════════════════════════════════════════════════════╣')
		print(' ║  \033[1;35mTo see a list of available Commands, enter \033[1;33m"cmd"   \033[1;0m\033[1;33m║')
		print(' ╚═════════════════════════════════════════════════════╝')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
		getpass('\033[1;33mPress ENTER to continue...')
	except:
		print('AN UNEXPECTED ERROR HAS OCCCURED. PLEASE TRY AGAIN')
		Sleep(1)
		Main()
################################################################################################################


################################################################################################################
#                                                   COMMANDS                                                   #
################################################################################################################
def cmds():
	try:
		os.system('mode 57,20 && title All available commands && cls')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
		print('                ╔════════════════════════╗')
		print(' ╔══════════════╣ \033[1;31mALL AVAILABLE COMMANDS\033[1;33m ╠═════════════╗')
		print(' ║              ╚════════════════════════╝             ║')
		print(' \033[1;33m║ \033[1;0mHELP = \033[1;33m"H"                                          \033[1;33m║')
		print(' \033[1;33m║ \033[1;0mLIST OF POSSIBLE LANGUAGES = \033[1;33m"L"                    \033[1;33m║')
		print(' \033[1;33m║ \033[1;0mALGORITHM VIEWER = \033[1;33m"ALG"                            \033[1;33m║')
		print(' \033[1;33m║ \033[1;0mMULTI-LANGUAGE TRANSLATOR = \033[1;33m"MT"                    \033[1;33m║')
		print(' \033[1;33m║ \033[1;0mREVERSE MULTI-LANGUAGE TRANSLATOR = \033[1;33m"RMT"           \033[1;33m║')
		print(' \033[1;33m║ \033[1;0mNORMAL ENCRYPTER = \033[1;33m"E"                              \033[1;33m║')
		print(' \033[1;33m║ \033[1;0mNORMAL DECRYPTER = \033[1;33m"D"                              \033[1;33m║')
		print(' \033[1;33m║ \033[1;0mADVANCED ENCRYPTER = \033[1;33m"AE"                           \033[1;33m║')
		print(' \033[1;33m║ \033[1;0mADVANCED DECRYPTER = \033[1;33m"AD"                           \033[1;33m║')
		print(' \033[1;33m║ \033[1;0mSUPER ENCRYPTER = \033[1;33m"SE"                              \033[1;33m║')
		print(' \033[1;33m║ \033[1;0mSUPER DECRYPTER = \033[1;33m"SD"                              \033[1;33m║')
		print(' \033[1;33m║ \033[1;0mSHOW LETTERS OF A ALPHABET = \033[1;33m"S"                    \033[1;33m║')
		print(' \033[1;33m║ \033[1;0mCREATE YOUR OWN LANGUAGE = \033[1;33m"C"                      \033[1;33m║')
		print(' \033[1;33m║ \033[1;0mREVERSE/DECRYPT WITH GIVEN ALPHABET = \033[1;33m"R"           \033[1;33m║')
		print(' \033[1;33m╚═════════════════════════════════════════════════════╝')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
		getpass('\033[1;33mPress ENTER to continue...')
	except:
		print('AN UNEXPECTED ERROR HAS OCCCURED. PLEASE TRY AGAIN')
		Sleep(1)
		Main()
################################################################################################################


################################################################################################################
#                                                 LANGUAGE LIST                                                #
################################################################################################################
def list_langs():
	try:
		os.system('mode 57,27 && title All available alphabets/languages && cls')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
		print('                  ╔═════════════════════╗')
		print(' ╔════════════════╣\033[1;31m  List of Languages  \033[1;33m╠══════════════╗')
		print(' ║                ╚═════════════════════╝              ║')
		print(' \033[1;33m║\033[1;0m BACKWARDS ALPHABET = \033[1;33m"BW"                           \033[1;33m║')
		print(' \033[1;33m║\033[1;0m RYA LANGUAGE= \033[1;33m"RYA"                                 \033[1;33m║')
		print(' \033[1;33m║\033[1;0m LAZY LANGUAGE = \033[1;33m"LAZY"                              \033[1;33m║')
		print(' \033[1;33m║\033[1;0m 0X\'s LANGUAGE = \033[1;33m"0X"                                \033[1;33m║')
		print(' \033[1;33m║\033[1;0m 0X\'s LANGUAGE-QWERTY EDITION = \033[1;33m"0XQ"                \033[1;33m║')
		print(' \033[1;33m║\033[1;0m CRAZY LANGUAGE = \033[1;33m"CRAZY"                            \033[1;33m║')
		print(' \033[1;33m║\033[1;0m CRAZY LANGUAGE #2 = \033[1;33m"CRAZY2"                        \033[1;33m║')
		print(' \033[1;33m║\033[1;0m 1337 5P34K = \033[1;33m"LEET"                                 \033[1;33m║')
		print(' \033[1;33m║\033[1;0m BINARY CODE = \033[1;33m"BINARY"                              \033[1;33m║')
		print(' \033[1;33m║\033[1;0m SHIFTED 3 TO THE RIGHT = \033[1;33m"3R"                       \033[1;33m║')
		print(' \033[1;33m║\033[1;0m SHIFTED 3 TO THE LEFT = \033[1;33m"3L"                        \033[1;33m║')
		print(' \033[1;33m║\033[1;0m SHIFTED 2 TO THE RIGHT = \033[1;33m"2R"                       \033[1;33m║')
		print(' \033[1;33m║\033[1;0m SHIFTED 2 TO THE LEFT = \033[1;33m"2L"                        \033[1;33m║')
		print(' \033[1;33m║\033[1;0m SHIFTED 1 TO THE RIGHT = \033[1;33m"1R"                       \033[1;33m║')
		print(' \033[1;33m║\033[1;0m SHIFTED 1 TO THE LEFT = \033[1;33m"1L"                        \033[1;33m║')
		print(' \033[1;33m║\033[1;0m VOWEL REPLACER = \033[1;33m"VR"                               \033[1;33m║')
		print(' \033[1;33m║\033[1;0m UPPERCASE = \033[1;33m"UC"                                    \033[1;33m║')
		print(' \033[1;33m║\033[1;0m LOWERCASE = \033[1;33m"LC"                                    \033[1;33m║')
		print(' \033[1;33m║                \033[1;31m╔══════════════════════╗             \033[1;33m║')
		print(' \033[1;33m╚════════════════\033[1;31m║ ENTER \033[1;33m"B"\033[1;31m TO GO BACK ║\033[1;33m═════════════╝')
		print('                  \033[1;31m╚══════════════════════╝')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
		getpass('\033[1;33mPress ENTER to continue...')
	except:
		print('AN UNEXPECTED ERROR HAS OCCCURED. PLEASE TRY AGAIN')
		Sleep(1)
		Main()
################################################################################################################

################################################################################################################
#                                                SUPER ENCRYPTER                                               #
################################################################################################################
def S_ENCRYPT():
	try:
		global SE_Seperator, inputcode_1, inputcode_2, inputcode_3, inputcode_4, inputcode_5, inputcode_6, inputcode_7, inputcode_8, inputcode_9, inputcode_10, inputcode_11, inputcode_13, inputcode_14, inputcode_15, inputcode_16, inputcode_17, inputcode_18, inputcode_19, inputcode_20, inputcode_21
		os.system('mode 57,21 && title Super Encrypter && cls')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
		print('                  ╔═══════════════════╗')
		print('     ╔════════════╣\033[1;31m  Super Encrypter  \033[1;33m╠════════════╗')
		print('     ║            ╚═══════════════════╝            ║')
		print('     ║    \033[1;33m1. \033[1;36mEnter all 20 codes to secure with     \033[1;33m║')
		print('     ║        \033[1;33m2. \033[1;36mEnter the text to encrypt         \033[1;33m║')
		print('     ║     \033[1;35m-Enter \033[1;33m"auto"\033[1;35m to change all codes-      \033[1;33m║')
		print('     ║             \033[1;31mENTER \033[1;33m"B"\033[1;31m TO GO BACK            \033[1;33m║')
		print('     ║        ╔════════════════════════════╗       ║')
		print('     ╚════════╣ \033[1;31m# of possible combinations\033[1;33m ╠═══════╝\033[1;33m')
		print('              ║          \033[1;36m1 Googol          \033[1;33m║')
		print('              ╚════════════════════════════╝')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
		SE_Seperator = input('\033[1;36mSeperator \033[1;35m[\033[1;31mLETTERS \033[1;36m+ \033[1;31mSYMBOLS ONLY\033[1;35m]\033[1;36m: \033[1;33m')
	if len(SE_Seperator) <= 0:
		S_ENCRYPT()
	CANT_PASS = '0123456789'
	for a in CANT_PASS:
		for b in SE_Seperator:
			if a == b:
				raise ValueError
	except ValueError:
		print('INVALID OPTION. PLEASE TRY AGAIN')
		Sleep(1)
		S_Encrypt()
	inputcode_eval_1 = input('\033[1;36mFirst code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_1)
	inputcode_1 = int(inputcode_eval_1)
	inputcode_eval_2 = input('\033[1;36mSecond code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_2)
	inputcode_2 = int(inputcode_eval_2)
	inputcode_eval_3 = input('\033[1;36mThird code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_3)
	inputcode_3 = int(inputcode_eval_3)
	inputcode_eval_4 = input('\033[1;36mFourth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_4)
	inputcode_4 = int(inputcode_eval_4)
	inputcode_eval_5 = input('\033[1;36mFifth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_5)
	inputcode_5 = int(inputcode_eval_5)
	inputcode_eval_6 = input('\033[1;36mSixth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_6)
	inputcode_6 = int(inputcode_eval_6)
	inputcode_eval_7 = input('\033[1;36mSeventh code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_7)
	inputcode_7 = int(inputcode_eval_7)
	inputcode_eval_8 = input('\033[1;36mEighth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_8)
	inputcode_8 = int(inputcode_eval_8)
	inputcode_eval_9 = input('\033[1;36mNinth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_9)
	inputcode_9 = int(inputcode_eval_9)
	inputcode_eval_10 = input('\033[1;36mTenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_10)
	inputcode_10 = int(inputcode_eval_10)
	inputcode_eval_11 = input('\033[1;36mEleventh code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_11)
	inputcode_11 = int(inputcode_eval_11)
	inputcode_eval_13 = input('\033[1;36mTwelfth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_13)
	inputcode_13 = int(inputcode_eval_13)
	inputcode_eval_14 = input('\033[1;36mThirteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_14)
	inputcode_14 = int(inputcode_eval_14)
	inputcode_eval_15 = input('\033[1;36mFourteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_15)
	inputcode_15 = int(inputcode_eval_15)
	inputcode_eval_16 = input('\033[1;36mFifteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_16)
	inputcode_16 = int(inputcode_eval_16)
	inputcode_eval_17 = input('\033[1;36mSixteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_17)
	inputcode_17 = int(inputcode_eval_17)
	inputcode_eval_18 = input('\033[1;36mSeventeenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_18)
	inputcode_18 = int(inputcode_eval_18)
	inputcode_eval_19 = input('\033[1;36mEighteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_19)
	inputcode_19 = int(inputcode_eval_19)
	inputcode_eval_20 = input('\033[1;36mNineteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_20)
	inputcode_20 = int(inputcode_eval_20)
	inputcode_eval_21 = input('\033[1;36mTwentieth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_21)
	inputcode_21 = int(inputcode_eval_21)

	SE_ENDING()

def SE_ENDING():
	T2E()
	S_ENCRYPT_NUMBERS()
	ENC_Output('se')
	S_ENCRYPT()

def SE_CHECKER(input_1):
	global inputcode_1, inputcode_2, inputcode_3, inputcode_4, inputcode_5, inputcode_6, inputcode_7, inputcode_8, inputcode_9, inputcode_10, inputcode_11, inputcode_13, inputcode_14, inputcode_15, inputcode_16, inputcode_17, inputcode_18, inputcode_19, inputcode_20, inputcode_21
	if input_1 == 'auto':
		AutoCode = input('\033[1;36mEnter the number for all codes: \033[1;33m')
		SE_STRINGCHECK(AutoCode)
		SE_CODECHECK(AutoCode)
		inputcode_1 = inputcode_2 = inputcode_3 = inputcode_4 = inputcode_5 = inputcode_6 = inputcode_7 = inputcode_8 = inputcode_9 = inputcode_10 = inputcode_11 = inputcode_13 = inputcode_14 = inputcode_15 = inputcode_16 = inputcode_17 = inputcode_18 = inputcode_19 = inputcode_20 = inputcode_21 = int(AutoCode)
		SE_ENDING()
	SE_STRINGCHECK(input_1)
	SE_CODECHECK(input_1)

def SE_STRINGCHECK(inputcode):
	if len(inputcode) <= 0 or inputcode.isspace() == True:
		INV_OPT()
		S_ENCRYPT()
	if inputcode == 'b':
		Main()
	CANT_PASS = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+|{}:"<>?`-=\\[];\',./' # List of all the text that would be considered 'not allowed'
	for a in CANT_PASS:
		for b in inputcode:
			if a == b:
				INV_OPT()
				S_ENCRYPT()

def SE_CODECHECK(inputcode):
	inputcode = int(inputcode)
	if inputcode <= 0 or inputcode > 100000:
		INV_OPT()
		S_ENCRYPT()
################################################################################################################


def S_ENCRYPT_NUMBERS():
	global text_raw
	inputcode_22 = inputcode_1 + inputcode_2 * inputcode_3 + inputcode_4 - inputcode_5 - inputcode_6 + inputcode_7 * inputcode_8 + inputcode_9 - inputcode_10 - inputcode_11 + inputcode_13 * inputcode_14 + inputcode_15 - inputcode_16 - inputcode_17 + inputcode_18 * inputcode_19 + inputcode_20 - inputcode_21
	E_S_1 = str(7 * inputcode_22 * 2055) + SE_Seperator
	E_S_a = str(17 * inputcode_22 * 2055) + SE_Seperator
	E_S_b = str(27 * inputcode_22 * 2055) + SE_Seperator
	E_S_c = str(37 * inputcode_22 * 2055) + SE_Seperator
	E_S_d = str(47 * inputcode_22 * 2055) + SE_Seperator
	E_S_e = str(57 * inputcode_22 * 2055) + SE_Seperator
	E_S_f = str(67 * inputcode_22 * 2055) + SE_Seperator
	E_S_g = str(77 * inputcode_22 * 2055) + SE_Seperator
	E_S_h = str(87 * inputcode_22 * 2055) + SE_Seperator
	E_S_i = str(97 * inputcode_22 * 2055) + SE_Seperator
	E_S_j = str(107 * inputcode_22 * 2055) + SE_Seperator
	E_S_k = str(117 * inputcode_22 * 2055) + SE_Seperator
	E_S_l = str(137 * inputcode_22 * 2055) + SE_Seperator
	E_S_m = str(147 * inputcode_22 * 2055) + SE_Seperator
	E_S_n = str(157 * inputcode_22 * 2055) + SE_Seperator
	E_S_o = str(167 * inputcode_22 * 2055) + SE_Seperator
	E_S_p = str(177 * inputcode_22 * 2055) + SE_Seperator
	E_S_q = str(187 * inputcode_22 * 2055) + SE_Seperator
	E_S_r = str(197 * inputcode_22 * 2055) + SE_Seperator
	E_S_s = str(207 * inputcode_22 * 2055) + SE_Seperator
	E_S_t = str(217 * inputcode_22 * 2055) + SE_Seperator
	E_S_u = str(227 * inputcode_22 * 2055) + SE_Seperator
	E_S_v = str(237 * inputcode_22 * 2055) + SE_Seperator
	E_S_w = str(247 * inputcode_22 * 2055) + SE_Seperator
	E_S_x = str(257 * inputcode_22 * 2055) + SE_Seperator
	E_S_y = str(267 * inputcode_22 * 2055) + SE_Seperator
	E_S_z = str(277 * inputcode_22 * 2055) + SE_Seperator
	E_S_A = str(287 * inputcode_22 * 2055) + SE_Seperator
	E_S_B = str(297 * inputcode_22 * 2055) + SE_Seperator
	E_S_C = str(307 * inputcode_22 * 2055) + SE_Seperator
	E_S_D = str(317 * inputcode_22 * 2055) + SE_Seperator
	E_S_E = str(327 * inputcode_22 * 2055) + SE_Seperator
	E_S_F = str(337 * inputcode_22 * 2055) + SE_Seperator
	E_S_G = str(347 * inputcode_22 * 2055) + SE_Seperator
	E_S_H = str(357 * inputcode_22 * 2055) + SE_Seperator
	E_S_I = str(367 * inputcode_22 * 2055) + SE_Seperator
	E_S_J = str(377 * inputcode_22 * 2055) + SE_Seperator
	E_S_K = str(387 * inputcode_22 * 2055) + SE_Seperator
	E_S_L = str(397 * inputcode_22 * 2055) + SE_Seperator
	E_S_M = str(407 * inputcode_22 * 2055) + SE_Seperator
	E_S_N = str(417 * inputcode_22 * 2055) + SE_Seperator
	E_S_O = str(427 * inputcode_22 * 2055) + SE_Seperator
	E_S_P = str(437 * inputcode_22 * 2055) + SE_Seperator
	E_S_Q = str(447 * inputcode_22 * 2055) + SE_Seperator
	E_S_R = str(457 * inputcode_22 * 2055) + SE_Seperator
	E_S_S = str(467 * inputcode_22 * 2055) + SE_Seperator
	E_S_T = str(477 * inputcode_22 * 2055) + SE_Seperator
	E_S_U = str(487 * inputcode_22 * 2055) + SE_Seperator
	E_S_V = str(497 * inputcode_22 * 2055) + SE_Seperator
	E_S_W = str(507 * inputcode_22 * 2055) + SE_Seperator
	E_S_X = str(517 * inputcode_22 * 2055) + SE_Seperator
	E_S_Y = str(527 * inputcode_22 * 2055) + SE_Seperator
	E_S_Z = str(537 * inputcode_22 * 2055) + SE_Seperator
	text_raw = text_raw.replace(' ',E_S_1)
	text_raw = text_raw.replace('a',E_S_a)
	text_raw = text_raw.replace('b',E_S_b)
	text_raw = text_raw.replace('c',E_S_c)
	text_raw = text_raw.replace('d',E_S_d)
	text_raw = text_raw.replace('e',E_S_e)
	text_raw = text_raw.replace('f',E_S_f)
	text_raw = text_raw.replace('g',E_S_g)
	text_raw = text_raw.replace('h',E_S_h)
	text_raw = text_raw.replace('i',E_S_i)
	text_raw = text_raw.replace('j',E_S_j)
	text_raw = text_raw.replace('k',E_S_k)
	text_raw = text_raw.replace('l',E_S_l)
	text_raw = text_raw.replace('m',E_S_m)
	text_raw = text_raw.replace('n',E_S_n)
	text_raw = text_raw.replace('o',E_S_o)
	text_raw = text_raw.replace('p',E_S_p)
	text_raw = text_raw.replace('q',E_S_q)
	text_raw = text_raw.replace('r',E_S_r)
	text_raw = text_raw.replace('s',E_S_s)
	text_raw = text_raw.replace('t',E_S_t)
	text_raw = text_raw.replace('u',E_S_u)
	text_raw = text_raw.replace('v',E_S_v)
	text_raw = text_raw.replace('w',E_S_w)
	text_raw = text_raw.replace('x',E_S_x)
	text_raw = text_raw.replace('y',E_S_y)
	text_raw = text_raw.replace('z',E_S_z)
	text_raw = text_raw.replace('A',E_S_A)
	text_raw = text_raw.replace('B',E_S_B)
	text_raw = text_raw.replace('C',E_S_C)
	text_raw = text_raw.replace('D',E_S_D)
	text_raw = text_raw.replace('E',E_S_E)
	text_raw = text_raw.replace('F',E_S_F)
	text_raw = text_raw.replace('G',E_S_G)
	text_raw = text_raw.replace('H',E_S_H)
	text_raw = text_raw.replace('I',E_S_I)
	text_raw = text_raw.replace('J',E_S_J)
	text_raw = text_raw.replace('K',E_S_K)
	text_raw = text_raw.replace('L',E_S_L)
	text_raw = text_raw.replace('M',E_S_M)
	text_raw = text_raw.replace('N',E_S_N)
	text_raw = text_raw.replace('O',E_S_O)
	text_raw = text_raw.replace('P',E_S_P)
	text_raw = text_raw.replace('Q',E_S_Q)
	text_raw = text_raw.replace('R',E_S_R)
	text_raw = text_raw.replace('S',E_S_S)
	text_raw = text_raw.replace('T',E_S_T)
	text_raw = text_raw.replace('U',E_S_U)
	text_raw = text_raw.replace('V',E_S_V)
	text_raw = text_raw.replace('W',E_S_W)
	text_raw = text_raw.replace('X',E_S_X)
	text_raw = text_raw.replace('Y',E_S_Y)
	text_raw = text_raw.replace('Z',E_S_Z)
################################################################################################################